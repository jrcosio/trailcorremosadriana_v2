import reflex as rx


def barra_de_navegacion() -> rx.Component:
    return rx.box(
        #Componente de barra de navegación
        rx.hstack(
            rx.image(src="/logos/logo.png", alt="Logo", height="60px"),  # Logo de la página
            rx.spacer(),  # Espacio entre el logo y los enlaces de navegación
            #Boton para incripciones
            rx.link(
                rx.button("Inscríbete", color_scheme="orange", font_size="2em"),
                href="https://www.gedsports.com/race/trail-sierra-de-penasagra",
                is_external=True,
            ),

            rx.spacer(),
            rx.tablet_and_desktop(
                rx.hstack(
                    rx.link("Inicio", href="/", font_size="1.2em", color="black", _hover={"text_decoration": "underline"}),
                    rx.link("Carreras", href="/recorridos", font_size="1.2em", color="black", _hover={"text_decoration": "underline"}),
                    rx.link("Galería", href="/galeria", font_size="1.2em", color="black", _hover={"text_decoration": "underline"}),
                    rx.link("Contacto", href="/contacto", font_size="1.2em", color="black", _hover={"text_decoration": "underline"}),
                    spacing="4",
                ),
            ),
            rx.mobile_only(
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", color="black")),
                    rx.menu.content(
                        rx.menu.item(
                            rx.icon("home", color="black"),
                            rx.box(width="5px"),
                            rx.link("Inicio", href="/", font_size="1.2em"),
                        ),
                        rx.menu.item(
                            rx.icon("map", color="black"),
                            rx.box(width="5px"),
                            rx.link("Carreras", href="/recorridos", font_size="1.2em"),
                        ),
                        rx.menu.item(
                            rx.icon("camera", color="black"),
                            rx.box(width="5px"),
                            rx.link("Galería", href="/galeria", font_size="1.2em"),
                        ),
                        rx.menu.item(
                            rx.icon("contact", color="black"),
                            rx.box(width="5px"),
                            rx.link("Contacto", href="/contacto", font_size="1.2em"),
                        ),
                        background_color="#EBEBEB",
                    ),
                ),
            ),
            rx.box(width="5px"),  # Espacio para alinear el menú a la derecha
            width="100%",
            align="center",
        ),
        padding="4",
        display="flex",
        justify="center",
        align_items="center",
        background_color="#EBEBEB",   #Color de fondo de la barra de navegación
        border_bottom="3px solid orange",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
        # height="7vh",
    )