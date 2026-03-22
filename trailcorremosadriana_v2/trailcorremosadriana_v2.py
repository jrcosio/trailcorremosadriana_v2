"""Trail Peñasagra - Corremos por Adriana V2 """

import reflex as rx
from rxconfig import config
from trailcorremosadriana_v2.pages.galeria.galeria import ver_galeria



app = rx.App()
app.add_page(ver_galeria, route="/galeria")
# la de galeria, noticias, etc se añadirá más adelante