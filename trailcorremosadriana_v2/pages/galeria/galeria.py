#Pablo aquí va el código de la página galería, que se muestra al hacer click en el enlace "Galería" de la barra de navegación.
import reflex as rx

def galeria():
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.box(
                    rx.text("Galería 2024", font_size="2em", font_weight="bold", color_scheme="#FFFFFF"),
                    color_scheme="#FF0000",
                )
            ),
            rx.button("Ver")
        ),
        rx.hstack(
            rx.box(
                rx.box(
                    rx.text("Galería 2025", font_size="2em", font_weight="bold", color_scheme="#FFFFFF"),
                    color_scheme="#FF0000",
                )
            ),
            rx.button("Ver")
        ),
        rx.hstack(
            rx.box(
                rx.box(
                    rx.text("Galería 2026", font_size="2em", font_weight="bold", color_scheme="#FFFFFF"),
                    color_scheme="#FF0000",
                )
            ),
            rx.button("Próximamente")
        ),
    )

app = rx.App()
app.add_page(galeria, route="/galeria")