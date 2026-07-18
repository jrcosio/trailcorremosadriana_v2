import reflex as rx
from datetime import datetime

_ANIO_ACTUAL = datetime.now().year


def pie_pagina():
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.heading("Trail Peñasagra", color="white", size="7"),
                    rx.text(
                        "Corremos por Adriana",
                        color="#94A3B8",
                        font_size="21px"
                    ),
                    rx.text(
                        "Organizado por la Asociación Peñasagra. Fomentando el deporte, el respeto por la naturaleza y la solidaridad en el Valle del Nansa.",
                        color="#94A3B8",
                        font_size="16px"
                    ),
                    align_items="start",
                    max_width="300px",
                ),
                rx.vstack(
                    rx.text("ENLACES", color="white", font_weight="bold"),
                    rx.link("Instagram", href="https://www.instagram.com/asociacion_penasagra/", is_external=True, color="#94A3B8"),
                    rx.link("Clasificaciones", href="/clasificaciones", color="#94A3B8"),
                    rx.link("Galería", href="/galeria", color="#94A3B8"),
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("LEGAL", color="white", font_weight="bold"),
                    rx.link("Reglamento", href="/reglamento", color="#94A3B8"),
                    align_items="start",
                ),
                direction=rx.breakpoints(initial="column", md="row"),
                justify="between",
                gap=rx.breakpoints(initial="2em", md="1em"),
                width="100%",
            ),
            rx.divider(border_color="#1E3A5F"),
            rx.flex(
                rx.text(f"Cosío © {_ANIO_ACTUAL} Asociación Peñasagra | Hackers Cosío | www.jrblanco.es", color="#64748B", font_size="14px"),
                rx.link("asociacionpenasagra@gmail.com", href="mailto:asociacionpenasagra@gmail.com", color="#94A3B8"),
                direction=rx.breakpoints(initial="column", md="row"),
                justify="between",
                gap="0.5em",
                width="100%",
            ),
            spacing="6",
            width="100%",
            max_width="1200px",
            margin="0 auto",
        ),
        bg="#434c53",
        padding="40px 20px",
        width="100%",
    )
