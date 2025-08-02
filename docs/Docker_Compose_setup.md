# Dockerizando una aplicación de un proyecto de ML

## Dependencias

- Poetry
- Docker (y docker compose)

## Usage

1. Tienes que ir a la carpeta raíz en tu sistema de archivos

    ```bash
    cd path/to/your/project/
    ```

2. Ejecuta el siguiente comando para construir las imágenes de Docker y levantar los contenedores necesarios:

   ```bash
    docker compose up -d
    ```

3. Puedes explorar los logs a traves de comandos de docker

    ```bash
    docker compose logs -f
    ```

4. Accede al swagger mediante el browser en (localhost:8000/docs)[localhost:8000/docs]

5. Para detener los contenedores, puedes usar:

   ```bash
   docker compose down
   ```

### Inicializando el repo desde cero


1. Inicia el folder del proyecto con Poetry:

    ```bash
    poetry init
    ```

Sigue las instrucciones para configurar tu proyecto. (Asegúrate de incluir los `__init__.py` y `README.md` correspondientes.) 

2. Instala las dependencias que necesites

    ```bash
    poetry add pandas numpy matplotlib seaborn scikit-learn
    ```

3. Desarrolla tu aplicación

4. Crea tu `dockerfile`

5. Configura tu `docker-compose.yml`

