# Noticias de la web

Cada noticia es un fichero `.txt` en esta carpeta con contenido JSON. La home
muestra **solo las 4 más recientes**; el resto se ignoran sin borrarlas.

## Cómo publicar una noticia

1. Crea un fichero con el nombre `AAAA-MM-DD-titulo-corto.txt` (la fecha del
   nombre define el orden; la más nueva sale primero).
2. Pega dentro este contenido y rellénalo:

```json
{
  "titulo": "Título de la noticia (obligatorio)",
  "subtitulo": "Subtítulo opcional",
  "imagen": "nombre-imagen.webp",
  "texto": "Texto de la noticia.\n\nUsa \\n\\n para separar párrafos.",
  "fecha": "2026-07-13"
}
```

3. Si la noticia lleva imagen, copia el fichero a `assets/noticias/img/`
   (solo se escribe el nombre en el campo `imagen`, sin rutas).
4. Despliega: en local basta reiniciar `uv run reflex run`; en producción
   `docker compose up --build -d`.

## Reglas

- `titulo` es obligatorio: sin él la noticia no se publica.
- `subtitulo`, `imagen`, `texto` y `fecha` son opcionales.
- `fecha` (formato `AAAA-MM-DD`) tiene prioridad sobre la fecha del nombre.
- Si la imagen no existe en `assets/noticias/img/`, la tarjeta sale con un
  icono de periódico en su lugar (no rompe nada).
- Un fichero con JSON mal formado se ignora sin romper la web.
- Imágenes: formato **webp**, tamaño ideal **1200 × 750 px (proporción 16:10)**
  y **menos de 200 KB**. La web recorta centrado lo que sobre, así que evita
  texto o caras pegadas a los bordes superior e inferior.
