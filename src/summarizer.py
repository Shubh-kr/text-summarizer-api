from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.summarizer import TextSummarizer

app = FastAPI()
summarizer = TextSummarizer()

class TextIn(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(payload: TextIn):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Input text is empty")
    summary = summarizer.summarize(payload.text)
    return {"summary": summary}