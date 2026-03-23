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
                "/fondos/fondo.webp",
                #Contenido de la cabecera 
                rx.center(
                    rx.vstack(
                        rx.text("TRAIL PEÑASAGRA", color="orange", font_size=rx.breakpoints(initial="3em", sm="6em", lg="7em"), font_weight="bold",align="center"),
                        rx.text("Corremos por Adriana", color="#FF90FB", font_size=rx.breakpoints(initial="2em", sm="3em", lg="4em"), align="center"),
                        rx.spacer(),
                        rx.box(
                            rx.text("Ya solo faltan", font_size=rx.breakpoints(initial="1.5em", sm="2em", lg="2.5em"), color="orange", align="center"),
                            rx.hstack(
                                time_unit(DateCountdownState.formatted_days, "Días"),
                                time_unit(DateCountdownState.formatted_hours, "Horas"),
                                time_unit(DateCountdownState.formatted_minutes, "Minutos"),
                                time_unit(DateCountdownState.formatted_seconds, "Segundos"),
                                justify="center",
                                spacing="3",
                            ),
                            background_color="#3333339D",
                            border_radius="1em",
                            padding="1.5em",
                        ),
                        rx.spacer(),
                        align="center",
                    ),
                    width="100%",
                    height="100%",
                ),
            ),
            # Resto del contenido de la página
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            rx.text("Corremos por Adriana!", size="6", font_weight="bold", align="center"),
            
            
            
            spacing="5",
            width="100%",
            
        ),
        on_mount=DateCountdownState.start_clock,
        background_color="#333333",

    )