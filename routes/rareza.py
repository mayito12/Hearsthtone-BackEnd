from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.rareza import Rareza
from schemas.rareza import rareza

r_rareza = APIRouter()

@r_rareza.get("/rareza")
def get_all_rarezas():
    return conn.execute(Rareza.select()).fetchall()

@r_rareza.get("/rareza/{id}")
def get_rareza_id(id : int):
    res = conn.execute(Rareza.select().where(Rareza.c.id == id)).first()
    print(res)
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")

    return conn.execute(Rareza.select().where(Rareza.c.id== id)).first()

@r_rareza.post("/rareza/create")
def create_rareza(new_rareza : rareza):
    new_card = {
        "id" : new_rareza.id,
        "name" : new_rareza.name 
        }
    result = conn.execute(Rareza.insert().values(new_card))
    return conn.execute(Rareza.select().where(Rareza.c.id == result.lastrowid)).first()

@r_rareza.delete("/rareza/delete/{id}")
def delete_rareza(id : int):
    res = conn.execute(Rareza.delete().where(Rareza.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)