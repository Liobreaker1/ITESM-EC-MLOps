# ITESM-MLOps-EC

# Wine Quality Prediction (Testing Suite).

Esta rama introduce pruebas automatizadas para validar el comportamiento del pipeline de Machine Learning, utilizando `pytest` y un enfoque modular.

## Cambios principales respecto a la rama anterior

- Se agregó la carpeta `tests/` con pruebas unitarias para:
  - `WineQualityModel`
  - `DataExplorer`
- Se incluyó un archivo de configuración `pytest.ini`
- Se añadió una prueba intencionalmente fallida para propósitos didácticos

## Estructura de pruebas

```bash
tests/
├── test_wine_model.py
├── test_data_explorer.py
├── test_fail_example.py
pytest.ini
```

## Ejecución de la suite de pruebas

Asegurarse de tener instalado pytest, sino es así, ejecutar el siguiente comando en la terminal, con el entorno virtual actuvado:

```bash
pip install pytest
```

Después en la terminal:

```bash
PYTHONPATH=src pytest -v
```

Si deseamos ejecutar un archivo específico:

```bash
PYTHONPATH=src pytest tests/test_wine_model.py
```

## Next Steps.

La siguiente rama (`feature/sklearn-pipeline`) convierte el flujo de entrenamiento a un `Pipeline` real de scikit-learn que es mejor práctica al ser reutilizabe y serilizable.

Esto trae los siguientes beneficios:
- Persistencia del flujo (joblib, pickle, mlflow, etc.)
- Integración más ordenada con APIs, pruebas y despliegue.
- Mejor modularidad del preprocesamiento y el modelo