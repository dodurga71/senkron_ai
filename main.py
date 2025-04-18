from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Senkron AI Server Active. Welcome!"}

@app.get("/status")
async def get_status():
    return {"status": "success", "message": "Senkron AI is up and running!"}
