from fastapi import FastAPI
from routes.status import router as status_router
from routes.predict import router as predict_router

app = FastAPI(
    title="SENKRON AI Core V1",
    description="Geleceğin astro-finansal ve zaman tabanlı yapay zeka motoru.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(status_router, prefix="/senkron")
app.include_router(predict_router, prefix="/senkron")