import asyncio

async def generate_answer(question: str) -> str:
    """Genera una respuesta local de demostración; no utiliza ningún LLM."""
    await asyncio.sleep(0)
    normalized = question.strip().lower()

    if "fastapi" in normalized:
        return (
            "FastAPI es un framework de Python para crear APIs. "
            "Utiliza tipos de Python y Pydantic para validar datos, "
            "y permite definir endpoints asíncronos con async y await."
        )
    if "pydantic" in normalized:
        return (
            "Pydantic permite validar y estructurar datos usando modelos "
            "y anotaciones de tipos de Python."
        )
    if "asyncio" in normalized or "asíncrono" in normalized or "asincrono" in normalized:
        return (
            "AsyncIO proporciona herramientas para ejecutar operaciones "
            "asíncronas en Python y coordinar tareas que esperan operaciones de entrada/salida."
        )

    return (
        "Esta es una respuesta local de demostración del AI Knowledge Assistant. "
        "Todavía no se ha conectado ningún modelo de lenguaje. "
        f"Tu pregunta fue: {question.strip()}"
    )
