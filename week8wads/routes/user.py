from fastapi import APIRouter
from config.db import conn
from models.index import users
import schemas.index import User
user = APIRouter

@user.get("/")
async def read_data():
    return conn.execute(users.select())

@user.get("/{id}")
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.get("/")
async def write_data(user: User):
    return conn.execute(users.insert().values(
       name=user.name,
       email=user.email,
       password=user.password
       )).fetchall()

 