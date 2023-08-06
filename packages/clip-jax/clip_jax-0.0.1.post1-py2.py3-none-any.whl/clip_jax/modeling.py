# coding=utf-8
# Copyright 2021 The OpenAI Team Authors, The Google Flax Team Authors and The HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Callable, Iterable, Optional, Tuple, Union

import flax
import flax.linen as nn
import jax
import jax.numpy as jnp
from flax.core.frozen_dict import FrozenDict, freeze, unfreeze
from flax.linen import combine_masks, make_causal_mask
from flax.linen import partitioning as nn_partitioning
from flax.linen.attention import dot_product_attention_weights
from flax.linen.dtypes import canonicalize_dtype
from flax.linen.module import Module
from flax.linen.normalization import _canonicalize_axes
from flax.traverse_util import flatten_dict, unflatten_dict
from jax import lax
from transformers import AutoTokenizer
from transformers.modeling_flax_outputs import (
    FlaxBaseModelOutput,
    FlaxBaseModelOutputWithPooling,
    FlaxSequenceClassifierOutput,
)
from transformers.modeling_flax_utils import (
    ACT2FN,
    FlaxPreTrainedModel,
    append_replace_return_docstrings,
    overwrite_call_docstring,
)
from transformers.utils import ModelOutput, add_start_docstrings, logging

from .configuration_clip import CLIPConfig, CLIPTextConfig, CLIPVisionConfig
from .utils import PretrainedFromWandbMixin

remat = nn_partitioning.remat

Axes = Union[int, Iterable[int]]

logger = logging.get_logger(__name__)

CLIP_START_DOCSTRING = r"""

    This model inherits from [`FlaxPreTrainedModel`]. Check the superclass documentation for the generic methods the
    library implements for all its model (such as downloading, saving and converting weights from PyTorch models)

    This model is also a Flax Linen [flax.linen.Module](https://flax.readthedocs.io/en/latest/flax.linen.html#module)
    subclass. Use it as a regular Flax linen Module and refer to the Flax documentation for all matter related to
    general usage and behavior.

    Finally, this model supports inherent JAX features such as:

    - [Just-In-Time (JIT) compilation](https://jax.readthedocs.io/en/latest/jax.html#just-in-time-compilation-jit)
    - [Automatic Differentiation](https://jax.readthedocs.io/en/latest/jax.html#automatic-differentiation)
    - [Vectorization](https://jax.readthedocs.io/en/latest/jax.html#vectorization-vmap)
    - [Parallelization](https://jax.readthedocs.io/en/latest/jax.html#parallelization-pmap)

    Parameters:
        config ([`CLIPConfig`]): Model configuration class with all the parameters of the model.
            Initializing with a config file does not load the weights associated with the model, only the
            configuration. Check out the [`~FlaxPreTrainedModel.from_pretrained`] method to load the model weights.
        dtype (`jax.numpy.dtype`, *optional*, defaults to `jax.numpy.float32`):
            The data type of the computation. Can be one of `jax.numpy.float32`, `jax.numpy.float16` (on GPUs) and
            `jax.numpy.bfloat16` (on TPUs).

            This can be used to enable mixed-precision training or half-precision inference on GPUs or TPUs. If
            specified all the computation will be performed with the given `dtype`.

            **Note that this only specifies the dtype of the computation and does not influence the dtype of model
            parameters.**

            If you wish to change the dtype of the model parameters, see [`~FlaxPreTrainedModel.to_fp16`] and
            [`~FlaxPreTrainedModel.to_bf16`].
"""

CLIP_TEXT_INPUTS_DOCSTRING = r"""
    Args:
        input_ids (`numpy.ndarray` of shape `(batch_size, sequence_length)`):
            Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you provide
            it.

            Indices can be obtained using [`CLIPTokenizer`]. See [`PreTrainedTokenizer.encode`] and
            [`PreTrainedTokenizer.__call__`] for details.

            [What are input IDs?](../glossary#input-ids)
        attention_mask (`numpy.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

            [What are attention masks?](../glossary#attention-mask)
        position_ids (`numpy.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0,
            config.max_position_embeddings - 1]`.

            [What are position IDs?](../glossary#position-ids)
        output_attentions (`bool`, *optional*):
            Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
            tensors for more detail.
        output_hidden_states (`bool`, *optional*):
            Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
            more detail.
        return_dict (`bool`, *optional*):
            Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
"""

CLIP_VISION_INPUTS_DOCSTRING = r"""
    Args:
        pixel_values (`numpy.ndarray` of shape `(batch_size, num_channels, height, width)`):
            Pixel values. Padding will be ignored by default should you provide it. Pixel values can be obtained using
            [`CLIPFeatureExtractor`]. See [`CLIPFeatureExtractor.__call__`] for details.
        output_attentions (`bool`, *optional*):
            Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
            tensors for more detail.
        output_hidden_states (`bool`, *optional*):
            Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
            more detail.
        return_dict (`bool`, *optional*):
            Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
"""

