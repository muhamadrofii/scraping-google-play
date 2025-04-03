# 📥 Google Play Store Scraper  

Scraping data aplikasi dari Google Play Store menggunakan **Google-Play-Scraper** dengan Python. Repositori ini berisi skrip untuk mengambil data aplikasi seperti nama, rating, jumlah ulasan, deskripsi, dan informasi lainnya langsung dari Play Store.  

## 🚀 Fitur  
✅ Scraping informasi aplikasi (nama, developer, rating, jumlah download, dll.)  
✅ Scraping ulasan aplikasi dengan filter rating dan jumlah ulasan  
✅ Simpan hasil scraping ke format **CSV** atau **JSON**  
✅ Menggunakan **Google-Play-Scraper** yang efisien dan mudah digunakan  

## 🛠️ Instalasi  
Pastikan Python sudah terinstal, lalu jalankan perintah berikut:  

```bash
pip install google-play-scraper pandas
```

# 📌 Penggunaan


```Python
from google_play_scraper import app

result = app('com.example.app')  # Ganti dengan package name aplikasi
print(result)

from google_play_scraper import reviews, Sort

reviews_list, _ = reviews(
    'com.example.app',  
    count=100,  
    sort=Sort.NEWEST  
)
print(reviews_list)

```

## 📂 Output

Hasil scraping dapat disimpan ke CSV atau JSON untuk analisis lebih lanjut.

## 🔥 Kontribusi
Jika ingin berkontribusi, silakan buat Pull Request atau laporkan masalah di Issues.

📌 Repo ini dibuat oleh Fathony Syaennulloh untuk keperluan riset dan eksplorasi data. 🚀✨