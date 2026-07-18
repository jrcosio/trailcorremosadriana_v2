import reflex as rx

from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina


def _hero_reglamento() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(
                "11 de julio, 2026 | Cosío, Cantabria",
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
                "REGLAMENTO OFICIAL",
                color="white",
                font_size=rx.breakpoints(initial="2.4em", sm="4em", lg="5.5em"),
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
                "Desafía tus límites en el corazón de Rionansa. Tres distancias, una montaña legendaria.",
                color="#E5E7EB",
                font_size=rx.breakpoints(initial="1em", sm="1.15em", lg="1.3em"),
                text_align="center",
                max_width="760px",
                line_height="1.7",
            ),
            spacing="4",
            align="center",
            padding=rx.breakpoints(initial="2em 1em", sm="3em 2em"),
        ),
        min_height=rx.breakpoints(initial="560px", lg="640px"),
        width="100%",
        background_image="linear-gradient(rgba(0,0,0,0.55), rgba(51,51,51,0.92)), url('/fondos/fondo.webp')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
    )


def _dato_carrera(texto: str, color: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", color=color, size=18),
        rx.text(texto, color="#CBD5E1", font_size="0.95em"),
        spacing="2",
        align="center",
        width="100%",
    )


def _tarjeta_modalidad(
    etiqueta: str,
    titulo: str,
    distancia: str,
    desnivel: str,
    precio: str,
    nota_precio: str,
    enlace: str,
    color: str,
    datos: list[str],
) -> rx.Component:
    return rx.box(
        rx.box(height="4px", background_color=color, width="100%"),
        rx.vstack(
            rx.text(
                etiqueta,
                color=color,
                font_size="0.75em",
                font_weight="800",
                text_transform="uppercase",
                letter_spacing="0.16em",
            ),
            rx.heading(
                titulo,
                color="white",
                font_size=rx.breakpoints(initial="1.8em", lg="2.15em"),
                font_weight="900",
                line_height="1.05",
            ),
            rx.hstack(
                rx.text(distancia, color="white", font_size="3em", font_weight="900", line_height="1"),
                rx.text("KM", color="#94A3B8", font_weight="800", padding_top="1.6em"),
                rx.spacer(),
                rx.text(desnivel, color=color, font_size="1.25em", font_weight="800"),
                width="100%",
                align="end",
            ),
            rx.vstack(
                *[_dato_carrera(dato, color) for dato in datos],
                spacing="3",
                width="100%",
            ),
            rx.hstack(
                rx.vstack(
                    rx.text(precio, color="white", font_size="1.7em", font_weight="900", line_height="1"),
                    rx.cond(
                        nota_precio != "",
                        rx.text(nota_precio, color="#94A3B8", font_size="0.7em", text_transform="uppercase"),
                    ),
                    align="start",
                    spacing="1",
                ),
                rx.spacer(),
                rx.button(
                    "Inscripciones cerradas",
                    color_scheme="gray",
                    variant="soft",
                    border_radius="999px",
                    font_weight="800",
                    disabled=True,
                ),
                border_top="1px solid rgba(255,255,255,0.08)",
                padding_top="1.5em",
                width="100%",
                align="center",
            ),
            spacing="5",
            align="start",
            padding="1.75em",
            width="100%",
        ),
        background_color="rgba(255,255,255,0.04)",
        border="1px solid rgba(255,255,255,0.08)",
        border_radius="18px",
        overflow="hidden",
        box_shadow="0 16px 40px rgba(0,0,0,0.22)",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-6px)",
            "border_color": color,
            "box_shadow": f"0 18px 45px {color}33",
        },
    )


def _modalidades() -> rx.Component:
    return rx.grid(
        _tarjeta_modalidad(
            "Competición",
            "Trail Peñasagra",
            "27",
            "+1700m",
            "28€",
            "",
            "https://www.gedsports.com/inscription/trail-sierra-de-penasagra--27-km",
            "#30a46c",
            ["3 avituallamientos + meta", "Cronometraje GedSPORT", "Salida: 9:00h Plaza Cosío"],
        ),
        _tarjeta_modalidad(
            "Competición",
            "Speed Trail Peñasagra",
            "14",
            "+800m",
            "18€",
            "",
            "https://www.gedsports.com/inscription/trail-sierra-de-penasagra--14-km",
            "orange",
            ["2 avituallamientos + meta", "Cronometraje GedSPORT", "Salida: 9:00h Plaza Cosío"],
        ),
        _tarjeta_modalidad(
            "Familiar",
            "Familiar Peñasagra",
            "7",
            "+250m",
            "12€ / 5€",
            "Niños < 8 años gratis",
            "https://www.gedsports.com/inscription/trail-sierra-de-penasagra--menores-de-8-anos",
            "#38BDF8",
            ["Avituallamiento en meta", "Para todas las edades", "Participación conjunta"],
        ),
        columns=rx.breakpoints(initial="1", md="3"),
        spacing="5",
        width="100%",
        margin_top=rx.breakpoints(initial="-4em", lg="-6em"),
        position="relative",
        z_index="2",
    )


