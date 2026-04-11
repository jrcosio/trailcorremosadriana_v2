import reflex as rx
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()


class ContactoState(rx.State):
    # 1. Variables de estado (conectadas a los inputs del formulario)
    name: str = ""
    email: str = ""
    subject: str = ""
    description: str = ""
    
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
    def reset_form(self):
        self.name = ""
        self.email = ""
        self.subject = ""
        self.description = ""
        self.submitted = False
        self.feedback_message = ""
    
    # 4. Método para manejar el envío del formulario
    def send_email(self):
        """Manejador de evento asociado al botón de 'Enviar'."""
        
        # Validación básica antes de intentar enviar
        if not self.name or not self.email or not self.description:
            self.feedback_message = "Por favor, rellena los campos obligatorios (Nombre, Email y Descripción)."
            return

        # Cambiamos el estado a enviando y actualizamos la UI (útil para un spinner de carga)
        self.is_sending = True
        self.feedback_message = ""
        yield  # El 'yield' pausa la función y actualiza la interfaz del usuario inmediatamente.

        try:

            smtp_server = "smtp.gmail.com" # Ejemplo con Gmail
            smtp_port = 465
            sender_email = os.environ.get("SENDER_EMAIL","")
            sender_password = os.environ.get("SENDER_PASSWORD","")
            receiver_email = os.environ.get("RECEIVER_EMAIL","")

            # Construcción del mensaje
            msg = EmailMessage()
            msg['Subject'] = f"Nuevo contacto web: {self.subject}"
            msg['From'] = sender_email
            msg['To'] = receiver_email

            body = f"""
            Has recibido un nuevo mensaje desde el formulario web:

            👤 Nombre: {self.name}
            ✉️ Email: {self.email}
            📝 Asunto: {self.subject}

            📄 Descripción:
            {self.description}
            """
            msg.set_content(body)

            # Envío del correo usando SSL
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)

            # Si todo sale bien, marcamos como enviado
            self.submitted = True
            self.name = ""
            self.email = ""
            self.subject = ""
            self.description = ""

        except Exception as e:
            # Capturamos cualquier error (fallo de red, credenciales incorrectas, etc.)
            print(f"Error enviando correo: {e}") # Para los logs del servidor
            self.feedback_message = "Hubo un error al enviar el mensaje. Por favor, inténtalo más tarde."

        finally:
            # Pase lo que pase, terminamos el estado de "cargando"
            self.is_sending = False
            yield # Actualizamos la UI por última vez