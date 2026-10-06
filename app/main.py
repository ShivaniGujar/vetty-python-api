from fastapi import FastAPI
app =FastAPI() # create FastAPI application object


@app.get("/health")
def health():
    return{"status":"healthy"}