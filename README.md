# 🌍 Avrupa Arama Botu - Advanced Search Tool

**Multi-user, spam-protected web scraper for European business data**  
*(3 kullanıcılı, Excel raporlamalı gelişmiş arama motoru)*

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Temel Özellikler
- **Çoklu Arama Motoru** (Google/Bing/Yandex/DuckDuckGo)
- **Avrupa Ülke/Şehir Filtreleme** (35+ ülke, 500+ şehir)
- **3 Kullanıcılı Yönetim Paneli** (Admin/Editor/Viewer)
- **Otomatik Excel Raporu** (Filtreli, formatlı çıktı)
- **Spam Koruması** (CAPTCHA + IP Limit + Aktivite İzleme)

## 🛠 Kurulum
```bash
# 1. Gereksinimler
brew install python git

# 2. Projeyi klonla
git clone https://github.com/[KULLANICI_ADINIZ]/avrupa-arama-botu.git
cd avrupa-arama-botu

# 3. Sanal ortam oluştur
python3 -m venv venv
source venv/bin/activate

# 4. Paketleri yükle
pip install -r requirements.txt
