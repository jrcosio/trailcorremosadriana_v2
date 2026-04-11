import reflex as rx
from .contacto_state import ContactoState
from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina


def _info_contacto() -> rx.Component:
    """Columna izquierda: datos de contacto."""
    return rx.vstack(
        rx.text(
            "INFORMACIÓN DE CONTACTO",
            font_size="2em",
            color="orange",
            font_weight="bold",
        ),
        rx.divider(
            border_color="#30a46c",
            width="100px",
            border_width="2px",
        ),
        rx.text(
            "¿Tienes alguna pregunta sobre la carrera? No dudes en contactarnos.",
            color="#CBD5E1",
            font_size="1.1em",
            line_height="1.8",
        ),
        # Email
        rx.hstack(
            rx.icon("mail", color="orange", size=22),
            rx.link(
                "asociacionpenasagra@gmail.com",
                href="mailto:asociacionpenasagra@gmail.com",
                color="white",
                font_size="1.1em",
                _hover={"color": "orange"},
            ),
            spacing="3",
            align="center",
        ),
        # Teléfono
        rx.hstack(
            rx.icon("phone", color="orange", size=22),
            rx.link(
                "619 364 819 (Imanol)",
                href="tel:+34619364819",
                color="white",
                font_size="1.1em",
                _hover={"color": "orange"},
            ),
            spacing="3",
            align="center",
        ),
        # Ubicación
        rx.hstack(
            rx.icon("map-pin", color="orange", size=22),
            rx.text(
                "Cosío, Cantabria",
                color="white",
                font_size="1.1em",
            ),
            spacing="3",
            align="center",
        ),
        # Redes sociales
        rx.vstack(
            rx.text(
                "SÍGUENOS",
                color="orange",
                font_weight="bold",
                font_size="1em",
                letter_spacing="2px",
            ),
            rx.hstack(
                rx.link(
                    rx.icon("instagram", color="white", size=28),
                    href="https://www.instagram.com/asociacion_penasagra/",
                    is_external=True,
                    _hover={"opacity": "0.7"},
                ),
                spacing="4",
            ),
            spacing="2",
            margin_top="1em",
        ),
        spacing="5",
        width="100%",
        padding=rx.breakpoints(initial="2em", lg="3em"),
    )
def _formulario_contacto() -> rx.Component:
    """Columna derecha: formulario de contacto."""
    input_style = {
        "width": "100%",
        "height": "40px",
        "background_color": "rgba(255,255,255,0.05)",
        "border": "1px solid rgba(255,255,255,0.15)",
        "color": "white",
        "border_radius": "8px",
        "font_size": "1em",
        "_placeholder": {"color": "#94A3B8"},
        "_focus": {"border_color": "orange", "box_shadow": "0 0 0 1px orange"},
    }

    return rx.vstack(
        rx.text(
            "ENVÍANOS UN MENSAJE",
            font_size="2em",
            color="orange",
            font_weight="bold",
        ),
        rx.divider(
            border_color="#30a46c",
            width="100px",
            border_width="2px",
        ),
        rx.vstack(
            rx.input(placeholder="Tu nombre", 
                    value=ContactoState.name, 
                    on_change=ContactoState.set_name,
                    **input_style
            ),
            rx.input(placeholder="Tu email", 
                     type="email", 
                    value=ContactoState.email, 
                    on_change=ContactoState.set_email, 
                     **input_style
            ),
            rx.input(placeholder="Asunto", 
                    value=ContactoState.subject, 
                    on_change=ContactoState.set_subject, 
                     **input_style
            ),
            rx.text_area(
                placeholder="Escribe tu mensaje aquí...",
                value=ContactoState.description,
                on_change=ContactoState.set_description,
                rows="6",
                width="100%",
                background_color="rgba(255,255,255,0.05)",
                border="1px solid rgba(255,255,255,0.15)",
                color="white",
                border_radius="8px",
                font_size="1em",
                resize="vertical",
                _placeholder={"color": "#94A3B8"},
                _focus={"border_color": "orange", "box_shadow": "0 0 0 1px orange"},
            ),
            rx.button(
                "Enviar mensaje",
                on_click=ContactoState.send_email,
                disabled=ContactoState.is_sending,
                loading=ContactoState.is_sending,
                color_scheme="orange",
                width="100%",
                size="3",
                cursor="pointer",
                _hover={"opacity": "0.9"},
            ),
            spacing="4",
            width="100%",
        ),
        spacing="5",
        width="100%",
        padding=rx.breakpoints(initial="2em", lg="3em"),
    )

def contacto() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        rx.vstack(
            # Título y subtítulo
            rx.text(
                "CONTACTA CON NOSOTROS",
                color="white",
                font_size=rx.breakpoints(initial="28px", sm="36px", lg="42px"),
                font_weight="800",
                text_align="center",
            ),
            rx.text(
                "Cuéntanos tu pregunta o sugerencia. Responderemos pronto.",
                color="#CBD5E1",
                font_size="18px",
                text_align="center",
            ),
            # Contenedor de dos columnas
            rx.flex(
                rx.box(
                    _info_contacto(),
                    width=rx.breakpoints(initial="100%", lg="40%"),
                    background_color="rgba(255,255,255,0.03)",
                    border_radius="16px",
                    border="1px solid rgba(255,255,255,0.08)",
                ),
                rx.box(
                    _formulario_contacto(),
                    width=rx.breakpoints(initial="100%", lg="58%"),
                    background_color="rgba(255,255,255,0.03)",
                    border_radius="16px",
                    border="1px solid rgba(255,255,255,0.08)",
                ),
                direction=rx.breakpoints(initial="column", lg="row"),
                spacing="5",
                width="100%",
                max_width="1200px",
                margin="0 auto",
                padding=rx.breakpoints(initial="1em", sm="2em"),
            ),
            spacing="5",
            width="100%",
            align="center",
            padding_top="2em",
            padding_bottom="2em",
        ),
        pie_pagina(),
        background_color="#333333",

    )