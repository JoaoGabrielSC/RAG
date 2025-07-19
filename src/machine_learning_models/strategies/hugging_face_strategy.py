from typing import List, Any
from PIL import Image
import torch
import numpy as np
from torch import nn

from src.machine_learning_models.strategies import (
    EmbeddingStrategy,
)


class HuggingFaceStrategy(EmbeddingStrategy):
    def get_embedding(
        self, model: nn.Module, processor: Any, image: Image.Image
    ) -> List[float]:
        raise NotImplementedError("I will implement this method later.")
