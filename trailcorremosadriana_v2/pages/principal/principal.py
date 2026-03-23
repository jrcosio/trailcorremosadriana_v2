import reflex as rx
from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.cabecera import cabecera
from trailcorremosadriana_v2.components.contador_regresivo import _countdown_script, _time_unit
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina
from trailcorremosadriana_v2.pages.principal.secciones.colaboradores import colaboradores
from trailcorremosadriana_v2.pages.principal.secciones.inscripciones import inscripciones
from trailcorremosadriana_v2.pages.principal.secciones.noticias import noticias
from trailcorremosadriana_v2.pages.principal.secciones.patrocinadores import patrocinadores
from trailcorremosadriana_v2.pages.principal.secciones.voluntarios import voluntarios



def index() -> rx.Component:
    return rx.box(
        _countdown_script(),
        barra_de_navegacion(),
        rx.vstack(
            cabecera(
                "/fondos/fondo.webp",
                rx.center(
                    rx.vstack(
                        rx.image(src="/logos/logo_aso.png",height="150px"),
                        rx.text("TRAIL PEÑASAGRA",
                            color="orange",
                            font_size=rx.breakpoints(initial="3.5em", sm="5em", lg="8em"),
                            font_weight="bold",
                            align="center",
                        ),
                        rx.text("Corremos por Adriana",
                            color="#FF90FB",
                            font_size=rx.breakpoints(initial="2em", sm="3em", lg="4em"),
                            font_weight="bold",
                            align="center",
                        ),
                        # rx.spacer(),
                        rx.box(
                            rx.text(
                                "Ya solo faltan",
                                font_size=rx.breakpoints(initial="1.5em", sm="2em", lg="2.5em"),
                                color="orange",
                                align="center",
                            ),
                            # _countdown_script(),
                            rx.hstack(
                                _time_unit("cd-days", "Días"),
                                _time_unit("cd-hours", "Horas"),
                                _time_unit("cd-minutes", "Min"),
                                _time_unit("cd-seconds", "Seg"),
                                justify="center",
                                align="end",
                                spacing="3",
                            ),
                            background_color="#3333339D",
                            border_radius="1em",
                            padding="1.5em",
                        ),
                        rx.text(
                            "Sábado, 11 de Julio de 2026",
                            color="orange",
                            font_size=rx.breakpoints(initial="1.5em", sm="2em", lg="2.5em"),
                            font_weight="bold",
                            align="center",
                        ),
                        rx.spacer(),
                        align="center",
                    ),
                    width="100%",
                    height="100%",
                ),
            ),
            # Resto del contenido de la página
            inscripciones(),
            noticias(),
            patrocinadores(),
            # voluntarios(),
            colaboradores(),

            pie_pagina(),
            spacing="0",
            width="100%",
            
        ),
        background_color="#333333",


    )