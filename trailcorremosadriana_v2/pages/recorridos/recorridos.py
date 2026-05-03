import reflex as rx

from trailcorremosadriana_v2.components.barra_navegacion import barra_de_navegacion
from trailcorremosadriana_v2.components.pie_pagina import pie_pagina


class RecorridosState(rx.State):
    recorrido: str = "27"

    def seleccionar_recorrido(self, recorrido: str) -> None:
        self.recorrido = recorrido


def _hero_recorridos() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(
                "11 de julio, 2026 | Cosío, Cantabria",
                color="white",
                font_size=rx.breakpoints(initial="0.75em", sm="0.9em"),
                font_weight="600",
                letter_spacing="0.16em",
                text_transform="uppercase",
                background_color="rgba(255,255,255,0.12)",
                border="1px solid rgba(255,255,255,0.25)",
                border_radius="999px",
                padding="0.5em 1em",
                text_align="center",
            ),
            rx.heading(
                "RECORRIDOS",
                color="white",
                font_size=rx.breakpoints(initial="2.8em", sm="4.5em", lg="6em"),
                font_weight="900",
                line_height="0.95",
                text_align="center",
                letter_spacing="-0.04em",
            ),
            rx.heading(
                "SIERRA DE PEÑASAGRA",
                color="orange",
                font_size=rx.breakpoints(initial="2em", sm="3.2em", lg="4.5em"),
                font_weight="900",
                line_height="1",
                text_align="center",
                letter_spacing="-0.03em",
            ),
            rx.text(
                "Elige tu prueba y explora la ficha técnica, los avituallamientos y el track interactivo de Wikiloc.",
                color="#E5E7EB",
                font_size=rx.breakpoints(initial="1em", sm="1.15em", lg="1.3em"),
                text_align="center",
                max_width="760px",
                line_height="1.7",
            ),
            spacing="4",
            align="center",
            padding=rx.breakpoints(initial="2em 1em", sm="3em 2em"),
        ),
        min_height=rx.breakpoints(initial="520px", lg="620px"),
        width="100%",
        background_image="linear-gradient(rgba(0,0,0,0.55), rgba(51,51,51,0.92)), url('/fondos/fondo.webp')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
    )


def _selector_boton(clave: str, titulo: str, subtitulo: str, color: str) -> rx.Component:
    activo = RecorridosState.recorrido == clave
    return rx.button(
        rx.vstack(
            rx.text(titulo, font_size="1em", font_weight="900", line_height="1.1"),
            rx.text(subtitulo, font_size="0.75em", font_weight="700", opacity="0.85"),
            spacing="1",
            align="center",
        ),
        on_click=RecorridosState.seleccionar_recorrido(clave),
        width="100%",
        min_height="82px",
        border_radius="18px",
        color="white",
        background_color=rx.cond(activo, color, "rgba(255,255,255,0.04)"),
        border=rx.cond(activo, f"1px solid {color}", "1px solid rgba(255,255,255,0.10)"),
        box_shadow=rx.cond(activo, f"0 18px 45px {color}33", "none"),
        cursor="pointer",
        transition="all 0.25s ease",
        _hover={"transform": "translateY(-3px)", "border_color": color},
    )


def _selector_recorridos() -> rx.Component:
    return rx.box(
        rx.grid(
            _selector_boton("27", "Trail Peñasagra", "27K | +1700m", "#30a46c"),
            _selector_boton("14", "Speed Trail Peñasagra", "14K | +800m", "orange"),
            _selector_boton("7", "Familiar Peñasagra", "7K | +250m", "#38BDF8"),
            columns=rx.breakpoints(initial="1", md="3"),
            spacing="4",
            width="100%",
        ),
        width="100%",
        max_width="1000px",
        margin="0 auto",
        margin_top=rx.breakpoints(initial="-3.5em", lg="-5em"),
        position="relative",
        z_index="2",
    )


def _stat(icono: str, valor: str, unidad: str, color: str) -> rx.Component:
    return rx.vstack(
        rx.icon(icono, color=color, size=28),
        rx.hstack(
            rx.text(valor, color="white", font_size="2.2em", font_weight="900", line_height="1"),
            rx.text(unidad, color="#CBD5E1", font_size="0.9em", font_weight="800", padding_top="1.1em"),
            spacing="1",
            align="end",
        ),
        spacing="2",
        align="center",
        justify="center",
        min_width="120px",
        padding="1em",
        background_color="rgba(255,255,255,0.08)",
        border="1px solid rgba(255,255,255,0.12)",
        border_radius="18px",
    )


