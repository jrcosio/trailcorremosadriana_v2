## Project Overview

Official website for the "Trail Sierra de Peñasagra - Corremos por Adriana" race event. Built with [Reflex](https://reflex.dev/), a Python framework that compiles Python code into a React frontend with a FastAPI backend.

Stack: Python **3.12** (pinned in `.python-version`), Reflex `>=0.8.27`, `python-dotenv`. Dependencies are managed with [uv](https://docs.astral.sh/uv/) and locked in `uv.lock`.

## Commands

```bash
# Install dependencies (from uv.lock)
uv sync

# Run development server (starts both backend and frontend)
uv run reflex run

# Run in production mode
uv run reflex run --env prod

# Export static build
uv run reflex export
```

There is no test suite or linter configured yet.

### Deployment

Production runs in Docker behind a Caddy reverse proxy:

- [Dockerfile](Dockerfile) — multi-stage build on `python:3.12-slim`; installs uv + Node 20, runs `uv sync --locked --no-dev`, exposes frontend `3000` / backend `8000`, and launches `uv run reflex run --env prod --backend-host 0.0.0.0`.
- [docker-compose.yml](docker-compose.yml) — `app` + `caddy` services on a private `webnet` network.
- [Caddyfile](Caddyfile) — serves domain `trailpeñasagra.com`; proxies backend routes (`/_event/*`, `/_upload/*`, `/ping`) to `8000` and everything else to the frontend `3000`.

```bash
# Build and run the full production stack
docker compose up --build
```

## Architecture

Reflex apps use a **component/state/page** pattern where Python functions return UI trees that compile to React components.

### Key Files

- [rxconfig.py](rxconfig.py) — Reflex config: app name, `show_built_with_reflex=False`, plugins (`SitemapPlugin`, `TailwindV4Plugin`)
- [trailcorremosadriana_v2/trailcorremosadriana_v2.py](trailcorremosadriana_v2/trailcorremosadriana_v2.py) — App entry point: creates the `app` instance with `theme=rx.theme(appearance="light")` and registers the five pages via `app.add_page(...)`.

### Pages

Five routes are registered in [trailcorremosadriana_v2.py](trailcorremosadriana_v2/trailcorremosadriana_v2.py) (`/`, `/contacto`, `/recorridos`, `/galeria`, `/reglamento`):

- [pages/principal/principal.py](trailcorremosadriana_v2/pages/principal/principal.py) — Home (`/`). Composes the hero + countdown with sections from [pages/principal/secciones/](trailcorremosadriana_v2/pages/principal/secciones/): `inscripciones`, `camiseta`, `patrocinadores` are active; `noticias`, `voluntarios`, `colaboradores` are scaffolded but commented out.
- [pages/contacto/contacto.py](trailcorremosadriana_v2/pages/contacto/contacto.py) — Contact form (`/contacto`), backed by [contacto_state.py](trailcorremosadriana_v2/pages/contacto/contacto_state.py). Sends mail via `smtplib` (Gmail SMTP over SSL, port 465); credentials from env vars `SENDER_EMAIL`, `SENDER_PASSWORD`, `RECEIVER_EMAIL` loaded via `python-dotenv`.
- [pages/recorridos/recorridos.py](trailcorremosadriana_v2/pages/recorridos/recorridos.py) — Race routes page (`/recorridos`). Backed by `RecorridosState` (var `recorrido` ∈ `"27"`/`"14"`/`"7"`, handler `seleccionar_recorrido`). A 3-distance selector toggles per-distance spec / refreshment (avituallamientos) / mandatory-equipment cards, an embedded Wikiloc map iframe, and a GPX download link.
- [pages/galeria/galeria.py](trailcorremosadriana_v2/pages/galeria/galeria.py) — Gallery (`/galeria`). Grid of album cards built from the `ALBUMES` dict (year → Google Photos URL), newest first.
- [pages/reglamento/reglamento.py](trailcorremosadriana_v2/pages/reglamento/reglamento.py) — Official regulations (`/reglamento`). Pricing cards per distance, a logistics/equipment info section, and an accordion of rules (environment & safety, responsibility & insurance, penalties, image rights).

### Components

Reusable UI in [trailcorremosadriana_v2/components/](trailcorremosadriana_v2/components/):

- `barra_navegacion.py` — Sticky top nav bar (70px, dark slate `#434c53`). Desktop links + mobile hamburger menu, with a central orange "Inscríbete" CTA.
- `cabecera.py` — Reusable full-screen hero (100dvh) that takes a background image path plus child content.
- `contador_regresivo.py` — Live countdown to race date (July 11, 2026). Exposes `_countdown_script()` (injects client-side JS) and `_time_unit(id, label)` helpers, consumed directly by the home page rather than as a single wrapper component.
- `pie_pagina.py` — Footer with links, legal section, and contact email.

### State and Models

- [trailcorremosadriana_v2/state/](trailcorremosadriana_v2/state/) — Global state (empty, pending). Page-scoped state lives alongside its page (e.g. `ContactoState` in `pages/contacto/contacto_state.py`, `RecorridosState` in `pages/recorridos/recorridos.py`).
- [trailcorremosadriana_v2/models/](trailcorremosadriana_v2/models/) — SQLAlchemy models (empty, pending). No database is wired up yet.

### Assets

Static assets live in [assets/](assets/) and are served at the root URL path by Reflex.

### Generated Code

The [.web/](.web/) directory contains Reflex-generated React/Node code. Do not edit files here directly — they are regenerated on each `reflex run`.

## Reflex Patterns

- Pages are plain functions registered in the app entry point with `app.add_page(fn, route="/...")`.
- State classes inherit from `rx.State`. Async event handlers update state variables and trigger UI re-renders; `python-dotenv`'s `load_dotenv()` loads `.env` (e.g. SMTP credentials in `contacto_state.py`).
- Components are plain Python functions returning `rx.*` elements. Tailwind CSS classes are used for styling via `class_name=`.
- The race date target for the countdown is **July 11, 2026**.

## Related Docs

- [README.md](README.md) — project README (Spanish), MIT license.
- [AGENTS.md](AGENTS.md) — concise agent setup/structure notes (Spanish).
