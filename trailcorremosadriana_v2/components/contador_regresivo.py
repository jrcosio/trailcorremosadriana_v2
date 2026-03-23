import reflex as rx
from datetime import datetime, timezone

# Fecha objetivo
FECHA_CARRERA = datetime(2026, 7, 11, 0, 0, 0, tzinfo=timezone.utc)

# Timestamp en ms para JS
TARGET_TIMESTAMP_MS = int(FECHA_CARRERA.timestamp() * 1000)


def _countdown_script() -> rx.Component:
    """JS client-side: cero carga en el servidor."""
    return rx.script(
        f"""
        (function() {{
            const target = {TARGET_TIMESTAMP_MS};
            const ids = ["cd-days","cd-hours","cd-minutes","cd-seconds"];

            function pad(n) {{ return String(n).padStart(2, '0'); }}

            function tick() {{
                const diff = Math.max(0, target - Date.now());
                const s = Math.floor(diff / 1000);
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
                if (diff > 0) requestAnimationFrame(() => setTimeout(tick, 250));
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
            # background="rgba(255,140,0,0.15)",
            # border=f"1px solid rgba(255,140,0,0.3)",
            # border_radius="12px",
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


def _separator() -> rx.Component:
    return rx.text(
        ":",
        color="orange",
        font_size=rx.breakpoints(initial="1.8em", sm="2.5em", lg="3.5em"),
        font_weight="bold",
        line_height="1",
        padding_bottom="1.2em",  # compensa el label de abajo
    )


# def countdown() -> rx.Component:
#     return rx.box(
#         _countdown_script(),
#         rx.hstack(
#             _time_unit("cd-days", "Días"),
#             _separator(),
#             _time_unit("cd-hours", "Horas"),
#             _separator(),
#             _time_unit("cd-minutes", "Min"),
#             _separator(),
#             _time_unit("cd-seconds", "Seg"),
#             align="end",
#             justify="center",
#             spacing=rx.breakpoints(initial="2", sm="3", lg="4"),
#             flex_wrap="wrap",
#         ),
#     )