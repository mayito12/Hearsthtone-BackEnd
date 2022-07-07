from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.TipoCarta import TipoCarta
from schemas.tipocarta import tipocarta

r_tipocarta = APIRouter()

@r_tipocarta.get("/typecard")
def get_all_typescards():
    return conn.execute(TipoCarta.select()).fetchall()

@r_tipocarta.get("/Typecard/{id}")
def get_typecard_id(id : int):
    res = conn.execute(TipoCarta.select().where(TipoCarta.c.id == id)).first()
    print(res)
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")

    return conn.execute(TipoCarta.select().where(TipoCarta.c.id== id)).first()

@r_tipocarta.post("/Typecard/create")
def create_Typecard(new_TipoCarta : tipocarta):
    new_typecard = {
        "id" : new_TipoCarta.id,
        "name" : new_TipoCarta.name 
        }
    result = conn.execute(TipoCarta.insert().values(new_typecard))
    return conn.execute(TipoCarta.select().where(TipoCarta.c.id == result.lastrowid)).first()

@r_tipocarta.delete("/Typecard/delete/{id}")
def delete_Typecard(id : int):
    res = conn.execute(TipoCarta.delete().where(TipoCarta.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)