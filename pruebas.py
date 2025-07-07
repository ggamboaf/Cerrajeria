import tkinter as tk
from tkinter import filedialog, messagebox
from jinja2 import Environment, FileSystemLoader
import pdfkit
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Configura tu correo
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_USER = "tu_correo@example.com"
EMAIL_PASS = "tu_contraseña"

# Cargar plantilla
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('plantillas/reporte/factura_template.html')

def generar_pdf(contexto):
    path_wkhtmltopdf = 'assets/wkhtmltox/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    html = template.render(contexto)
    pdf_bytes = pdfkit.from_string(html, False,configuration=config)
    return pdf_bytes

def enviar_correo(destinatario, pdf_bytes):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = destinatario
    msg['Subject'] = "Factura de su compra"
    msg.attach(MIMEText("Adjunto encontrará su factura.", 'plain'))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(pdf_bytes)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="factura.pdf"')
    msg.attach(part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.send_message(msg)
    server.quit()

def obtener_contexto():
    return {
    "company": {"logo_url": "https://via.placeholder.com/150"},
    "supplier": {
        "name": "Supplier Name", "number": "123456", "vat": "VAT123456",
        "address": "123 Supplier St.", "city": "Supplier City", "zip": "12345",
        "country": "Supplier Country", "email": "supplier@example.com", "phone": "+1234567890"
    },
    "customer": {
        "name": "Customer Name", "number": "654321", "vat": "VAT654321",
        "address": "456 Customer St.", "city": "Customer City", "zip": "54321",
        "country": "Customer Country"
    },
    "invoice": {
        "date": "2023-01-01", "number": "INV123456",
        "itemsr": [
            {"description": "Product 1", "price": 100.00, "quantity": 2, "vat": 10, "subtotal": 200.00, "total": 220.00},
            {"description": "Product 2", "price": 50.00, "quantity": 1, "vat": 5, "subtotal": 50.00, "total": 52.50}
        ],
        "net_total": 250.00, "vat_total": 22.50, "total": 272.50,
        "notes": "Thank you for your business!"
    },
    "payment": {
        "bank_name": "Bank Name", "sort_code": "00-00-00", "account_number": "12345678"
    }
}

def enviar():
    contexto = obtener_contexto()
    pdf = generar_pdf(contexto)
    enviar_correo(contexto["receptor"]["email"], pdf)
    messagebox.showinfo("Éxito", "Factura enviada por correo.")

def descargar():
    contexto = obtener_contexto()
    pdf = generar_pdf(contexto)
    ruta = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if ruta:
        with open(ruta, "wb") as f:
            f.write(pdf)
        messagebox.showinfo("Éxito", "Factura descargada.")

# Interfaz
root = tk.Tk()
root.title("Generador de Facturas")

def campo(label, row):
    tk.Label(root, text=label).grid(row=row, column=0)
    e = tk.Entry(root)
    e.grid(row=row, column=1)
    return e

emisor_nombre = campo("Emisor Nombre", 0)
emisor_direccion = campo("Emisor Dirección", 1)
emisor_telefono = campo("Emisor Teléfono", 2)
emisor_email = campo("Emisor Email", 3)

receptor_nombre = campo("Receptor Nombre", 4)
receptor_direccion = campo("Receptor Dirección", 5)
receptor_telefono = campo("Receptor Teléfono", 6)
receptor_email = campo("Receptor Email", 7)

factura_numero = campo("Factura N°", 8)
factura_emision = campo("Fecha Emisión", 9)
factura_vencimiento = campo("Fecha Vencimiento", 10)

tk.Button(root, text="Enviar por Correo", command=enviar).grid(row=11, column=0, columnspan=2)
tk.Button(root, text="Descargar PDF", command=descargar).grid(row=12, column=0, columnspan=2)

root.mainloop()
