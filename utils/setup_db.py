from models.base import db, BaseModel
import models
import inspect
from utils.utils import encriptar_password
import json

def obtener_modelos():
    modelos = []
    for nombre in dir(models):
        obj = getattr(models, nombre)
        if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj is not BaseModel:
            modelos.append(obj)
    return modelos

def inicializar_db():
    db.connect()
    db.create_tables(obtener_modelos())

    # Datos por defecto
    default_user = {
        "email": "admin",
        "nombre": "Administrador",
        "cedula": "00000000",
        "password": encriptar_password("admin"),
        "permisos": json.dumps({"admin": True})
    }

    default_Ajuste = [
        {"key": 'color.fondo', "valor": '#F8F9FA'},
        {"key": 'color.frame', "valor": '#FEFEFF'},
        {"key": 'color.btn.1', "valor": '#05d7ff'},
        {"key": 'color.btn.2', "valor": 'BLACK'},
        {"key": 'color.btn.3', "valor": '#65e7ff'},
        {"key": 'color.btn.4', "valor": 'WHITE'},
        {"key": 'img.logo', "valor": 'assets/images/img_login_sing.png'},
        {"key": 'smtp.servidor', "valor": 'smtp.gmail.com'},
        {"key": 'smtp.puerto', "valor": '465'},
        {"key": 'smtp.usuario', "valor": 'algo@gmail.com'},
        {"key": 'smtp.contrasena', "valor": 'AAAAA'},
        {"key": 'empresa.nombre', "valor": 'Empresa S.A'},
        {"key": 'empresa.telefono', "valor": '88888888'},
        {"key": 'empresa.correo', "valor": 'empresa@empresa.com'},
        {"key": 'empresa.direccion', "valor": 'Av. Central 123, Edificio Empresarial Colima, Piso 4, San José, Costa Rica'},
    ]

    default_Seq = [
        {"nombre": 'FacturaCliente', "prefijo": 'FACT', "padding": 4, "ultimo_numero": 0},
        {"nombre": 'OrdenVenta', "prefijo": 'OV', "padding": 4, "ultimo_numero": 0},
        {"nombre": 'FacturaProveedor', "prefijo": 'FACTP', "padding": 4, "ultimo_numero": 0},
        {"nombre": 'OrdenCompra', "prefijo": 'OC', "padding": 4, "ultimo_numero": 0},
    ]

    from models import User, Ajuste, Secuencia

    if not User.select().where(User.email == default_user["email"]).exists():
        User.create(**default_user)

    for ajuste in default_Ajuste:
        if not Ajuste.select().where(Ajuste.key == ajuste["key"]).exists():
            Ajuste.create(**ajuste)

    for seq in default_Seq:
        if not Secuencia.select().where(Secuencia.nombre == seq["nombre"]).exists():
            Secuencia.create(**seq)

    print("Base de datos inicializada dinámicamente con datos por defecto.")

if __name__ == "__main__":
    inicializar_db()
