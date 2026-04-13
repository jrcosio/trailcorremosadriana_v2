import reflex as rx


def barra_de_navegacion() -> rx.Component:
    return rx.box(
        rx.box(
            #Componente de barra de navegación
            rx.hstack(
                rx.image(src="/logos/logo1.webp", alt="Logo", height="50px"),  # Logo de la página
                rx.spacer(),
                rx.tablet_and_desktop(
                    rx.hstack(
                        rx.link("Inicio", href="/", font_size="1.2em", color="white", _hover={"text_decoration": "underline"}),
                        rx.link("Carreras", href="/recorridos", font_size="1.2em", color="white", _hover={"text_decoration": "underline"}),
                        rx.link("Galería", href="/galeria", font_size="1.2em", color="white", _hover={"text_decoration": "underline"}),
                        rx.link("Contacto", href="/contacto", font_size="1.2em", color="white", _hover={"text_decoration": "underline"}),
                        spacing="4",
                    ),
                ),
                rx.mobile_only(
                    rx.menu.root(
                        rx.menu.trigger(rx.icon("menu", color="white", box_size="30px")),
                        rx.menu.content(
                            rx.menu.item(
                                rx.icon("home", color="black"),
                                rx.box(width="5px"),
                                rx.link("Inicio", href="/", font_size="1.2em", color="black"),
                            ),
                            rx.menu.item(
                                rx.icon("map", color="black"),
                                rx.box(width="5px"),
                                rx.link("Carreras", href="/recorridos", font_size="1.2em", color="black"),
                            ),
                            rx.menu.item(
                                rx.icon("camera", color="black"),
                                rx.box(width="5px"),
                                rx.link("Galería", href="/galeria", font_size="1.2em", color="black"),
                            ),
                            rx.menu.item(
                                rx.icon("contact", color="black"),
                                rx.box(width="5px"),
                                rx.link("Contacto", href="/contacto", font_size="1.2em", color="black"),
                            ),
                            background_color="#EBEBEB",
                        ),
                    ),
                ),
                rx.box(width="5px"),  # Espacio para alinear el menú a la derecha
                width="100%",
                align="center",
            ),
            # Botón para inscripciones centrado respecto a la ventana
            rx.link(
                rx.button("Inscríbete", color_scheme="orange", font_size="2em", border_radius="25px", border="1px solid white", size="3"),
                href="https://www.gedsports.com/race/trail-sierra-de-penasagra",
                is_external=True,
                position="absolute",
                left="50%",
                top="50%",
                transform="translate(-50%, -50%)",
            ),
            position="relative",
            width="100%",
            padding="4",
        ),
        display="flex",
        justify="center",
        align_items="center",
        background_color="#434c53",   #Color de fondo de la barra de navegación
        border_bottom="3px solid orange",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
        height="70px",
    )