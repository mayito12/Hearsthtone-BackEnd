from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.TipoClase import TipoClase
from schemas.tipoclase import tipoclase

r_tipoclase = APIRouter()

@r_tipoclase.get("/typeclass")
def get_all_typesclass():
    return conn.execute(TipoClase.select()).fetchall()

@r_tipoclase.get("/Typeclass/{id}")
def get_typeclass_id(id : int):
    res = conn.execute(TipoClase.select().where(TipoClase.c.id == id)).first()
    print(res)
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")

    return conn.execute(TipoClase.select().where(TipoClase.c.id== id)).first()

@r_tipoclase.post("/Typeclass/create")
def create_Typecard(new_TypeClass : tipoclase):
    new_typeclass = {
        "id" : new_TypeClass.id,
        "name" : new_typeclass.name 
        }
    result = conn.execute(TipoClase.insert().values(new_typeclass))
    return conn.execute(TipoClase.select().where(TipoClase.c.id == result.lastrowid)).first()

@r_tipoclase.delete("/Typeclass/delete/{id}")
def delete_Typecard(id : int):
    res = conn.execute(TipoClase.delete().where(TipoClase.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)