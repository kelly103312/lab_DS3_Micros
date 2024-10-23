from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/servicioeyder")
async def root():
    words = ["Eyder", "visited", "this", "amazing", "service", "and", "left", "his", "mark", "here!"]
    random.shuffle(words)  
    return {"message": " ".join(words)}
