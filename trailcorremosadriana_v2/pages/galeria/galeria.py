#Pablo aquí va el código de la página galería, que se muestra al hacer click en el enlace "Galería" de la barra de navegación.
import reflex as rx

def tarjeta_galeria(titulo, imagen_url,texto_boton):
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
            background_image=f"url('{imagen_url}')",
            background_size="cover",
            background_position="center",
            height="250px",
            width="400px",
            position="relative",
            border_radius="0px",
            overflow="hidden",
        ),
        rx.box(width="500px"),
        rx.button(texto_boton, color_scheme="red", border_radius = "0px", width="200px"),
        align="center",
        spacing="4",
    )

def ver_galeria():
    return rx.vstack(
        tarjeta_galeria("Galería 2024", "/correr_prueba.jpg", "V E R"),
        tarjeta_galeria("Galería 2025", "/correr_prueba.jpg", "V E R"),
        tarjeta_galeria("Galería 2026", "/correr_prueba.jpg", "P R Ó X I M A M E N T E"),
        spacing="6",
        padding="20px",
    )

app = rx.App()
app.add_page(ver_galeria, route="/galeria")