import pytest
from models.wine_model import WineQualityModel


def test_model_accuracy_above_threshold():
    """
    Este test falla a propósito si el modelo no supera una precisión de 0.90.
    """
    model = WineQualityModel("data/raw/wine_quality_df.csv")
    model.load_data().preprocess_data().train_model()

    accuracy = model.model_pipeline.score(model.X_test, model.y_test)

    # Intencionalmente alto para que falle
    assert accuracy >= 0.90, f"Accuracy was too low: {accuracy:.2f}"
