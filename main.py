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
articles = []

# Rute untuk mendapatkan semua artikel yang disimpan dalam daftar.
# Parameter "response_model" menentukan bahwa respons akan berupa daftar objek "Artikel".
@app.get('/articles', response_model=List[Article])
async def read_articles():
    return articles

# Rute untuk membuat artikel baru.
# Parameter "response_model" menentukan bahwa respons akan berupa objek "Artikel".
@app.post('/articles', response_model=List[Article])
async def create_article(article: Article):
    articles.append(article) # Menambahkan artikel ke daftar.
    return articles

# Rute untuk memperbarui artikel yang sudah ada berdasarkan ID-nya.
# Parameter "response_model" menentukan bahwa respons akan berupa objek "Artikel".
@app.put('/articles/{id}', response_model=Article)
async def update_article(id: int, article: Article):
    articles[id] = article # Memperbarui artikel dalam daftar.
    return article

# Rute untuk menghapus artikel berdasarkan ID-nya.
# "response_model" tidak ditentukan karena tidak ada objek yang dikembalikan dalam respons.
@app.delete('/articles/{id}')
async def delete_article(id: int):
    del articles[id]
    return {'message': 'Article deleted'}

