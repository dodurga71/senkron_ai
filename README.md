# SENKRON AI Core V1

Bu proje FastAPI ile hazırlanmış, astro-finansal ve zaman tabanlı yapay zeka motorunun çekirdek versiyonudur.

## Özellikler:
- `/senkron/status` ➔ Sunucu sağlık kontrolü
- `/senkron/predict` ➔ Basit sayı tahmini
- `/docs` ➔ API dokümantasyonu (Swagger UI)
- `/redoc` ➔ Alternatif API dokümantasyonu

## Başlatmak İçin:
- `pip install -r requirements.txt`
- `uvicorn main:app --reload`