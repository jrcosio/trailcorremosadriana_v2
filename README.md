# 🏔️ Trail Peñasagra — Corremos por Adriana v2

Sitio web oficial de la carrera **Trail Peñasagra Corremos por Adriana**, desarrollado con [Reflex](https://reflex.dev/) (Python) y gestionado con [uv](https://docs.astral.sh/uv/).

---

## 🛠️ Stack tecnológico

| Capa | Tecnología |
|---|---|
| Framework web | [Reflex](https://reflex.dev/) |
| Lenguaje | Python 3.12+ |
| Base de datos | SQLite (dev) / PostgreSQL (prod) |
| ORM | SQLAlchemy (integrado en Reflex) |
| Gestor de entorno | [uv](https://docs.astral.sh/uv/) |

---

## 📋 Requisitos previos

- Python **3.12+**
- [uv](https://docs.astral.sh/uv/) instalado:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 🚀 Instalación y puesta en marcha

### 1. Clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/trailcorremosadriana_v2.git
cd trailcorremosadriana_v2
```

### 2. Crear el entorno virtual e instalar dependencias

```bash
uv sync
```

### 3. Inicializar Reflex

```bash
uv run reflex init
```

### 4. Levantar el servidor de desarrollo

```bash
uv run reflex run
```

La aplicación estará disponible en `http://localhost:3000`.

---

## 📁 Estructura del proyecto

```
trailcorremosadriana_v2/
├── trailcorremosadriana_v2/      # Paquete principal de la app Reflex
│   ├── __init__.py
│   ├── trailcorremosadriana_v2.py  # Punto de entrada de la app
│   ├── components/               # Componentes reutilizables
│   ├── pages/                    # Páginas de la web
│   ├── models/                   # Modelos SQLAlchemy
│   └── state/                    # Estado global de Reflex
├── assets/                       # Imágenes, fuentes y estáticos
├── pyproject.toml                # Dependencias y configuración del proyecto
├── uv.lock                       # Lockfile de uv
├── rxconfig.py                   # Configuración de Reflex
└── README.md
```

---

## 🗄️ Base de datos

El proyecto usa **SQLAlchemy** a través de la integración nativa de Reflex. Los modelos se definen heredando de `rx.Model`:

```python
import reflex as rx

class Inscripcion(rx.Model, table=True):
    nombre: str
    dorsal: int
    categoria: str
```

Las migraciones se gestionan automáticamente con Reflex al ejecutar `reflex run`.

---

## ⚙️ Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# Base de datos (producción)
DATABASE_URL=postgresql+psycopg2://usuario:password@host:5432/trailcorremosadriana

# Entorno
REFLEX_ENV=dev   # dev | prod
```

---

## 🏗️ Despliegue en producción

```bash
# Compilar los assets estáticos
uv run reflex export

# Levantar en modo producción
uv run reflex run --env prod
```
---

## 🤝 Contribución

1. Haz un fork del repositorio
2. Crea una rama: `git checkout -b feature/mi-mejora`
3. Commitea los cambios: `git commit -m "feat: descripción del cambio"`
4. Abre un Pull Request

---

## 📄 Licencia

MIT © Trail Peñasagra — Corremos por Adriana
