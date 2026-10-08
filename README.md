
# Vetty Python API

A production-oriented REST API built with Python and FastAPI for retrieving cryptocurrency market data from the CoinGecko API.

This project was developed as part of the **Vetty Python API Technical Exercise – 2026**.

## Overview

The API acts as a backend service between API clients and the external CoinGecko cryptocurrency API.

It provides endpoints to:

* Check application health
* List cryptocurrencies
* List cryptocurrency categories
* Retrieve cryptocurrency market data in CAD
* Support pagination
* Protect application endpoints using API-key authentication
* Validate request parameters
* Handle failures from the external cryptocurrency service

The project is being developed incrementally with a focus on clean structure, asynchronous HTTP communication, configuration management, validation, error handling, and production-oriented practices.

---

## Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Pydantic / Pydantic Settings**
* **HTTPX**
* **Uvicorn**
* **CoinGecko API**
* **Git / GitHub**
* **Swagger / OpenAPI**

---

## Project Structure

```text
vetty-python-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── security.py
│   │
│   └── services/
│       ├── __init__.py
│       └── coingecko_service.py
│
├── tests/
│
├── .env
├── .gitignore
├── PROJECT_NOTES.md
├── README.md
└── requirements.txt
```

### Main Components

#### `app/main.py`

Contains the FastAPI application and API endpoints.

#### `app/config.py`

Loads application configuration from environment variables using Pydantic Settings.

#### `app/security.py`

Contains API-key authentication logic used to protect application endpoints.

#### `app/services/coingecko_service.py`

Contains the integration with the external CoinGecko API.

The service uses asynchronous HTTP requests through HTTPX.

---

## Architecture

The application follows a simple layered structure:

```text
Client
  │
  ▼
FastAPI API Layer
  │
  ├── Request Validation
  ├── Authentication
  │
  ▼
CoinGecko Service Layer
  │
  ▼
HTTPX Async Client
  │
  ▼
CoinGecko API
```

The API layer is responsible for receiving and validating requests, while the service layer is responsible for communication with the external cryptocurrency service.

---

## API Endpoints

### 1. Health Check

```http
GET /health
```

The health endpoint is intentionally public.

Example response:

```json
{
  "status": "healthy",
  "app_name": "Vetty Python API",
  "version": "1.0.0"
}
```

The technical exercise requires the health endpoint to report application health and application version, as well as external cryptocurrency service information as the implementation is completed.

---

### 2. List Coins

```http
GET /coins
```

Returns a paginated list of cryptocurrencies.

#### Query Parameters

| Parameter  | Type    | Default | Rules                     |
| ---------- | ------- | ------: | ------------------------- |
| `page_num` | integer |     `1` | Must be ≥ 1               |
| `per_page` | integer |    `10` | Must be between 1 and 100 |

Example:

```http
GET /coins?page_num=1&per_page=10
```

Example response:

```json
[
  {
    "id": "bitcoin",
    "name": "Bitcoin",
    "symbol": "btc"
  }
]
```

---

### 3. List Categories

```http
GET /categories
```

Returns a paginated list of cryptocurrency categories.

#### Query Parameters

| Parameter  | Type    | Default | Rules                     |
| ---------- | ------- | ------: | ------------------------- |
| `page_num` | integer |     `1` | Must be ≥ 1               |
| `per_page` | integer |    `10` | Must be between 1 and 100 |

Example:

```http
GET /categories?page_num=1&per_page=10
```

---

### 4. Market Data

```http
GET /market-data
```

Returns cryptocurrency market data in **CAD**.

At least one of `coin_id` or `category` must be provided.

#### Query Parameters

| Parameter  | Type    | Required    | Rules                   |
| ---------- | ------- | ----------- | ----------------------- |
| `coin_id`  | string  | Conditional | Minimum length 1        |
| `category` | string  | Conditional | Minimum length 1        |
| `page_num` | integer | No          | Default 1, must be ≥ 1  |
| `per_page` | integer | No          | Default 10, maximum 100 |

Examples:

```http
GET /market-data?coin_id=bitcoin
```

```http
GET /market-data?category=defi
```

Pagination can also be used:

```http
GET /market-data?coin_id=bitcoin&page_num=1&per_page=10
```

