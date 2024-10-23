from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def read_info_personal():
    return {
        "nombre": "Hernan",
        "edad": "23",
        "gustos":"Idiomas, puzzles, tech, musica"
    }
