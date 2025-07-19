import pytesseract  # type: ignore
from pytesseract import Output
from cv2.typing import MatLike
import cv2
from typing import Union
from pathlib import Path


class ImageTextExtractor:
    def __init__(self):
        self.extractor = pytesseract.image_to_string

    def extract_text(self, image: Union[Path, MatLike, None]) -> str:
        """Extract text from an image."""
        if isinstance(image, Path):
            image = cv2.imread(str(image))

        if image is None:
            raise ValueError(f"Image not found or unable to read: {image}")

        text = self.extractor(image)

        return text.strip()
