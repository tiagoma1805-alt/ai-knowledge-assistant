from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse, ProjectInfo
from app.services.assistant import generate_answer

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat(request: ChatRequest) -> ChatResponse:
    """Recibe una pregunta validada y devuelve una respuesta local."""
    answer = await generate_answer(request.question)
    return ChatResponse(answer=answer, provider="bootstrap-local")

@router.get("/info", response_model=ProjectInfo, tags=["Info"])
async def project_info() -> ProjectInfo:
    """Devuelve información básica del proyecto."""
    return ProjectInfo(
        name="AI Knowledge Assistant",
        version="0.1.0",
        environment="development",
        llm_enabled=False,
    )
