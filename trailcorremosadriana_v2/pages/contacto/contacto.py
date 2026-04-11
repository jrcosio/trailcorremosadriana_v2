import reflex as rx

from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina



def contacto() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        rx.vstack(
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
            
            
            spacing="2",
            width="100%",
            align="center",
        ),
        pie_pagina(),
        background_color="#333333",

    )