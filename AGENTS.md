# Notas para agentes

## Comandos
- Instala dependencias con `uv sync`; la versión local de Python es `3.12` según `.python-version`.
- Arranca desarrollo con `uv run reflex run`; la app queda en `http://localhost:3000`.
- Exporta/build de producción con `uv run reflex export`.
- Ejecuta en modo producción con `uv run reflex run --env prod`.
- No hay comandos configurados de tests, lint, formatter ni typecheck en `pyproject.toml`.

## Estructura Reflex
- El cableado principal está en `trailcorremosadriana_v2/trailcorremosadriana_v2.py`; las rutas se registran ahí con `app.add_page(...)`.
- Los componentes reutilizables están en `trailcorremosadriana_v2/components/`; las páginas están en `trailcorremosadriana_v2/pages/`.
- Los componentes Reflex son funciones Python que devuelven elementos `rx.*`; el estado vive en clases que heredan de `rx.State`.
- Los archivos de `assets/` se sirven desde rutas raíz: por ejemplo `assets/logos/logo.png` se referencia como `/logos/logo.png`.
- No edites `.web/` ni `.states/`; Reflex los regenera.

## Particularidades del repo
- `rxconfig.py` activa `SitemapPlugin` y `TailwindV4Plugin`.
- La cuenta atrás está fijada al 11 de julio de 2026 en `components/contador_regresivo.py`; la home usa `_countdown_script()` y `_time_unit()` directamente.
- El formulario de contacto envía email desde `pages/contacto/contacto_state.py` y necesita `SENDER_EMAIL`, `SENDER_PASSWORD` y `RECEIVER_EMAIL` en el entorno.
- En Docker, producción ejecuta `uv run reflex run --env prod --backend-host 0.0.0.0`; Caddy proxyfía `/_event/*`, `/_upload/*` y `/ping` al backend `8000`, y el resto al frontend `3000`.
- Las clasificaciones (`/clasificaciones` y la ruta dinámica `/clasificaciones/[anio]`) leen los CSVs de `datos/<año>/` (`Clasificacion_27km.csv`, `Clasificacion_14km.csv`, `Clasificacion_marcha.csv`) en el backend vía `on_load`; para publicar una edición nueva basta con crear la carpeta `datos/<año>/` con los CSVs, sin tocar código.
- No declares una var `anio` en ningún state: la genera Reflex automáticamente por la ruta dinámica (si la declaras, lanza `DynamicRouteArgShadowsStateVarError` al arrancar).
