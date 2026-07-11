"""
Document Processing Service

Responsible for:

PDF Parsing

DOCX Parsing

TXT Parsing

Chunking

Metadata Extraction
"""

from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter

import fitz

from docx import Document as DocxDocument


class DocumentProcessingService:

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=700,

        chunk_overlap=150
    )

    @staticmethod
    def extract_text(file_path: str):

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":

            return DocumentProcessingService.read_pdf(file_path)

        if extension == ".docx":

            return DocumentProcessingService.read_docx(file_path)

        if extension == ".txt":

            return DocumentProcessingService.read_txt(file_path)

        raise ValueError("Unsupported file.")

    @staticmethod
    def read_pdf(file_path):

        doc = fitz.open(file_path)

        pages = []

        for page_number, page in enumerate(doc):

            pages.append(

                {

                    "page": page_number + 1,

                    "text": page.get_text()

                }

            )

        return pages

    @staticmethod
    def read_docx(file_path):

        document = DocxDocument(file_path)

        text = "\n".join(

            paragraph.text

            for paragraph in document.paragraphs

        )

        return [

            {

                "page": 1,

                "text": text,

            }

        ]

    @staticmethod
    def read_txt(file_path):

        with open(

            file_path,

            encoding="utf8",

        ) as file:

            text = file.read()

        return [

            {

                "page": 1,

                "text": text,

            }

        ]

    @classmethod
    def create_chunks(

        cls,

        pages,

    ):

        chunks = []

        index = 0

        for page in pages:

            texts = cls.splitter.split_text(

                page["text"]

            )

            for chunk in texts:

                chunks.append(

                    {

                        "page": page["page"],

                        "chunk_index": index,

                        "text": chunk,

                    }

                )

                index += 1

        return chunks