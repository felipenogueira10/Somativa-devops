import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def funcaoteste(true=None):
    return {"teste": true, "num_aleatorio": random.radint (0, 1000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0