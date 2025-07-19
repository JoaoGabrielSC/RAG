from src.services.text_extractor import ImageTextExtractor
from src.utils import Parser
from pathlib import Path


def main(file_path: str) -> None:
    image_extractor = ImageTextExtractor()

    text = image_extractor.extract_text(Path(file_path))
    print(text)


if __name__ == "__main__":
    parser = Parser()
    parse = parser.parse()
    print(parse.dataset_path)

    main(parse.dataset_path)
