from fastembed import TextEmbedding
import numpy as np

class EmbeddingService:
    def __init__(self):
        # Local BAAI Small configuration engine execution initialization
        self.model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

    def generate_embeddings(self, texts: list[str]) -> list[list[float]]:
        embeddings_generator = self.model.embed(texts)
        return [emb.tolist() for emb in embeddings_generator]

    def generate_single_embedding(self, text: str) -> list[float]:
        return self.generate_embeddings([text])[0]