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
    
        try:
            respuesta_lenin = await client.get("http://serviciolenin/serviciolenin")
            data_lenin = respuesta_lenin.json()
        except httpx.RequestError:
            data_lenin = "El servicio de Lenin no está disponible"

        try:
            respuesta_luis = await client.get("http://servicio_luis/servicioluis")
            data_luis = respuesta_luis.json()
        except httpx.RequestError:
            data_luis = "El servicio de Luis no está disponible"


    return {"respuesta_kelly": data_a,"respuesta_lenin": data_lenin}