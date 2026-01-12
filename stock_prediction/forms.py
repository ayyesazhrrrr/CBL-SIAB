from django import forms
from .models import Prediction
import pandas as pd


class PredictionForm(forms.Form):
    """Form untuk input manual prediksi"""
    open_price = forms.FloatField(
        label='Open Price',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 10000',
            'step': '0.01'
        })
    )
    high_price = forms.FloatField(
        label='High Price',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 10500',
            'step': '0.01'
        })
    )
    low_price = forms.FloatField(
        label='Low Price',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 9800',
            'step': '0.01'
        })
    )
    close_price = forms.FloatField(
        label='Close Price',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 10200',
            'step': '0.01'
        })
    )
    volume = forms.IntegerField(
        label='Volume',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 50000000'
        })
    )
    ma5 = forms.FloatField(
        label='MA5 (Moving Average 5 days)',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 10100',
            'step': '0.01'
        })
    )
    ma10 = forms.FloatField(
        label='MA10 (Moving Average 10 days)',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 10050',
            'step': '0.01'
        })
    )
    return_value = forms.FloatField(
        label='Return',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 0.005',
            'step': '0.0001'
        })
    )
    return_1 = forms.FloatField(
        label='Return_1 (Previous Return)',
        widget=forms.NumberInput(attrs={
            'class': 'input-pro',
            'placeholder': 'e.g., 0.003',
            'step': '0.0001'
        })
    )


class CSVUploadForm(forms.Form):
    """Form untuk upload CSV file"""
    csv_file = forms.FileField(
        label='Upload CSV File',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.csv'
        }),
        help_text='File CSV harus memiliki kolom: Date, Open, High, Low, Close, Volume'
    )
    
    def clean_csv_file(self):
        csv_file = self.cleaned_data['csv_file']
        
        # Check file extension
        if not csv_file.name.endswith('.csv'):
            raise forms.ValidationError('File harus berformat CSV')
        
        # Check file size (max 10MB)
        if csv_file.size > 10 * 1024 * 1024:
            raise forms.ValidationError('File terlalu besar. Maksimal 10MB')
        
        # Try to read CSV
        try:
            df = pd.read_csv(csv_file)
            required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
            
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise forms.ValidationError(
                    f'Kolom yang hilang: {", ".join(missing_columns)}'
                )
            
            # Reset file pointer
            csv_file.seek(0)
            
        except pd.errors.EmptyDataError:
            raise forms.ValidationError('File CSV kosong')
        except Exception as e:
            raise forms.ValidationError(f'Error membaca CSV: {str(e)}')
        
        return csv_file
