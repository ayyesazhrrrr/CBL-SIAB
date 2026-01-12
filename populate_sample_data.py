"""
Script untuk mengisi database dengan sample data dari CSV
Jalankan: python populate_sample_data.py
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siab_project.settings')
django.setup()

from stock_prediction.models import Prediction
from stock_prediction.ml_model import SIABModel
import pandas as pd

def populate_data():
    """Populate database with sample predictions"""
    print("Loading model...")
    model = SIABModel()
    
    print("Loading CSV data...")
    csv_path = "data/BBCA.JK_extended.csv"
    
    if not os.path.exists(csv_path):
        print(f"Error: File {csv_path} tidak ditemukan!")
        return
    
    # Predict from CSV
    print("Making predictions...")
    df_result = model.predict_from_csv(csv_path)
    
    # Clear existing data (optional)
    print(f"Current predictions in DB: {Prediction.objects.count()}")
    response = input("Hapus data lama? (y/n): ")
    if response.lower() == 'y':
        Prediction.objects.all().delete()
        print("Data lama dihapus.")
    
    # Save last 50 predictions to database
    print("Saving predictions to database...")
    saved_count = 0
    for _, row in df_result.tail(50).iterrows():
        Prediction.objects.create(
            open_price=row["Open"],
            high_price=row["High"],
            low_price=row["Low"],
            close_price=row["Close"],
            volume=int(row["Volume"]),
            ma5=row["MA5"],
            ma10=row["MA10"],
            return_value=row["Return"],
            return_1=row["Return_1"],
            ma_diff=row["MA_diff"],
            predicted_label=int(row["Predicted_Label"]),
            probability=row["Probability"],
            rekomendasi_aksi=row.get("Recommendation", "HOLD")
        )
        saved_count += 1
    
    print(f"\nBerhasil menyimpan {saved_count} prediksi ke database!")
    print(f"Total predictions sekarang: {Prediction.objects.count()}")
    print("\nSekarang buka /visualize/ untuk melihat chart!")

if __name__ == "__main__":
    populate_data()
