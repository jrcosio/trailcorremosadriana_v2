import reflex as rx

def card(imagen: str, titulo: str, descripcion: str) -> rx.Component:
    return rx.card(
        rx.image(src=imagen, width="100%", border_radius="5px"),
        rx.heading(titulo, size="5", color="orange", width="100%", text_align="center", margin_top="3"),
        rx.box(height="4px"),
        rx.center(
            rx.button("Ir al track", color_scheme="green", margin_top="3", width="50%", size="3")
        ),
        rx.box(height="4px"),
        rx.text(descripcion, margin_top="1"),
       
        padding="4",
        #background_color="white",
        border_radius="md",
        box_shadow="md"
    )

def carreras():
    return rx.center(
        rx.vstack(
            rx.grid(
                card(
                    imagen="/fondos/Trail.jpg", 
                    titulo="Trail - 27 Km", 
                    descripcion="27 Km por los senderos más exigentes de la sierra."
                ),
                card(
                    imagen="/fondos/Speed.jpg", 
                    titulo="Speed Trail - 17 Km", 
                    descripcion="Una carrera rápida y técnica para volar sobre el terreno."
                ),
                card(
                    imagen="/fondos/Familiar.jpg", 
                    titulo="Ruta Familiar - 8 Km", 
                    descripcion="Disfruta de la montaña en familia con un recorrido accesible."
                ),
                columns=rx.breakpoints(initial="1", sm="2", lg="3"), # Responsive: 1 col móvil, 3 en PC
                spacing="4",
            ),
            spacing="5",
            align="center",
            width="50%",
        ),
        padding_y="50px",
        background_image="url('/fondos/carreras.jpg')",
        background_size="contain",
        background_repeat="no-repeat",
        background_position="center",
        width="100%",
        min_height="100vh",
    )

