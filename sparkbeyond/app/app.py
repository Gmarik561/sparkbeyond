from fastapi import FastAPI
from typing import List
from process_articles import process_articles

app = FastAPI()

@app.get("/common-words/")
async def get_common_words(folder_path: str, num_articles: int = 4, top_n: int = 10):
    top_words = process_articles(folder_path, num_articles, top_n)
    return {"top_words": top_words}
