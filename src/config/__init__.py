from os import PathLike
from typing_extensions import Literal
from torch import nn
from dataclasses import dataclass
from typing import Any, Union, Protocol
from enum import IntEnum, StrEnum


class ModelType(StrEnum):
    VIT = "vit"
    RESNET50 = "resnet50"


class DownloadModelPaths(StrEnum):
    VIT = "google/vit-base-patch16-224-in21k"
    RESNET50 = "resnet50"


class ModelEmbeddingDimensions(IntEnum):
    VIT = 768
    RESNET50 = 2048


class TorchModelLoader(Protocol):
    def __call__(self) -> nn.Module: ...


class PretrainedModel(Protocol):
    @classmethod
    def from_pretrained(
        cls,
        pretrained_model_name_or_path: str | PathLike[Any],
        *args: Any,
        **kwargs: Any,
    ) -> nn.Module: ...


class PretrainedProcessor(Protocol):
    @classmethod
    def from_pretrained(
        cls,
        pretrained_model_name_or_path: str | PathLike[Any],
        *args: Any,
        **kwargs: Any,
    ) -> Any: ...


@dataclass
class HFModelConfig:
    model_class: PretrainedModel
    processor_class: PretrainedProcessor
    model_name: str
    dim: int
    source: str = "hf"


@dataclass
class TorchModelConfig:
    loader: TorchModelLoader
    dim: int
    source: str = "torchvision"


ModelConfig = Union[HFModelConfig, TorchModelConfig]


@dataclass
class Embedding:
    model: nn.Module
    processor: Any
    dim: int
    source: str
