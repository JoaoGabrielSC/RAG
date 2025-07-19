from dataclasses import dataclass
from typing import Any, Union

import torch
from torch import nn
from transformers import ViTModel, ViTImageProcessor
from torchvision import models

from database.models.embedding import Embedding
from services.preprocessing.image import ImagePreprocessor
from src.config import (
    HFModelConfig,
    ModelConfig,
    TorchModelConfig,
    ModelEmbeddingDimensions,
    DownloadModelPaths,
)


class EmbeddingFactory:
    _MODELS: dict[str, ModelConfig] = {
        "vit": HFModelConfig(
            model_class=ViTModel,
            processor_class=ViTImageProcessor,
            model_name=DownloadModelPaths.VIT,
            dim=ModelEmbeddingDimensions.VIT,
        ),
        "resnet50": TorchModelConfig(
            loader=lambda: models.resnet50(weights=models.ResNet50_Weights.DEFAULT),
            dim=ModelEmbeddingDimensions.RESNET50,
        ),
    }

    @classmethod
    def create_embedding(cls, model_type: str) -> Embedding:
        config = cls._get_model_config(model_type.lower())

        if isinstance(config, HFModelConfig):
            return cls._load_hf_embedding(config)
        if isinstance(config, TorchModelConfig):
            return cls._load_torch_embedding(config)

        raise ValueError(f"Unsupported model config type: {type(config)}")

    @classmethod
    def _get_model_config(cls, model_type: str) -> ModelConfig:
        config = cls._MODELS.get(model_type)
        if not config:
            raise ValueError(f"Model '{model_type}' is not supported.")
        return config

    @staticmethod
    def _load_hf_embedding(config: HFModelConfig) -> Embedding:
        model = config.model_class.from_pretrained(
            config.model_name, use_safetensors=True, torch_dtype=torch.float32
        )
        processor = config.processor_class.from_pretrained(config.model_name)
        return Embedding(
            model=model, processor=processor, dim=config.dim, source=config.source
        )

    @staticmethod
    def _load_torch_embedding(config: TorchModelConfig) -> Embedding:
        model = config.loader()
        model = nn.Sequential(*list(model.children())[:-1])
        processor = ImagePreprocessor.get_default_transform()
        return Embedding(
            model=model, processor=processor, dim=config.dim, source=config.source
        )
