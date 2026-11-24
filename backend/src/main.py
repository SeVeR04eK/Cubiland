from fastapi import FastAPI

app = FastAPI(title="Cubiland API")

@app.get("/health")
async def health():
    return {"status": "ok"}
