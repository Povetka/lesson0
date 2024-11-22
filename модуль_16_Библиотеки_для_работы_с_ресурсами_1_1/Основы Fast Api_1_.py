# !!! Запускать из файла mainn

from fastapi import FastAPI

app = FastAPI()  # Инициализация приложения


@app.get("/")  # Гет запрос, если мы получили гет запрос такого типа, сделай функцию ниже
async def welcome() -> dict:  # Указали какой тип данных возвращает функция. Необязательно, но полезно.
    return {"message": "Hello world"}


@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main page"}
