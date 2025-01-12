from typing import Any, List, Tuple

import torch
from torch import Tensor


def fill_tensor(
    max_len: int,
    indices: Tuple[torch.Tensor, torch.Tensor],
    tns: torch.Tensor,
    accumulate: bool,
    current_device: str = None,
) -> Tensor:
    """
    Creates a tensor of shape (bs, num_spans, contexutalised_embedding_size).
    The tns argument is the contextualised token embeddings is grouped according to spans and summed.
    A span is defined as a sequence of tokens that have the same accumulated sum value.
    An accumulated sum value increases when a token that marks the starts (inclusive) or end (exclusive)
    is an entity is reached.
    The groups that refer to entities can be selected using the entity mask tensors on the return value.
    The values from tns (shape = (bs, seq_len, contexutalised_embedding_size)) are
    (note num_spans >= num_ents because not all spans are entity mentions)
    :param max_len: maximum number of spans (note num_spans >= num_ents because not all spans are entity mentions)
    :param indices: tensors for indexing into first and second dimension
    :param tns: contexutalised token embeddings. Shape = (bs, seq_len, contexutalised_embedding_size)
    :param accumulate: whether to accumulate sum or take the last token embedding/value only
    :param current_device: device to store the resulting tensor on
    :return: a tensor that holds summed tokens for spans together
      Shape = (bs, num_spans, contexutalised_embedding_size)
    """
    to_fill = torch.zeros(
        [tns.size(0), max_len, tns.size(2)], dtype=tns.dtype, device=current_device
    )
    to_fill.index_put_(indices, tns, accumulate)
    return to_fill


def get_transformer_layers_params(model, requires_grad: bool = True) -> List[Any]:
    """
    Helper to fetch BERT parameters of model.
    :param model: model
    :return: list of parameters
    """
    return [
        params
        for layer_name, params in model.named_parameters()
        if "transformer" in layer_name and (params.requires_grad or not requires_grad)
    ]


def get_mention_detection_layers_params(model, requires_grad: bool = True) -> List[Any]:
    """
    Helper to fetch ner parameters of model.
    :param model: model
    :return: list of parameters
    """
    return [
        params
        for layer_name, params in model.named_parameters()
        if "mention_detection" in layer_name and (params.requires_grad or not requires_grad)
    ]


def get_entity_typing_layers_params(model, requires_grad: bool = True) -> List[Any]:
    """
    Helper to fetch ner parameters of model.
    :param model: model
    :return: list of parameters
    """
    return [
        params
        for layer_name, params in model.named_parameters()
        if "entity_typing" in layer_name and (params.requires_grad or not requires_grad)
    ]


def get_ed_layers_params(model, requires_grad: bool = True) -> List[Any]:
    """
    Helper to fetch ed parameters of model.
    :param model: model
    :return: list of parameters
    """
    return [
        params
        for layer_name, params in model.named_parameters()
        if "entity_disambiguation" in layer_name and (params.requires_grad or not requires_grad)
    ]