If neither `coin_id` nor `category` is supplied, the API returns a validation error.

---

## Authentication

All application endpoints except `/health` are protected using an API key.

The API key is provided through the request header:

```http
X-API-Key: <your-api-key>
```

Example:

```http
X-API-Key: vetty-development-key
```

The API key is stored in the environment configuration and is not committed to Git.

---

## Configuration

Configuration is loaded through environment variables.

Create a `.env` file in the project root:

```env
APP_NAME=Vetty Python API
APP_VERSION=1.0.0

COINGECKO_BASE_URL=https://api.coingecko.com/api/v3

CACHE_TTL=60

WEBHOOK_URL=

API_KEY=your-development-api-key
```

### Configuration Variables

| Variable             | Description                |
| -------------------- | -------------------------- |
| `APP_NAME`           | Application name           |
| `APP_VERSION`        | Application version        |
| `COINGECKO_BASE_URL` | Base URL for CoinGecko API |
| `CACHE_TTL`          | Cache lifetime in seconds  |
| `WEBHOOK_URL`        | Webhook destination        |
| `API_KEY`            | API authentication key     |

Sensitive configuration should be provided through environment variables rather than hardcoded in source code.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shivanigujar01/vetty-python-api.git
cd vetty-python-api
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` in the project root and provide the required configuration values.

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger can be used to test authenticated endpoints by providing the required API key.

---

## Validation

The API validates incoming query parameters.

Examples of invalid requests include:

```http
GET /coins?page_num=0
```

```http
GET /coins?per_page=101
```

```http
GET /market-data
```

The API uses FastAPI/Pydantic validation for parameter constraints and application-level validation for business rules.

---

## External API Integration

The application communicates with CoinGecko using HTTPX's asynchronous client.

External requests use a configured timeout and handle:

* Request timeouts
* Connection/request failures
* HTTP status errors returned by CoinGecko

This prevents external service failures from being silently ignored.

---

## Error Handling

External API failures are detected in the CoinGecko service layer.

The application is designed to provide meaningful and consistent HTTP responses for:

* Invalid requests
* Authentication failures
* External API failures
* Timeouts
* Other application errors

Centralized exception handling is being implemented as part of the project's error-handling layer.

---

## Pagination

List endpoints support:

```text
page_num
per_page
```

The default page number is:

```text
1
```

The default page size is:

```text
10
```

The maximum supported page size is:

```text
100
```

Pagination is applied after retrieving the relevant data from the external service.

---

This makes the development process easier to review and understand.

---

## Current Implementation Status

### Completed

* [x] Initial FastAPI application
* [x] Project structure
* [x] Environment-based configuration
* [x] CoinGecko API integration
* [x] Coins endpoint
* [x] Categories endpoint
* [x] Market data endpoint
* [x] Pagination
* [x] API-key authentication
* [x] Request validation
* [x] Basic response validation
* [x] External API timeout handling
* [x] External API connection error handling
* [x] External API HTTP error handling

### Remaining

* [ ] Centralized exception handling
* [ ] Structured logging
* [ ] In-memory caching with configurable TTL
* [ ] Webhook notification after successful uncached market-data retrieval
* [ ] Comprehensive unit tests and coverage
* [ ] Additional Swagger/API documentation improvements
* [ ] Docker support
* [ ] Linting and quality checks
* [ ] Final cleanup and production-readiness review

---

## Running Tests

Tests will be added and expanded as part of the testing stage.

The target is to provide meaningful unit-test coverage for the API and service layers, with a goal of exceeding 80% coverage where practical.

---

## Future Improvements

The remaining implementation will focus on:

1. Centralized exception handling
2. Structured logging
3. In-memory caching
4. Webhook notifications
5. Unit tests and coverage
6. API documentation improvements
7. Dockerization
8. Linting and code-quality checks
9. Final production-readiness review

---

## Security Considerations

* API keys are loaded from environment variables.
* `.env` is excluded from Git using `.gitignore`.
* Application endpoints are protected using API-key authentication.
* External HTTP calls use a configured timeout.
* Sensitive configuration is not hardcoded in the application source code.

---

## License

This project was created as a technical assessment project.
