import reflex as rx
import asyncio
from datetime import datetime, timezone

# Tu fecha objetivo
Fecha_carrera = datetime(2026, 7, 11, 0, 0, 0, tzinfo=timezone.utc)

class DateCountdownState(rx.State):
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    is_active: bool = False

    @rx.var
    def formatted_days(self) -> str:
        return f"{self.days:02d}"

    @rx.var
    def formatted_hours(self) -> str:
        return f"{self.hours:02d}"

    @rx.var
    def formatted_minutes(self) -> str:
        return f"{self.minutes:02d}"

    @rx.var
    def formatted_seconds(self) -> str:
        return f"{self.seconds:02d}"

    @rx.event(background=True)
    async def start_clock(self):
        async with self:
            if self.is_active: return
            self.is_active = True

        while self.is_active:
            now = datetime.now(timezone.utc)
            time_diff = Fecha_carrera - now
            
            async with self:
                if time_diff.total_seconds() <= 0:
                    self.days = self.hours = self.minutes = self.seconds = 0
                    self.is_active = False
                    return
                
                self.days = time_diff.days
                self.hours = (time_diff.seconds // 3600)
                self.minutes = (time_diff.seconds // 60) % 60
                self.seconds = time_diff.seconds % 60

            await asyncio.sleep(1)

def time_unit(value: str, label: str): 
    return rx.vstack(
        rx.text(value, font_size="5em", font_weight="bold", font_family="Fjalla One", color="white"),
        rx.text(label, font_size="1.5em", color="white"),
        align="center",
        spacing="2",
    )

def index():
    return rx.center(
        rx.vstack(
            rx.text("TRAIL SIERRA DE PEÑASAGRA", color="white", size="9", font_weight="bold"),
            rx.text("Corremos por Adriana", color="white", size="9"),
            rx.hstack(
                rx.text("Solo faltan", size="8", font_weight="bold", color="white"),
                time_unit(DateCountdownState.formatted_days, "Días"),
                time_unit(DateCountdownState.formatted_hours, "Horas"),
                time_unit(DateCountdownState.formatted_minutes, "Minutos"),
                time_unit(DateCountdownState.formatted_seconds, "Segundos"),
                spacing="9",
                padding="3em",
                ),
                 ),
        # --- CONFIGURACIÓN DEL FONDO ---
        on_mount=DateCountdownState.start_clock, 
        width="100%",
        height="100vh",
        background_image="url('/Peñasagra.png')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
    )

app = rx.App()
app.add_page(index, on_load=DateCountdownState.start_clock)
