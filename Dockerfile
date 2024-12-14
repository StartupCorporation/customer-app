ARG GID
ARG UID

FROM python:3.12 AS dependencies
ARG GID
ARG UID

COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.12-slim AS final
ARG APP_DIR=/app
ARG GID
ARG UID

ENV PYTHONPATH="${PYTHONPATH}:${APP_DIR}"

WORKDIR $APP_DIR

COPY --from=dependencies /root/.local /root/.local
COPY ./src .

RUN groupadd -g $GID appgroup && \
    useradd -u $UID -g $GID appuser

USER appuser