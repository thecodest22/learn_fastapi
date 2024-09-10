FROM python:3.12.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

RUN pip install --upgrade pip && pip install uv

WORKDIR /app
COPY requirements.lock ./

RUN uv pip install --no-cache --system -r requirements.lock