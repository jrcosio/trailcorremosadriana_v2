# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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
- [trailcorremosadriana_v2/pages/principal/principal.py](trailcorremosadriana_v2/pages/principal/principal.py) — Home page (`/`)
- [trailcorremosadriana_v2/pages/galeria/galeria.py](trailcorremosadriana_v2/pages/galeria/galeria.py) — Gallery page (`/galeria`), currently a placeholder

### Components

All reusable UI is in [trailcorremosadriana_v2/components/](trailcorremosadriana_v2/components/):

- `barra_navegacion.py` — Sticky top nav bar (7vh, green background)
- `cabecera.py` — Full-screen hero section (93vh, background image overlay)
- `contador_regresivo.py` — Live countdown to race date (July 11, 2026), uses a Reflex `State` class with an async `tick()` event handler

### State and Models

- [trailcorremosadriana_v2/state/](trailcorremosadriana_v2/state/) — Global state (empty, pending)
- [trailcorremosadriana_v2/models/](trailcorremosadriana_v2/models/) — SQLAlchemy models (empty, pending)

### Assets

Static assets live in [assets/](assets/) and are served at the root URL path by Reflex.

### Generated Code

The [.web/](.web/) directory contains Reflex-generated React/Node code. Do not edit files here directly — they are regenerated on each `reflex run`.

## Reflex Patterns

- Pages are decorated with `@rx.page(route="/...")` and registered in the app entry point.
- State classes inherit from `rx.State`. Async event handlers update state variables and trigger UI re-renders.
- Components are plain Python functions returning `rx.*` elements. Tailwind CSS classes are used for styling via `class_name=`.
- The race date target for the countdown is **July 11, 2026**.
