"""Trail Peñasagra - Corremos por Adriana V2 """

import reflex as rx
from rxconfig import config
from trailcorremosadriana_v2.pages.principal.principal import index



app = rx.App()
app.add_page(index, route="/")
# la de galeria, noticias, etc se añadirá más adelante