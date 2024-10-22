from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def read_info_personal():
    return {
        "nombre": "Kelly",
        "edad": "23",
        "gustos":"Música, animalitos, leer, tecnología 📚"
    }
