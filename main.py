from fastapi import FastAPI
from routes.status import router as status_router
from routes.predict import router as predict_router
from engines.energy_engine import calculate_energy_flow
from engines.finance_engine import calculate_finance
from engines.quantum_engine import run_quantum_analysis
from engines.astro_engine import generate_astro_report

app = FastAPI(
    title="SENKRON AI Core V1",
    description="Geleceğin astro-finansal ve zaman tabanlı yapay zeka motoru.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(status_router, prefix="/senkron")
app.include_router(predict_router, prefix="/senkron")
