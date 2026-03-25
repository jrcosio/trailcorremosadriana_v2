import reflex as rx


def card(imagen: str) -> rx.Component:
    return rx.card(
        rx.image(src=imagen, width="100%", border_radius="5px"),
        padding="4",
        border_radius="35px",
        box_shadow="35px"
    )
    
listado_patrocinadores = [
    "/logos/patrocinadores/banner_carandia.png",
    "/logos/patrocinadores/banner_jvcosio.png",
    "/logos/patrocinadores/banner_andros.png",
    "/logos/patrocinadores/banner_aljomar.png",
    "/logos/patrocinadores/banner_artipublic.png",
    "/logos/patrocinadores/banner_grupochovi.png",
    "/logos/patrocinadores/banner_natuber.png",
    "/logos/patrocinadores/banner_rionansa.png",

]

    

def patrocinadores() -> rx.Component:
    return rx.center( 
        rx.vstack(
            rx.text("Patrocinadores", font_size="2em", color="orange", font_weight="bold",text_align="center"),
            rx.divider(border_color="#30a46c", width="100px", margin="0 auto", border_width="2px"),
            rx.text(
                "¡Conoce a nuestros patrocinadores! Gracias a ellos, el Trail Peñasagra se hace posible. Descubre quiénes apoyan esta increíble experiencia.",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            rx.grid(
                rx.foreach(
                    listado_patrocinadores,
                    lambda imagen: card(imagen),
                ),
                columns=rx.breakpoints(initial="2", md="3", lg="6"),
                spacing="3",
                width="100%",
                place_items="center",
            ),
            align="center",
            padding="2em",
            width="100%",
        ),
        width="100%",
    )