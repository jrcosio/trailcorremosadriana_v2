import reflex as rx
from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina
from trailcorremosadriana_v2.components.carreras import carreras


def recorridos() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        rx.vstack(
           
        carreras(),
            

        ),
        pie_pagina(),
        background_color="#EBEBEB",

    )