def _cabecera_prueba(
    etiqueta: str,
    titulo: str,
    destacado: str,
    distancia: str,
    desnivel: str,
    hora: str,
    color: str,
    icono: str,
) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.icon(icono, color=color, size=18),
                rx.text(etiqueta, color=color, font_weight="900", letter_spacing="0.12em", text_transform="uppercase"),
                spacing="2",
                align="center",
                padding="0.45em 1em",
                background_color="rgba(0,0,0,0.26)",
                border="1px solid rgba(255,255,255,0.12)",
                border_radius="999px",
            ),
            rx.heading(
                rx.text(titulo, as_="span"),
                " ",
                rx.text(destacado, as_="span", color=color),
                color="white",
                font_size=rx.breakpoints(initial="2.4em", sm="4.2em", lg="5.4em"),
                font_weight="900",
                line_height="0.95",
                text_align="center",
                letter_spacing="-0.04em",
            ),
            rx.flex(
                _stat("route", distancia, "KM", color),
                _stat("trending-up", desnivel, "M", color),
                _stat("clock", hora, "H", "#38BDF8"),
                wrap="wrap",
                justify="center",
                gap="1em",
                width="100%",
            ),
            spacing="5",
            align="center",
            width="100%",
            padding="2em",
        ),
        min_height="420px",
        width="100%",
        background_image=f"linear-gradient(rgba(0,0,0,0.35), rgba(51,51,51,0.88)), url('/fondos/fondo.webp')",
        background_size="cover",
        background_position="center",
        border_radius="26px",
        overflow="hidden",
        border="1px solid rgba(255,255,255,0.10)",
        box_shadow="0 20px 60px rgba(0,0,0,0.25)",
    )


def _glass_card(*children: rx.Component, border_color: str | None = None) -> rx.Component:
    return rx.box(
        rx.vstack(*children, spacing="5", align="start", width="100%"),
        width="100%",
        padding=rx.breakpoints(initial="1.35em", sm="1.75em"),
        background_color="rgba(255,255,255,0.04)",
        border="1px solid rgba(255,255,255,0.08)",
        border_top=rx.cond(border_color is not None, f"4px solid {border_color}", "1px solid rgba(255,255,255,0.08)"),
        border_radius="18px",
        box_shadow="0 16px 40px rgba(0,0,0,0.20)",
    )


def _ficha_item(icono: str, etiqueta: str, valor: str, color: str) -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.icon(icono, color=color, size=18),
            rx.text(etiqueta, color="white", font_weight="800"),
            spacing="2",
            align="center",
        ),
        rx.spacer(),
        rx.text(valor, color="#CBD5E1", text_align="right", font_weight="600"),
        width="100%",
        align="center",
        gap="1em",
    )


def _ficha_tecnica(color: str, terreno: str, precio: str | None = None, familiar: bool = False) -> rx.Component:
    precio_componentes = [
        _ficha_item("tag", "Precio", precio, color),
    ] if precio else []

    precios_familiares = [
        rx.box(
            rx.vstack(
                rx.hstack(rx.icon("tag", color=color, size=18), rx.text("Precios de Inscripción", color="white", font_weight="800"), spacing="2"),
                rx.hstack(rx.text("General", color="#CBD5E1"), rx.spacer(), rx.text("12 €", color="white", font_weight="900"), width="100%"),
                rx.hstack(rx.text("Niños (8 a 12 años)", color="#CBD5E1"), rx.spacer(), rx.text("12 €", color="white", font_weight="900"), width="100%"),
                rx.hstack(rx.text("Niños (< 8 años)", color="#CBD5E1"), rx.spacer(), rx.text("5 € / Gratis", color=color, font_weight="900"), width="100%"),
                spacing="3",
                width="100%",
            ),
            padding_top="1em",
            border_top="1px solid rgba(255,255,255,0.08)",
            width="100%",
        )
    ] if familiar else []

    return _glass_card(
        rx.heading("FICHA TÉCNICA", color="white", font_size="1.6em", font_weight="900"),
        rx.vstack(
            _ficha_item("map-pin", "Salida / Meta", "Plaza de Cosío", color),
            _ficha_item("calendar-days", "Fecha", "11 de Julio de 2026", color),
            _ficha_item("timer", "Hora de Salida", "9:00 AM", color),
            _ficha_item("mountain", "Terreno", terreno, color),
            *precio_componentes,
            *precios_familiares,
            spacing="4",
            width="100%",
        ),
        border_color=color,
    )


