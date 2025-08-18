# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Base workdir for build steps
WORKDIR /app

# Minimal OS deps; keep lean
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl \
 && rm -rf /var/lib/apt/lists/*

# Python install behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# ---- Install deps with cache-friendly layering ----
# Your requirements.txt is inside NLWeb/code/python
COPY NLWeb/code/python/requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip \
 && pip install -r /app/requirements.txt

# ---- Bring in the rest of the source ----
COPY . /app

# Create canonical data dir and link expected path (../data from code/python)
RUN mkdir -p /app/NLWeb/data/jsonld \
 && rm -rf /app/NLWeb/code/data \
 && ln -s /app/NLWeb/data /app/NLWeb/code/data

# Optional: set envs for components that read them
ENV NLWEB_JSON_DATA_DIR=/app/NLWeb/data/jsonld
ENV NLWEB_CACHE_DIR=/app/NLWeb/.cache
RUN mkdir -p "$NLWEB_CACHE_DIR"

# (Optional) run as non-root
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Cloud Run will pass $PORT; aiohttp must listen on it
ENV PORT=8080
EXPOSE 8080

# Run from where app-aiohttp.py lives so ../data → /app/NLWeb/code/data (the symlink)
WORKDIR /app/NLWeb/code/python
CMD ["python", "app-aiohttp.py"]
