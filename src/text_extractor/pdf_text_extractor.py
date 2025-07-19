from pypdf import PdfReader


class PdfTextExtractor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        """Extract text from a PDF file."""
        try:
            reader = PdfReader(self.file_path)
            print(reader)
            text = []
            for page in reader.pages:
                text.append(page.extract_text())
            return "\n".join(text)
        except Exception as e:
            raise RuntimeError(f"Failed to extract text from PDF: {e}")
