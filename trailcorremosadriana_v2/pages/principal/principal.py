import reflex as rx
from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.cabecera import cabecera as cabecera_index



def index() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        rx.vstack(
            #Componente principal de la página
            cabecera_index( 
                "/cabecera_index.jpg",
                #Contenido de la cabecera 
                rx.vstack(
                    rx.heading("Trail Peñasagra", size="8", color="red"),
                    rx.text("Corremos por Adriana", color="red", font_size="1.5em"),
                    align="center",
                    # justify="center",
                    height="100%",
                    width="100%",
                )
            ),

            # Resto del contenido de la página
            
            
            
            
            spacing="5",
            width="100%",
            
        ),

    )