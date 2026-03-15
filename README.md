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
├── trailcorremosadriana_v2/                # Paquete principal de la app Reflex
│   ├── __init__.py
│   ├── trailcorremosadriana_v2.py          # Punto de entrada (registro de páginas)
│   ├── components/                         # Componentes reutilizables
│   │   ├── barra_navegacion.py             # Barra de navegación sticky
│   │   └── cabecera.py                     # Cabecera hero con imagen de fondo
│   ├── pages/                              # Páginas de la web
│   │   ├── principal/
│   │   │   └── principal.py               # Página de inicio (ruta /)
│   │   └── galeria/
│   │       └── galeria.py                 # Galería fotográfica (ruta /galeria) [WIP]
│   ├── models/                             # Modelos SQLAlchemy (pendiente)
│   └── state/                              # Estado global de Reflex (pendiente)
├── assets/                                 # Imágenes, fuentes y estáticos
│   └── cabecera_index.jpg                  # Imagen de fondo de la cabecera principal
├── pyproject.toml                          # Dependencias y configuración del proyecto
├── uv.lock                                 # Lockfile de uv
├── rxconfig.py                             # Configuración de Reflex
└── README.md
```

---

## 🧩 Componentes

Bloques de UI reutilizables ubicados en `trailcorremosadriana_v2/components/`.

### `barra_navegacion.py` — `barra_de_navegacion()`

Barra de navegación superior fija que permanece visible durante el scroll.

| Propiedad | Valor |
|---|---|
| Posición | `sticky`, `top: 0` |
| Altura | `7vh` |
| Fondo | verde |
| Z-index | `100` (siempre por encima del contenido) |

### `cabecera.py` — `cabecera(imagen, *children)`

Componente de cabecera tipo *hero* que ocupa el 93% restante de la pantalla. Recibe una imagen de fondo y componentes hijos superpuestos sobre ella.

| Parámetro | Descripción |
|---|---|
| `imagen` | Ruta a la imagen de fondo (ej. `"/cabecera_index.jpg"`) |
| `*children` | Contenido superpuesto (titulares, botones, etc.) |

| Propiedad | Valor |
|---|---|
| Altura | `93vh` |
| Imagen | `background-size: cover`, centrada |

---

## 📄 Páginas

Páginas de la web en `trailcorremosadriana_v2/pages/`, cada una en su propio subdirectorio.

### `pages/principal/principal.py` — `index()`

**Ruta:** `/`

Página de inicio del sitio. Estructura:

1. `barra_de_navegacion()` — barra sticky en la parte superior.
2. `cabecera()` — hero a pantalla completa con la imagen `cabecera_index.jpg` y el título **"Trail Peñasagra"** / subtítulo **"Corremos por Adriana"** superpuestos.

### `pages/galeria/galeria.py`

**Ruta:** `/galeria` *(en desarrollo — asignado a Pablo)*

Página destinada a mostrar la galería fotográfica del evento. Pendiente de implementación.

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
