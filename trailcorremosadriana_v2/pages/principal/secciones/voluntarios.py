import reflex as rx




def voluntarios() -> rx.Component:
    return rx.center( 
        rx.vstack(
            rx.text("Voluntarios", font_size="2em", color="orange", font_weight="bold",text_align="center"),
            rx.divider(border_color="#30a46c", width="100px", margin="0 auto", border_width="2px"),
            rx.text(
                "¡Nuestros voluntarios! Gracias a ellos, el Trail Peñasagra - Corremos por ADRIANA es posible. Su entrega y generosidad hacen que cada corredor llegue a meta con una sonrisa.",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            rx.grid(
                rx.foreach(
                    list(range(50)),
                    lambda _: rx.avatar(src="/logos/logo_aso.png", size="8", border_radius="full"),
                ),
                columns=rx.breakpoints(initial="5", md="7", lg="10"),
                
            ),
            align="center",
            padding="2em",
        ),
        width="100%",
    )