import reflex as rx
from rxconfig import config
from trailcorremosadriana_v2.pages.clasificacion.clasificacion import clasificacion
from trailcorremosadriana_v2.pages.clasificacion.clasificacion_state import (
    ClasificacionesIndexState,
    ClasificacionState,
)
from trailcorremosadriana_v2.pages.clasificacion.clasificaciones import clasificaciones
from trailcorremosadriana_v2.pages.contacto.contacto import contacto
from trailcorremosadriana_v2.pages.galeria.galeria import galeria
from trailcorremosadriana_v2.pages.principal.principal import index
from trailcorremosadriana_v2.pages.recorridos.recorridos import recorridos
from trailcorremosadriana_v2.pages.reglamento.reglamento import reglamento




app = rx.App(
    theme=rx.theme(appearance="light"),
)
app.add_page(index, route="/")
app.add_page(contacto, route="/contacto") #<-- está aquí
app.add_page(recorridos, route="/recorridos")
app.add_page(galeria, route="/galeria")
app.add_page(reglamento, route="/reglamento") #<-- está aquí
app.add_page(
    clasificaciones,
    route="/clasificaciones",
    on_load=ClasificacionesIndexState.cargar_anios,
)
app.add_page(
    clasificacion,
    route="/clasificaciones/[anio]",
    on_load=ClasificacionState.cargar_datos,
)


# la de galeria, noticias, etc se añadirá más adelante