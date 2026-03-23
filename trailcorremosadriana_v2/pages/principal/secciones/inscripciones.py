import reflex as rx



def card(imagen: str, titulo: str, descripcion: str) -> rx.Component:
    return rx.card(
        rx.image(src=imagen, width="100%", border_radius="5px"),
        rx.heading(titulo, size="5", color="orange", width="100%", text_align="center", margin_top="3"),
        rx.box(height="4px"),
        rx.button("Inscribirme", color_scheme="green", margin_top="3", width="100%", size="3"),
        rx.box(height="4px"),
        rx.text(descripcion, margin_top="1"),
       
        padding="4",
        #background_color="white",
        border_radius="md",
        box_shadow="md"
    )

def inscripciones() -> rx.Component:
    return rx.center( 
        rx.vstack(
            rx.text("Inscripciones", font_size="2em", color="orange", font_weight="bold",text_align="center"),
            rx.divider(border_color="#30a46c", width="100px", margin="0 auto", border_width="2px"),
            rx.text(
                "¡Las inscripciones para el Trail Peñasagra ya están abiertas! No pierdas la oportunidad de ser parte de esta increíble experiencia. Inscríbete ahora y asegura tu lugar en la carrera más emocionante del año.",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            rx.grid(
                card(imagen="/img/trail_inscripciones.png", titulo="Trail Peñasagra - 28 Km", descripcion="28 Km por los senderos más exigentes de la Sierra. Un reto para los que buscan superarse entre montañas."),
                card(imagen="/img/trail_inscripciones.png", titulo="Speed Trail Peñasagra - 15 Km", descripcion="15 Km de ritmo intenso y paisajes inolvidables. La distancia perfecta para disfrutar y competir."),
                card(imagen="/img/trail_inscripciones.png", titulo="Familiar Peñasagra - 8 Km", descripcion="8 Km para compartir en familia. Una jornada pensada para que pequeños y mayores disfruten juntos de la naturaleza."),
                
                columns=rx.breakpoints(initial="1", sm="3", lg="3"),
                spacing="5",
                width=rx.breakpoints(initial="100%", sm="90%", lg="70%"),
                padding="20px",
            ),
            align="center",
            padding="2em",
        ),
        width="100%",
    )