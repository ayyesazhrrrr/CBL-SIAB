"""
ML Model Integration for SIAB Stock Prediction
Wrapper untuk model XGBoost yang sudah ditraining
"""

import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from django.conf import settings
from sklearn.preprocessing import StandardScaler


class SIABModel:
    """Wrapper class untuk model XGBoost SIAB"""
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.model_path = settings.MODEL_PATH
        self.threshold = 0.003  # 0.3% threshold seperti di notebook
        self.load_model()
    
    def load_model(self):
        """Load model dari file pkl"""
        try:
            self.model = joblib.load(self.model_path)
            print(f"Model loaded successfully from {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
    def calculate_features(self, df):
        """
        Calculate technical indicators (MA5, MA10, Return, Return_1, MA_diff)
        Input: DataFrame dengan kolom [Date, Open, High, Low, Close, Volume]
        Output: DataFrame dengan semua features
        """
        df = df.copy()
        
        # Ensure proper data types
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
        df['High'] = pd.to_numeric(df['High'], errors='coerce')
        df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
        df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
        
        # Moving Average 5 hari
        df['MA5'] = df['Close'].rolling(window=5).mean()
        
        # Moving Average 10 hari
        df['MA10'] = df['Close'].rolling(window=10).mean()
        
        # Return (untuk label, tapi kita tidak pakai di prediksi)
        df['Return'] = (df['Close'].shift(-1) - df['Close']) / df['Close']
        
        # Return_1 (percentage change)
        df['Return_1'] = df['Close'].pct_change()
        
        # MA difference
        df['MA_diff'] = df['MA5'] - df['MA10']
        
        # Drop rows with NaN values
        df = df.dropna()
        
        return df
    
    def prepare_features(self, data):
        """
        Prepare features untuk prediksi
        Input: dict atau DataFrame dengan data saham
        Output: numpy array siap untuk prediksi
        """
        if isinstance(data, dict):
            # Single prediction
            features = np.array([[
                data['Open'],
                data['High'],
                data['Low'],
                data['Close'],
                data['Volume'],
                data['MA5'],
                data['MA10'],
                data['Return'],
                data['Return_1'],
                data['MA_diff']
            ]])
        elif isinstance(data, pd.DataFrame):
            # Batch prediction
            feature_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 
                             'MA5', 'MA10', 'Return', 'Return_1', 'MA_diff']
            features = data[feature_columns].values
        else:
            raise ValueError("Data must be dict or DataFrame")
        
        return features
    
    def get_trading_recommendation(self, prediction_label, probability, probability_naik):
        """
        Generate trading recommendation based on prediction and confidence
        
        Logic:
        - BUY: Prediksi Naik dengan confidence >= 70%
        - SELL: Prediksi Turun dengan confidence >= 70%
        - HOLD: Confidence < 70% (tidak yakin)
        """
        confidence_threshold = 0.70  # 70% confidence threshold
        
        if prediction_label == 1 and probability >= confidence_threshold:
            return {
                'action': 'BUY',
                'action_text': '📈 BUY (Beli)',
                'reason': f'Prediksi NAIK dengan confidence {probability*100:.1f}%',
                'color': 'success'
            }
        elif prediction_label == 0 and probability >= confidence_threshold:
            return {
                'action': 'SELL',
                'action_text': '📉 SELL (Jual)',
                'reason': f'Prediksi TURUN dengan confidence {probability*100:.1f}%',
                'color': 'danger'
            }
        else:
            return {
                'action': 'HOLD',
                'action_text': '⏸️ HOLD (Tahan)',
                'reason': f'Confidence rendah ({probability*100:.1f}%), tunggu sinyal lebih jelas',
                'color': 'warning'
            }
    
    def predict(self, data):
        """
        Make prediction with trading recommendation
        Input: dict atau DataFrame
        Output: dict dengan label, probability, dan trading recommendation
        """
        if self.model is None:
            raise ValueError("Model not loaded")
        
        features = self.prepare_features(data)
        
        # Predict
        prediction = self.model.predict(features)
        probability = self.model.predict_proba(features)
        
        if len(prediction) == 1:
            # Single prediction
            pred_label = int(prediction[0])
            prob = float(probability[0][prediction[0]])
            prob_naik = float(probability[0][1])
            prob_turun = float(probability[0][0])
            
            # Get trading recommendation
            recommendation = self.get_trading_recommendation(pred_label, prob, prob_naik)
            
            return {
                'label': pred_label,
                'label_text': 'Naik' if pred_label == 1 else 'Turun',
                'probability': prob,
                'probability_naik': prob_naik,
                'probability_turun': prob_turun,
                'recommendation': recommendation['action'],
                'recommendation_text': recommendation['action_text'],
                'recommendation_reason': recommendation['reason'],
                'recommendation_color': recommendation['color']
            }
        else:
            # Batch prediction
            results = []
            for i in range(len(prediction)):
                pred_label = int(prediction[i])
                prob = float(probability[i][prediction[i]])
                prob_naik = float(probability[i][1])
                prob_turun = float(probability[i][0])
                
                # Get trading recommendation
                recommendation = self.get_trading_recommendation(pred_label, prob, prob_naik)
                
                results.append({
                    'label': pred_label,
                    'label_text': 'Naik' if pred_label == 1 else 'Turun',
                    'probability': prob,
                    'probability_naik': prob_naik,
                    'probability_turun': prob_turun,
                    'recommendation': recommendation['action'],
                    'recommendation_text': recommendation['action_text'],
                    'recommendation_reason': recommendation['reason'],
                    'recommendation_color': recommendation['color']
                })
            return results
    
    def predict_from_csv(self, csv_path):
        """
        Predict dari file CSV
        Input: path ke CSV file
        Output: DataFrame dengan predictions
        """
        # Read CSV
        df = pd.read_csv(csv_path)
        
        # Ensure Date column exists
        if 'Date' not in df.columns:
            raise ValueError("CSV must have 'Date' column")
        
        # Calculate features
        df = self.calculate_features(df)
        
        # Make predictions
        predictions = self.predict(df)
        
        # Add predictions to dataframe
        df['Predicted_Label'] = [p['label'] for p in predictions]
        df['Predicted_Text'] = [p['label_text'] for p in predictions]
        df['Probability'] = [p['probability'] * 100 for p in predictions]  # Convert to percentage
        df['Probability_Naik'] = [p['probability_naik'] * 100 for p in predictions]
        df['Probability_Turun'] = [p['probability_turun'] * 100 for p in predictions]
        df['Recommendation'] = [p['recommendation'] for p in predictions]
        df['Recommendation_Text'] = [p['recommendation_text'] for p in predictions]
        df['Recommendation_Reason'] = [p['recommendation_reason'] for p in predictions]
        df['Recommendation_Color'] = [p['recommendation_color'] for p in predictions]
        
        return df
    
    def get_model_info(self):
        """Get model information"""
        if self.model is None:
            return None
        
        return {
            'model_type': type(self.model).__name__,
            'n_estimators': getattr(self.model, 'n_estimators', 'N/A'),
            'max_depth': getattr(self.model, 'max_depth', 'N/A'),
            'learning_rate': getattr(self.model, 'learning_rate', 'N/A'),
            'threshold': self.threshold,
            'features': ['Open', 'High', 'Low', 'Close', 'Volume', 
                        'MA5', 'MA10', 'Return', 'Return_1', 'MA_diff']
        }


# Global model instance
_model_instance = None

def get_model():
    """Get or create model instance (singleton pattern)"""
    global _model_instance
    if _model_instance is None:
        _model_instance = SIABModel()
    return _model_instance
