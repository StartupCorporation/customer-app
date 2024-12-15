ARG GROUP_ID
ARG USER_ID

FROM python:3.12 AS dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --prefix=venv


FROM python:3.12-slim AS final
ARG APP_DIR=/app
ARG GROUP_ID
ARG USER_ID

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR $APP_DIR

COPY --from=dependencies /venv /usr/local
COPY ./src .

RUN groupadd -g $GROUP_ID appgroup && \
    useradd -u $USER_ID -g $GROUP_ID appuser

USER appuser