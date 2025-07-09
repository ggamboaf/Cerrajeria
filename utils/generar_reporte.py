from tkinter import filedialog, messagebox

import pdfkit
import xml.etree.ElementTree as ET

from jinja2 import Template
from models import *
from utils.ajuste import ParametroAjuste

class GenerarReporte:
    def __init__(self):
        self.ParametroAjuste = ParametroAjuste()

    def renderizar_plantilla_xml(self,model):
        contexto = model.get_contexto()
        contexto = self.ParametroAjuste.get_contexto_empresa(contexto)
        tree = ET.parse(f"plantillas/reporte/{model.accion_Config['reporte_Template']}")
        root = tree.getroot()

        body_template = Template(root.find("body").text.strip())

        cuerpo_html = body_template.render(contexto)

        return cuerpo_html


    def descargar_plantilla_pdf(self,model):
        path_wkhtmltopdf = 'assets/wkhtmltox/bin/wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

        html = self.renderizar_plantilla_xml(model)

        pdf = pdfkit.from_string(html, False,configuration=config)

        ruta = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")],initialfile=f"{model.nombre}.pdf",)
        if ruta:
            with open(ruta, "wb") as f:
                f.write(pdf)
            messagebox.showinfo("Éxito", "Factura descargada.")

    def obtener_plantilla_pdf(self,model):
        path_wkhtmltopdf = 'assets/wkhtmltox/bin/wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

        html = self.renderizar_plantilla_xml(model)

        pdf = pdfkit.from_string(html, False,configuration=config)
        return pdf