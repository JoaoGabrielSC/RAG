class EmbeddingService:
    def __init__(self, embedding_model: EmbeddingModel) -> None:
        self.embedding_model = embedding_model

    def embed(self, text: str) -> list:
        """
        Generate embeddings for the given text using the specified embedding model.

        :param text: The input text to be embedded.
        :return: A list of embeddings.
        """
        return self.embedding_model.embed(text)
