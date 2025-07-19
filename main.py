from src.text_extractor.pdf_text_extractor import PdfTextExtractor


def main():
    file_path = "examples/volume_tracing.pdf"
    extractor = PdfTextExtractor(file_path)

    full_text = extractor.extract_text()

    print(full_text)


if __name__ == "__main__":
    main()
