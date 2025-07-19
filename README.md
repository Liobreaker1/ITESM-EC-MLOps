# ITESM-MLOps-EC

# Wine Quality Prediction (POO Refactor)

Esta rama contiene una versión refactorizada del notebook original, aplicando principios de **Programación Orientada a Objetos (POO)** para organizar y reutilizar mejor el código del pipeline de Machine Learning.

## Cambios principales respecto a `main`

- Se creó la clase `WineQualityModel` para encapsular todo el flujo ML:
  - Carga de datos
  - Preprocesamiento
  - Entrenamiento
  - Evaluación
  - Validación cruzada
- Se incluyó la clase `DataExplorer` para visualización y análisis básico del dataset
- Se utilizaron docstrings y tipado estático (`typing`) para mejorar legibilidad y mantenibilidad

## Archivos relevantes

```bash
notebooks/Demo
├── Wine_EDA.ipynb # Notebook exploratorio (original en main)
├── Wine_Refactored_POO.ipynb # Notebook refactorizado con POO (esta rama)
```

## Dataset

No hay cambios en el dataset y es el mismo dataset de vinos que se tiene en la rama main, y es descargable desde [Kaggle](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)

## Notebook

Para visualizar el notebook, basta con abrirlo desde JupyterLab o Jupyter y ejecutar todo el código

## Clases introducidas

### `WineQualityModel`

Encapsula todo el flujo de Machine Learning y permite ejecutar de forma encadenada con `model.run_all()`.

### `DataExplorer`

Contiene funciones estáticas para explorar, describir y visualizar relaciones entre variables del dataset.

## Next Steps.

La siguiente rama (`feature/convert-to-scripts`) convierte el código de este notebook en scripts modulares `.py` organizados en `src/`.

