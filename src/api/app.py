from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import List, Union

# Cargando el pipeline entrenado
model = joblib.load("models/wine_quality_pipeline.joblib")

app = FastAPI(
    title="Wine Quality Predictor",
    description="API para predecir la calidad del vino.",
    version="1.0.0"
)

class WineFeatures(BaseModel):
    """
    Modelo de entrada para las características del vino.
    Todas las variables deben ser numéricas (float).
    """
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    ph: float
    sulphates: float
    alcohol: float

@app.get("/")
def root() -> dict[str, str]:
    """
    Endpoint de prueba para verificar que la API está corriendo.
    """
    return {"message": "API de predicción de calidad de vino"}

@app.post("/predict")
def predict_quality(features: WineFeatures) -> dict[str, Union[int, str]]:
    """
    Recibe las características de un vino y devuelve la predicción de su calidad.

    Args:
        features (WineFeatures): Objeto con los atributos fisicoquímicos del vino.

    Returns:
        dict: Predicción de la calidad como entero.
    """
    data = pd.DataFrame([features.dict()])
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
