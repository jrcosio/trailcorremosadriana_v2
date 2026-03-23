import reflex as rx
from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion



def recorridos() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        rx.vstack(
           
            # Resto del contenido de la página
            rx.text("Recorridos", size="6", font_weight="bold", align="center", color="black"),
            rx.text("En Construcción", size="6", font_weight="bold", align="center", color="black"),
  
            
            spacing="5",
            width="100%",
            
        ),
        background_color="#EBEBEB",

    )