def _avituallamiento_item(km: str, titulo: str, texto: str, color: str, destacado: str = "") -> rx.Component:
    return rx.hstack(
        rx.box(
            width="16px",
            height="16px",
            border_radius="999px",
            background_color=color,
            border="4px solid #333333",
            flex_shrink="0",
            margin_top="0.25em",
        ),
        rx.vstack(
            rx.heading(f"Km {km}: {titulo}", color="white", font_size="1em", font_weight="900"),
            rx.cond(
                destacado != "",
                rx.text(
                    destacado,
                    color=color,
                    font_size="0.72em",
                    font_weight="900",
                    text_transform="uppercase",
                    background_color="rgba(255,255,255,0.08)",
                    padding="0.25em 0.6em",
                    border_radius="999px",
                ),
            ),
            rx.text(texto, color="#CBD5E1", font_size="0.86em", line_height="1.5"),
            spacing="1",
            align="start",
        ),
        spacing="3",
        align="start",
        width="100%",
    )


def _avituallamientos(color: str, items: list[tuple[str, str, str, str]]) -> rx.Component:
    return _glass_card(
        rx.heading("AVITUALLAMIENTOS" if len(items) > 1 else "AVITUALLAMIENTO", color="white", font_size="1.6em", font_weight="900"),
        rx.vstack(
            *[_avituallamiento_item(km, titulo, texto, color, destacado) for km, titulo, texto, destacado in items],
            spacing="5",
            width="100%",
            border_left=f"2px solid {color}55",
            padding_left="1em",
        ),
    )


def _aviso(icono: str, titulo: str, texto: str, color: str, extra: str = "") -> rx.Component:
    return rx.hstack(
        rx.icon(icono, color=color, size=28),
        rx.vstack(
            rx.heading(titulo, color="white", font_size="1.05em", font_weight="900"),
            rx.text(texto, color="#CBD5E1", font_size="0.92em", line_height="1.6"),
            rx.cond(
                extra != "",
                rx.text(
                    extra,
                    color="white",
                    font_size="0.78em",
                    font_weight="700",
                    background_color="rgba(255,255,255,0.08)",
                    padding="0.75em",
                    border_radius="10px",
                ),
            ),
            spacing="2",
            align="start",
        ),
        spacing="4",
        align="start",
        width="100%",
        padding="1.4em",
        background_color=f"{color}14",
        border=f"1px solid {color}45",
        border_radius="18px",
    )


def _wikiloc(track_id: str) -> rx.Component:
    return rx.box(
        rx.el.iframe(
            src=(
                f"https://es.wikiloc.com/wikiloc/embedv2.do"
                f"?id={track_id}&elevation=on&images=off&maptype=H"
            ),
            # OJO: NO pasar width/height como atributos HTML al iframe.
            # Wikiloc usa las dimensiones nativas para inicializar el mapa
            # y entra en conflicto con el width/height: 100% del CSS.
            scrolling="no",
            allow_full_screen=True,
            loading="lazy",
            key=f"wikiloc-{track_id}",  # fuerza remount al cambiar de recorrido
            style={
                "width": "100%",
                "height": "100%",
                "border": "0",
                "display": "block",
            },
        ),
        width="100%",
        min_width="0",
        # Subo un pelín el alto mínimo: por debajo de ~480px el embed
        # también colapsa a la tarjeta sin mapa.
        height=rx.breakpoints(initial="520px", md="580px", lg="640px"),
        border_radius="14px",
        overflow="hidden",
        background_color="#111827",
        border="1px solid rgba(255,255,255,0.10)",
    )


