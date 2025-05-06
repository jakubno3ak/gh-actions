from fastapi import FastAPI
from src.inference import Inference
from settings import settings

app = FastAPI()
inference = Inference(settings=settings)


@app.get("/health")
async def health():
    return 200


@app.get("/")
async def home():
    return {"INFO": "Go to '/docs' endpoint"}


@app.post("/predict")
async def predict(text: str):
    return {"sentiment": inference.predict(text)}
