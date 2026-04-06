import reflex as rx

def card(imagen: str, titulo: str, descripcion: str) -> rx.Component:
    return rx.card(
        rx.image(src=imagen, width="100%", border_radius="5px"),
        rx.heading(titulo, size="5", color="orange", width="100%", text_align="center", margin_top="3"),
        rx.box(height="4px"),
        rx.text(descripcion, margin_top="1"),
       
        padding="4",
        #background_color="white",
        border_radius="md",
        box_shadow="md"
    )


def noticias() -> rx.Component:
    return rx.center( 
        rx.vstack(
            rx.text("Noticias", font_size="2em", color="orange", font_weight="bold",text_align="center"),
            rx.divider(border_color="#30a46c", width="100px", margin="0 auto", border_width="2px"),
            rx.text(
                "¡Mantente al día con las últimas noticias del Trail Peñasagra! Aquí encontrarás todas las actualizaciones, anuncios y novedades sobre la carrera más emocionante del año.",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            
            align="center",
            padding="2em",
        ),
        width="100%",
    )