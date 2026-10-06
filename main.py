from fastapi import FastAPI

app = FastAPI()# create fastApi application


@app.get("/health")
def health():
    return {"status": "healthy"}