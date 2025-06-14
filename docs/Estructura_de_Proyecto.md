# Estructura de código de un Proyecto de ML


## Dependencias

Es importante contar con la herramienta de **poetry** para poder ejecutar los ejercicios de esta guía, antes de continuar revisa la [documentación](https://python-poetry.org/docs/#installation) para hacer la instalación de la herramienta.

En esencia se utiliza 

```bash
pipx install poetry
```

## Guía del demo


1. Muévete a la posición deseada
```bash
cd /path/to/your/folder
poetry --version
```

  - _Opcional_ Puedes asegurarte de tener la versión más actualizada de poetry
```bash
poetry self update
```

2. Crearemos un nuevo proyecto

```bash
poetry new demo
```

3. Agregaremos dependencias

```bash
poetry add numpy
poetry add pandas@2.3
poetry add "plotnine>=0.14.5"
```

4. Revisa el contenido de `pyproject.toml`

5. Instala el proyecto

```bash
poetry install
```

6. Revisa el contenido de `poetry.lock`

```bash
poetry env list
poetry env info
poetry show --tree
```
  - _Opcional_ remueve dependencias del proyecto

```bash
poetry remove pandas
```

  - _Opcional_ Añade dependencias al grupo de herramientas de desarrrollo (`dev`)

```bash
poetry add -G dev black
```

7. Empaqueta tu proyecto

```bash
poetry build
```

  - _Opcional_ Puedes publicar tu proyecto en Pypi

```bash
poetry publish
```

## Otras herramientas

Con poetry se pueden exportar los archivos de dependencias a otros formatos (no suele ser recomendable, pero en algunos ambientes de desarrollo podría ser útil)

```bash
poetry self add poetry-plugin-export
poetry export -f requirements.txt --output requirements.txt
```




