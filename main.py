from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Articulo(BaseModel):
    id: int
    titulo: str
    descripcion: str

# Almacenamiento temporal en memoria
articulos = []

@app.post("/articulos/")
async def crear_articulo(articulo: Articulo):
    articulos.append(articulo)
    return {"mensaje": "Artículo creado", "articulo": articulo}

@app.get("/articulos/", response_model=List[Articulo])
async def leer_articulos():
    return articulos
