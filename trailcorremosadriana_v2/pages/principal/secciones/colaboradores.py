import reflex as rx




def colaboradores() -> rx.Component:
    return rx.center( 
        rx.vstack(
            rx.text("Colaboradores", font_size="2em", color="orange", font_weight="bold",text_align="center"),
            rx.divider(border_color="#30a46c", width="100px", margin="0 auto", border_width="2px"),
            rx.text(
                "Este evento no sería posible sin el compromiso de quienes creen en el deporte y la solidaridad. Nuestros colaboradores son parte esencial de cada kilómetro.",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            align="center",
            padding="2em",
        ),
        width="100%",
    )