from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def read_info_personal():
    return {
        "nombre": "Juleipssy",
        "edad": "20",
        "gustos":"Música, fútbol, leer, ver peliculas"
    }
