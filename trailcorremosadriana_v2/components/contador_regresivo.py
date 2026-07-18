import reflex as rx
from datetime import datetime, timedelta, timezone

# Fecha objetivo. Al confirmar la edición 2027 basta con actualizarla (y los
# literales de año de los bloques): el contador vuelve a la fase "pre" solo.
FECHA_CARRERA = datetime(2026, 7, 11, 0, 0, 0, tzinfo=timezone.utc)
FECHA_LEGIBLE = "Sábado, 11 de Julio de 2026"
LUGAR = "Cosío, Rionansa (Cantabria)"
PROXIMA_EDICION = "Trail Peñasagra 2027"

# Timestamp en ms para JS
TARGET_TIMESTAMP_MS = int(FECHA_CARRERA.timestamp() * 1000)
DIA = timedelta(days=1)


def _fase_inicial() -> str:
    """Fase calculada en el servidor al compilar: evita el flash del bloque
    equivocado antes de que corra el JS (que la corrige en vivo)."""
    ahora = datetime.now(timezone.utc)
    if ahora < FECHA_CARRERA:
        return "pre"
    if ahora < FECHA_CARRERA + DIA:
        return "hoy"
    return "post"


def _countdown_script() -> rx.Component:
    """JS client-side: cero carga en el servidor. Alterna los bloques de fase
    (cd-fase-pre / cd-fase-hoy / cd-fase-post) y actualiza los dígitos."""
    return rx.script(
        f"""
        (function() {{
            const target = {TARGET_TIMESTAMP_MS};
            const finDia = target + 86400000;
            const ids = ["cd-days","cd-hours","cd-minutes","cd-seconds"];

            function pad(n) {{ return String(n).padStart(2, '0'); }}

            function fase(now) {{
                return now < target ? "pre" : (now < finDia ? "hoy" : "post");
            }}

            function mostrar(f) {{
                ["pre","hoy","post"].forEach(x => {{
                    const el = document.getElementById("cd-fase-" + x);
                    if (el) el.style.display = (x === f ? "" : "none");
                }});
            }}

            function tick() {{
                const now = Date.now();
                const f = fase(now);
                mostrar(f);
                if (f === "pre") {{
                    const s = Math.floor((target - now) / 1000);
                    const vals = [
                        Math.floor(s / 86400),
                        Math.floor((s % 86400) / 3600),
                        Math.floor((s % 3600) / 60),
                        s % 60
                    ];
                    ids.forEach((id, i) => {{
                        const el = document.getElementById(id);
                        if (el) el.textContent = pad(vals[i]);
                    }});
                    setTimeout(tick, 250);
                }} else if (f === "hoy") {{
                    setTimeout(tick, 60000);
                }}
            }}
            tick();
        }})();
        """
    )


def _time_unit(element_id: str, label: str) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "00",
                id=element_id,
                font_weight="800",
                font_family="monospace",
                color="white",
                font_size=rx.breakpoints(
                    initial="2.2em", sm="3em", lg="4em"
                ),
                line_height="1",
                text_align="center",
            ),
            padding=rx.breakpoints(
                initial="0.6em 0.8em", sm="0.6em 1em", lg="0.8em 1.2em"
            ),
            min_width=rx.breakpoints(initial="3em", sm="4em", lg="5em"),
        ),
        rx.text(
            label,
            color="rgba(255,165,0,0.8)",
            font_size=rx.breakpoints(initial="0.7em", sm="0.85em", lg="1em"),
            font_weight="600",
            text_transform="uppercase",
            letter_spacing="0.1em",
        ),
        align="center",
        spacing="2",
    )


def _texto_destacado(texto: str) -> rx.Component:
    return rx.text(
        texto,
        font_size=rx.breakpoints(initial="1.5em", sm="2em", lg="2.5em"),
        color="orange",
        text_align="center",
    )


def _texto_secundario(texto: str) -> rx.Component:
    return rx.text(
        texto,
        color="rgba(255,165,0,0.8)",
        font_size=rx.breakpoints(initial="0.9em", sm="1.1em", lg="1.3em"),
        font_weight="600",
        text_transform="uppercase",
        letter_spacing="0.1em",
        text_align="center",
    )


def _bloque_pre() -> rx.Component:
    return rx.vstack(
        _texto_destacado("Ya solo faltan"),
        rx.hstack(
            _time_unit("cd-days", "Días"),
            _time_unit("cd-hours", "Horas"),
            _time_unit("cd-minutes", "Min"),
            _time_unit("cd-seconds", "Seg"),
            justify="center",
            align="end",
            spacing="3",
        ),
        rx.text(
            FECHA_LEGIBLE,
            color="orange",
            font_size=rx.breakpoints(initial="1.3em", sm="1.8em", lg="2.2em"),
            font_weight="bold",
            text_align="center",
        ),
        align="center",
        spacing="2",
        id="cd-fase-pre",
        display="" if _fase_inicial() == "pre" else "none",
    )


def _bloque_hoy() -> rx.Component:
    return rx.vstack(
        _texto_destacado("¡Hoy es el gran día!"),
        rx.text(
            "Mucha suerte a todos los corredores",
            color="white",
            font_size=rx.breakpoints(initial="1.1em", sm="1.4em", lg="1.7em"),
            font_weight="bold",
            text_align="center",
        ),
        align="center",
        spacing="2",
        id="cd-fase-hoy",
        display="" if _fase_inicial() == "hoy" else "none",
    )


def _bloque_post() -> rx.Component:
    return rx.vstack(
        _texto_destacado("¡Próximamente...!"),
        rx.text(
            PROXIMA_EDICION,
            font_weight="800",
            font_family="monospace",
            color="white",
            font_size=rx.breakpoints(initial="1.6em", sm="2.4em", lg="3em"),
            line_height="1.2",
            text_align="center",
        ),
        _texto_secundario("¡Gracias por hacer posible la edición 2026!"),
        align="center",
        spacing="3",
        id="cd-fase-post",
        display="" if _fase_inicial() == "post" else "none",
    )


def contador_hero() -> rx.Component:
    """Caja del hero: script + bloques de fase + lugar. Único export público."""
    return rx.vstack(
        _countdown_script(),
        rx.box(
            _bloque_pre(),
            _bloque_hoy(),
            _bloque_post(),
            background_color="#3333339D",
            border_radius="1em",
            border="2px solid orange",
            padding="1.5em",
        ),
        rx.text(
            LUGAR,
            color="orange",
            font_size=rx.breakpoints(initial="1em", sm="1.5em", lg="2em"),
            font_weight="bold",
            text_align="center",
        ),
        align="center",
        spacing="3",
    )
