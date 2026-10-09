from fastapi import FastAPI
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="AI Knowledge Assistant",
    description="API inicial local para preparar una futura integración de IA.",
    version="0.1.0",
)

@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """Indica que la API está disponible."""
    return {"status": "ok"}

app.include_router(chat_router, prefix="/api/v1")
