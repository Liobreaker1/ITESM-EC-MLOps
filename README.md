# ITESM-MLOps-EC

# Wine Quality Prediction (Pipeline Persistance).

Esta rama agrega la funcionalidad de **guardar** el pipeline de scikit-learn entrenado en disco usando `joblib`. El pipeline ya estaba definido en ramas anteriores; aquí simplemente se hace persistente para poder ser reutilizado en despliegues futuros (por ejemplo, en la API de FastAPI).

## Cambios principales respecto a la rama anterior

- Se añadió el método `save_pipeline()` en la clase `WineQualityModel`
- Se creó el directorio `models/` para almacenar el pipeline entrenado
- Se agregó una línea al final de `main.py` para guardar el pipeline después de entrenar

---

## ¿Por qué guardar el pipeline?

Guardar el pipeline permite:

- Cargar el modelo entrenado desde un archivo `.joblib` sin necesidad de reentrenarlo
- Separar el entrenamiento de la predicción
- Usar el modelo en producción a través de una API.

---

## 📦 Estructura relevante

```
src/
└── models/
    └── wine_model.py            
scripts/
└── main.py                      
models/
└── wine_quality_pipeline.joblib 
```

---

## Pasos para ejecución

Desde la raíz del proyecto, con tu entorno virtual activado:

```bash
PYTHONPATH=src python scripts/main.py
```

Esto ejecutará todo el flujo:

1. Carga del dataset
2. Exploración inicial
3. Entrenamiento del pipeline
4. Evaluación del modelo
5. Validación cruzada
6. **Guardado del pipeline entrenado**

---

## Resultado esperado

Al finalizar la ejecución, se debe crear el archivo:

```
models/wine_quality_pipeline.joblib
```

## Next Steps

En la siguiente rama (`feature/api`), se utilizará este archivo `.joblib` para cargar el pipeline y exponerlo a través de una API REST con `FastAPI`, permitiendo hacer predicciones desde herramientas como Postman.
