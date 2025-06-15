from src.summarizer import TextSummarizer

def test_summarizer():
    model = TextSummarizer()
    result = model.summarize("Transformers are a new state-of-the-art NLP model architecture.")
    assert isinstance(result, str)
    assert len(result) > 0