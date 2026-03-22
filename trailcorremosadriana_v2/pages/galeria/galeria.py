#Pablo aquí va el código de la página galería, que se muestra al hacer click en el enlace "Galería" de la barra de navegación.
import reflex as rx

def tarjeta_galeria(titulo, texto_boton):
    return rx.hstack(
        rx.box(
            rx.box(
                rx.text(titulo, font_size="1.5em", font_weight="bold", color="white"),
                bg="#FF0000",
                padding="10px",
                position="absolute",
                bottom="15px",
                left="15px",
                right="15px",
                border_radius="5px",
            ),
            background_image=f"url('/correr_prueba.jpg')",
            background_size="cover",
            background_position="center",
            height="250px",
            width="400px",
            position="relative",
            border_radius="10px",
            overflow="hidden",
        ),
        rx.button(texto_boton, color_scheme="red", border_radius = "0px"),
        align="center",
        spacing="4",
    )

def ver_galeria():
    return rx.center(
        rx.vstack(
            tarjeta_galeria("Galería 2024", "Ver"),
            tarjeta_galeria("Galería 2025", "Ver"),
            tarjeta_galeria("Galería 2026", "Próximamente"),
            spacing="6",
            padding="20px",
        )
    )

app = rx.App()
app.add_page(ver_galeria, route="/galeria")