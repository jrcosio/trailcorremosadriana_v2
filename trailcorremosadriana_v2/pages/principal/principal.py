import reflex as rx
from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.cabecera import cabecera
from trailcorremosadriana_v2.components.contador_regresivo import contador_hero
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina
from trailcorremosadriana_v2.components.revelar import efecto_revelar
from trailcorremosadriana_v2.pages.principal.secciones.camiseta import camiseta
from trailcorremosadriana_v2.pages.principal.secciones.colaboradores import colaboradores
from trailcorremosadriana_v2.pages.principal.secciones.inscripciones import inscripciones
from trailcorremosadriana_v2.pages.principal.secciones.noticias import noticias
from trailcorremosadriana_v2.pages.principal.secciones.patrocinadores import patrocinadores
from trailcorremosadriana_v2.pages.principal.secciones.voluntarios import voluntarios



def index() -> rx.Component:
    return rx.box(
        efecto_revelar(),
        barra_de_navegacion(),
        rx.vstack(
            cabecera(
                "/fondos/fondo.webp",
                rx.center(
                    rx.vstack(

                        rx.box(height="60px"),
                        rx.tablet_and_desktop(
                            rx.image(src="/logos/nombre_desktop.webp", height=rx.breakpoints(initial="70px", sm="100px", lg="150px")),
                        ),
                        rx.mobile_only(
                            rx.image(src="/logos/nombre_mobile.webp", height="150px"),

                        ),
                        rx.image(src="/logos/corremos_por_adriana.webp", height=rx.breakpoints(initial="60px", sm="90px", lg="120px")),
                       
                        contador_hero(),
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
            #camiseta(),
            patrocinadores(),
            # voluntarios(),
            # colaboradores(),

            pie_pagina(),
            spacing="0",
            width="100%",
            
        ),
        background_color="#333333",


    )