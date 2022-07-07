from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Meta, engine

card = Table(
    "card",
    Meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name",String(255)),
    Column("description",String(255))
)

Meta.create_all(engine)