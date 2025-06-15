# 🚀 Text Summarizer API

This is a text summarization service using HuggingFace's BART model. It exposes both a REST API and a Streamlit UI.

## 🧪 How to Run
```bash
git clone https://github.com/yourusername/text-summarizer-api.git
cd text-summarizer-api
pip install -r requirements.txt

# API
uvicorn src.main:app --reload

# Streamlit UI
streamlit run streamlit_app.py
```

## 🐳 Docker
```bash
docker build -t text-summarizer .
docker run -p 8000:8000 text-summarizer
```

## 🧪 Test
```bash
pytest
```

## 🔗 Endpoints
- `POST /summarize` → Accepts `{text: "..."}` and returns summary

## 📦 Tech Stack
Python, FastAPI, Streamlit, Transformers (BART), GitHub Actions

## 📄 License
MIT