def _mapa_y_descripcion(
    color: str,
    subtitulo: str,
    enlace: str,
    track_id: str,
    parrafos: list[str],
) -> rx.Component:
    return _glass_card(
        rx.flex(
            rx.vstack(
                rx.heading("PERFIL Y RUTA INTERACTIVA", color="white", font_size="1.9em", font_weight="900"),
                rx.text(subtitulo, color="#CBD5E1", line_height="1.6"),
                spacing="1",
                align="start",
            ),
            rx.link(
                rx.button(
                    rx.icon("download", size=18),
                    "Descargar Track (GPX)",
                    color="white",
                    background_color="rgba(0,0,0,0.35)",
                    border=f"1px solid {color}77",
                    border_radius="14px",
                    font_weight="900",
                    _hover={"background_color": color},
                ),
                href=enlace,
                is_external=True,
                width=rx.breakpoints(initial="100%", md="auto"),
            ),
            direction=rx.breakpoints(initial="column", md="row"),
            justify="between",
            align=rx.breakpoints(initial="stretch", md="center"),
            gap="1em",
            width="100%",
        ),
        _wikiloc(track_id),

        rx.vstack(
            rx.heading("Descripción del Recorrido", color="white", font_size="1.3em", font_weight="900"),
            *[rx.text(parrafo, color="#CBD5E1", line_height="1.75") for parrafo in parrafos],
            spacing="3",
            align="start",
            width="100%",
            padding_top="0.5em",
        ),
    )


def _layout_prueba(
    cabecera: rx.Component,
    ficha: rx.Component,
    avituallamientos: rx.Component,
    aviso: rx.Component,
    mapa: rx.Component,
) -> rx.Component:
    return rx.vstack(
        cabecera,
        rx.grid(
            rx.vstack(ficha, avituallamientos, aviso, spacing="5", width="100%", min_width="0"),
            rx.box(
                mapa,
                width="100%",
                min_width="0",
            ),
            grid_template_columns=rx.breakpoints(initial="1fr", lg="minmax(280px, 360px) minmax(0, 1fr)"),
            spacing="6",
            width="100%",
            min_width="0",
            align_items="start",
        ),
        spacing="6",
        width="100%",
    )


def _recorrido_27() -> rx.Component:
    color = "#30a46c"
    return _layout_prueba(
        _cabecera_prueba("Prueba Reina", "TRAIL", "PEÑASAGRA", "27", "+1700", "9:00", color, "medal"),
        _ficha_tecnica(color, "90% Sendero y Pista", "28 €"),
        _avituallamientos(
            color,
            [
                ("5", "Braña de Roja", "Sólido / Líquido", ""),
                ("13", "Refugio de Busneu", "Sólido / Líquido", ""),
                ("22", "Pozo Verde", "Sólido / Líquido", "Exclusivo Distancia Larga"),
                ("27", "Meta (Plaza Cosío)", "Avituallamiento Final", ""),
            ],
        ),
        _aviso(
            "triangle-alert",
            "Material Obligatorio",
            "No habrá vasos en los avituallamientos. Es obligatorio llevar recipiente para líquidos. Se recomienda manta térmica.",
            "orange",
        ),
        _mapa_y_descripcion(
            color,
            "Explora el desnivel y el recorrido en detalle.",
            "https://es.wikiloc.com/rutas-carrera-por-montana/trail-sierra-penasagra-260167031",
            "260167031",
            [
                "La prueba reina de la Sierra de Peñasagra es un desafío técnico y espectacular. Con salida desde la plaza de Cosío, el recorrido se adentra rápidamente en las laderas del valle y afronta desde el inicio el duro cortafuegos, uno de los tramos que marca el carácter de la carrera. A lo largo de sus 27 kilómetros, los corredores se enfrentarán a 1.700 metros de desnivel positivo, transitando en su gran mayoría por senderos de montaña históricos, zonas técnicas y paisajes de gran belleza natural.",
                "Puntos clave como la Braña de Roja y el Refugio de Busneu marcarán el ritmo antes de afrontar la zona exclusiva de la prueba larga: el paso por el Pozo Verde, donde la carrera alcanza su punto más salvaje antes de iniciar el trepidante descenso de vuelta hacia la línea de meta en Cosío.",
            ],
        ),
    )


