"""
Document Schemas

Purpose:
    Schemas for document upload, metadata and retrieval.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentBase(BaseModel):
    """
    Common Document Fields
    """

    title: str
    access_level: str


class DocumentCreate(DocumentBase):
    """
    Metadata used after upload.
    """

    pass


class DocumentChunkResponse(BaseModel):
    """
    Individual chunk returned from retrieval.
    """

    id: int
    page_number: int
    chunk_index: int
    chunk_text: str

    model_config = ConfigDict(from_attributes=True)


class DocumentResponse(DocumentBase):
    """
    Document Details
    """

    id: int
    file_name: str
    file_type: str
    s3_url: str | None = None
    owner_id: int
    created_at: datetime

    chunks: list[DocumentChunkResponse] = []

    model_config = ConfigDict(from_attributes=True)


class UploadResponse(BaseModel):
    """
    Response after successful upload.
    """

    document_id: int
    filename: str
    message: str


class DeleteDocumentResponse(BaseModel):
    """
    Delete Response
    """

    message: str