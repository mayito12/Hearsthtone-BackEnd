from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.card import card
from schemas.card import Card

r_card = APIRouter()

@r_card.get("/card")
def get_all_cards():
    return conn.execute(card.select()).fetchall()

@r_card.get("/dishes/{id}")
def get_card(id : int):
    res = conn.execute(card.select().where(card.c.id == id)).first()
    print(res)
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")

    return conn.execute(card.select().where(card.c.id== id)).first()

@r_card.post("/card/create")
def create_card(new_card : Card):
    new_card = {
        "id" : new_card.id,
        "name" : new_card.name, 
        "description" : new_card.description, 
        "id_R" : new_card.id_R, 
        "id_tc" : new_card.id_tc, 
        "id_TClass": new_card.id_TClass}
    result = conn.execute(card.insert().values(new_card))
    return conn.execute(card.select().where(card.c.id == result.lastrowid)).first()

@r_card.delete("/card/delete/{id}")
def delete_card(id : int):
    res = conn.execute(card.delete().where(card.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)
    

