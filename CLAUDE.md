## Project Overview

Official website for the "Trail Sierra de Peñasagra - Corremos por Adriana" race event. Built with [Reflex](https://reflex.dev/), a Python framework that compiles Python code into a React frontend with a FastAPI backend.

## Commands

```bash
# Install dependencies
uv sync

# Run development server (starts both backend and frontend)
uv run reflex run

# Run in production mode
uv run reflex run --env prod

# Export static build
uv run reflex export
```

There is no test suite or linter configured yet.

## Architecture

Reflex apps use a **component/state/page** pattern where Python functions return UI trees that compile to React components.

### Key Files

- [rxconfig.py](rxconfig.py) — Reflex config: app name, plugins (Sitemap, TailwindV4)
- [trailcorremosadriana_v2/trailcorremosadriana_v2.py](trailcorremosadriana_v2/trailcorremosadriana_v2.py) — App entry point: registers pages, creates the `app` instance

### Pages

Routes are registered in [trailcorremosadriana_v2.py](trailcorremosadriana_v2/trailcorremosadriana_v2.py):

- [pages/principal/principal.py](trailcorremosadriana_v2/pages/principal/principal.py) — Home (`/`). Composes hero + sections from [pages/principal/secciones/](trailcorremosadriana_v2/pages/principal/secciones/): `inscripciones`, `camiseta`, `patrocinadores` are active; `noticias`, `voluntarios`, `colaboradores` are scaffolded but commented out.
- [pages/contacto/contacto.py](trailcorremosadriana_v2/pages/contacto/contacto.py) — Contact form (`/contacto`), backed by [contacto_state.py](trailcorremosadriana_v2/pages/contacto/contacto_state.py). Sends mail via `smtplib` (Gmail SMTP over SSL); credentials from env vars `SENDER_EMAIL`, `SENDER_PASSWORD`, `RECEIVER_EMAIL`.
- [pages/recorridos/recorridos.py](trailcorremosadriana_v2/pages/recorridos/recorridos.py) — Race routes page (`/recorridos`).
- [pages/galeria/galeria.py](trailcorremosadriana_v2/pages/galeria/galeria.py) — Gallery (`/galeria`), placeholder.

### Components

Reusable UI in [trailcorremosadriana_v2/components/](trailcorremosadriana_v2/components/):

- `barra_navegacion.py` — Sticky top nav bar (7vh, green background)
- `cabecera.py` — Full-screen hero section (93vh, background image overlay)
- `contador_regresivo.py` — Live countdown to race date (July 11, 2026). Exposes `_countdown_script()` (injects client-side JS) and `_time_unit(id, label)` helpers, consumed directly by the home page rather than as a single wrapper component.
- `pie_pagina.py` — Footer with links, legal section, and contact email.

### State and Models

- [trailcorremosadriana_v2/state/](trailcorremosadriana_v2/state/) — Global state (empty, pending). Page-scoped state lives alongside its page (e.g. `contacto_state.py`).
- [trailcorremosadriana_v2/models/](trailcorremosadriana_v2/models/) — SQLAlchemy models (empty, pending).

### Assets

Static assets live in [assets/](assets/) and are served at the root URL path by Reflex.

### Generated Code

The [.web/](.web/) directory contains Reflex-generated React/Node code. Do not edit files here directly — they are regenerated on each `reflex run`.

## Reflex Patterns

- Pages are decorated with `@rx.page(route="/...")` and registered in the app entry point.
- State classes inherit from `rx.State`. Async event handlers update state variables and trigger UI re-renders.
- Components are plain Python functions returning `rx.*` elements. Tailwind CSS classes are used for styling via `class_name=`.
- The race date target for the countdown is **July 11, 2026**.
