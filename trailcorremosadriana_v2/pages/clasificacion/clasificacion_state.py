import csv
import unicodedata
from pathlib import Path

import reflex as rx

# datos/ vive en la raíz del repo (fuera de assets/): se lee en el backend.
DATOS_DIR = Path(__file__).resolve().parents[3] / "datos"

# clave -> (fichero, título, subtítulo, color, icono)
CARRERAS: dict[str, tuple[str, str, str, str, str]] = {
    "27": ("Clasificacion_27km.csv", "Trail Peñasagra", "27K", "#30a46c", "medal"),
    "14": ("Clasificacion_14km.csv", "Speed Trail Peñasagra", "14K", "#F59E0B", "zap"),
    "marcha": ("Clasificacion_marcha.csv", "Marcha Familiar", "7K", "#38BDF8", "users"),
}


def _normalizar(texto: str) -> str:
    """Minúsculas y sin acentos, para búsqueda tipo LIKE insensible."""
    return "".join(
        c for c in unicodedata.normalize("NFD", texto)
        if not unicodedata.combining(c)
    ).casefold()


def _leer_csv(ruta: Path) -> list[dict[str, str]]:
    # utf-8-sig elimina el BOM; newline="" deja que csv gestione los CRLF.
    with ruta.open(encoding="utf-8-sig", newline="") as f:
        return [
            {
                (clave or "").strip().lower().replace(" ", "_"): (valor or "").strip()
                for clave, valor in fila.items()
            }
            for fila in csv.DictReader(f)
        ]


class ClasificacionesIndexState(rx.State):
    """Índice: años disponibles escaneando datos/ en cada carga de la página."""

    anios: list[str] = []

    @rx.event
    def cargar_anios(self):
        if not DATOS_DIR.is_dir():
            self.anios = []
            return
        self.anios = sorted(
            (
                d.name
                for d in DATOS_DIR.iterdir()
                if d.is_dir() and d.name.isdigit() and any(d.glob("Clasificacion_*.csv"))
            ),
            reverse=True,
        )


class ClasificacionState(rx.State):
    """Detalle de un año. La var `anio` la genera Reflex automáticamente
    por la ruta dinámica /clasificaciones/[anio]: no declararla aquí."""

    carrera: str = "27"
    genero: str = "General"  # General | Masculino | Femenino
    busqueda: str = ""
    carreras_disponibles: list[str] = []
    _datos: dict[str, list[dict[str, str]]] = {}  # backend-only, no viaja al cliente

    @rx.event
    def cargar_datos(self):
        """on_load: lee los CSVs del año indicado en la URL."""
        self.busqueda = ""
        self.genero = "General"
        self._datos = {}
        anio = self.anio
        if not anio.isdigit() or not (DATOS_DIR / anio).is_dir():
            return rx.redirect("/clasificaciones")
        disponibles: list[str] = []
        for clave, (fichero, *_resto) in CARRERAS.items():
            ruta = DATOS_DIR / anio / fichero
            if ruta.is_file():
                self._datos[clave] = _leer_csv(ruta)
                disponibles.append(clave)
        self.carreras_disponibles = disponibles
        if disponibles and self.carrera not in disponibles:
            self.carrera = disponibles[0]

    @rx.event
    def seleccionar_carrera(self, clave: str):
        self.carrera = clave

    @rx.event
    def seleccionar_genero(self, genero: str):
        self.genero = genero

    @rx.event
    def actualizar_busqueda(self, valor: str):
        self.busqueda = valor

    @rx.var
    def es_marcha(self) -> bool:
        return self.carrera == "marcha"

    @rx.var
    def color_carrera(self) -> str:
        return CARRERAS.get(self.carrera, ("", "", "", "orange", ""))[3]

    @rx.var
    def filas(self) -> list[dict[str, str]]:
        filas = self._datos.get(self.carrera, [])
        clave_pos = "pos"
        if self.genero in ("Masculino", "Femenino"):
            filas = [f for f in filas if f.get("genero") == self.genero]
            clave_pos = "pos_genero"
        consulta = _normalizar(self.busqueda.strip())
        if consulta:
            filas = [
                f
                for f in filas
                if consulta in _normalizar(f.get("nombre", "") + " " + f.get("apellidos", ""))
            ]
        resultado: list[dict[str, str]] = []
        for f in filas:
            pos = f.get(clave_pos) or f.get("pos", "")
            podium = pos if pos in ("1", "2", "3") else ("top5" if pos in ("4", "5") else "")
            resultado.append({**f, "pos_mostrada": pos or "—", "podium": podium})
        return resultado

    @rx.var
    def total_filas(self) -> int:
        return len(self.filas)
