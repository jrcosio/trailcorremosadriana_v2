import json
import re
from datetime import date
from pathlib import Path

import reflex as rx

# datos/ vive en la raíz del repo (fuera de assets/): se lee en el backend.
# Las imágenes sí van en assets/ para que el navegador pueda pedirlas.
_RAIZ = Path(__file__).resolve().parents[4]
NOTICIAS_DIR = _RAIZ / "datos" / "noticias"
ASSETS_IMG_DIR = _RAIZ / "assets" / "noticias" / "img"
MAX_NOTICIAS = 4

_PREFIJO_FECHA = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")
_MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]


def _parsear_fecha(texto: str) -> date | None:
    m = _PREFIJO_FECHA.match(texto or "")
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def _fecha_de(data: dict, nombre_fichero: str) -> date:
    # Prioridad: campo "fecha" del JSON > prefijo AAAA-MM-DD del nombre.
    return (
        _parsear_fecha(str(data.get("fecha", "")))
        or _parsear_fecha(nombre_fichero)
        or date.min
    )


def _fecha_legible(f: date) -> str:
    if f == date.min:
        return ""
    return f"{f.day} de {_MESES[f.month - 1]} de {f.year}"


def _imagen_src(data: dict) -> str:
    # Solo se admite el nombre de fichero (sin rutas), resuelto en assets.
    nombre = Path(str(data.get("imagen", ""))).name
    if not nombre or not (ASSETS_IMG_DIR / nombre).is_file():
        return ""
    return f"/noticias/img/{nombre}"


class NoticiasState(rx.State):
    noticias: list[dict[str, str]] = []

    @rx.var
    def hay_noticias(self) -> bool:
        return len(self.noticias) > 0

    @rx.event
    def cargar_noticias(self):
        """on_load de la home: escanea datos/noticias/*.txt (JSON) y publica
        las MAX_NOTICIAS más recientes. Un fichero inválido se ignora."""
        items: list[tuple[date, str, dict]] = []
        if NOTICIAS_DIR.is_dir():
            for fichero in NOTICIAS_DIR.glob("*.txt"):
                try:
                    data = json.loads(fichero.read_text(encoding="utf-8-sig"))
                except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                    continue
                if not isinstance(data, dict) or not str(data.get("titulo", "")).strip():
                    continue
                items.append((_fecha_de(data, fichero.name), fichero.name, data))

        items.sort(key=lambda item: (item[0], item[1]), reverse=True)
        self.noticias = [
            {
                "titulo": str(data["titulo"]).strip(),
                "subtitulo": str(data.get("subtitulo", "")).strip(),
                "texto": str(data.get("texto", "")).strip(),
                "fecha_legible": _fecha_legible(fecha),
                "imagen_src": _imagen_src(data),
            }
            for fecha, _, data in items[:MAX_NOTICIAS]
        ]
