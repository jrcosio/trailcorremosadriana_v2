import reflex as rx


def pie_pagina():
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.heading("Trail Peñasagra", color="white", size="7"),
                    rx.text(
                        "Corremos por Adriana", 
                        color="#94A3B8",
                        font_size="21px"
                    ),
                    align_items="start",
                    width="300px",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.text("ENLACES", color="white", font_weight="bold"),
                    rx.link("Instagram", href="#", color="#94A3B8"),
                    align_items="start",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.text("LEGAL", color="white", font_weight="bold"),
                    rx.link("Reglamento", href="#", color="#94A3B8"),
                    align_items="start",
                ),
                width="100%",
            ),
            rx.divider(border_color="#1E3A5F"),
            rx.hstack(
                rx.text("Cosío © 2026 Asociación Peñasagra | Hackers Cosío [José, Lanza, Pablo, Hugo, Diego y Mireite]", color="#64748B", font_size="14px"),
                rx.spacer(),
                rx.link("email", href="mailto:asociacionpenasagra@gmail.com", color="#94A3B8"),
                width="100%",
            ),
            spacing="6",
            width="100%",
            max_width="1200px",
            margin="0 auto",
        ),
        bg="#061B36",
        padding="40px 20px",
        width="100%",
    )