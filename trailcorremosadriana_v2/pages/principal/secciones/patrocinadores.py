import reflex as rx


def card(imagen: str, nombre: str, url: str = "") -> rx.Component:
    tarjeta = rx.card(
        rx.image(src=imagen, alt=nombre, loading="lazy", width="100%", border_radius="5px"),
        class_name="reveal",
        padding="4",
        border_radius="18px",
        box_shadow="0 10px 25px rgba(0,0,0,0.22)",
        transition="all 0.3s ease",
        _hover={"transform": "translateY(-4px)", "box_shadow": "0 14px 32px rgba(0,0,0,0.3)"},
    )
    if url:
        return rx.link(tarjeta, href=url, is_external=True)
    return tarjeta


# url vacía = sin enlace; rellenar cuando el patrocinador facilite su web.
listado_patrocinadores = [
    {"imagen": "/logos/patrocinadores/banner_carandia.png", "nombre": "Carandía", "url": ""},
    {"imagen": "/logos/patrocinadores/banner_jvcosio.png", "nombre": "JV Cosío", "url": ""},
    {"imagen": "/logos/patrocinadores/banner_andros.png", "nombre": "Andros", "url": ""},
    {"imagen": "/logos/patrocinadores/banner_aljomar.png", "nombre": "Aljomar", "url": ""},
    {"imagen": "/logos/patrocinadores/banner_artipublic.png", "nombre": "Artipublic", "url": ""},
    {"imagen": "/logos/patrocinadores/banner_grupochovi.png", "nombre": "Grupo Choví", "url": ""},
    {"imagen": "/logos/patrocinadores/banner_natuber.png", "nombre": "Natuber", "url": ""},
    {"imagen": "/logos/patrocinadores/banner_rionansa.png", "nombre": "Ayuntamiento de Rionansa", "url": ""},
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
                *[card(p["imagen"], p["nombre"], p["url"]) for p in listado_patrocinadores],
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
