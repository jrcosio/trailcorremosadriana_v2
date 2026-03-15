import reflex as rx


def barra_de_navegacion() -> rx.Component:
    return rx.box(
        #Componente de barra de navegación
        
        padding="4",
        
        display="flex",
        justify="center",
        align_items="center",
        background_color="green",   #Color de fondo de la barra de navegación
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
        height="7vh",
    )