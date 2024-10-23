from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://servicio-kelly-service/info")
            data_kelly = respuesta_a.json()
        except httpx.RequestError:
            data_kelly = "El servicio de Kelly no está disponible"
    
        try:
            respuesta_lenin = await client.get("http://serviciolenin/serviciolenin")
            data_lenin = respuesta_lenin.json()
        except httpx.RequestError:
            data_lenin = "El servicio de Lenin no está disponible"

        try:
            respuesta_santi = await client.get("http://santi-service-service/greeting")
            data_santi = respuesta_santi.json()
        except httpx.RequestError:
            data_santi = "El servicio de Santi no está disponible"

    return {
        "respuesta_kelly": data_kelly,
        "respuesta_lenin": data_lenin,
        "respuesta_santi": data_santi,
    }