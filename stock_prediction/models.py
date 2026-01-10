from django.db import models
from django.utils import timezone


class StockData(models.Model):
    """Model untuk menyimpan data saham historis"""
    date = models.DateTimeField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.BigIntegerField()
    
    # Technical indicators
    ma5 = models.FloatField(null=True, blank=True)
    ma10 = models.FloatField(null=True, blank=True)
    return_value = models.FloatField(null=True, blank=True)
    return_1 = models.FloatField(null=True, blank=True)
    ma_diff = models.FloatField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Stock Data'
        verbose_name_plural = 'Stock Data'
    
    def __str__(self):
        return f"BBCA - {self.date.strftime('%Y-%m-%d')}"


class Prediction(models.Model):
    """Model untuk menyimpan hasil prediksi"""
    LABEL_CHOICES = [
        (0, 'Turun'),
        (1, 'Naik'),
    ]
    
    stock_data = models.ForeignKey(StockData, on_delete=models.CASCADE, null=True, blank=True)
    
    # Input features
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.BigIntegerField()
    ma5 = models.FloatField()
    ma10 = models.FloatField()
    return_value = models.FloatField()
    return_1 = models.FloatField()
    ma_diff = models.FloatField()
    
    # Prediction results
    predicted_label = models.IntegerField(choices=LABEL_CHOICES)
    probability = models.FloatField()
    rekomendasi_aksi = models.CharField(max_length=16, null=True, blank=True, help_text="Rekomendasi aksi trading: BUY/SELL")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Prediction'
        verbose_name_plural = 'Predictions'
    
    def __str__(self):
        label_text = 'Naik' if self.predicted_label == 1 else 'Turun'
        return f"Prediction: {label_text} ({self.probability:.2%}) - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    def get_label_display_custom(self):
        return 'Naik' if self.predicted_label == 1 else 'Turun'