def _titulo_bloque(numero: str, titulo: str, color: str) -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.text(numero, color="white", font_weight="900"),
            width="42px",
            height="42px",
            border_radius="999px",
            background_color=color,
            flex_shrink="0",
        ),
        rx.heading(
            titulo,
            color="white",
            font_size=rx.breakpoints(initial="1.8em", sm="2.4em"),
            font_weight="900",
        ),
        spacing="3",
        align="center",
    )


def _info_item(icono: str, titulo: str, texto: str) -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.icon(icono, color="orange", size=24),
            width="48px",
            height="48px",
            border_radius="12px",
            background_color="rgba(255,165,0,0.12)",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(titulo, color="white", font_size="1.1em", font_weight="800"),
            rx.text(texto, color="#CBD5E1", font_size="0.95em", line_height="1.6"),
            spacing="1",
            align="start",
        ),
        spacing="4",
        align="start",
        padding="1em",
        background_color="rgba(255,255,255,0.03)",
        border="1px solid rgba(255,255,255,0.08)",
        border_radius="16px",
        width="100%",
        _hover={"border_color": "rgba(255,165,0,0.45)"},
    )


def _equipamiento_item(icono: str, texto: str) -> rx.Component:
    return rx.vstack(
        rx.icon(icono, color="#CBD5E1", size=26),
        rx.text(texto, color="white", font_size="0.8em", font_weight="800", text_align="center"),
        spacing="2",
        align="center",
        justify="center",
        padding="1em",
        min_height="110px",
        border="1px solid rgba(255,255,255,0.08)",
        border_radius="14px",
        background_color="rgba(255,255,255,0.025)",
    )


def _informacion() -> rx.Component:
    return rx.grid(
        rx.vstack(
            _titulo_bloque("01", "LOGÍSTICA Y CARRERA", "#30a46c"),
            rx.vstack(
                _info_item(
                    "id-card",
                    "Inscripciones",
                    "Cerradas: la edición 2026 ya se ha celebrado. Estrictamente personales e intransferibles.",
                ),
                _info_item(
                    "clock",
                    "Retirada de dorsales",
                    "Día 11 de julio, de 7:30 a 8:30 en la carpa de la Plaza de Cosío.",
                ),
                _info_item(
                    "trophy",
                    "Categorías",
                    "Absoluta, Sénior, Veterano A (40-45), B (46-50) y C (+50). Premios locales para Rionansa.",
                ),
                spacing="4",
                width="100%",
            ),
            spacing="5",
            align="start",
            width="100%",
        ),
        rx.vstack(
            _titulo_bloque("02", "EQUIPAMIENTO", "orange"),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("triangle-alert", color="orange", size=24),
                        rx.text(
                            '"Sin vaso no hay paraíso": trae tu propio recipiente para líquidos.',
                            color="#FED7AA",
                            font_size="0.95em",
                            font_weight="700",
                            font_style="italic",
                        ),
                        spacing="3",
                        align="center",
                        padding="1em",
                        background_color="rgba(255,165,0,0.12)",
                        border_radius="12px",
                        width="100%",
                    ),
                    rx.grid(
                        _equipamiento_item("footprints", "Calzado trail"),
                        _equipamiento_item("circle-check", "Recipiente líquido"),
                        _equipamiento_item("shield", "Manta térmica"),
                        _equipamiento_item("shirt", "Cortavientos*"),
                        columns="2",
                        spacing="3",
                        width="100%",
                    ),
                    rx.text(
                        "*Sujeto a condiciones meteorológicas el día de la prueba.",
                        color="#94A3B8",
                        font_size="0.8em",
                        font_style="italic",
                        text_align="center",
                        width="100%",
                    ),
                    spacing="5",
                    width="100%",
                ),
                padding="1.5em",
                background_color="rgba(255,255,255,0.04)",
                border="1px solid rgba(255,255,255,0.08)",
                border_radius="18px",
                width="100%",
            ),
            spacing="5",
            align="start",
            width="100%",
        ),
        columns=rx.breakpoints(initial="1", lg="2"),
        spacing="6",
        width="100%",
    )


