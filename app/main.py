from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from transformers import pipeline
from app.models import ModelManager
from app.cache import cache, get_cached_response, set_cached_response
from app.auth import get_current_user

app = FastAPI()

model_manager = ModelManager()

class TextInput(BaseModel):
    text: str
    task: str

@app.post("/evaluate/")
async def evaluate(input: TextInput, user: str = Depends(get_current_user)):
    if input.task not in ["text-classification", "ner", "question-answering", "summarization"]:
        raise HTTPException(status_code=400, detail="Invalid task type")

    cached_response = get_cached_response(input.text, input.task)
    if cached_response:
        return cached_response

    results = model_manager.evaluate(input.text, input.task)
    set_cached_response(input.text, input.task, results)
    return results

@app.post("/benchmark/")
async def benchmark(dataset: str, user: str = Depends(get_current_user)):
    results = model_manager.benchmark(dataset)
    return results

@app.get("/health/")
async def health():
    return {"status": "ok"}
