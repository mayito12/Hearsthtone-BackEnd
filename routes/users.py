from fastapi import APIRouter
from config.db import conn
from models.user import users

user = APIRouter()

@user.get("/user")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/user")
def helloword():
    return "hello word"

@user.get("/user")
def helloword():
    return "hello word"

@user.get("/user")
def helloword():
    return "hello word"