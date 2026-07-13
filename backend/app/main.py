from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import Base, engine

# Import models so SQLAlchemy registers tables
from app.models.user import User
from app.models.document import Document

# Import routers
from app.routers import auth, document, chat


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)


# CORS Configuration
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).rstrip("/")
            for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Create database tables
Base.metadata.create_all(bind=engine)


# Register Routers

app.include_router(
    auth.router,
    prefix=f"{settings.API_V1_STR}/auth",
    tags=["Auth"]
)


app.include_router(
    document.router,
    prefix=f"{settings.API_V1_STR}/documents",
    tags=["Documents"]
)


app.include_router(
    chat.router,
    prefix=f"{settings.API_V1_STR}/chat",
    tags=["Chat"]
)


@app.get("/health")
def health_check():
    return {
        "status": "operational",
        "message": "Company Policy Assistant backend running successfully"
    }