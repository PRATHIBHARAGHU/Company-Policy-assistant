from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.role import Role
from app.models.chat_history import Conversation, ChatMessage
from app.services.rag_service import RAGService
from pydantic import BaseModel

router = APIRouter()
rag_service = RAGService()

class MessageIn(BaseModel):
    content: str

@router.post("/conversations/{conversation_id}/messages")
def post_chat_message(
    conversation_id: int,
    msg: MessageIn,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    conv = db.query(Conversation).filter(Conversation.id == conversation_id, Conversation.user_id == current_user.id).first()
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation session structure missing.")
        
    role = db.query(Role).filter(Role.id == current_user.role_id).first()
    
    # Context summary rolling history execution
    history_messages = db.query(ChatMessage).filter(ChatMessage.conversation_id == conversation_id).order_by(ChatMessage.created_at.desc()).limit(4).all()
    history_context = "\n".join([f"{m.role.upper()}: {m.content}" for m in reversed(history_messages)])
    
    user_msg = ChatMessage(conversation_id=conversation_id, role="user", content=msg.content)
    db.add(user_msg)
    db.commit()
    
    output = rag_service.query_pipeline(msg.content, role.clearance_level, history_context)
    
    ai_msg = ChatMessage(
        conversation_id=conversation_id,
        role="assistant",
        content=output["answer"],
        citations=output["citations"]
    )
    db.add(ai_msg)
    db.commit()
    
    return {"answer": ai_msg.content, "citations": ai_msg.citations}