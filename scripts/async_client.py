"""Cliente HTTPX asíncrono de demostración. La API debe estar iniciada."""
import asyncio
import httpx

BASE_URL = "http://127.0.0.1:8000"

async def main() -> None:
    timeout = httpx.Timeout(10.0)
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=timeout) as client:
        health_response = await client.get("/health")
        health_response.raise_for_status()
        print("Health:", health_response.json())

        chat_response = await client.post(
            "/api/v1/chat",
            json={"question": "¿Qué es FastAPI?"},
        )
        chat_response.raise_for_status()
        print("Chat:", chat_response.json())

if __name__ == "__main__":
    asyncio.run(main())
