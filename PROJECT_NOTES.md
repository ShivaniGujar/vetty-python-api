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
## Step 4 — Environment Variables and Configuration

### Why we need configuration management

The technical requirements specify that configuration should be handled using environment variables.

We should not hardcode configuration values or secrets directly inside Python source code.

### Files added

```text
.env
app/config.py
```

### `.env`

The `.env` file contains local configuration values such as:

* Application name
* Application version
* CoinGecko API base URL
* Cache TTL
* Webhook URL

The `.env` file is included in `.gitignore` so it is not pushed to GitHub.

### `app/config.py`

`pydantic-settings` is used to load environment variables into a centralized `Settings` class.

Important configuration values:

```text
app_name
app_version
coingecko_base_url
cache_ttl
webhook_url
```

### Important Python concepts learned

#### Environment variable

A value provided outside the Python source code that can be changed without modifying the application code.

#### `.env`

A local file used during development to store environment-specific configuration.

#### `BaseSettings`

A Pydantic Settings class that loads and validates configuration values.

#### Type annotations

Examples:

```python
app_name: str
cache_ttl: int
```

They specify the expected type of a configuration value.

#### Default value

```python
cache_ttl: int = 60
```

Means the cache TTL defaults to 60 seconds if another value is not provided.

### Security rule

Never commit `.env` or secrets to GitHub.

`.gitignore` contains:

```text
.env
```

### Current application

The health endpoint now reads the application name and version from configuration:

```text
GET /health
```

Example response:

```json
{
    "status": "healthy",
    "app_name": "Vetty Python API",
    "version": "1.0.0"
}
```
