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
from trailcorremosadriana_v2.pages.principal.secciones.noticias_state import NoticiasState
from trailcorremosadriana_v2.pages.recorridos.recorridos import recorridos
from trailcorremosadriana_v2.pages.reglamento.reglamento import reglamento

DOMINIO = "https://trailpeñasagra.com"
OG_IMAGEN = f"{DOMINIO}/logos/corremos_por_adriana.webp"


def _meta_og(titulo: str, descripcion: str) -> list[dict[str, str]]:
    """Metas Open Graph / Twitter para que al compartir por WhatsApp o redes
    salga imagen, título y descripción. La imagen (og:image) la emite Reflex
    a partir del parámetro image= de add_page."""
    return [
        {"property": "og:type", "content": "website"},
        {"property": "og:title", "content": titulo},
        {"property": "og:description", "content": descripcion},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": titulo},
        {"name": "twitter:description", "content": descripcion},
    ]


app = rx.App(
    theme=rx.theme(appearance="light"),
)

_DESC_HOME = (
    "Web oficial del Trail Sierra de Peñasagra – Corremos por Adriana. "
    "Carrera solidaria de montaña en Cosío, Rionansa (Cantabria)."
)
app.add_page(
    index,
    route="/",
    image=OG_IMAGEN,
    title="Trail Sierra de Peñasagra – Corremos por Adriana",
    description=_DESC_HOME,
    meta=_meta_og("Trail Sierra de Peñasagra – Corremos por Adriana", _DESC_HOME),
    on_load=NoticiasState.cargar_noticias,
)

_DESC_CONTACTO = "Contacta con la organización del Trail Sierra de Peñasagra."
app.add_page(
    contacto,
    route="/contacto",
    image=OG_IMAGEN,
    title="Contacto | Trail Peñasagra",
    description=_DESC_CONTACTO,
    meta=_meta_og("Contacto | Trail Peñasagra", _DESC_CONTACTO),
)

_DESC_RECORRIDOS = (
    "Recorridos del Trail Peñasagra: 27K, 14K y marcha familiar de 7K. "
    "Perfiles, avituallamientos, material obligatorio y tracks GPX."
)
app.add_page(
    recorridos,
    route="/recorridos",
    image=OG_IMAGEN,
    title="Recorridos | Trail Peñasagra",
    description=_DESC_RECORRIDOS,
    meta=_meta_og("Recorridos | Trail Peñasagra", _DESC_RECORRIDOS),
)

_DESC_GALERIA = "Galería de fotos de las ediciones del Trail Sierra de Peñasagra."
app.add_page(
    galeria,
    route="/galeria",
    image=OG_IMAGEN,
    title="Galería | Trail Peñasagra",
    description=_DESC_GALERIA,
    meta=_meta_og("Galería | Trail Peñasagra", _DESC_GALERIA),
)

_DESC_REGLAMENTO = (
    "Reglamento oficial del Trail Sierra de Peñasagra: precios, categorías, "
    "material, seguridad y normativa."
)
app.add_page(
    reglamento,
    route="/reglamento",
    image=OG_IMAGEN,
    title="Reglamento | Trail Peñasagra",
    description=_DESC_REGLAMENTO,
    meta=_meta_og("Reglamento | Trail Peñasagra", _DESC_REGLAMENTO),
)

_DESC_CLASIFICACIONES = "Clasificaciones y resultados oficiales del Trail Sierra de Peñasagra."
app.add_page(
    clasificaciones,
    route="/clasificaciones",
    image=OG_IMAGEN,
    title="Clasificaciones | Trail Peñasagra",
    description=_DESC_CLASIFICACIONES,
    meta=_meta_og("Clasificaciones | Trail Peñasagra", _DESC_CLASIFICACIONES),
    on_load=ClasificacionesIndexState.cargar_anios,
)
app.add_page(
    clasificacion,
    route="/clasificaciones/[anio]",
    image=OG_IMAGEN,
    title="Resultados | Trail Peñasagra",
    description=_DESC_CLASIFICACIONES,
    meta=_meta_og("Resultados | Trail Peñasagra", _DESC_CLASIFICACIONES),
    on_load=ClasificacionState.cargar_datos,
)
