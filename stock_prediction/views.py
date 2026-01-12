import csv
import json
from pathlib import Path

import pandas as pd
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import CSVUploadForm, PredictionForm
from .ml_model import get_model
from .models import Prediction, StockData


def index(request):
    """Homepage dengan informasi model dan quick stats"""
    model = get_model()
    model_info = model.get_model_info()

    # Get statistics
    total_predictions = Prediction.objects.count()
    total_stock_data = StockData.objects.count()
    recent_predictions = Prediction.objects.all()[:5]

    # Calculate accuracy if we have predictions
    naik_count = Prediction.objects.filter(predicted_label=1).count()
    turun_count = Prediction.objects.filter(predicted_label=0).count()

    context = {
        "model_info": model_info,
        "total_predictions": total_predictions,
        "total_stock_data": total_stock_data,
        "recent_predictions": recent_predictions,
        "naik_count": naik_count,
        "turun_count": turun_count,
    }

    return render(request, "stock_prediction/index.html", context)


def predict_manual(request):
    """Halaman untuk prediksi manual"""
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            try:
                model = get_model()

                # Prepare data
                data = {
                    "Open": form.cleaned_data["open_price"],
                    "High": form.cleaned_data["high_price"],
                    "Low": form.cleaned_data["low_price"],
                    "Close": form.cleaned_data["close_price"],
                    "Volume": form.cleaned_data["volume"],
                    "MA5": form.cleaned_data["ma5"],
                    "MA10": form.cleaned_data["ma10"],
                    "Return": form.cleaned_data["return_value"],
                    "Return_1": form.cleaned_data["return_1"],
                    "MA_diff": form.cleaned_data["ma5"] - form.cleaned_data["ma10"], # Calculate automatically
                }

                # Make prediction
                result = model.predict(data)

                # Save to database
                prediction = Prediction.objects.create(
                    open_price=data["Open"],
                    high_price=data["High"],
                    low_price=data["Low"],
                    close_price=data["Close"],
                    volume=data["Volume"],
                    ma5=data["MA5"],
                    ma10=data["MA10"],
                    return_value=data["Return"],
                    return_1=data["Return_1"],
                    ma_diff=data["MA_diff"],
                    predicted_label=result["label"],
                    probability=result["probability"] * 100,  # Convert to percentage
                    rekomendasi_aksi=result["recommendation"],
                )

                messages.success(
                    request, f"Prediksi berhasil! Hasil: {result['label_text']}"
                )
                return render(
                    request,
                    "stock_prediction/predict_result.html",
                    {"result": result, "data": data, "prediction": prediction},
                )

            except Exception as e:
                messages.error(request, f"Error saat prediksi: {str(e)}")
    else:
        form = PredictionForm()

    return render(request, "stock_prediction/predict_manual.html", {"form": form})


def predict_csv(request):
    """Halaman untuk upload dan prediksi dari CSV"""
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = request.FILES["csv_file"]

                # Save file temporarily
                import tempfile

                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".csv"
                ) as tmp_file:
                    for chunk in csv_file.chunks():
                        tmp_file.write(chunk)
                    tmp_path = tmp_file.name

                # Make predictions
                model = get_model()
                df_result = model.predict_from_csv(tmp_path)

                # Save to database
                saved_count = 0
                for _, row in df_result.iterrows():
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
                        probability=row[
                            "Probability"
                        ],  # Already in percentage from ml_model
                    )
                    saved_count += 1

                # Clean up temp file
                Path(tmp_path).unlink()

                messages.success(
                    request, f"Berhasil memprediksi {saved_count} data dari CSV!"
                )

                # Convert to JSON for display
                results = df_result.to_dict("records")

                return render(
                    request,
                    "stock_prediction/predict_csv_result.html",
                    {
                        "results": results[:100],  # Limit to 100 for display
                        "total_count": len(results),
                        "saved_count": saved_count,
                    },
                )

            except Exception as e:
                messages.error(request, f"Error saat memproses CSV: {str(e)}")
    else:
        form = CSVUploadForm()

    return render(request, "stock_prediction/predict_csv.html", {"form": form})


def predictions_list(request):
    """Halaman daftar semua prediksi"""
    predictions = Prediction.objects.all().order_by("-created_at")

    # Pagination
    paginator = Paginator(predictions, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "total_count": predictions.count()}

    return render(request, "stock_prediction/predictions_list.html", context)


def clean_predictions_history(request):
    """Hapus semua riwayat prediksi"""
    Prediction.objects.all().delete()

    context = {"total_count": 0}

    return render(request, "stock_prediction/predictions_list.html", context)


def export_predictions_history(request):
    """Export riwayat prediksi"""
    # Create HTTP response with CSV headers
    response = HttpResponse(
        content_type="text/csv",
    )
    response["Content-Disposition"] = 'attachment; filename="predictions.csv"'

    writer = csv.writer(response)

    # Write header
    fields = [field.name for field in Prediction._meta.fields]
    writer.writerow(fields)

    # Write rows
    for obj in Prediction.objects.all():
        writer.writerow([getattr(obj, field) for field in fields])

    return response


def visualize(request):
    """Halaman visualisasi data"""
    # Get recent stock data or predictions for visualization
    predictions = Prediction.objects.all().order_by("-created_at")[:100]

    # Prepare data for charts
    chart_data = {
        "dates": [p.created_at.strftime("%Y-%m-%d %H:%M") for p in predictions],
        "close_prices": [p.close_price for p in predictions],
        "predictions": [p.get_label_display_custom() for p in predictions],
        "probabilities": [p.probability for p in predictions],
    }

    context = {"chart_data": json.dumps(chart_data), "predictions": predictions[:20]}

    return render(request, "stock_prediction/visualize.html", context)


@require_http_methods(["POST"])
def api_predict(request):
    """API endpoint untuk prediksi (JSON)"""
    try:
        data = json.loads(request.body)

        # Validate required fields
        required_fields = [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "MA5",
            "MA10",
            "Return",
            "Return_1",
            "MA10",
            "Return",
            "Return_1",
        ]

        for field in required_fields:
            if field not in data:
                return JsonResponse(
                    {"error": f"Missing required field: {field}"}, status=400
                )

        # Calculate MA_diff if not provided
        if "MA_diff" not in data:
            data["MA_diff"] = data["MA5"] - data["MA10"]

        # Make prediction
        model = get_model()
        result = model.predict(data)

        return JsonResponse({"success": True, "prediction": result})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
