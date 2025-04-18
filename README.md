# SENKRON AI Core V1

Bu proje FastAPI ile hazırlanmış, astro-finansal ve zaman tabanlı yapay zeka sisteminin çekirdek versiyonudur.

## Özellikler:
- `/senkron/status` ➔ Sistem durumu
- `/senkron/predict` ➔ Basit tahmin API'si
- `/docs` ➔ Swagger UI
- `/redoc` ➔ ReDoc API dökümantasyonu

## Çalıştırmak İçin:
- `pip install -r requirements.txt`
- `uvicorn app.main:app --reload`