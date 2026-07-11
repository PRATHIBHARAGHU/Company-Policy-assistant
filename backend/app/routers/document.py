from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import RBACChecker, get_current_user
from app.models.user import User
from app.models.role import Role
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.services.s3_service import S3Service
from app.services.rag_service import RAGService
from app.services.document_processing_service import DocumentProcessingService

router = APIRouter()
s3_service = S3Service()
rag_service = RAGService()

@router.post("/upload")
async def upload_policy(
    file: UploadFile = File(...),
    min_clearance_level: int = Form(...),
    current_user: User = Depends(RBACChecker("document:upload")),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only structural PDF parsing parameters allowed.")
        
    s3_key = f"policies/{uuid.uuid4()}_{file.filename}"
    await s3_service.upload_file(file, s3_key)
    
    doc = Document(
        filename=file.filename,
        s3_key=s3_key,
        file_type="pdf",
        uploaded_by=current_user.id,
        min_clearance_level=min_clearance_level
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    
    try:
        file.file.seek(0)
        chunks = DocumentProcessingService.extract_text_chunks_from_pdf(file.file)
        
        if chunks:
            point_ids = rag_service.index_document(chunks, doc.id, doc.filename, min_clearance_level)
            for idx, chk in enumerate(chunks):
                db_chunk = DocumentChunk(
                    document_id=doc.id,
                    chunk_index=chk["chunk_index"],
                    page_number=chk["page_number"],
                    content=chk["content"],
                    qdrant_point_id=point_ids[idx]
                )
                db.add(db_chunk)
            db.commit()
    except Exception as e:
        db.delete(doc)
        db.commit()
        s3_service.delete_file(s3_key)
        raise HTTPException(status_code=500, detail=f"Pipeline failure during storage mapping: {str(e)}")
        
    return {"status": "success", "document_id": doc.id}