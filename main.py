from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

# Definisi model Pydantic bernama "Item" dengan tiga bidang: id, nama, dan harga.
class Article(BaseModel):
    id: int
    name: str
    price: float

app = FastAPI()

# Rute untuk halaman beranda yang menampilkan pesan selamat datang.
@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI application'}

# Daftar kosong untuk menyimpan artikel yang dibuat.
article = []

# Rute untuk mendapatkan semua artikel yang disimpan dalam daftar.
# Parameter "response_model" menentukan bahwa respons akan berupa daftar objek "Artikel".
@app.get('articles', response_model=List[Article])
async def read_articles():
    return articles # type: ignore

# Rute untuk membuat artikel baru.
# Parameter "response_model" menentukan bahwa respons akan berupa objek "Artikel".
@app.post('/articles', response_model=List[Article])
async def create_article(article: Article):
    articles.append(article) # type: ignore # Menambahkan artikel ke daftar.
    return articles # type: ignore

# Rute untuk memperbarui artikel yang sudah ada berdasarkan ID-nya.
# Parameter "response_model" menentukan bahwa respons akan berupa objek "Artikel".
@app.put('articles/{article_id}', response_model=List[Article])
async def update_article(article_id: int, article: Article):
    articles[article_id] = article # type: ignore # Memperbarui artikel dalam daftar.
    return articles # type: ignore

# Rute untuk menghapus artikel berdasarkan ID-nya.
# "response_model" tidak ditentukan karena tidak ada objek yang dikembalikan dalam respons.
@app.delete('articles/{article_id}')
async def delete_article(article_id: int):
    del articles[article_id] # type: ignore
    return {'message': 'Article deleted'}

