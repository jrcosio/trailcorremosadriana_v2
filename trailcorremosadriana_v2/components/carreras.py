import reflex as rx

def card(imagen: str, titulo_izq: str, titulo_der: str, descripcion: str, overlay_text: str = "", texto_inferior: str = "") -> rx.Component:
    return rx.card(
        rx.text(overlay_text, color="blue", size="8", font_weight="bold", width="100%", text_align="center", margin_bottom="3"),
        rx.box(
            rx.image(src=imagen, width="100%", border_radius="5px"),
            position="relative",
            width="100%",
            border_radius="5px",
            overflow="hidden",
        ),
        rx.hstack(
            rx.heading(titulo_izq, size="5", color="grey"),
            rx.heading(titulo_der, size="5", color="black"),
            width="100%",
            justify_content="space-between",
            align_items="center",
            margin_top="3",
        ),
        rx.box(height="10px"),
        rx.center(
            rx.button("Ir al track", color_scheme="green", margin_top="3", width="50%", size="3")
        ),
        rx.box(height="10px"),
        rx.text(descripcion, margin_top="1", size="5"),
        rx.box(height="10px"),
        rx.text(texto_inferior, margin_top="1", size="3", color="black"),    
        padding="4",
        # background_color="white",
        border_radius="md",
        box_shadow="md"
    )

def carreras():
    return rx.center(
        rx.vstack(
            rx.text("Recorridos de la prueba", size="9",
                    font_family="Impact,",
                    font_weight="bold",
                    font_style="italic",
                    color="red"),
            rx.box(height="100px"),
            rx.grid(
                card(
                    imagen="/fondos/Trail.jpg", 
                    titulo_izq="27 Km",
                    titulo_der="+1700m",
                    descripcion="3 avituallamientos + meta\nCronometraje GedSPORT\nSalida: 9:00 Plaza de Cosío",
                    overlay_text="Trail Peñasagra",
                    texto_inferior="Inscripcion: 28 €",       
                ),
                card(
                    imagen="/fondos/Speed.jpg", 
                    titulo_izq="14 Km",
                    titulo_der="+800m", 
                    descripcion="2 avituallamientos + meta\nCronometraje GedSPORT\nSalida: 9:00 Plaza de Cosío",
                    overlay_text="Speed Trail Peñasagra",
                    texto_inferior="Inscripcion: 18 €",    
                ),
                card(
                    imagen="/fondos/Familiar.jpg", 
                    titulo_izq="7 Km",
                    titulo_der="+250m", 
                    descripcion="Avituallamiento en meta\nPara todas las edades\nParticipación conjunta",
                    overlay_text="Familiar Peñasagra",
                    texto_inferior="Inscripcion: 12€/5€\n(<8 años gratis)",  
                ),
                columns=rx.breakpoints(initial="1", sm="2", lg="3"), # Responsive: 1 col móvil, 3 en PC
                spacing="4",
            ),
            spacing="5",
            align="center",
            width="50%",
        ),
        padding_y="50px",
        background_image="url('/fondos/carreras.jpg')",
        background_size="contain",
        background_repeat="no-repeat",
        background_position="center",
        width="100%",
        min_height="100vh",
    )

