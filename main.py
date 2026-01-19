from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    name:str
    edad:int

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Buenos días grupo."}

@app.get('/caffe')
async def read_root():
    return {"message": "el caffe esta bueno"}

@app.post('/usuarios')
async def crear_usuario(usuario: Usuario):
    return {'usuario': usuario, 'name':usuario.name, 'edad': usuario.edad}

