from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Meta, engine

card = Table(
    "card",
    Meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name",String(255)),
    Column("description",String(255)),
    Column("Id-tc", Integer, ForeignKey("TipoClase.id")),
    Column("Id-R", Integer,  ForeignKey("rareza.id")),
    Column("Id-TClass", Integer,  ForeignKey("TipoCarta.id"))
)

Meta.create_all(engine)