def _recorrido_14() -> rx.Component:
    color = "#F59E0B"
    return _layout_prueba(
        _cabecera_prueba("Rápida e Intensa", "SPEED TRAIL", "PEÑASAGRA", "14", "+800", "9:00", color, "zap"),
        _ficha_tecnica(color, "Senderos boscosos", "18 €"),
        _avituallamientos(
            color,
            [
                ("5", "Braña de Roja", "Sólido / Líquido", ""),
                ("13", "Refugio de Busneu", "Sólido / Líquido", ""),
                ("14", "Meta (Plaza Cosío)", "Avituallamiento Final", ""),
            ],
        ),
        _aviso(
            "triangle-alert",
            "Material Obligatorio",
            "No habrá vasos en los avituallamientos. Es obligatorio llevar recipiente para líquidos. Se recomienda manta térmica.",
            "orange",
        ),
        _mapa_y_descripcion(
            color,
            "Explora el recorrido del Speed Trail.",
            "https://es.wikiloc.com/rutas-carrera-por-montana/trail-sierra-penasagra-14k-176672547",
            "176672547",
            [
                "El Speed Trail Peñasagra es el recorrido ideal tanto para quienes quieren iniciarse en las carreras por montaña como para corredores explosivos que buscan ritmos altos. En sus 14 kilómetros concentra 800 metros de desnivel positivo y conserva uno de los puntos más reconocibles del trazado: el famoso cortafuegos, un tramo exigente que garantiza la esencia pura del trail running.",
                "Compartiendo la salida desde Cosío con la prueba larga, el circuito transcurre por senderos boscosos y zonas rápidas que permiten disfrutar del entorno sin perder intensidad. Con la ayuda de los avituallamientos de Braña de Roja y el Refugio de Busneu, podrás exprimir tus piernas hasta el trepidante regreso a meta.",
            ],
        ),
    )


def _recorrido_7() -> rx.Component:
    color = "#38BDF8"
    return _layout_prueba(
        _cabecera_prueba("Para todos los públicos", "FAMILIAR", "PEÑASAGRA", "7", "+250", "9:00", color, "users"),
        _ficha_tecnica(color, "Senderos sencillos", familiar=True),
        _avituallamientos(
            color,
            [
                ("7", "Meta (Plaza Cosío)", "Avituallamiento Final. Disfruta de tu merecida recompensa al finalizar el recorrido junto al resto de participantes.", ""),
            ],
        ),
        _aviso(
            "info",
            "Información Importante",
            "Se recomienda llevar agua durante el recorrido. No hay puntos intermedios de avituallamiento.",
            color,
            "Menores de 16 años: imprescindible autorización de tutor legal y estar acompañados por un adulto en todo momento.",
        ),
        _mapa_y_descripcion(
            color,
            "Un paseo para disfrutar del entorno de Rionansa.",
            "https://es.wikiloc.com/rutas-carrera-por-montana/trail-sierra-penasagra-marcha-7k-260165721",
            "260165721",
            [
                "La Marcha Familiar está diseñada para que todos puedan ser partícipes de la gran fiesta del Trail Sierra de Peñasagra. Olvídate del cronómetro: aquí lo importante es respirar aire puro, disfrutar de la naturaleza y compartir una mañana deportiva en familia o con amigos.",
                "Con apenas 250 metros de desnivel positivo a lo largo de 7 kilómetros, es una ruta suave, mayoritariamente por pistas anchas y senderos accesibles, que invita a caminar a buen ritmo y deleitarse con el paisaje que envuelve la localidad de Cosío. El gran ambiente de meta te estará esperando a la vuelta.",
            ],
        ),
    )


def _contenido_recorrido() -> rx.Component:
    return rx.cond(
        RecorridosState.recorrido == "27",
        _recorrido_27(),
        rx.cond(
            RecorridosState.recorrido == "14",
            _recorrido_14(),
            _recorrido_7(),
        ),
    )


def recorridos() -> rx.Component:
    return rx.box(
        barra_de_navegacion(),
        _hero_recorridos(),
        rx.box(
            rx.vstack(
                _selector_recorridos(),
                _contenido_recorrido(),
                spacing="7",
                width="100%",
                max_width="1200px",
                margin="0 auto",
                padding=rx.breakpoints(initial="0 1em 3em", sm="0 2em 4em"),
            ),
            width="100%",
            background_color="#333333",
        ),
        pie_pagina(),
        background_color="#333333",
    )