def _parrafo(texto: str, destacado: bool = False) -> rx.Component:
    return rx.text(
        texto,
        color="white" if destacado else "#CBD5E1",
        font_size="1em",
        line_height="1.7",
        font_weight="700" if destacado else "400",
    )


def _norma(texto: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", color="#30a46c", size=18),
        rx.text(texto, color="#CBD5E1", line_height="1.6"),
        spacing="3",
        align="start",
        width="100%",
    )


def _acordeon_item(valor: str, titulo: str, *contenido: rx.Component) -> rx.Component:
    return rx.accordion.item(
        rx.accordion.header(
            rx.accordion.trigger(
                rx.hstack(
                    rx.text(titulo, color="white", font_size="1em", font_weight="900", text_align="left"),
                    rx.spacer(),
                    rx.accordion.icon(color="orange"),
                    width="100%",
                    align="center",
                ),
                width="100%",
                padding="1.25em",
                background_color="transparent",
                _hover={"background_color": "rgba(255,255,255,0.04)"},
            )
        ),
        rx.accordion.content(
            rx.vstack(
                *contenido,
                spacing="3",
                align="start",
                width="100%",
                padding="1.25em",
                border_top="1px solid rgba(255,255,255,0.08)",
            )
        ),
        value=valor,
        background_color="rgba(255,255,255,0.04)",
        border="1px solid rgba(255,255,255,0.08)",
        border_radius="16px",
        overflow="hidden",
    )


def _reglamento_completo() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "REGLAMENTO COMPLETO",
            color="white",
            font_size=rx.breakpoints(initial="2em", sm="2.6em"),
            font_weight="900",
            text_align="center",
            letter_spacing="0.08em",
        ),
        rx.divider(border_color="#30a46c", width="100px", border_width="2px"),
        rx.accordion.root(
            _acordeon_item(
                "medio-ambiente",
                "MEDIO AMBIENTE Y SEGURIDAD",
                _parrafo(
                    "La carrera se desarrolla por parajes boscosos, pistas y senderos. Es obligación de todos preservar el entorno."
                ),
                _parrafo(
                    "Arrojar desperdicios fuera de las áreas de control será motivo de descalificación inmediata.",
                    destacado=True,
                ),
                _parrafo(
                    "La organización se reserva el derecho a desviar la carrera por recorridos alternativos para asegurar la integridad de los participantes."
                ),
            ),
            _acordeon_item(
                "responsabilidad",
                "RESPONSABILIDAD Y SEGURO",
                _parrafo(
                    "El participante manifiesta estar en forma física y psíquica óptima. La organización cuenta con seguro de Responsabilidad Civil, pero no se hace responsable de daños sufridos por el participante o causados a terceros."
                ),
                _parrafo(
                    "Es obligatorio conocer el recorrido previo al día de la prueba y cumplir las normas de circulación vial en los tramos compartidos."
                ),
            ),
            _acordeon_item(
                "penalizaciones",
                "PENALIZACIONES",
                _norma("No pasar por los puntos de control de paso."),
                _norma("Ensuciar o degradar el itinerario."),
                _norma("Participar con el dorsal de otra persona."),
                _norma("Comportamientos no deportivos o falta de respeto a la organización."),
                _norma("Ser acompañado por vehículos a motor durante el trayecto."),
            ),
            _acordeon_item(
                "imagen",
                "DERECHOS DE IMAGEN",
                _parrafo(
                    "La aceptación de este reglamento implica que el participante autoriza a la Asociación Sierra de Peñasagra el uso de su imagen (fotos, videos, nombre) para la promoción y difusión de la prueba en cualquier medio de comunicación sin compensación económica."
                ),
            ),
            type="single",
            collapsible=True,
            default_value="medio-ambiente",
            width="100%",
        ),
        spacing="5",
        align="center",
        width="100%",
        max_width="900px",
        margin="0 auto",
    )


def reglamento() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        _hero_reglamento(),
        rx.box(
            rx.vstack(
                _modalidades(),
                _informacion(),
                _reglamento_completo(),
                spacing="8",
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
