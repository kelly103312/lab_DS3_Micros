from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://servicio-kelly-service/info")
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "El servicio A no está disponible"
    
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://serviciolenin:8000/serviciolenin")
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "El servicio de Lenin no está disponible"


    return {"respuesta_a": data_a}