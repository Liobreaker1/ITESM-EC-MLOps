# ITESM-MLOps-EC

# Wine Quality Prediction (FastAPI inclusion).

Esta rama agrega una API REST construida con **FastAPI** para consumir el modelo de clasificación entrenado, expuesto como un endpoint que recibe características fisicoquímicas del vino y devuelve su predicción de calidad.

---

## Cambios principales respecto a la rama anterior

- Se crea un archivo `src/api/app.py` con la lógica de la API
- Se utiliza el pipeline previamente entrenado y guardado (`wine_quality_pipeline.joblib`)
- Se define un modelo de entrada `WineFeatures` con `pydantic` para validar los datos
- Se incluye un endpoint `/predict` que devuelve la calidad estimada

---

## Cómo levantar la API

Desde la raíz del proyecto, ejecuta:

```bash
uvicorn src.api.app:app --reload
```

Esto iniciará la API en:

```
http://127.0.0.1:8000
```

Puedes interactuar visualmente con la documentación automática de Swagger en:

```
http://127.0.0.1:8000/docs
```

---

## Ejemplo de input

Puedes enviar un JSON como el siguiente:

```json
{
  "fixed_acidity": 7.4,
  "volatile_acidity": 0.7,
  "citric_acid": 0.0,
  "residual_sugar": 1.9,
  "chlorides": 0.076,
  "free_sulfur_dioxide": 11.0,
  "total_sulfur_dioxide": 34.0,
  "density": 0.9978,
  "ph": 3.51,
  "sulphates": 0.56,
  "alcohol": 9.4
}
```
---

## Cómo hacer la petición

### Usando Postman

1. Método: `POST`
2. URL: `http://127.0.0.1:8000/predict`
3. Headers:
   - `Content-Type: application/json`
4. Body (raw - JSON): copiar el ejemplo anterior

---

## Archivos relevantes

```
src/
└── api/
    └── app.py                    # Código de la API FastAPI
models/
└── wine_quality_pipeline.joblib  # Pipeline previamente entrenado
```

---

## Pruebas sugeridas

- Prueba con inputs válidos y espera un valor entero (predicción)
- Prueba con un campo faltante o tipo incorrecto para ver el manejo de errores
