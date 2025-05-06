import xgboost as xgb
import json
from django.http import JsonResponse
import numpy as np
import os
from django.shortcuts import render  


# Getting the model path from the api folder
def load_model():
    model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'api', 'xgboost_model.json')
    model = xgb.XGBRegressor()
    model.load_model(model_path)
    return model

# View for price prediction
def predict_price(request):
    model = load_model()  # Loading the model

    # We assume that the input features are received from the request.
    features = request.GET.getlist('features')  # We get the features from the URL query.
    features = [float(f) for f in features]  # We convert the features to numbers.


    # Price prediction

    price = model.predict([features])[0]  # Prediction for a single sample.

    price = float(price)
    
    # Return as a JsonResponse.

    return JsonResponse({'predicted_price': price})

# View function for the homepage.

def home(request):
    return render(request, 'home.html')  # It displays the homepage using the 'home.html' template.


# View function for the prediction form page.
def predict_form(request):
    return render(request, 'predict_form.html')  # صفحه فرم پیش‌بینی را نشان می‌دهد
