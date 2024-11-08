from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class Article(BaseModel):
    id: int
    name: str
    price: float

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI application'}

article = []

@app.get('articles', response_model=List[Article])
async def read_articles():
    return articles # type: ignore

@app.post('/articles', response_model=List[Article])
async def create_article(article: Article):
    articles.append(article) # type: ignore
    return articles # type: ignore

@app.put('articles/{article_id}', response_model=List[Article])
async def update_article(article_id: int, article: Article):
    articles[article_id] = article # type: ignore
    return articles # type: ignore

@app.delete('articles/{article_id}')
async def delete_article(article_id: int):
    del articles[article_id] # type: ignore
    return {'message': 'Article deleted'}

