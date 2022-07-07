from fastapi import APIRouter
from config.db import conn
from models.TipoCarta import TipoCarta
from models.card import card
from models.rareza import Rareza
from models.TipoClase import TipoClase

user = APIRouter()

@user.get("/card")
def get_users():
    return conn.execute(card.select()).fetchall()

@user.get("/TipoCarta")
def helloword():
    return conn.execute(TipoCarta.select()).fetchall()

@user.get("/rareza")
def helloword():
    return conn.execute(Rareza.select()).fetchall()

@user.get("/tipoClase")
def helloword():
    return conn.execute(TipoClase.select()).fetchall()