from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    # siempre que llamamos a un servidor, la operación que se ejecuta tiene que se asíncrona
    # que signific síncrono? que hasta que el servidor no mande nada, la web/aplicación no se va a cargar
    return "Hello World"

@app.get("/url")
async def url():
    # siempre que llamamos a un servidor, la operación que se ejecuta tiene que se asíncrona
    # que signific síncrono? que hasta que el servidor no mande nada, la web/aplicación no se va a cargar
    return {"url_curso": "https://mouredev.com/python"}