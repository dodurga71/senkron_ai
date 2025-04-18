# Zaman hesaplamaları için yardımcı fonksiyonlar

def get_current_time():
    from datetime import datetime
    return datetime.utcnow().isoformat()