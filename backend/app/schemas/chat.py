"""
Chat Schemas

Purpose:
    Request and Response schemas for RAG chat.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ChatRequest(BaseModel):
    """
    User Question
    """

    question: str
    session_id: str


class Citation(BaseModel):
    """
    Source Citation
    """

    document_name: str
    page_number: int
    confidence: float | None = None


class ChatResponse(BaseModel):
    """
    AI Response
    """

    answer: str
    citations: list[Citation]


class ChatHistoryResponse(BaseModel):
    """
    Chat History Record
    """

    id: int
    question: str
    answer: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ConversationResponse(BaseModel):
    """
    Complete Conversation
    """

    session_id: str
    history: list[ChatHistoryResponse]