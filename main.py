from fastapi import FastAPI
from routes.status import router as status_router

app = FastAPI(
    title="Senkron AI",
    description="Geleceği astro-finansal örüntülerle tahmin eden yapay zeka sistemi",
    version="1.0.0",
    docs_url="/docs",     # Swagger UI aktif
    redoc_url="/redoc"    # Alternatif ReDoc dökümanı aktif
)

# Ana rotaları ekliyoruz
app.include_router(status_router)

@app.get("/")
async def root():
    return {"message": "Welcome to SENKRON AI. API is up and running!"}
