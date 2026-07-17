import reflex as rx

from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina
from trailcorremosadriana_v2.pages.clasificacion.clasificacion_state import (
    CARRERAS,
    ClasificacionState,
)

_ORO = "#FFD700"
_PLATA = "#C0C0C0"
_BRONCE = "#CD7F32"
_SOLO_ESCRITORIO = rx.breakpoints(initial="none", md="table-cell")


def _hero_clasificacion() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(
                f"Edición {ClasificacionState.anio} | Cosío, Cantabria",
                color="white",
                font_size=rx.breakpoints(initial="0.75em", sm="0.9em"),
                font_weight="600",
                letter_spacing="0.16em",
                text_transform="uppercase",
                background_color="rgba(255,255,255,0.12)",
                border="1px solid rgba(255,255,255,0.25)",
                border_radius="999px",
                padding="0.5em 1em",
                text_align="center",
            ),
            rx.heading(
                "CLASIFICACIONES",
                color="white",
                font_size=rx.breakpoints(initial="2.8em", sm="4.5em", lg="6em"),
                font_weight="900",
                line_height="0.95",
                text_align="center",
                letter_spacing="-0.04em",
            ),
            rx.heading(
                "SIERRA DE PEÑASAGRA",
                color="orange",
                font_size=rx.breakpoints(initial="2em", sm="3.2em", lg="4.5em"),
                font_weight="900",
                line_height="1",
                text_align="center",
                letter_spacing="-0.03em",
            ),
            rx.text(
                "Consulta los resultados oficiales de cada prueba: filtra por género o busca a un corredor por su nombre.",
                color="#E5E7EB",
                font_size=rx.breakpoints(initial="1em", sm="1.15em", lg="1.3em"),
                text_align="center",
                max_width="760px",
                line_height="1.7",
            ),
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", color="orange", size=18),
                    rx.text("Otras ediciones", color="orange", font_weight="600"),
                    spacing="2",
                    align="center",
                ),
                href="/clasificaciones",
                text_decoration="none",
                _hover={"opacity": "0.8"},
            ),
            spacing="4",
            align="center",
            padding=rx.breakpoints(initial="2em 1em", sm="3em 2em"),
        ),
        min_height=rx.breakpoints(initial="520px", lg="620px"),
        width="100%",
        background_image="linear-gradient(rgba(0,0,0,0.55), rgba(51,51,51,0.92)), url('/fondos/fondo.webp')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
    )


def _boton_carrera(clave: str) -> rx.Component:
    _fichero, titulo, subtitulo, color, _icono = CARRERAS[clave]
    activo = ClasificacionState.carrera == clave
    return rx.cond(
        ClasificacionState.carreras_disponibles.contains(clave),
        rx.button(
            rx.vstack(
                rx.text(titulo, font_size="1em", font_weight="900", line_height="1.1"),
                rx.text(subtitulo, font_size="0.75em", font_weight="700", opacity="0.85"),
                spacing="1",
                align="center",
            ),
            on_click=ClasificacionState.seleccionar_carrera(clave),
            width="100%",
            min_height="82px",
            border_radius="18px",
            color="white",
            background_color=rx.cond(activo, color, "rgba(255,255,255,0.04)"),
            border=rx.cond(activo, f"1px solid {color}", "1px solid rgba(255,255,255,0.10)"),
            box_shadow=rx.cond(activo, f"0 18px 45px {color}33", "none"),
            cursor="pointer",
            transition="all 0.25s ease",
            _hover={"transform": "translateY(-3px)", "border_color": color},
        ),
    )


def _selector_carreras() -> rx.Component:
    return rx.box(
        rx.grid(
            *[_boton_carrera(clave) for clave in CARRERAS],
            columns=rx.breakpoints(initial="1", md="3"),
            spacing="4",
            width="100%",
        ),
        width="100%",
        max_width="1000px",
        margin="0 auto",
        margin_top=rx.breakpoints(initial="-3.5em", lg="-5em"),
        position="relative",
        z_index="2",
    )


def _pill_genero(valor: str, etiqueta: str, icono: str) -> rx.Component:
    activo = ClasificacionState.genero == valor
    return rx.button(
        rx.icon(icono, size=16),
        etiqueta,
        on_click=ClasificacionState.seleccionar_genero(valor),
        border_radius="999px",
        color="white",
        font_weight="700",
        background_color=rx.cond(
            activo, ClasificacionState.color_carrera, "rgba(255,255,255,0.05)"
        ),
        border=rx.cond(
            activo,
            f"1px solid transparent",
            "1px solid rgba(255,255,255,0.12)",
        ),
        cursor="pointer",
        transition="all 0.2s ease",
        _hover={"transform": "translateY(-1px)"},
    )


def _filtros() -> rx.Component:
    return rx.flex(
        rx.hstack(
            _pill_genero("General", "General", "users"),
            _pill_genero("Masculino", "Masculino", "user"),
            _pill_genero("Femenino", "Femenino", "user"),
            spacing="2",
            wrap="wrap",
        ),
        rx.spacer(),
        rx.hstack(
            rx.input(
                rx.input.slot(rx.icon("search", size=16, color="#94A3B8")),
                placeholder="Buscar por nombre o apellidos...",
                value=ClasificacionState.busqueda,
                on_change=ClasificacionState.actualizar_busqueda,
                width=rx.breakpoints(initial="100%", md="320px"),
                size="3",
                radius="full",
                variant="soft",
                background_color="rgba(255,255,255,0.06)",
                color="white",
            ),
            rx.text(
                ClasificacionState.total_filas,
                " corredores",
                color="#94A3B8",
                font_size="0.9em",
                white_space="nowrap",
            ),
            spacing="3",
            align="center",
            width=rx.breakpoints(initial="100%", md="auto"),
        ),
        direction=rx.breakpoints(initial="column", md="row"),
        gap="1em",
        align=rx.breakpoints(initial="start", md="center"),
        width="100%",
    )


