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
│   │   ├── cabecera.py                     # Cabecera hero con imagen de fondo
│   │   ├── contador_regresivo.py           # Cuenta atrás / día de carrera / próxima edición
│   │   ├── revelar.py                      # Animación de aparición al hacer scroll
│   │   └── pie_pagina.py                   # Pie de página
│   ├── pages/                              # Páginas de la web
│   │   ├── principal/                      # Inicio (/) + secciones de la home
│   │   ├── recorridos/                     # Recorridos y tracks (/recorridos)
│   │   ├── reglamento/                     # Reglamento oficial (/reglamento)
│   │   ├── galeria/                        # Galería fotográfica (/galeria)
│   │   ├── clasificacion/                  # Clasificaciones (/clasificaciones y /clasificaciones/[anio])
│   │   └── contacto/                       # Formulario de contacto (/contacto)
│   ├── models/                             # Modelos SQLAlchemy (pendiente)
│   └── state/                              # Estado global de Reflex (pendiente)
├── assets/                                 # Imágenes, fuentes y estáticos
│   └── noticias/img/                       # Imágenes de las noticias
├── datos/                                  # Datos que el backend lee en caliente
│   ├── 2026/                               # CSVs de clasificaciones por edición
│   │   ├── Clasificacion_27km.csv
│   │   ├── Clasificacion_14km.csv
│   │   └── Clasificacion_marcha.csv
│   └── noticias/                           # Noticias de la home (un .txt JSON por noticia)
├── Dockerfile                              # Build multi-stage para producción
├── docker-compose.yml                      # Stack app + Caddy
├── Caddyfile                               # Reverse proxy (trailpeñasagra.com)
├── pyproject.toml                          # Dependencias y configuración del proyecto
├── uv.lock                                 # Lockfile de uv
├── rxconfig.py                             # Configuración de Reflex
└── README.md
```

---

## 🧩 Componentes

Bloques de UI reutilizables ubicados en `trailcorremosadriana_v2/components/`.

### `barra_navegacion.py` — `barra_de_navegacion()`

Barra de navegación superior fija que permanece visible durante el scroll (70px, fondo gris pizarra `#434c53` con borde inferior naranja). Enlaces de escritorio y menú hamburguesa en móvil.

### `cabecera.py` — `cabecera(imagen, *children)`

Componente de cabecera tipo *hero* a pantalla completa (`100dvh`). Recibe una imagen de fondo y componentes hijos superpuestos sobre ella.

### `contador_regresivo.py` — `contador_hero()`

Caja del hero con tres fases automáticas según la fecha de la carrera (`FECHA_CARRERA`): cuenta atrás en vivo antes de la prueba, «¡Hoy es el gran día!» durante el día de la carrera y «¡Próximamente... Trail Peñasagra 2027!» a partir del día siguiente. Para abrir la siguiente edición basta con actualizar `FECHA_CARRERA` (y los literales de año).

### `revelar.py` — `efecto_revelar()`

Animación de aparición al hacer scroll para los elementos con `class_name="reveal"` (respeta `prefers-reduced-motion`). Se incluye una vez por página.

### `pie_pagina.py` — `pie_pagina()`

Pie de página con enlaces, sección legal y email de contacto. Columnas apiladas en móvil y año de copyright dinámico.

---

## 📄 Páginas

Páginas de la web en `trailcorremosadriana_v2/pages/`, cada una en su propio subdirectorio.

| Ruta | Página | Descripción |
|---|---|---|
| `/` | `principal/principal.py` | Inicio: hero con cuenta atrás, inscripciones, noticias y patrocinadores |
| `/recorridos` | `recorridos/recorridos.py` | Selector de las 3 pruebas con ficha técnica, avituallamientos, material y track de Wikiloc |
| `/reglamento` | `reglamento/reglamento.py` | Reglamento oficial: precios, logística y normas |
| `/galeria` | `galeria/galeria.py` | Álbumes de fotos por edición (Google Fotos) |
| `/clasificaciones` | `clasificacion/clasificaciones.py` | Índice de clasificaciones: una tarjeta por edición |
| `/clasificaciones/[anio]` | `clasificacion/clasificacion.py` | Resultados de una edición: selector de prueba, filtro general/masculino/femenino, buscador por nombre y podium destacado |
| `/contacto` | `contacto/contacto.py` | Formulario de contacto (envío por email) |

### Clasificaciones automáticas por edición

Los resultados se leen de `datos/<año>/` en cada carga de página. Para publicar una edición nueva basta con crear la carpeta del año con los tres CSVs (`Clasificacion_27km.csv`, `Clasificacion_14km.csv`, `Clasificacion_marcha.csv`) — no hay que tocar código. Si falta un CSV, esa prueba simplemente no se muestra.

### Noticias sin tocar código

La sección de noticias de la home se alimenta de `datos/noticias/`: cada noticia es un fichero `AAAA-MM-DD-titulo.txt` con contenido JSON (`titulo`, `subtitulo`, `imagen`, `texto`, `fecha` opcional). Solo se muestran las **4 más recientes**; la imagen (webp, 1200×750 px, <200 KB) se copia a `assets/noticias/img/` y en el JSON se escribe solo su nombre. Un JSON inválido se ignora, sin imagen sale un icono y con la carpeta vacía la sección desaparece. Formato completo y flujo de publicación en [datos/noticias/README.md](datos/noticias/README.md).

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
