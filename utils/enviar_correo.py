import xml.etree.ElementTree as ET
import smtplib
from email.message import EmailMessage
from jinja2 import Template
from utils.ajuste import ParametroAjuste

class EnviarCorreo:
    def __init__(self):
        self.ParametroAjuste = ParametroAjuste()

    def renderizar_plantilla_xml(self,nombre_plantilla,contexto):
        tree = ET.parse(f"plantillas/correo/{nombre_plantilla}")
        root = tree.getroot()

        subject_template = Template(root.find("subject").text)
        body_template = Template(root.find("body").text.strip())

        asunto = subject_template.render(contexto)
        cuerpo_html = body_template.render(contexto)

        return asunto, cuerpo_html

    def enviar_correo(self,destinatario, nombre_plantilla, contexto):
        asunto, cuerpo_html = self.renderizar_plantilla_xml(nombre_plantilla,contexto)

        msg = EmailMessage()
        msg.set_content(cuerpo_html, subtype='html')
        msg["Subject"] = asunto
        msg["From"] = self.ParametroAjuste.smtp_usuario
        msg["To"] = destinatario

        with smtplib.SMTP_SSL( self.ParametroAjuste.smtp_servidor, int(self.ParametroAjuste.smtp_puerto)) as smtp:
            smtp.login(self.ParametroAjuste.smtp_usuario, self.ParametroAjuste.smtp_contrasena)
            smtp.send_message(msg)

        return True
