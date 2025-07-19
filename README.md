# ITESM-MLOps-EC

# Wine Quality Prediction (Code Style & Linting)

Esta rama agrega herramientas de formato automático, ordenamiento de imports y análisis estático para mantener un código limpio, legible y mantenible.

## Cambios principales respecto a la rama anterior

- Se agregaron configuraciones para:
  - `black`: formateo automático de código Python
  - `isort`: ordenamiento automático de imports
  - `flake8`: detección de errores de estilo y código redundante
  - `mypy`: análisis estático de tipos
- Se incluyó un archivo `pyproject.toml` con configuraciones compartidas
- Se documentó cómo ejecutar cada herramienta y corregir errores

## Herramientas utilizadas

| Herramienta | Propósito                              |
|-------------|----------------------------------------|
| black       | Formato de código consistente          |
| isort       | Orden automático de imports            |
| flake8      | Revisión de estilo y convenciones PEP8 |
| mypy        | Validación de anotaciones de tipo      |

## Estructura nueva

```bash
├── pyproject.toml # Configuración de black, isort
├── .flake8 # Opcional: configuración flake8
├── src/...
├── scripts/...
```

## Ejecución de las herramientas

Asegurate de tener instaladas las librerías ya mencionadas

```bash
pip install black isort flake8 mypy
```

Después, desde la raíz del proyecto, ejecuta:

### Formato con `black`

```bash
black src/ scripts/
```

### Orden de imports con `isort`

```bash
isort src/ scripts/
```

### Revisión de estilo con `flake8`

```bash
flake8 src/ scripts/
```

### Revisión de tipado con `mypy`

```bash
mypy src/
```

## Recomendaciones

- Usa `black` antes de cada commit.
- Corre `flake8` y `mypy` para detectar errores antes del push.

## Next Steps.

La siguiente rama (`feature/testing-suite`) introducirá pruebas unitarias con `pytest`, cubriendo las clases `WineQualityModel` y `DataExplorer`.
