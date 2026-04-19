import reflex as rx
from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina



def recorridos() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        rx.vstack(
           
            # Resto del contenido de la página
            rx.text("Recorridos", size="6", font_weight="bold", align="center", color="black"),
            rx.text("En Construcción", size="6", font_weight="bold", align="center", color="black"),
            rx.text("¡Próximamente podrás explorar nuestros emocionantes recorridos! Estamos trabajando arduamente para ofrecerte experiencias inolvidables. Mantente atento a nuestras actualizaciones para descubrir las aventuras que tenemos preparadas para ti.", size="5", align="center", color="black"),
            
            
            spacing="5",
            width="100%",
            
        ),
        pie_pagina(),
        background_color="#EBEBEB",

    )