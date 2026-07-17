import reflex as rx

from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina
from trailcorremosadriana_v2.pages.clasificacion.clasificacion_state import (
    ClasificacionesIndexState,
)


def _tarjeta_anio(anio: rx.Var) -> rx.Component:
    """Tarjeta individual para la clasificación de cada edición."""
    return rx.link(
        rx.box(
            rx.vstack(
                rx.icon("trophy", color="orange", size=48),
                rx.text(
                    f"Edición {anio}",
                    font_size="1.8em",
                    font_weight="bold",
                    color="white",
                ),
                rx.text(
                    "Resultados oficiales de las tres pruebas",
                    color="#CBD5E1",
                    font_size="0.95em",
                ),
                rx.hstack(
                    rx.text("Ver clasificaciones", color="orange", font_weight="600"),
                    rx.icon("arrow-right", color="orange", size=18),
                    spacing="2",
                    align="center",
                ),
                spacing="4",
                align="center",
                justify="center",
                padding="2.5em",
                width="100%",
            ),
            background_color="rgba(255,255,255,0.03)",
            border="1px solid rgba(255,255,255,0.08)",
            border_radius="16px",
            width="100%",
            transition="all 0.3s ease",
            _hover={
                "border_color": "orange",
                "transform": "translateY(-4px)",
                "box_shadow": "0 8px 30px rgba(255,165,0,0.15)",
            },
        ),
        href=f"/clasificaciones/{anio}",
        text_decoration="none",
        width=rx.breakpoints(initial="100%", sm="45%", lg="30%"),
    )


def clasificaciones() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        rx.vstack(
            rx.text(
                "CLASIFICACIONES",
                color="white",
                font_size=rx.breakpoints(initial="28px", sm="36px", lg="42px"),
                font_weight="800",
                text_align="center",
            ),
            rx.text(
                "Consulta los resultados oficiales de cada edición.",
                color="#CBD5E1",
                font_size="18px",
                text_align="center",
            ),
            rx.divider(
                border_color="#30a46c",
                width="100px",
                border_width="2px",
            ),
            # Tarjetas por año (se detectan automáticamente en datos/)
            rx.flex(
                rx.foreach(ClasificacionesIndexState.anios, _tarjeta_anio),
                direction="row",
                wrap="wrap",
                spacing="5",
                justify="center",
                width="100%",
                max_width="1200px",
                margin="0 auto",
                padding=rx.breakpoints(initial="1em", sm="2em"),
            ),
            rx.cond(
                ClasificacionesIndexState.anios.length() == 0,
                rx.text(
                    "Todavía no hay clasificaciones publicadas.",
                    color="#94A3B8",
                    text_align="center",
                ),
            ),
            spacing="5",
            width="100%",
            align="center",
            padding_top="2em",
            padding_bottom="2em",
        ),
        rx.spacer(),
        pie_pagina(),
        background_color="#333333",
        min_height="100vh",
    )
