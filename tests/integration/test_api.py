from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_returns_200():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_chat_valid_question_returns_bootstrap_response():
    response = client.post("/api/v1/chat", json={"question": "¿Qué es FastAPI?"})
    assert response.status_code == 200
    data = response.json()
    assert data["answer"]
    assert data["provider"] == "bootstrap-local"

def test_chat_rejects_question_that_is_too_short():
    response = client.post("/api/v1/chat", json={"question": "Hi"})
    assert response.status_code == 422

def test_chat_rejects_question_that_is_too_long():
    response = client.post("/api/v1/chat", json={"question": "a" * 2001})
    assert response.status_code == 422

def test_info_returns_expected_fields_and_llm_disabled():
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "AI Knowledge Assistant"
    assert data["version"] == "0.1.0"
    assert data["environment"] == "development"
    assert data["llm_enabled"] is False

def test_openapi_docs_are_available():
    response = client.get("/openapi.json")
    assert response.status_code == 200
