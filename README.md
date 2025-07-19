# ITESM-MLOps-EC Demo

# Wine Quality Prediction (Exploratory Analysis)

Este proyecto tiene como objetivo predecir la calidad del vino utilizando técnicas de aprendizaje automático, comenzando desde un enfoque exploratorio con Python y Jupyter Notebooks.

## Estructura del proyecto

```bash
.
├── data/
│   └── raw/
│       └── wine_quality_df.csv
├── notebooks/
│   └── Wine_EDA.ipynb
├── README.md
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
pip install pandas numpy matplotlib seaborn scikit-learn 
```

### Notas:

También se puede instalar el archivo requirements con el siguiente comando:

```bash
pip install -r requirements.txt
```

solo hay que considerar que también tiene dependencias de otras cosas vistas durante el curso.

## Notebook

Para visualizar el notebook, desde Jupyterlab o Notebook, solo hay que cargar el archivo:

```
notebooks/Demo/Wine_EDA.ipynb
```

## Next Steps

La siguiente rama (`feature/notebook-poo-refactor`) contiene una versión refactorizada con programación orientada a objetos (POO).
