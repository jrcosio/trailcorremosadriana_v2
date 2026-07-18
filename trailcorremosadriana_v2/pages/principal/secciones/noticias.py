import reflex as rx

from trailcorremosadriana_v2.pages.principal.secciones.noticias_state import NoticiasState


def _imagen_noticia(noticia: rx.Var, aspect_ratio: str) -> rx.Component:
    return rx.box(
        rx.cond(
            noticia["imagen_src"] != "",
            rx.image(
                src=noticia["imagen_src"],
                alt=noticia["titulo"],
                loading="lazy",
                width="100%",
                height="100%",
                object_fit="cover",
                transition="transform 0.35s ease",
            ),
            rx.center(
                rx.icon("newspaper", color="rgba(255,255,255,0.25)", size=42),
                width="100%",
                height="100%",
            ),
        ),
        width="100%",
        aspect_ratio=aspect_ratio,
        background_color="rgba(0,0,0,0.22)",
        overflow="hidden",
        _group_hover={"img": {"transform": "scale(1.04)"}},
    )


def _dialogo_noticia(noticia: rx.Var) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Leer más",
                variant="ghost",
                color="orange",
                font_weight="900",
                padding="0",
                margin_top="auto",
                _hover={"background": "transparent", "filter": "brightness(1.2)"},
            ),
        ),
        rx.dialog.content(
            _imagen_noticia(noticia, "16 / 8"),
            rx.vstack(
                rx.text(
                    noticia["fecha_legible"],
                    color="#30a46c",
                    font_size="0.72em",
                    font_weight="900",
                    letter_spacing="0.16em",
                    text_transform="uppercase",
                ),
                rx.dialog.title(noticia["titulo"], color="orange", font_weight="900"),
                rx.cond(
                    noticia["subtitulo"] != "",
                    rx.text(noticia["subtitulo"], color="#94A3B8", font_weight="700"),
                ),
                rx.text(
                    noticia["texto"],
                    color="#CBD5E1",
                    line_height="1.7",
                    white_space="pre-line",
                ),
                rx.dialog.close(
                    rx.button(
                        "Cerrar",
                        border_radius="999px",
                        font_weight="900",
                        color="white",
                        background_color="#30a46c",
                        margin_top="0.5em",
                    ),
                ),
                spacing="3",
                align="start",
                padding="1.4em",
            ),
            background="#2b2b2b",
            border="1px solid rgba(255,255,255,0.08)",
            max_width="640px",
            max_height="85vh",
            overflow_y="auto",
            padding="0",
        ),
    )


def noticia_card(noticia: rx.Var) -> rx.Component:
    return rx.box(
        _imagen_noticia(noticia, "16 / 10"),
        rx.vstack(
            rx.text(
                noticia["fecha_legible"],
                color="#30a46c",
                font_size="0.72em",
                font_weight="900",
                letter_spacing="0.16em",
                text_transform="uppercase",
            ),
            rx.heading(
                noticia["titulo"],
                color="orange",
                font_size="1.25em",
                font_weight="900",
                line_height="1.2",
            ),
            rx.cond(
                noticia["subtitulo"] != "",
                rx.text(
                    noticia["subtitulo"],
                    color="#94A3B8",
                    font_size="0.9em",
                    font_weight="700",
                ),
            ),
            rx.text(
                noticia["texto"],
                color="#CBD5E1",
                font_size="0.95em",
                line_height="1.65",
                style={
                    "display": "-webkit-box",
                    "-webkit-line-clamp": "3",
                    "-webkit-box-orient": "vertical",
                    "overflow": "hidden",
                },
            ),
            _dialogo_noticia(noticia),
            spacing="3",
            align="start",
            width="100%",
            height="100%",
            padding="1.4em",
        ),
        role="group",
        class_name="reveal",
        height="100%",
        display="flex",
        flex_direction="column",
        background_color="rgba(255,255,255,0.04)",
        border="1px solid rgba(255,255,255,0.08)",
        border_radius="18px",
        overflow="hidden",
        box_shadow="0 16px 40px rgba(0,0,0,0.22)",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-6px)",
            "border_color": "orange",
            "box_shadow": "0 18px 45px rgba(255,165,0,0.2)",
        },
    )


def noticias() -> rx.Component:
    return rx.cond(
        NoticiasState.hay_noticias,
        rx.center(
            rx.vstack(
                rx.vstack(
                    rx.text(
                        "Noticias",
                        font_size=rx.breakpoints(initial="2em", sm="2.5em"),
                        color="orange",
                        font_weight="900",
                        text_align="center",
                        letter_spacing="0.04em",
                    ),
                    rx.divider(border_color="#30a46c", width="100px", margin="0 auto", border_width="2px"),
                    rx.text(
                        "¡Mantente al día con las últimas noticias del Trail Peñasagra!",
                        font_size=rx.breakpoints(initial="1em", sm="1.15em"),
                        color="#CBD5E1",
                        text_align="center",
                        line_height="1.7",
                        max_width="780px",
                    ),
                    spacing="4",
                    align="center",
                    width="100%",
                ),
                rx.grid(
                    rx.foreach(NoticiasState.noticias, noticia_card),
                    columns=rx.breakpoints(initial="1", sm="2", lg="4"),
                    spacing="5",
                    width="100%",
                    align_items="stretch",
                ),
                align="center",
                spacing="7",
                width="100%",
                max_width="1200px",
                padding=rx.breakpoints(initial="3em 1em", sm="4em 2em"),
            ),
            width="100%",
        ),
        rx.fragment(),
    )
