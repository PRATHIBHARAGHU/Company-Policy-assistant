"""
Embedding Service

Uses FastEmbed to generate embeddings.
"""

from fastembed import TextEmbedding


class EmbeddingService:

    embedding_model = TextEmbedding()

    @classmethod
    def embed_text(

        cls,

        text: str,

    ):

        embedding = list(

            cls.embedding_model.embed(

                [text]

            )

        )

        return embedding[0]

    @classmethod
    def embed_documents(

        cls,

        chunks,

    ):

        texts = [

            chunk["text"]

            for chunk in chunks

        ]

        vectors = list(

            cls.embedding_model.embed(

                texts

            )

        )

        return vectors