def _celda_pos(fila: rx.Var) -> rx.Component:
    def medalla(color: str) -> rx.Component:
        return rx.hstack(
            rx.icon("medal", color=color, size=18),
            rx.text(fila["pos_mostrada"], color=color, font_weight="900"),
            spacing="1",
            align="center",
        )

    return rx.match(
        fila["podium"],
        ("1", medalla(_ORO)),
        ("2", medalla(_PLATA)),
        ("3", medalla(_BRONCE)),
        rx.text(fila["pos_mostrada"], color="white", font_weight="700"),
    )


def _fila_tabla(fila: rx.Var) -> rx.Component:
    return rx.table.row(
        rx.table.cell(_celda_pos(fila)),
        rx.table.cell(
            rx.text(fila["dorsal"], color="#94A3B8"),
            display=_SOLO_ESCRITORIO,
        ),
        rx.table.cell(
            rx.text(
                fila["nombre"] + " " + fila["apellidos"],
                color="white",
                font_weight="600",
            ),
        ),
        rx.cond(
            ~ClasificacionState.es_marcha,
            rx.table.cell(
                rx.text(fila["categoria"], color="#CBD5E1"),
                display=_SOLO_ESCRITORIO,
            ),
            rx.fragment(),
        ),
        rx.table.cell(
            rx.text(
                rx.cond(fila["club"] != "", fila["club"], "—"),
                color="#94A3B8",
            ),
            display=_SOLO_ESCRITORIO,
        ),
        rx.table.cell(
            rx.cond(
                fila["estado"] == "Finalizado",
                rx.text(
                    fila["meta"],
                    font_family="monospace",
                    color="white",
                    font_weight="700",
                ),
                rx.badge(fila["estado"], color_scheme="red", variant="soft"),
            ),
        ),
        background_color=rx.match(
            fila["podium"],
            ("1", "rgba(255,215,0,0.10)"),
            ("2", "rgba(192,192,192,0.10)"),
            ("3", "rgba(205,127,50,0.12)"),
            ("top5", "rgba(255,255,255,0.05)"),
            "transparent",
        ),
        border_left=rx.match(
            fila["podium"],
            ("1", f"3px solid {_ORO}"),
            ("2", f"3px solid {_PLATA}"),
            ("3", f"3px solid {_BRONCE}"),
            "3px solid transparent",
        ),
        transition="background-color 0.15s ease",
        _hover={"background_color": "rgba(255,255,255,0.07)"},
    )


def _cabecera_col(texto: str, **props) -> rx.Component:
    return rx.table.column_header_cell(
        texto,
        color="#CBD5E1",
        font_size="0.75em",
        font_weight="800",
        text_transform="uppercase",
        letter_spacing="0.08em",
        background_color="#3a3a3a",  # opaco: necesario con la cabecera sticky
        **props,
    )


def _tabla_clasificacion() -> rx.Component:
    return rx.box(
        rx.box(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        _cabecera_col("Pos"),
                        _cabecera_col("Dorsal", display=_SOLO_ESCRITORIO),
                        _cabecera_col("Nombre"),
                        rx.cond(
                            ~ClasificacionState.es_marcha,
                            _cabecera_col("Categoría", display=_SOLO_ESCRITORIO),
                            rx.fragment(),
                        ),
                        _cabecera_col("Club", display=_SOLO_ESCRITORIO),
                        _cabecera_col("Meta"),
                    ),
                    position="sticky",
                    top="0",
                    z_index="1",
                ),
                rx.table.body(
                    rx.foreach(ClasificacionState.filas, _fila_tabla),
                ),
                variant="ghost",
                size="2",
                width="100%",
            ),
            max_height="70vh",
            overflow_y="auto",
            overflow_x="auto",
            width="100%",
        ),
        rx.cond(
            ClasificacionState.total_filas == 0,
            rx.center(
                rx.vstack(
                    rx.icon("search-x", color="#94A3B8", size=32),
                    rx.text("Sin resultados para esta búsqueda.", color="#94A3B8"),
                    spacing="2",
                    align="center",
                ),
                padding="3em",
            ),
        ),
        width="100%",
        background_color="rgba(255,255,255,0.04)",
        border="1px solid rgba(255,255,255,0.08)",
        border_radius="18px",
        box_shadow="0 16px 40px rgba(0,0,0,0.20)",
        overflow="hidden",
    )


def clasificacion() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        _hero_clasificacion(),
        rx.box(
            rx.vstack(
                _selector_carreras(),
                _filtros(),
                _tabla_clasificacion(),
                spacing="7",
                width="100%",
                max_width="1200px",
                margin="0 auto",
                padding=rx.breakpoints(initial="0 1em 3em", sm="0 2em 4em"),
            ),
            width="100%",
            background_color="#333333",
        ),
        pie_pagina(),
        background_color="#333333",
    )
