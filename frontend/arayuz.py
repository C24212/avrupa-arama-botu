# backend/bot.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def ara(ulke: str, sehir: str, max_sonuc: int = 50) -> list:
    """Avrupa şehirlerine göre veri toplar"""
    print(f"🔍 {ulke}/{sehir} için arama başlatılıyor...")
    
    # Örnek veri (gerçekte web scraping yapılacak)
    veriler = [
        {"email": "info@example.com", "telefon": "+901234567890"},
        {"email": "contact@test.com", "telefon": "+901234567891"}
    ]
    return veriler[:max_sonuc]

def excel_kaydet(veriler: list, dosya_adi: str = "sonuclar.xlsx"):
    """Excel'e kaydetme fonksiyonu"""
    df = pd.DataFrame(veriler)
    df.to_excel(dosya_adi, index=False)
    print(f"✅ {len(df)} kayıt {dosya_adi} dosyasına kaydedildi")

if __name__ == "__main__":
    sonuclar = ara("Türkiye", "İstanbul", 10)
    excel_kaydet(sonuclar)
