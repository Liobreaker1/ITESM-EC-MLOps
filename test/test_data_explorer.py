import pytest
import pandas as pd
from explorer.data_explorer import DataExplorer


@pytest.fixture
def sample_data():
    """Crea un DataFrame de ejemplo para pruebas visuales de DataExplorer."""
    return pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [5, 4, 3, 2, 1],
        "quality": [3, 4, 5, 6, 5]
    })


def test_explore_data(sample_data):
    """
    Valida que el método explore_data se ejecute sin errores.
    """
    DataExplorer.explore_data(sample_data)


def test_plot_histograms(sample_data):
    """
    Valida que el método plot_histograms se ejecute sin errores.
    """
    DataExplorer.plot_histograms(sample_data)


def test_plot_correlation_matrix(sample_data):
    """
    Valida que el método plot_correlation_matrix se ejecute sin errores.
    """
    DataExplorer.plot_correlation_matrix(sample_data)
