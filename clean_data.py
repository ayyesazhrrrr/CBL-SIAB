# Script untuk menghapus data duplikat dan reset database

from stock_prediction.models import Prediction

# Hapus semua prediksi lama
Prediction.objects.all().delete()

print("Database berhasil dibersihkan!")
