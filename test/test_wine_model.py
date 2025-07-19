import pytest
import pandas as pd
from models.wine_model import WineQualityModel


@pytest.fixture
def wine_model():
    """Fixture que instancia y carga el dataset en un modelo WineQualityModel."""
    path = "data/raw/wine_quality_df.csv"
    model = WineQualityModel(path)
    return model.load_data()


def test_load_data_shape(wine_model):
    """
    Valida que los datos hayan sido cargados correctamente.
    Además, revisa que `data` no sea None, que sea un DataFrame y que tenga al menos una fila.
    """
    assert wine_model.data is not None
    assert isinstance(wine_model.data, pd.DataFrame)
    assert wine_model.data.shape[0] > 0


def test_preprocess_data_shapes(wine_model):
    """
    Valida que el preprocesamiento genere conjuntos de entrenamiento y prueba con dimensiones coherentes.
    """
    wine_model.preprocess_data()
    assert wine_model.X_train.shape[0] == wine_model.y_train.shape[0]
    assert wine_model.X_test.shape[0] == wine_model.y_test.shape[0]


def test_model_training(wine_model):
    """
    Valida que el modelo se entrene y entregue un score entre 0 y 1.
    """
    wine_model.preprocess_data().train_model()
    score = wine_model.model_pipeline.score(wine_model.X_test, wine_model.y_test)
    assert 0 <= score <= 1
