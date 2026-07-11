from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

# Import ALL models before create_all()
# This registers tables with SQLAlchemy metadata
from app.models.user import User
from app.models.role import Role
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.models.chat_history import ChatHistory
from app.models.upload import Upload


# Create database tables
Base.metadata.create_all(bind=engine)


# Routers
from app.routers import auth
from app.routers import chat
from app.routers import document
from app.routers import admin_router


app = FastAPI(
    title="Company Policy Assistant",
    description="AI powered company policy assistant using RAG",
    version="1.0.0"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # React Vite frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Company Policy Assistant API is running 🚀"
    }


# Register Routers

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    document.router,
    prefix="/documents",
    tags=["Documents"]
)

app.include_router(
    chat.router,
    prefix="/chat",
    tags=["Chat"]
)

app.include_router(
    admin_router.router,
    prefix="/admin",
    tags=["Admin"]
)