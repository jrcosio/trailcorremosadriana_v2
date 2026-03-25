import reflex as rx



def card(imagen: str, titulo: str, descripcion: str, on_click: callable) -> rx.Component:
    return rx.card(
        rx.image(src=imagen, width="100%", border_radius="5px"),
        rx.heading(titulo, size="5", color="orange", width="100%", text_align="center", margin_top="3"),
        rx.box(height="4px"),
        rx.button("Inscribirme", color_scheme="green", margin_top="3", width="100%", size="3", on_click=on_click),
        rx.box(height="4px"),
        rx.text(descripcion, margin_top="1"),
       
        padding="4",
        #background_color="white",
        border_radius="md",
        box_shadow="md"
    )

def inscripciones() -> rx.Component:
    return rx.center( 
        rx.vstack(
            rx.text("Inscripciones", font_size="2em", color="orange", font_weight="bold",text_align="center"),
            rx.divider(border_color="#30a46c", width="100px", margin="0 auto", border_width="2px"),
            rx.text(
                "¡Las inscripciones para el Trail Peñasagra ya están abiertas! No pierdas la oportunidad de ser parte de esta increíble experiencia. Inscríbete ahora y asegura tu lugar en la carrera más emocionante del año.",
                font_size="1.2em",
                color="#FFFFFF",
                text_align="center",
            ),
            rx.grid(
                card(
                    imagen="/img/trail_inscripciones.webp",
                    titulo="Trail Peñasagra - 27 Km", 
                    descripcion="28 Km por los senderos más exigentes de la Sierra. Un reto para los que buscan superarse entre montañas.",
                    on_click=lambda: rx.redirect("https://www.gedsports.com/inscription/trail-sierra-de-penasagra--27-km")
                ),
                
                card(
                    imagen="/img/speed_trail_inscripciones.webp", 
                    titulo="Speed Trail Peñasagra - 14 Km", 
                    descripcion="15 Km de ritmo intenso y paisajes inolvidables. La distancia perfecta para disfrutar y competir.", 
                    on_click=lambda: rx.redirect("https://www.gedsports.com/inscription/speed-trail-sierra-de-penasagra--14-km")
                ),
                
                card(
                    imagen="/img/familiar_trail_inscripciones.webp", 
                    titulo="Familiar Peñasagra - 7 Km", 
                    descripcion="8 Km para compartir en familia. Una jornada pensada para que pequeños y mayores disfruten juntos de la naturaleza.",
                    on_click=lambda: rx.redirect("https://www.gedsports.com/inscription/familiar-sierra-de-penasagra--7-km")
                ),
                                
                card(
                    imagen="/img/familiar_menor_12.webp",
                    titulo="Familiar Peñasagra Menores de 8 a 12 años - 7 Km",
                    descripcion="Una carrera pensada especialmente para las familias, con un recorrido seguro y divertido para que disfruten de la naturaleza en familia.",
                    on_click=lambda: rx.redirect("https://www.gedsports.com/inscription/familiar-sierra-de-penasagra-menores-de-8-a-12-anos--7-km")
                ),
                
                card(
                    imagen="/img/familiar_menor_8.webp", 
                    titulo="Familiar Peñasagra Menores de 8 años - 7 Km", 
                    descripcion="Una carrera pensada especialmente para los más pequeños de 8 años, con un recorrido seguro y divertido de 7 kilómetros.",
                    on_click=lambda: rx.redirect("https://www.gedsports.com/inscription/familiar-sierra-de-penasagra-menores-de-8-anos--7-km")
                ),
                
                card(
                    imagen="/img/dorsal_solidario.webp",
                    titulo="Dorsal Solidario",
                    descripcion="Participa con el Dorsal Solidario, una opción para aquellos que quieran apoyar la causa sin correr. Con tu aportación",
                    on_click=lambda: rx.redirect("https://www.gedsports.com/inscription/trail-sierra-de-penasagra--dorsal-solidario")
                ),
                
                columns=rx.breakpoints(initial="1", sm="3", lg="3"),
                spacing="5",
                width=rx.breakpoints(initial="100%", sm="90%", lg="70%"),
                padding="20px",
            ),
            align="center",
            padding="2em",
        ),
        width="100%",
    )