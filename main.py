from fastapi import FastAPI
from routes.status import router as status_router

app = FastAPI(
    title="SENKRON AI",
    description="Geleceğin astro-finansal yapay zekâ motoru.",
    version="1.0.0",
)

app.include_router(status_router, prefix="/senkron")