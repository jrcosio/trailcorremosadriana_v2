import reflex as rx


def cabecera(imagen: str, *children) -> rx.Component:
    return rx.box(
        *children,
        background_image=f"url('{imagen}')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        width="100%",
        height="100dvh",
    )