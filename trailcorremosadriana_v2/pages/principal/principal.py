import reflex as rx
from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.cabecera import cabecera
from trailcorremosadriana_v2.components.contador_regresivo import DateCountdownState, time_unit




def index() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        rx.vstack(
            #Componente principal de la página
            cabecera( 
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
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            rx.text("cosas", padding="2em", size="6", text_align="center"),
            
            
            
            
            
            spacing="5",
            width="100%",
            
        ),
        on_mount=DateCountdownState.start_clock,

    )