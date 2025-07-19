from typing import List, Any
from PIL import Image
import torch
from torch import nn
import numpy as np

from .embedding_strategy import EmbeddingStrategy


class TorchVisionStrategy(EmbeddingStrategy):
    def generate_embedding(
        self, model: nn.Module, processor: Any, image: Image.Image
    ) -> List[float]:
        tensor = processor(image).unsqueeze(0)
        with torch.no_grad():
            emb = model(tensor).cpu().numpy()[0]
            normalized = self.normalize_embedding(emb)

            return normalized

    @staticmethod
    def normalize_embedding(embedding: List[float]) -> List[float]:
        norm = np.linalg.norm(embedding)
        is_norm_of_embedding_zero = norm == 0

        if is_norm_of_embedding_zero:
            return embedding

        return [float(x) for x in (np.array(embedding) / norm).tolist()]
