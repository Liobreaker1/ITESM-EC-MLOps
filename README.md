# ITESM-MLOps-EC

# Wine Quality Prediction (Scripts Refactor).

Esta rama convierte el código del notebook refactorizado con POO en scripts modulares de Python. El objetivo es separar las responsabilidades y preparar el código para pruebas, formateo, APIs, y más.

## Cambios principales respecto a la rama anterior.

- Se movieron las clases `WineQualityModel` y `DataExplorer` a archivos `.py` dentro de la carpeta `src/`
- Se agregó un archivo `scripts/main.py` para ejecutar el pipeline completo desde terminal
- Se respetó la estructura de clases y métodos definida en la rama anterior
- Se mantiene el enfoque en limpieza y reutilización del código

## Estructura del proyecto.

```bash
.
├── data/
│ └── raw/
│ └── wine_quality_df.csv
├── src/
│ ├── models/
│ │ └── wine_model.py
│ ├── explorer/
│ │ └── data_explorer.py
├── scripts/
│ └── main.py
├── README.md
```

## Ejecución del proyecto.

Para ejecutar el projecto, es necesario colocarse desde la raíz y ejecutar el siguiente comando en la terminal:

```bash
PYTHONPATH=src python scripts/main.py
```

Esto ejecutará la clase `WineQualityModel` que:

- Carga y valida los datos.
- Procesa y separa en train/test.
- Entrena un modelo.
- Evalúa con su matriz de confusión y genera un reporte.
- Aplica validación cruzada y genera los resultados.

## Dataset.

Se mantiene igual que en ramas anteriores, Wine dataset de [Kaggle](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)

## Componentes principales.

- `src/models/wine_model.py`: flujo completo del modelo como clase
- `src/explorer/data_explorer.py`: visualización y exploración de datos
- `scripts/main.py`: script ejecutable que orquesta el pipeline

## Next Steps.

La siguiente rama (`feature/code-style`) aplica herramientas de formateo y análisis estático (black, isort, flake8, mypy).
