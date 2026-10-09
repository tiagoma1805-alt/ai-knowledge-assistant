import pytest
from app.services.assistant import generate_answer

@pytest.mark.asyncio
async def test_service_answers_known_fastapi_question():
    answer = await generate_answer("¿Qué es FastAPI?")
    assert "framework de Python" in answer
    assert len(answer) > 0

@pytest.mark.asyncio
async def test_service_fallback_is_local_bootstrap():
    answer = await generate_answer("Explícame un tema desconocido")
    assert "respuesta local de demostración" in answer
    assert "no se ha conectado ningún modelo" in answer
