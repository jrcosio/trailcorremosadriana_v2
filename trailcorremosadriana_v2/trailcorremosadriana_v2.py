import reflex as rx
from rxconfig import config
from trailcorremosadriana_v2.pages.contacto.contacto import contacto
from trailcorremosadriana_v2.pages.galeria.galeria import galeria
from trailcorremosadriana_v2.pages.principal.principal import index
from trailcorremosadriana_v2.pages.recorridos.recorridos import recorridos




app = rx.App(
    theme=rx.theme(appearance="light"),
)
app.add_page(index, route="/")
app.add_page(contacto, route="/contacto") #<-- está aquí
app.add_page(recorridos, route="/recorridos")
app.add_page(galeria, route="/galeria")


# la de galeria, noticias, etc se añadirá más adelante