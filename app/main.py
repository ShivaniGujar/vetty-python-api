from fastapi import FastAPI

from app.config import settings

app =FastAPI(
    title=settings.app_name,
    version=settings.app_version
) # create FastAPI application object


@app.get("/health")
def health():
    return{
        "status":"healthy",
        "app_name":settings.app_name,
        "version":settings.app_version
        
        }