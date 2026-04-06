import reflex as rx

def card(imagen: str, titulo: str, descripcion: str) -> rx.Component:
    return rx.card(
        rx.image(src=imagen, border_radius="5px"),
        rx.heading(titulo, size="5", color="orange", width="100%", text_align="center", margin_top="3"),
        padding="4",
        background_color="black",
        border_radius="md",
        box_shadow="md",
        max_width="400px",
    )


def camiseta() -> rx.Component:
    return rx.center( 
        rx.vstack(
            rx.text("CAMISETA OFICIAL TRAIL PEÑASAGRA 2026", font_size="2em", color="orange", font_weight="bold",text_align="center"),
            rx.divider(border_color="#30a46c", width="100px", margin="0 auto", border_width="2px"),
            rx.text(
                "¡Descubre la camiseta oficial del Trail Peñasagra! Con un diseño exclusivo y materiales de alta calidad, es el recuerdo perfecto de tu participación en la carrera.",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            card(
                imagen="/varios/camiseta.webp",
                titulo="Camiseta Oficial Trail Peñasagra 2026",
                descripcion="Disponible en todas las tallas. ¡Consigue la tuya antes de que se agoten!"
            ),
            rx.text(
                "¡Disponible en todas las tallas! Asegúrate de conseguir la tuya antes de que se agoten (Fecha límite: 25 de junio).",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            rx.text(
                "Después del 25 de junio, las INSCRIPCIONES SON SIN CAMISETA, por lo que si quieres asegurarte de tenerla, ¡no esperes más para inscribirte!",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            
            align="center",
            padding="2em",
        ),
        width="100%",
    )