CLIP_INPUTS_DOCSTRING = r"""
    Args:
        input_ids (`numpy.ndarray` of shape `(batch_size, sequence_length)`):
            Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you provide
            it.

            Indices can be obtained using [`CLIPTokenizer`]. See [`PreTrainedTokenizer.encode`] and
            [`PreTrainedTokenizer.__call__`] for details.

            [What are input IDs?](../glossary#input-ids)
        attention_mask (`numpy.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

            [What are attention masks?](../glossary#attention-mask)
        position_ids (`numpy.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0,
            config.max_position_embeddings - 1]`.

            [What are position IDs?](../glossary#position-ids)
        pixel_values (`numpy.ndarray` of shape `(batch_size, num_channels, height, width)`):
            Pixel values. Padding will be ignored by default should you provide it. Pixel values can be obtained using
            [`CLIPFeatureExtractor`]. See [`CLIPFeatureExtractor.__call__`] for details.
        output_attentions (`bool`, *optional*):
            Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
            tensors for more detail.
        output_hidden_states (`bool`, *optional*):
            Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
            more detail.
        return_dict (`bool`, *optional*):
            Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
"""


def get_id_pos(mat, id):
    """
    Returns the position of the id in mat.
    """
    return jnp.where(mat == id, 1, 0).argmax(axis=-1)


@flax.struct.dataclass
class FlaxCLIPOutput(ModelOutput):
    """
    Args:
        logits_per_image:(`jnp.ndarray` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text:(`jnp.ndarray` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        text_embeds(`jnp.ndarray` of shape `(batch_size, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of
            [`FlaxCLIPTextModel`].
        image_embeds(`jnp.ndarray` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`FlaxCLIPVisionModel`].
        text_model_output(`FlaxBaseModelOutputWithPooling`):
            The output of the [`FlaxCLIPTextModel`].
        vision_model_output(`FlaxBaseModelOutputWithPooling`):
            The output of the [`FlaxCLIPVisionModel`].
    """

    logits_per_image: jnp.ndarray = None
    logits_per_text: jnp.ndarray = None
    text_embeds: jnp.ndarray = None
    image_embeds: jnp.ndarray = None
    text_model_output: FlaxBaseModelOutputWithPooling = None
    vision_model_output: FlaxBaseModelOutputWithPooling = None

    def to_tuple(self) -> Tuple[Any]:
        return tuple(
            self[k] if k not in ["text_model_output", "vision_model_output"] else getattr(self, k).to_tuple()
            for k in self.keys()
        )


# Adapted from flax.linen.normalization
def _normalize(
    mdl: Module,
    x: Any,
    mean: Any,
    var: Any,
    reduction_axes: Axes,
    feature_axes: Axes,
    dtype: jnp.dtype,
    param_dtype: jnp.dtype,
    epsilon: float,
    use_bias: bool,
    use_scale: bool,
    bias_init: Callable,
    scale_init: Callable,
):

    reduction_axes = _canonicalize_axes(x.ndim, reduction_axes)
    feature_axes = _canonicalize_axes(x.ndim, feature_axes)
    stats_shape = list(x.shape)
    for axis in reduction_axes:
        stats_shape[axis] = 1
    if mean is not None:
        mean = mean.reshape(stats_shape)
    var = var.reshape(stats_shape)
    feature_shape = [1] * x.ndim
    reduced_feature_shape = []
    for ax in feature_axes:
        feature_shape[ax] = x.shape[ax]
        reduced_feature_shape.append(x.shape[ax])
    y = x - mean if mean is not None else x
    mul = lax.rsqrt(var + epsilon)
    args = [x]
    if use_scale:
        scale = mdl.param("scale", scale_init, reduced_feature_shape, param_dtype).reshape(feature_shape)
        mul *= scale
        args.append(scale)
    y *= mul
    if use_bias:
        bias = mdl.param("bias", bias_init, reduced_feature_shape, param_dtype).reshape(feature_shape)
        y += bias
        args.append(bias)
    dtype = canonicalize_dtype(*args, dtype=dtype)
    return jnp.asarray(y, dtype)


class RMSNorm(nn.Module):
    """RMSNorm, adapted from flax LayerNorm"""

    epsilon: float = 1e-6
    dtype: Optional[jnp.dtype] = None
    param_dtype: jnp.dtype = jnp.float32
    use_bias: bool = True
    use_scale: bool = True
    bias_init: Callable = jax.nn.initializers.zeros
    scale_init: Callable = jax.nn.initializers.ones
    reduction_axes: Axes = -1
    feature_axes: Axes = -1

    @nn.compact
    def __call__(self, x):
        dtype = self.dtype or jnp.result_type(x)
        # promote x to at least float32, this avoids half precision computation
        # but preserves double or complex floating points
        dtype = jnp.promote_types(dtype, jnp.float32)
        x = jnp.asarray(x, dtype)
        # use mean2 instead of variance (not centered)
        var = jnp.mean(lax.square(x), self.reduction_axes)
        mean = None

        return _normalize(
            self,
            x,
            mean,
            var,
            self.reduction_axes,
            self.feature_axes,
            self.dtype,
            self.param_dtype,
            self.epsilon,
            self.use_bias,
            self.use_scale,
            self.bias_init,
            self.scale_init,
        )


def norm(use_rmsnorm):
    if use_rmsnorm:
        return RMSNorm
    else:
        return nn.LayerNorm


