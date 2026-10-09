from pydantic import BaseModel, Field, ConfigDict

class ChatRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    question: str = Field(
        min_length=3,
        max_length=2000,
        description="Pregunta que se enviará al asistente local.",
        examples=["¿Qué es FastAPI?"],
    )

class ChatResponse(BaseModel):
    answer: str
    provider: str

class ProjectInfo(BaseModel):
    name: str
    version: str
    environment: str
    llm_enabled: bool
