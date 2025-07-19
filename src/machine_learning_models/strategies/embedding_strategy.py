from abc import ABC, abstractmethod
from PIL import Image
from typing import List, Any


class EmbeddingStrategy(ABC):
    @abstractmethod
    def generate_embedding(
        self, model: Any, processor: Any, image: Image.Image
    ) -> List[float]:
        raise NotImplementedError(
            "Method 'get_embedding' should be implemented in subclasses."
        )
