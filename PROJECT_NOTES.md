# Vetty Python API - Project Notes

## Project Goal

Build a production-ready REST API in Python that retrieves
cryptocurrency market data from a public cryptocurrency API.

## Specification Source

Vetty - Python API Technical Exercise - 2026

## Technology

- Python 3.10+
- FastAPI
- Uvicorn
- CoinGecko API
- HTTPX
- Pydantic
- Pytest
- Docker
- Git
- GitHub

---

# Learning Notes

## 1. Python

Python is the programming language used for this project.

Python files use the `.py` extension.

Example:

`main.py`

---

## 2. Virtual Environment

A virtual environment isolates project dependencies.

Command:

`python -m venv .venv`

Our project uses:

`.venv`

---

## 3. pip

pip is Python's package manager.

Example:

`pip install fastapi`

---

## 4. FastAPI

FastAPI is the framework used to build our REST API.

---

## 5. Uvicorn

Uvicorn runs our FastAPI application as an ASGI server.

Command:

`uvicorn main:app --reload`

---

## 6. API Endpoint

An endpoint is a URL through which a client communicates
with our application.

Example:

`GET /health`

---

## 7. Decorator

`@app.get("/health")` connects an HTTP GET request to
the Python function below it.

---

# Current Implementation

## Health Endpoint

Endpoint:

`GET /health`

Current response:

```json
{
    "status": "healthy"
}

# Project Structure

The project uses an `app` package to keep application code
separate from tests and project configuration.

Current structure:

```text
vetty-python-api/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│
├── .gitignore
├── PROJECT_NOTES.md
└── requirements.txt