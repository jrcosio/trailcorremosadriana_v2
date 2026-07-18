import asyncio
import re
import reflex as rx
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _enviar_smtp(name: str, email: str, subject: str, description: str) -> None:
    """Envío SMTP síncrono; se ejecuta en un hilo para no bloquear el backend."""
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    sender_email = os.environ.get("SENDER_EMAIL", "")
    sender_password = os.environ.get("SENDER_PASSWORD", "")
    receiver_email = os.environ.get("RECEIVER_EMAIL", "")

    msg = EmailMessage()
    msg['Subject'] = f"Nuevo contacto web: {subject}"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    body = f"""
    Has recibido un nuevo mensaje desde el formulario web:

    👤 Nombre: {name}
    ✉️ Email: {email}
    📝 Asunto: {subject}

    📄 Descripción:
    {description}
    """
    msg.set_content(body)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


class ContactoState(rx.State):
    # 1. Variables de estado (conectadas a los inputs del formulario)
    name: str = ""
    email: str = ""
    subject: str = ""
    description: str = ""
    # Honeypot antispam: campo invisible que solo rellenan los bots.
    website: str = ""

    # 2. Variables de control de UI
    is_sending: bool = False
    submitted: bool = False
    feedback_message: str = ""

    # 3. Setters para actualizar el estado desde los inputs
    @rx.event
    def set_name(self, value: str):
        self.name = value

    @rx.event
    def set_email(self, value: str):
        self.email = value

    @rx.event
    def set_subject(self, value: str):
        self.subject = value

    @rx.event
    def set_description(self, value: str):
        self.description = value

    @rx.event
    def set_website(self, value: str):
        self.website = value

    @rx.event
    def reset_form(self):
        self.name = ""
        self.email = ""
        self.subject = ""
        self.description = ""
        self.website = ""
        self.submitted = False
        self.feedback_message = ""

    # 4. Método para manejar el envío del formulario
    @rx.event
    async def send_email(self):
        """Manejador de evento asociado al botón de 'Enviar'."""

        # Si el honeypot viene relleno es un bot: fingimos éxito y no enviamos.
        if self.website:
            self.submitted = True
            return

        # Validación antes de intentar enviar
        if not self.name or not self.email or not self.description:
            self.feedback_message = "Por favor, rellena los campos obligatorios (Nombre, Email y Descripción)."
            return
        if not _EMAIL_RE.match(self.email.strip()):
            self.feedback_message = "El email no parece válido. Revísalo, por favor."
            return

        # Cambiamos el estado a enviando y actualizamos la UI (útil para un spinner de carga)
        self.is_sending = True
        self.feedback_message = ""
        yield  # El 'yield' pausa la función y actualiza la interfaz del usuario inmediatamente.

        try:
            # En un hilo aparte: la conexión SMTP no bloquea al resto de usuarios.
            await asyncio.to_thread(
                _enviar_smtp, self.name, self.email.strip(), self.subject, self.description
            )

            # Si todo sale bien, marcamos como enviado
            self.submitted = True
            self.name = ""
            self.email = ""
            self.subject = ""
            self.description = ""

        except Exception as e:
            # Capturamos cualquier error (fallo de red, credenciales incorrectas, etc.)
            print(f"Error enviando correo: {e}")  # Para los logs del servidor
            self.feedback_message = "Hubo un error al enviar el mensaje. Por favor, inténtalo más tarde."

        finally:
            # Pase lo que pase, terminamos el estado de "cargando"
            self.is_sending = False
            yield  # Actualizamos la UI por última vez
