from fastapi import Request
from fastapi.responses import JSONResponse


class ExternalServiceError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


async def external_service_exception_handler(
    request: Request,
    exc: ExternalServiceError
):
    return JSONResponse(
        status_code=503,
        content={
            "error": {
                "code": "EXTERNAL_SERVICE_ERROR",
                "message": exc.message
            }
        }
    )