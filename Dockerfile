FROM python:3.12-slim

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Evita que uv intente descargar otra versión de Python
ENV UV_PYTHON_DOWNLOADS=0

# Copiamos primero metadatos para aprovechar caché
COPY pyproject.toml uv.lock ./

# Instalar dependencias del proyecto
RUN uv sync --locked --no-dev

# Copiar el resto del código
COPY . .

EXPOSE 3000 8000

CMD ["uv", "run", "reflex", "run", "--env", "prod", "--backend-host", "0.0.0.0"]
