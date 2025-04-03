# Install library jika belum terpasang
# pip install google-play-scraper pandas numpy

from google_play_scraper import Sort, reviews
import pandas as pd
import time
import os
import numpy as np

# ID Aplikasi yang ingin diambil ulasannya
app_id = 'com.ss.android.ugc.trill'
num_reviews = 1000  # Jumlah ulasan yang ingin diambil

# Fungsi untuk mengumpulkan ulasan
def collect_reviews(app_id, num_reviews):
    all_reviews = []
    batch_size = 200  # Ambil ulasan dalam batch kecil agar tidak terkena rate limit

    while len(all_reviews) < num_reviews:
        try:
            batch_reviews, _ = reviews(
                app_id,
                lang='id',  # Bahasa Indonesia
                country='id',  # Negara Indonesia
                sort=Sort.MOST_RELEVANT,
                count=min(batch_size, num_reviews - len(all_reviews)),
                filter_score_with=None if len(all_reviews) == 0 else 3,  # Ambil semua skor
            )
            all_reviews.extend(batch_reviews)
            time.sleep(1)  # Hindari terlalu sering mengakses server

        except Exception as e:
            print(f"Error occurred: {e}")
            break

    return all_reviews[:num_reviews]

# Ambil data ulasan
app_reviews = collect_reviews(app_id, num_reviews)

# Konversi ke DataFrame Pandas
df_busu = pd.DataFrame(np.array(app_reviews), columns=['review'])
df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))

# Cek jumlah ulasan yang berhasil diambil
print(f"Jumlah data yang diperoleh: {len(df_busu.index)}")

# Simpan ke dalam file CSV
folder = "data"
os.makedirs(folder, exist_ok=True)  # Pastikan folder ada
file_path = os.path.join(folder, "datasettiktok.csv")  # Simpan di dalam folder 'data'

df_busu.to_csv(file_path, index=False)
print(f"Data berhasil disimpan di: {file_path}")
