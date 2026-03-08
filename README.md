# 🏔️ Trail Peñasagra — Corremos por Adriana v2

Sitio web oficial de la carrera **Trail Peñasagra Corremos por Adriana**, desarrollado con [Reflex](https://reflex.dev/) (Python) y gestionado con [uv](https://docs.astral.sh/uv/).


![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Reflex](https://img.shields.io/badge/Reflex-Framework-8A2BE2?style=for-the-badge&logo=reflex&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![uv](https://img.shields.io/badge/uv-package%20manager-DE5FE9?style=for-the-badge&logo=astral&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-dev-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-prod-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-F59E0B?style=for-the-badge)

---
## Desarrolladores
- Jose Luis Gutiérrez
- Jose Alberto Lanza
- Pablo Blanco
- Hugo Cobo
- Diego González
- Mireite Alonso

### Uno que pasaba por el pueblo... 
- José Ramón Blanco

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
