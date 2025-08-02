FROM python:3.11-slim AS base

ENV APP_HOME=/app \
    # poetry:
    POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # virtualenv:
    VENV_PATH=/app/.venvs

ENV PATH="${POETRY_HOME}/bin:${PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
WORKDIR ${APP_HOME}


# ---- build ----

FROM base AS build

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    make \
    python3-dev \
    && curl -sSL 'https://install.python-poetry.org' | python3 - \
    && poetry --version


COPY poetry.lock pyproject.toml README.md ${APP_HOME}
RUN poetry install --only main --no-root


# install any additional dependencies here
#COPY installs.py ${APP_HOME}
#RUN poetry run python -m installs


# ---- development ----

FROM base AS devel


COPY --from=build ${POETRY_HOME}    ${POETRY_HOME}
COPY --from=build ${APP_HOME}       ${APP_HOME}

EXPOSE 8000
CMD poetry run uvicorn src.main:app --reload --host=0.0.0.0 --port=8000

#FROM base AS devel_2

#COPY --from=build ${POETRY_HOME}    ${POETRY_HOME}
#COPY --from=build ${APP_HOME}       ${APP_HOME}

#EXPOSE 8001
#CMD poetry run uvicorn src.main_2:app --reload --host=0.0.0.0 --port=8001


#FROM base AS devel_3

#COPY --from=build ${POETRY_HOME}    ${POETRY_HOME}
#COPY --from=build ${APP_HOME}       ${APP_HOME}

#EXPOSE 8001
#CMD poetry run uvicorn src.main_3:app --reload --host=0.0.0.0 --port=8002


# ---- testing ----

FROM base AS testing

COPY --from=build ${POETRY_HOME}    ${POETRY_HOME}
COPY --from=build ${APP_HOME}       ${APP_HOME}

COPY notebooks ${APP_HOME}/notebooks
COPY src ${APP_HOME}/src
COPY data ${APP_HOME}/data
RUN mkdir -p ${APP_HOME}/data/storage

EXPOSE 8000
CMD poetry run pytest .

#FROM base AS test_2

#COPY --from=build ${POETRY_HOME}    ${POETRY_HOME}
#COPY --from=build ${APP_HOME}       ${APP_HOME}

#COPY src ${APP_HOME}/src
#RUN mkdir -p ${APP_HOME}/data/raw
#RUN mkdir -p ${APP_HOME}/data/storage

#EXPOSE 8001
#CMD poetry run uvicorn src.main_2:app --host=0.0.0.0 --port=8001


#FROM base AS test_3

#COPY --from=build ${POETRY_HOME}    ${POETRY_HOME}
#COPY --from=build ${APP_HOME}       ${APP_HOME}

#COPY src ${APP_HOME}/src
#RUN mkdir -p ${APP_HOME}/data/processed

#EXPOSE 8002
#CMD poetry run uvicorn src.main_3:app --host=0.0.0.0 --port=8002
