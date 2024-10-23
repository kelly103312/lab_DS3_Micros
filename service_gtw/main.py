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

        try:
            respuesta_luis = await client.get("http://servicioluis/servicioluis")
            data_luis = respuesta_luis.json()
        except httpx.RequestError:
            data_luis = "El servicio de Luis no está disponible"
        
        try:
            respuesta_eyder = await client.get("http://servicioeyder/servicioeyder")
            data_eyder = respuesta_eyder.json()
        except httpx.RequestError:
            data_eyder = "El servicio de Eyder no está disponible"
        try:
            respuesta_july = await client.get("http://servicio-july-service/info")
            data_july = respuesta_july.json()
        except httpx.RequestError:
            data_july = "El servicio de July no está disponible"
        try:
            respuesta_a = await client.get("http://servicio-hernan-service/info")
            data_hernan = respuesta_a.json()
        except httpx.RequestError:
            data_hernan = "El servicio de hernan no está disponible"


    return {
        "respuesta_kelly": data_kelly,
        "respuesta_lenin": data_lenin,
        "respuesta_santi": data_santi,
        "respuesta_luis": data_luis,
        "respuesta_eyder": data_eyder,
        "respuesta_july": data_july,
        "respuesta_hernan": data_hernan,
    }