class FlaxCLIPVisionEmbeddings(nn.Module):
    config: CLIPVisionConfig
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        embed_dim = self.config.hidden_size
        image_size = self.config.image_size
        patch_size = self.config.patch_size

        self.patch_embedding = nn.Conv(
            embed_dim,
            kernel_size=(patch_size, patch_size),
            strides=(patch_size, patch_size),
            padding="VALID",
            use_bias=False,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(),
        )

        self.num_patches = (image_size // patch_size) ** 2
        self.position_embedding = nn.Embed(self.num_patches, embed_dim, embedding_init=jax.nn.initializers.normal())
        self.position_ids = jnp.expand_dims(jnp.arange(0, self.num_patches, dtype="i4"), axis=0)

    def __call__(self, pixel_values):
        patch_embeds = self.patch_embedding(pixel_values)
        batch_size, height, width, channels = patch_embeds.shape
        patch_embeds = jnp.reshape(patch_embeds, (batch_size, height * width, channels))
        embeddings = patch_embeds + self.position_embedding(self.position_ids)
        return embeddings


class FlaxCLIPTextEmbeddings(nn.Module):
    config: CLIPTextConfig
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        embed_dim = self.config.hidden_size

        self.token_embedding = nn.Embed(
            self.config.vocab_size,
            embed_dim,
            embedding_init=jax.nn.initializers.normal(),
        )
        self.position_embedding = nn.Embed(
            self.config.max_position_embeddings,
            embed_dim,
            embedding_init=jax.nn.initializers.normal(),
        )
        self.position_ids = jnp.expand_dims(
            jnp.arange(0, self.config.max_position_embeddings, dtype="i4"), axis=(0, 1)
        )

    def __call__(self, input_ids, position_ids):
        input_embeds = self.token_embedding(input_ids.astype("i4"))
        position_embeds = self.position_embedding(position_ids.astype("i4"))

        embeddings = input_embeds + position_embeds
        return embeddings


class FlaxCLIPAttention(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.embed_dim = self.config.hidden_size
        self.num_heads = self.config.num_attention_heads
        self.head_dim = self.embed_dim // self.num_heads
        if self.head_dim * self.num_heads != self.embed_dim:
            raise ValueError(
                "embed_dim must be divisible by num_heads (got `embed_dim`:"
                f" {self.embed_dim} and `num_heads`: {self.num_heads})."
            )
        self.scale = self.head_dim**-0.5
        self.dropout = self.config.attention_dropout

        self.k_proj = nn.Dense(
            self.embed_dim,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(0.01),
            use_bias=self.config.use_bias,
        )
        self.v_proj = nn.Dense(
            self.embed_dim,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(0.01),
            use_bias=self.config.use_bias,
        )
        self.q_proj = nn.Dense(
            self.embed_dim,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(0.01),
            use_bias=self.config.use_bias,
        )
        self.out_proj = nn.Dense(
            self.embed_dim,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(0.01),
            use_bias=self.config.use_bias,
        )

        if self.config.ln_type == "normformer":
            self.layer_norm_end = norm(self.config.use_rmsnorm)(
                epsilon=self.config.layer_norm_eps, dtype=self.dtype, use_bias=self.config.use_bias
            )

        self.causal = isinstance(self.config, CLIPTextConfig)
        # causal mask does not seem interesting so we never use it
        self.causal = False
        if self.causal:
            self.causal_mask = make_causal_mask(jnp.ones((1, self.config.max_position_embeddings), dtype="i4"))

    def _split_heads(self, hidden_states):
        return hidden_states.reshape(hidden_states.shape[:2] + (self.num_heads, self.head_dim))

    def _merge_heads(self, hidden_states):
        return hidden_states.reshape(hidden_states.shape[:2] + (self.embed_dim,))

    def __call__(
        self,
        hidden_states,
        attention_mask=None,
        deterministic: bool = True,
        output_attentions: bool = False,
    ):
        query = self.q_proj(hidden_states)
        key = self.k_proj(hidden_states)
        value = self.v_proj(hidden_states)

        query = self._split_heads(query)
        key = self._split_heads(key)
        value = self._split_heads(value)

        causal_attention_mask = None
        if self.causal:
            query_length, key_length = query.shape[1], key.shape[1]
            causal_attention_mask = self.causal_mask[:, :, key_length - query_length : key_length, :key_length]

        if attention_mask is not None and causal_attention_mask is not None:
            attention_mask = jnp.expand_dims(attention_mask, axis=(-3, -2))
            attention_mask = combine_masks(attention_mask, causal_attention_mask, dtype="i4")
        elif causal_attention_mask is not None:
            attention_mask = causal_attention_mask
        elif attention_mask is not None:
            attention_mask = jnp.expand_dims(attention_mask, axis=(-3, -2))

        if attention_mask is not None:
            attention_bias = lax.select(
                attention_mask > 0,
                jnp.full(attention_mask.shape, 0.0).astype(self.dtype),
                jnp.full(attention_mask.shape, -1e4).astype(self.dtype),
            )
        else:
            attention_bias = None

        dropout_rng = None
        if not deterministic and self.dropout > 0.0:
            dropout_rng = self.make_rng("dropout")

        attn_weights = dot_product_attention_weights(
            query,
            key,
            bias=attention_bias,
            dropout_rng=dropout_rng,
            dropout_rate=self.dropout,
            deterministic=deterministic,
            dtype=self.dtype,
            precision=None,
        )

        attn_output = jnp.einsum("...hqk,...khd->...qhd", attn_weights, value)
        attn_output = self._merge_heads(attn_output)
        attn_output = self.out_proj(attn_output)

        if self.config.ln_type == "normformer":
            attn_output = self.layer_norm_end(attn_output)

        outputs = (attn_output, attn_weights) if output_attentions else (attn_output,)
        return outputs


class FlaxCLIPMLP(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.activation_fn = ACT2FN[self.config.hidden_act]
        self.fc1 = nn.Dense(
            self.config.intermediate_size,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(0.01),
            use_bias=self.config.use_bias,
        )
        self.fc2 = nn.Dense(
            self.config.hidden_size,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(0.01),
            use_bias=self.config.use_bias,
        )
        if self.config.use_glu:
            self.fc1_glu = nn.Dense(
                self.config.intermediate_size,
                dtype=self.dtype,
                kernel_init=jax.nn.initializers.normal(0.01),
                use_bias=self.config.use_bias,
            )
        if self.config.ln_type == "normformer":
            self.layer_norm_mid = norm(self.config.use_rmsnorm)(
                epsilon=self.config.layer_norm_eps,
                dtype=self.dtype,
                use_bias=self.config.use_bias,
                use_scale=self.config.force_scale,
            )

    def __call__(self, hidden_states):
        h1 = self.fc1(hidden_states)
        h1 = self.activation_fn(h1)
        if self.config.use_glu:
            h2 = self.fc1_glu(hidden_states)
            h1 = h1 * h2
        if self.config.ln_type == "normformer":
            h1 = self.layer_norm_mid(h1)
        h1 = self.fc2(h1)
        return h1


class FlaxCLIPEncoderLayer(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.self_attn = FlaxCLIPAttention(self.config, dtype=self.dtype)
        self.layer_norm1 = norm(self.config.use_rmsnorm)(
            epsilon=self.config.layer_norm_eps,
            dtype=self.dtype,
            use_bias=self.config.use_bias,
            use_scale=self.config.force_scale,
        )
        self.layer_norm2 = norm(self.config.use_rmsnorm)(
            epsilon=self.config.layer_norm_eps,
            dtype=self.dtype,
            use_bias=self.config.use_bias,
            use_scale=self.config.force_scale,
        )
        self.mlp = FlaxCLIPMLP(self.config, dtype=self.dtype)

    def __call__(
        self,
        hidden_states,
        attention_mask,
        deterministic: bool = True,
        output_attentions: bool = False,
    ):
        residual = hidden_states

        hidden_states = self.layer_norm1(hidden_states)
        attn_outputs = self.self_attn(
            hidden_states=hidden_states,
            attention_mask=attention_mask,
            deterministic=deterministic,
            output_attentions=output_attentions,
        )
        hidden_states = attn_outputs[0]
        hidden_states = residual + hidden_states

        residual = hidden_states
        hidden_states = self.layer_norm2(hidden_states)
        hidden_states = self.mlp(hidden_states)
        hidden_states = residual + hidden_states

        if self.config.use_scan:
            return hidden_states, None

        outputs = (hidden_states,)

        if output_attentions:
            outputs += attn_outputs[1:]

        return outputs


class FlaxCLIPLayerCollection(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype = jnp.float32

    @nn.compact
    def __call__(
        self,
        hidden_states,
        attention_mask=None,
        deterministic: bool = True,
        output_attentions: bool = False,
        output_hidden_states: bool = False,
        return_dict: bool = True,
    ):
        all_attentions = () if output_attentions else None
        all_hidden_states = () if output_hidden_states else None

        # gradient checkpointing
        layer = (
            remat(
                FlaxCLIPEncoderLayer,
                static_argnums=(2, 3),
                prevent_cse=not self.config.use_scan,
            )
            if self.config.gradient_checkpointing
            else FlaxCLIPEncoderLayer
        )

        if self.config.use_scan:
            # keep it simple
            assert (
                not output_attentions and not output_hidden_states
            ), "scan does not support output_attentions or output_hidden_states"
            # FIXME: scan does not work:
            # - check if first layer has a different dimension and need to be out of scan
            # - potentially FlaxCLIPLayerCollection is compiled and loaded for both text and vision so may need 2 different names
            # - use checkify for potential errors
            hidden_states, _ = nn.scan(
                layer,
                variable_axes={"params": 0},
                split_rngs={"params": True, "dropout": True},
                in_axes=(nn.broadcast, nn.broadcast, nn.broadcast),
                length=self.config.num_hidden_layers,
            )(self.config, dtype=self.dtype, name="scanned")(
                hidden_states, attention_mask, deterministic, output_attentions
            )
        else:
            for i in range(self.config.num_hidden_layers):
                if output_hidden_states:
                    all_hidden_states += (hidden_states,)

                layer_outputs = layer(self.config, dtype=self.dtype, name=str(i))(
                    hidden_states,
                    attention_mask,
                    deterministic=deterministic,
                    output_attentions=output_attentions,
                )
                hidden_states = layer_outputs[0]

                if output_attentions:
                    all_attentions += (layer_outputs[1],)

        if output_hidden_states:
            all_hidden_states += (hidden_states,)

        outputs = (hidden_states,)

        if not return_dict:
            return tuple(v for v in outputs if v is not None)

        return FlaxBaseModelOutput(
            last_hidden_state=hidden_states,
            hidden_states=all_hidden_states,
            attentions=all_attentions,
        )


class FlaxCLIPEncoder(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.layers = FlaxCLIPLayerCollection(self.config, dtype=self.dtype)

    def __call__(
        self,
        inputs_embeds,
        attention_mask=None,
        deterministic: bool = True,
        output_attentions: bool = False,
        output_hidden_states: bool = False,
        return_dict: bool = True,
    ):
        return self.layers(
            hidden_states=inputs_embeds,
            attention_mask=attention_mask,
            deterministic=deterministic,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )


class FlaxCLIPTextTransformer(nn.Module):
    config: CLIPTextConfig
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.embeddings = FlaxCLIPTextEmbeddings(self.config, dtype=self.dtype)
        self.encoder = FlaxCLIPEncoder(self.config, dtype=self.dtype)
        self.final_layer_norm = norm(self.config.use_rmsnorm)(
            epsilon=self.config.layer_norm_eps,
            dtype=self.dtype,
            use_bias=self.config.use_bias,
            use_scale=self.config.force_scale,
        )

    def __call__(
        self,
        input_ids,
        attention_mask,
        position_ids,
        deterministic: bool = True,
        output_attentions: bool = False,
        output_hidden_states: bool = False,
        return_dict: bool = True,
    ):
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        hidden_states = self.embeddings(input_ids=input_ids, position_ids=position_ids)

        encoder_outputs = self.encoder(
            inputs_embeds=hidden_states,
            attention_mask=attention_mask,
            deterministic=deterministic,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        last_hidden_state = encoder_outputs[0]
        last_hidden_state = self.final_layer_norm(last_hidden_state)

        # text_embeds.shape = [batch_size, sequence_length, transformer.width]
        # take features from the BOS embedding instead of EOS (no causal mask anymore)
        pooled_output = last_hidden_state[:, 0, :]

        if not return_dict:
            return (last_hidden_state, pooled_output) + encoder_outputs[1:]

        return FlaxBaseModelOutputWithPooling(
            last_hidden_state=last_hidden_state,
            pooler_output=pooled_output,
            hidden_states=encoder_outputs.hidden_states,
            attentions=encoder_outputs.attentions,
        )


class FlaxCLIPVisionTransformer(nn.Module):
    config: CLIPVisionConfig
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.embeddings = FlaxCLIPVisionEmbeddings(self.config, dtype=self.dtype)
        self.pre_layernorm = norm(self.config.use_rmsnorm)(
            epsilon=self.config.layer_norm_eps,
            dtype=self.dtype,
            use_bias=self.config.use_bias,
            use_scale=self.config.force_scale,
        )
        self.encoder = FlaxCLIPEncoder(self.config, dtype=self.dtype)
        self.post_layernorm = norm(self.config.use_rmsnorm)(
            epsilon=self.config.layer_norm_eps,
            dtype=self.dtype,
            use_bias=self.config.use_bias,
            use_scale=self.config.force_scale,
        )

    def __call__(
        self,
        pixel_values=None,
        deterministic: bool = True,
        output_attentions=None,
        output_hidden_states=None,
        return_dict: bool = True,
    ):
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        hidden_states = self.embeddings(pixel_values)
        hidden_states = self.pre_layernorm(hidden_states)

        encoder_outputs = self.encoder(
            inputs_embeds=hidden_states,
            deterministic=deterministic,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        last_hidden_state = encoder_outputs[0]
        # average pool
        pooled_output = last_hidden_state.mean(axis=1)
        pooled_output = self.post_layernorm(pooled_output)

        if not return_dict:
            return (last_hidden_state, pooled_output) + encoder_outputs[1:]

        return FlaxBaseModelOutputWithPooling(
            last_hidden_state=last_hidden_state,
            pooler_output=pooled_output,
            hidden_states=encoder_outputs.hidden_states,
            attentions=encoder_outputs.attentions,
        )


class FlaxCLIPTextPreTrainedModel(FlaxPreTrainedModel):
    config_class = CLIPTextConfig
    module_class: nn.Module = None

    def __init__(
        self,
        config: CLIPTextConfig,
        input_shape=(1, 1),
        seed: int = 0,
        dtype: jnp.dtype = jnp.float32,
        _do_init: bool = True,
        **kwargs,
    ):
        module = self.module_class(config=config, dtype=dtype, **kwargs)
        super().__init__(
            config,
            module,
            input_shape=input_shape,
            seed=seed,
            dtype=dtype,
            _do_init=_do_init,
        )

    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict:
        # init input tensor
        input_ids = jnp.zeros(input_shape, dtype="i4")
        position_ids = jnp.broadcast_to(jnp.arange(jnp.atleast_2d(input_ids).shape[-1]), input_shape)
        attention_mask = jnp.ones_like(input_ids)

        params_rng, dropout_rng = jax.random.split(rng)
        rngs = {"params": params_rng, "dropout": dropout_rng}

        random_params = self.module.init(rngs, input_ids, attention_mask, position_ids)["params"]

        if params is not None:
            random_params = flatten_dict(unfreeze(random_params))
            params = flatten_dict(unfreeze(params))
            for missing_key in self._missing_keys:
                params[missing_key] = random_params[missing_key]
            self._missing_keys = set()
            return freeze(unflatten_dict(params))
        else:
            return random_params

    def __call__(
        self,
        input_ids,
        attention_mask=None,
        position_ids=None,
        params: dict = None,
        dropout_rng: jax.random.PRNGKey = None,
        train: bool = False,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
    ):
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.return_dict

        if position_ids is None:
            position_ids = jnp.broadcast_to(jnp.arange(jnp.atleast_2d(input_ids).shape[-1]), input_ids.shape)

        if attention_mask is None:
            attention_mask = jnp.ones_like(input_ids)

        # Handle any PRNG if needed
        rngs = {}
        if dropout_rng is not None:
            rngs["dropout"] = dropout_rng

        return self.module.apply(
            {"params": params or self.params},
            jnp.array(input_ids, dtype="i4"),
            jnp.array(attention_mask, dtype="i4"),
            jnp.array(position_ids, dtype="i4"),
            not train,
            output_attentions,
            output_hidden_states,
            return_dict,
            rngs=rngs,
        )


class FlaxCLIPVisionPreTrainedModel(FlaxPreTrainedModel):
    config_class = CLIPVisionConfig
    main_input_name = "pixel_values"
    module_class: nn.Module = None

    def __init__(
        self,
        config: CLIPVisionConfig,
        input_shape: Optional[Tuple] = None,
        seed: int = 0,
        dtype: jnp.dtype = jnp.float32,
        _do_init: bool = True,
        **kwargs,
    ):
        if input_shape is None:
            input_shape = (1, config.image_size, config.image_size, 3)
        module = self.module_class(config=config, dtype=dtype, **kwargs)
        super().__init__(
            config,
            module,
            input_shape=input_shape,
            seed=seed,
            dtype=dtype,
            _do_init=_do_init,
        )

    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict:
        # init input tensor
        pixel_values = jax.random.normal(rng, input_shape)

        params_rng, dropout_rng = jax.random.split(rng)
        rngs = {"params": params_rng, "dropout": dropout_rng}

        random_params = self.module.init(rngs, pixel_values)["params"]

        if params is not None:
            random_params = flatten_dict(unfreeze(random_params))
            params = flatten_dict(unfreeze(params))
            for missing_key in self._missing_keys:
                params[missing_key] = random_params[missing_key]
            self._missing_keys = set()
            return freeze(unflatten_dict(params))
        else:
            return random_params

    def __call__(
        self,
        pixel_values,
        params: dict = None,
        dropout_rng: jax.random.PRNGKey = None,
        train: bool = False,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
    ):
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.return_dict

        # Handle any PRNG if needed
        rngs = {}
        if dropout_rng is not None:
            rngs["dropout"] = dropout_rng

        return self.module.apply(
            {"params": params or self.params},
            jnp.array(pixel_values, dtype=jnp.float32),
            not train,
            output_attentions,
            output_hidden_states,
            return_dict,
            rngs=rngs,
        )


class FlaxCLIPPreTrainedModel(FlaxPreTrainedModel):
    config_class = CLIPConfig
    module_class: nn.Module = None

    def __init__(
        self,
        config: CLIPConfig,
        input_shape: Optional[Tuple] = None,
        seed: int = 0,
        dtype: jnp.dtype = jnp.float32,
        _do_init: bool = True,
        **kwargs,
    ):
        if input_shape is None:
            input_shape = (
                (1, 1),
                (
                    1,
                    config.vision_config.image_size,
                    config.vision_config.image_size,
                    3,
                ),
            )
        module = self.module_class(config=config, dtype=dtype, **kwargs)
        super().__init__(
            config,
            module,
            input_shape=input_shape,
            seed=seed,
            dtype=dtype,
            _do_init=_do_init,
        )

    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict:
        # init input tensor
        input_ids = jnp.zeros(input_shape[0], dtype="i4")
        position_ids = jnp.broadcast_to(jnp.arange(jnp.atleast_2d(input_ids).shape[-1]), input_shape[0])
        attention_mask = jnp.ones_like(input_ids)

        pixel_values = jax.random.normal(rng, input_shape[1])

        params_rng, dropout_rng = jax.random.split(rng)
        rngs = {"params": params_rng, "dropout": dropout_rng}

        random_params = self.module.init(rngs, input_ids, pixel_values, attention_mask, position_ids)["params"]

        if params is not None:
            random_params = flatten_dict(unfreeze(random_params))
            params = flatten_dict(unfreeze(params))
            for missing_key in self._missing_keys:
                params[missing_key] = random_params[missing_key]
            self._missing_keys = set()
            return freeze(unflatten_dict(params))
        else:
            return random_params

    def num_params(self, params=None):
        if params is None:
            params = self.params
        num_params = jax.tree_util.tree_map(lambda param: param.size, flatten_dict(unfreeze(params))).values()
        return sum(list(num_params))

    def unscan(self, params):
        if self.config.use_scan:
            self.config.use_scan = False
            params = flatten_dict(params)
            scanned_keys = [k for k in params.keys() if "scanned" in k]
            for k in scanned_keys:
                v = params[k]
                name_idx = k.index("scanned")
                for i in range(len(v)):
                    new_k = (
                        *k[:name_idx],
                        f"{i}",
                        *k[name_idx + 1 :],
                    )
                    params[new_k] = v[i]
                del params[k]
            params = unflatten_dict(params)
        return params

    def __call__(
        self,
        input_ids,
        pixel_values,
        attention_mask=None,
        position_ids=None,
        params: dict = None,
        dropout_rng: jax.random.PRNGKey = None,
        train: bool = False,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
    ):
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.return_dict

        if position_ids is None:
            position_ids = jnp.broadcast_to(jnp.arange(jnp.atleast_2d(input_ids).shape[-1]), input_ids.shape)

        if attention_mask is None:
            attention_mask = jnp.ones_like(input_ids)

        # Handle any PRNG if needed
        rngs = {}
        if dropout_rng is not None:
            rngs["dropout"] = dropout_rng

        return self.module.apply(
            {"params": params or self.params},
            jnp.array(input_ids, dtype="i4"),
            jnp.array(pixel_values, dtype=jnp.float32),
            jnp.array(attention_mask, dtype="i4"),
            jnp.array(position_ids, dtype="i4"),
            not train,
            output_attentions,
            output_hidden_states,
            return_dict,
            rngs=rngs,
        )

    def get_text_features(
        self,
        input_ids,
        attention_mask=None,
        position_ids=None,
        params: dict = None,
        dropout_rng: jax.random.PRNGKey = None,
        train=False,
    ):
        r"""
        Args:
            input_ids (`numpy.ndarray` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`CLIPTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)

        Returns:
            text_features (`jnp.ndarray` of shape `(batch_size, output_dim`): The text embeddings obtained by applying
            the projection layer to the pooled output of [`FlaxCLIPTextModel`].

        Examples:

        ```python
        >>> from transformers import CLIPTokenizer, FlaxCLIPModel

        >>> model = FlaxCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="np")
        >>> text_features = model.get_text_features(**inputs)
        ```"""
        if position_ids is None:
            position_ids = jnp.broadcast_to(jnp.arange(jnp.atleast_2d(input_ids).shape[-1]), input_ids.shape)

        if attention_mask is None:
            attention_mask = jnp.ones_like(input_ids)

        # Handle any PRNG if needed
        rngs = {}
        if dropout_rng is not None:
            rngs["dropout"] = dropout_rng

        def _get_features(module, input_ids, attention_mask, position_ids, deterministic):
            text_outputs = module.text_model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                position_ids=position_ids,
                deterministic=deterministic,
            )
            pooled_output = text_outputs[1]
            text_features = module.text_projection(pooled_output)
            return text_features

        return self.module.apply(
            {"params": params or self.params},
            jnp.array(input_ids, dtype="i4"),
            jnp.array(attention_mask, dtype="i4"),
            jnp.array(position_ids, dtype="i4"),
            not train,
            method=_get_features,
            rngs=rngs,
        )

    def get_image_features(
        self,
        pixel_values,
        params: dict = None,
        dropout_rng: jax.random.PRNGKey = None,
        train=False,
    ):
        r"""
        Args:
            pixel_values (`numpy.ndarray` of shape `(batch_size, num_channels, height, width)`):
                Pixel values. Padding will be ignored by default should you provide it. Pixel values can be obtained
                using [`CLIPFeatureExtractor`]. See [`CLIPFeatureExtractor.__call__`] for details.

        Returns:
            image_features (`jnp.ndarray` of shape `(batch_size, output_dim`): The image embeddings obtained by
            applying the projection layer to the pooled output of [`FlaxCLIPVisionModel`]

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import CLIPProcessor, FlaxCLIPModel

        >>> model = FlaxCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="np")

        >>> image_features = model.get_image_features(**inputs)
        ```"""

        # Handle any PRNG if needed
        rngs = {}
        if dropout_rng is not None:
            rngs["dropout"] = dropout_rng

        def _get_features(module, pixel_values, deterministic):
            vision_outputs = module.vision_model(pixel_values=pixel_values, deterministic=deterministic)
            pooled_output = vision_outputs[1]  # pooled_output
            image_features = module.visual_projection(pooled_output)
            return image_features

        return self.module.apply(
            {"params": params or self.params},
            jnp.array(pixel_values, dtype=jnp.float32),
            not train,
            method=_get_features,
            rngs=rngs,
        )


class FlaxCLIPTextModule(nn.Module):
    config: CLIPTextConfig
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.text_model = FlaxCLIPTextTransformer(self.config, dtype=self.dtype)

    def __call__(
        self,
        input_ids,
        attention_mask,
        position_ids,
        deterministic: bool = True,
        output_attentions: bool = False,
        output_hidden_states: bool = False,
        return_dict: bool = True,
    ):
        return self.text_model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            position_ids=position_ids,
            deterministic=deterministic,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )


class FlaxCLIPTextModel(FlaxCLIPTextPreTrainedModel):
    module_class = FlaxCLIPTextModule


FLAX_CLIP_TEXT_MODEL_DOCSTRING = """
    Returns:

    Example:

    ```python
    >>> from transformers import CLIPTokenizer, FlaxCLIPTextModel

    >>> model = FlaxCLIPTextModel.from_pretrained("openai/clip-vit-base-patch32")
    >>> tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")

    >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="np")

    >>> outputs = model(**inputs)
    >>> last_hidden_state = outputs.last_hidden_state
    >>> pooler_output = outputs.pooler_output  # pooled (BOS token) states
    ```
"""

overwrite_call_docstring(FlaxCLIPTextModel, CLIP_TEXT_INPUTS_DOCSTRING + FLAX_CLIP_TEXT_MODEL_DOCSTRING)
append_replace_return_docstrings(
    FlaxCLIPTextModel,
    output_type=FlaxBaseModelOutputWithPooling,
    config_class=CLIPTextConfig,
)


class FlaxCLIPVisionModule(nn.Module):
    config: CLIPVisionConfig
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.vision_model = FlaxCLIPVisionTransformer(self.config, dtype=self.dtype)

    def __call__(
        self,
        pixel_values,
        deterministic: bool = True,
        output_attentions: bool = False,
        output_hidden_states: bool = False,
        return_dict: bool = True,
    ):
        return self.vision_model(
            pixel_values=pixel_values,
            deterministic=deterministic,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )


class FlaxCLIPVisionModel(PretrainedFromWandbMixin, FlaxCLIPVisionPreTrainedModel):
    module_class = FlaxCLIPVisionModule


FLAX_CLIP_VISION_MODEL_DOCSTRING = """
    Returns:

    Example:

    ```python
    >>> from PIL import Image
    >>> import requests
    >>> from transformers import CLIPProcessor, FlaxCLIPVisionModel

    >>> model = FlaxCLIPVisionModel.from_pretrained("openai/clip-vit-base-patch32")
    >>> processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    >>> image = Image.open(requests.get(url, stream=True).raw)

    >>> inputs = processor(images=image, return_tensors="np")

    >>> outputs = model(**inputs)
    >>> last_hidden_state = outputs.last_hidden_state
    >>> pooler_output = outputs.pooler_output  # pooled CLS states
    ```
"""

overwrite_call_docstring(FlaxCLIPVisionModel, CLIP_VISION_INPUTS_DOCSTRING + FLAX_CLIP_VISION_MODEL_DOCSTRING)
append_replace_return_docstrings(
    FlaxCLIPVisionModel,
    output_type=FlaxBaseModelOutputWithPooling,
    config_class=CLIPVisionConfig,
)


class FlaxCLIPVisionModelForImageClassificationModule(nn.Module):
    config: CLIPVisionConfig
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        self.vision_model = FlaxCLIPVisionTransformer(self.config, dtype=self.dtype)
        self.classifier = nn.Dense(
            self.config.num_labels,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.variance_scaling(
                self.config.initializer_range**2, "fan_in", "truncated_normal"
            ),
        )

    def __call__(
        self,
        pixel_values=None,
        deterministic: bool = True,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
    ):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        outputs = self.vision_model(
            pixel_values,
            deterministic=deterministic,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=True,
        )

        logits = self.classifier(outputs.pooler_output)

        if not return_dict:
            output = (logits,) + outputs[2:]
            return output

        return FlaxSequenceClassifierOutput(
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )


class FlaxCLIPVisionModelForImageClassification(PretrainedFromWandbMixin, FlaxCLIPVisionPreTrainedModel):
    module_class = FlaxCLIPVisionModelForImageClassificationModule


class FlaxCLIPModule(nn.Module):
    config: CLIPConfig
    dtype: jnp.dtype = jnp.float32

    def setup(self):
        text_config = self.config.text_config
        vision_config = self.config.vision_config

        self.projection_dim = self.config.projection_dim
        self.text_embed_dim = text_config.hidden_size
        self.vision_embed_dim = vision_config.hidden_size

        self.text_model = FlaxCLIPTextTransformer(text_config, dtype=self.dtype)
        self.vision_model = FlaxCLIPVisionTransformer(vision_config, dtype=self.dtype)

        self.visual_projection = nn.Dense(
            self.projection_dim,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(0.02),
            use_bias=False,
        )
        self.text_projection = nn.Dense(
            self.projection_dim,
            dtype=self.dtype,
            kernel_init=jax.nn.initializers.normal(0.02),
            use_bias=False,
        )

        self.logit_scale = self.param(
            "logit_scale", jax.nn.initializers.constant(self.config.logit_scale_init_value, self.dtype), []
        )

    def __call__(
        self,
        input_ids=None,
        pixel_values=None,
        attention_mask=None,
        position_ids=None,
        deterministic: bool = True,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
    ):
        return_dict = return_dict if return_dict is not None else self.config.return_dict

        vision_outputs = self.vision_model(
            pixel_values=pixel_values,
            deterministic=deterministic,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        text_outputs = self.text_model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            position_ids=position_ids,
            deterministic=deterministic,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        image_embeds = vision_outputs[1]
        image_embeds = self.visual_projection(image_embeds)

        text_embeds = text_outputs[1]
        text_embeds = self.text_projection(text_embeds)

        # normalize features
        def normalize(x, epsilon=1e-6):
            mean2 = jnp.sum(jnp.square(x), axis=-1, keepdims=True)
            return x * lax.rsqrt(mean2 + epsilon)

        image_embeds = normalize(image_embeds)
        text_embeds = normalize(text_embeds)

        # cosine similarity as logits
        logit_scale = jnp.exp(self.logit_scale)
        logits_per_text = jnp.matmul(text_embeds, image_embeds.T) * logit_scale
        logits_per_image = logits_per_text.T

        if not return_dict:
            return (
                logits_per_image,
                logits_per_text,
                text_embeds,
                image_embeds,
                text_outputs,
                vision_outputs,
            )

        return FlaxCLIPOutput(
            logits_per_image=logits_per_image,
            logits_per_text=logits_per_text,
            text_embeds=text_embeds,
            image_embeds=image_embeds,
            text_model_output=text_outputs,
            vision_model_output=vision_outputs,
        )


@add_start_docstrings(CLIP_START_DOCSTRING)
class FlaxCLIPModel(PretrainedFromWandbMixin, FlaxCLIPPreTrainedModel):
    module_class = FlaxCLIPModule


FLAX_CLIP_MODEL_DOCSTRING = """
    Returns:

    Example:

    ```python
    >>> import jax
    >>> from PIL import Image
    >>> import requests
    >>> from transformers import CLIPProcessor, FlaxCLIPModel

    >>> model = FlaxCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    >>> processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    >>> image = Image.open(requests.get(url, stream=True).raw)

    >>> inputs = processor(
    ...     text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="np", padding=True
    ... )

    >>> outputs = model(**inputs)
    >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
    >>> probs = jax.nn.softmax(logits_per_image, axis=1)  # we can take the softmax to get the label probabilities
    ```
"""

overwrite_call_docstring(FlaxCLIPModel, CLIP_INPUTS_DOCSTRING + FLAX_CLIP_MODEL_DOCSTRING)
append_replace_return_docstrings(FlaxCLIPModel, output_type=FlaxCLIPOutput, config_class=CLIPConfig)


class AutoTokenizer(PretrainedFromWandbMixin, AutoTokenizer):
    pass
