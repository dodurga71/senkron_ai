from fastapi import FastAPI
from routes.status import router as status_router
from routes.predict import router as predict_router

app = FastAPI(
    title="SENKRON AI",
    description="Geleceğin astro-finansal yapay zekâ motoru.",
    version="1.0.0",
)

app.include_router(status_router, prefix="/senkron")
app.include_router(predict_router, prefix="/senkron")