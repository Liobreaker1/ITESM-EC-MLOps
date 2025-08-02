# ITESM-MLOps-EC Demo

# Wine Quality Prediction (Exploratory Analysis)

Este proyecto tiene como objetivo predecir la calidad del vino utilizando técnicas de aprendizaje automático, comenzando desde un enfoque exploratorio con Python y Jupyter Notebooks.

## Estructura del proyecto

```bash
.
├── data/
│   └── raw/
│       └── wine_quality_df.csv
├── docs/
├── models/
├── notebooks/
├── src/
│   ├── prediction/
│   ├── utils/
│   └── main.py
├── tests/
├── docker-compose.yml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Dataset

Se utiliza un dataset de calidad de vino (`wine_quality_df.csv`) con variables químicas y sensoriales. Puedes encontrarlo en la carpeta `data/raw`. 
El dataset es público y se puede dercargar directamente de [Kaggle](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)

## Setup mínimo

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Instalación rápida:

```bash
poetry install
```

solo hay que considerar que también tiene dependencias de otras cosas vistas durante el curso.

## Docker compose


Para ejecutar el proyecto con Docker, asegúrate de tener Docker y Docker Compose instalados. Luego, sigue estos pasos:

```bash
docker compose up
```


