# AI Knowledge Assistant

**Versión:** 0.1.0  
**Módulo:** 0 — Preparación del entorno de Ingeniería de IA

API REST inicial construida con Python, FastAPI y Pydantic. Este incremento utiliza una respuesta local de demostración y **no integra un modelo de lenguaje (LLM)**.

## Requisitos

- Python 3.12 o superior
- Git
- Visual Studio Code (recomendado)

## Instalación en Windows PowerShell

```powershell
py --version
git --version
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Si PowerShell bloquea la activación, ejecuta en esa terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Ejecutar la API

Desde la raíz del proyecto y con `.venv` activo:
```powershell
python -m uvicorn app.main:app --reload
```

Abre:
- Documentación Swagger: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health
- Info: http://127.0.0.1:8000/api/v1/info

Para detener el servidor, usa `Ctrl+C`.

## Probar el chat

En Swagger, abre `POST /api/v1/chat`, pulsa **Try it out** y envía:
```json
{
  "question": "¿Qué es FastAPI?"
}
```

Respuesta aproximada:
```json
{
  "answer": "FastAPI es un framework de Python para crear APIs. Utiliza tipos de Python y Pydantic para validar datos, y permite definir endpoints asíncronos con async y await.",
  "provider": "bootstrap-local"
}
```

La pregunta debe tener entre 3 y 2000 caracteres. Si no cumple la validación, FastAPI devuelve HTTP 422.

## Cliente HTTPX asíncrono

Con el servidor funcionando, abre otra terminal con el entorno virtual activado y ejecuta:
```powershell
python scripts/async_client.py
```

## Ejecutar las pruebas

Desde la raíz del proyecto:
```powershell
python -m pytest -q
```

Las pruebas cubren el servicio, los endpoints, las preguntas inválidas, la información del proyecto y OpenAPI.

## Endpoints

| Método | Ruta | Propósito |
|---|---|---|
| GET | `/health` | Verifica disponibilidad |
| POST | `/api/v1/chat` | Valida una pregunta y devuelve una respuesta local |
| GET | `/api/v1/info` | Muestra metadatos y confirma que `llm_enabled` es `false` |
| GET | `/docs` | Documentación Swagger generada por FastAPI |

## Arquitectura

`Cliente → FastAPI/router → Pydantic → servicio → respuesta`

- `app/main.py`: crea la aplicación y el endpoint de salud.
- `app/api/routes/chat.py`: define los endpoints HTTP.
- `app/schemas/chat.py`: valida las solicitudes y tipa las respuestas.
- `app/services/assistant.py`: contiene la lógica de respuesta local.
- `scripts/async_client.py`: demuestra consumo asíncrono con HTTPX.
- `tests/`: incluye pruebas unitarias y de integración.

## Flujo Git y GitHub

Después de revisar que las pruebas pasan:

```powershell
git init
git branch -M main
git add .
git commit -m "chore: initialize AI knowledge assistant project"
git switch -c feat/bootstrap-api
git add .
git commit -m "feat: add bootstrap API endpoints and service"
git add .
git commit -m "test: add bootstrap API test suite"
```

Crea un repositorio vacío en GitHub. Luego reemplaza `TU-USUARIO` por tu usuario real:
```powershell
git remote add origin https://github.com/TU-USUARIO/ai-knowledge-assistant.git
git push -u origin main
git push -u origin feat/bootstrap-api
```

En GitHub, crea un Pull Request desde `feat/bootstrap-api` hacia `main`. Si ya existe un repositorio Git configurado, no repitas `git init` ni `git remote add origin`; revisa primero `git status` y `git remote -v`.

## Seguridad y alcance

No agregues contraseñas, tokens, archivos `.env` ni credenciales al repositorio. No se utiliza proveedor LLM, base de datos, Docker, RAG ni agentes en este módulo.
