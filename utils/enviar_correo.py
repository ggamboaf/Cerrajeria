import xml.etree.ElementTree as ET
import smtplib
from email.message import EmailMessage
from jinja2 import Template
from utils.ajuste import ParametroAjuste
from utils.generar_reporte import GenerarReporte
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

class EnviarCorreo:
    def __init__(self):
        self.ParametroAjuste = ParametroAjuste()

    def renderizar_plantilla_xml(self,model):
        contexto = model.get_contexto()
        contexto = self.ParametroAjuste.get_contexto_empresa(contexto)
        tree = ET.parse(f"plantillas/correo/{model.accion_Config['correo_Template']}")
        root = tree.getroot()

        body_template = Template(root.find("body").text.strip())

        cuerpo_html = body_template.render(contexto)

        return cuerpo_html

    def enviar_correo(self,model):
        cuerpo_html = self.renderizar_plantilla_xml(model)

        msg = EmailMessage()
        msg.set_content(cuerpo_html, subtype='html')
        msg["Subject"] = "asunto"
        msg["From"] = self.ParametroAjuste.smtp_usuario
        msg["To"] = model.email

        with smtplib.SMTP_SSL( self.ParametroAjuste.smtp_servidor, int(self.ParametroAjuste.smtp_puerto)) as smtp:
            smtp.login(self.ParametroAjuste.smtp_usuario, self.ParametroAjuste.smtp_contrasena)
            smtp.send_message(msg)

        return True

    def enviar_correo_reporte(self,model):
        cuerpo_html = self.renderizar_plantilla_xml(model)
        pdf = GenerarReporte.obtener_plantilla_pdf(GenerarReporte(),model)

        msg = MIMEMultipart()
        msg["Subject"] = model.nombre
        msg["From"] = self.ParametroAjuste.smtp_usuario
        msg["To"] = model.cliente.email
        msg.attach(MIMEText(cuerpo_html, 'html'))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(pdf)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={model.nombre}.pdf")
        msg.attach(part)

        server = smtplib.SMTP_SSL(self.ParametroAjuste.smtp_servidor, int(self.ParametroAjuste.smtp_puerto))
        server.login(self.ParametroAjuste.smtp_usuario, self.ParametroAjuste.smtp_contrasena)
        server.send_message(msg)
        server.quit()