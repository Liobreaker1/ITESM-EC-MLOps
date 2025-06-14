# Estructura de código de un Proyecto de ML


## Dependencias

Es importante contar con la herramienta de **poetry** para poder ejecutar los ejercicios de esta guía, antes de continuar revisa la [documentación](https://python-poetry.org/docs/#installation) para hacer la instalación de la herramienta.


```bash
pipx install poetry
```

## Paquetes y módulos

Cada archivo `py` puede ser considerado como un módulo de Python. Un módulo de python puede ser ejecutado directamente desde la misma carpeta de ejecución, para ello es necesario cambiar el directorio de trabajo al directorio que contiene el módulo.

```bash
cd /path/to/module
python modulo.py
```

Los módulos pueden agruparse en paquetes, y estos también en paquetes más generales, generando estructuras jerárquicas como esta:

```
proyecto/
├── paquete_1/                      
│   ├── modulo_1.py
│   ├── subpaquete_1/
│   │   ├── modulo_2.py
│   │   └── modulo_3.py
│   └── subpaquete_2/
│       └── modulo_4.py
├── paquete_2/                      
│   ├── modulo_5.py
│   ├── subpaquete_3/
│   │   └── modulo_6.py
│   └── subpaquete_2/
│       ├── modulo_7.py
│       └── modulo_8.py
└── modulo_9.py
```


## Poetry

### Creación de un proyecto nuevo

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

### Usar un paquete preestablecido

1. Moverse a la ruta del paquete

```bash
cd /path/to/package
```

2. Inicializando el repo

```bash
poetry init
```

   - Sigue las instrucciones para la inicialización del paquete

3. Instala las dependencias

```bash
poetry install
```


### Otras herramientas

Con poetry se pueden exportar los archivos de dependencias a otros formatos (no suele ser recomendable, pero en algunos ambientes de desarrollo podría ser útil)

```bash
poetry self add poetry-plugin-export
poetry export -f requirements.txt --output requirements.txt
```




