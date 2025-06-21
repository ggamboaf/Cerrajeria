import json

from peewee import *
from utils.utils import encriptar_password, verificar_password

db = SqliteDatabase('cerrajeria.db')

class Char(CharField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True, **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        super().__init__(*args, **kwargs)

class Auto(AutoField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True, **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        super().__init__(*args, **kwargs)

class Text(TextField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True, **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        super().__init__(*args, **kwargs)

class Float(FloatField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True, **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        super().__init__(*args, **kwargs)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = Auto(mostrar_Tree=False,mostrar_Form=False)
    nombre = Char(mostrar_Tree=True)
    email = Char(unique=True,mostrar_Tree=True)
    cedula = Char(mostrar_Tree=True)
    password = Char(mostrar_Tree=False,mostrar_Form=False)
    codigo = Char(mostrar_Tree=False,mostrar_Form=False,null=True)
    permisos =  Text(default='{}',mostrar_Tree=False,mostrar_Form=True)

class ClienteProveedor(BaseModel):
    descripcion = "Cliente"
    tipo_choices = (
        ('Cliente', 'Cliente'),
        ('Proveedor', 'Proveedor'),
    )
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    tipo = Char(choices=tipo_choices,help_text="Tipo",mostrar_Tree=False,mostrar_Form=False)
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True)
    cedula = Char(help_text="Identificación",mostrar_Tree=True,mostrar_Form=True)
    email = Char(help_text="Correo",mostrar_Tree=True,mostrar_Form=True)
    telfono = Char(help_text="Teléfono",mostrar_Tree=True,mostrar_Form=True)

    @classmethod
    def crear_actualizar_desde_dict(cls, datos):
        """
        Crea o actualiza un registro a partir de un diccionario.
        Convierte automáticamente los valores a sus tipos correctos.
        """
        campos = cls._meta.fields

        def convertir_valor(campo, valor):
            tipo = type(campos[campo])
            if tipo == IntegerField:
                return int(valor)
            elif tipo == FloatField:
                return float(valor)
            elif tipo == BooleanField:
                return valor.lower() in ("1", "true", "yes", "on")
            else:
                return valor  # CharField, TextField, etc.

        datos_convertidos = {}
        for campo, valor in datos.items():
            if campo in campos and valor != "":
                try:
                    datos_convertidos[campo] = convertir_valor(campo, valor)
                except Exception as e:
                    raise ValueError(f"Error al convertir el campo '{campo}': {e}")

        if 'id' in datos_convertidos:
            try:
                instancia = cls.get_by_id(datos_convertidos['id'])
                for campo, valor in datos_convertidos.items():
                    if campo != 'id':
                        setattr(instancia, campo, valor)
                instancia.save()
                return instancia
            except cls.DoesNotExist:
                datos_convertidos.pop('id')
                return cls.create(**datos_convertidos)
        else:
            return cls.create(**datos_convertidos)

    @classmethod
    def obtener_columnas_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for ClienteProveedor in cls._meta.sorted_fields:
            datos.append(ClienteProveedor.name)
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls,tipo):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select().where(cls.tipo == tipo)
        datos = []
        for ClienteProveedor in registros:
            datos.append((ClienteProveedor.id, ClienteProveedor.tipo, ClienteProveedor.nombre,ClienteProveedor.cedula,ClienteProveedor.email,ClienteProveedor.telfono))
        return datos

class Impuesto(BaseModel):
    tipo_choices = (
        ('Venta', 'Venta'),
        ('Compra', 'Compra'),
    )
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True)
    tipo = Char(choices=tipo_choices,help_text="Tipo",mostrar_Tree=False,mostrar_Form=False)
    importe = Float(help_text="Importe",mostrar_Tree=True,mostrar_Form=True)

    @classmethod
    def crear_actualizar_desde_dict(cls, datos):
        """
        Crea o actualiza un registro a partir de un diccionario.
        Convierte automáticamente los valores a sus tipos correctos.
        """
        campos = cls._meta.fields

        def convertir_valor(campo, valor):
            tipo = type(campos[campo])
            if tipo == IntegerField:
                return int(valor)
            elif tipo == FloatField:
                return float(valor)
            elif tipo == BooleanField:
                return valor.lower() in ("1", "true", "yes", "on")
            else:
                return valor  # CharField, TextField, etc.

        datos_convertidos = {}
        for campo, valor in datos.items():
            if campo in campos and valor != "":
                try:
                    datos_convertidos[campo] = convertir_valor(campo, valor)
                except Exception as e:
                    raise ValueError(f"Error al convertir el campo '{campo}': {e}")

        if 'id' in datos_convertidos:
            try:
                instancia = cls.get_by_id(datos_convertidos['id'])
                for campo, valor in datos_convertidos.items():
                    if campo != 'id':
                        setattr(instancia, campo, valor)
                instancia.save()
                return instancia
            except cls.DoesNotExist:
                datos_convertidos.pop('id')
                return cls.create(**datos_convertidos)
        else:
            return cls.create(**datos_convertidos)

    @classmethod
    def obtener_columnas_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for registro in cls._meta.sorted_fields:
            datos.append(registro.name)
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls,tipo):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select().where(cls.tipo == tipo)
        datos = []
        for registro in registros:
            datos.append((registro.id, registro.nombre, registro.tipo,registro.importe))
        return datos

class Producto(BaseModel):
    tipo_choices = (
        ('Consumible', 'Cliente'),
        ('Servicio', 'Proveedor'),
    )
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True)
    tipo = Char(choices=tipo_choices,help_text="Tipo",mostrar_Tree=True,mostrar_Form=True)
    precio_Venta = Float(help_text="Precio de venta",mostrar_Tree=True,mostrar_Form=True)
    precio_Compra = Float(help_text="Precio de compra",mostrar_Tree=True,mostrar_Form=True)
    telfono = Char(help_text="Teléfono",mostrar_Tree=True,mostrar_Form=True)

    @classmethod
    def crear_actualizar_desde_dict(cls, datos):
        """
        Crea o actualiza un registro a partir de un diccionario.
        Convierte automáticamente los valores a sus tipos correctos.
        """
        campos = cls._meta.fields

        def convertir_valor(campo, valor):
            tipo = type(campos[campo])
            if tipo == IntegerField:
                return int(valor)
            elif tipo == FloatField:
                return float(valor)
            elif tipo == BooleanField:
                return valor.lower() in ("1", "true", "yes", "on")
            else:
                return valor  # CharField, TextField, etc.

        datos_convertidos = {}
        for campo, valor in datos.items():
            if campo in campos and valor != "":
                try:
                    datos_convertidos[campo] = convertir_valor(campo, valor)
                except Exception as e:
                    raise ValueError(f"Error al convertir el campo '{campo}': {e}")

        if 'id' in datos_convertidos:
            try:
                instancia = cls.get_by_id(datos_convertidos['id'])
                for campo, valor in datos_convertidos.items():
                    if campo != 'id':
                        setattr(instancia, campo, valor)
                instancia.save()
                return instancia
            except cls.DoesNotExist:
                datos_convertidos.pop('id')
                return cls.create(**datos_convertidos)
        else:
            return cls.create(**datos_convertidos)

    @classmethod
    def obtener_columnas_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for ClienteProveedor in cls._meta.sorted_fields:
            datos.append(ClienteProveedor.name)
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select().where(cls.tipo == "Cliente")
        datos = []
        for ClienteProveedor in registros:
            datos.append((ClienteProveedor.id, ClienteProveedor.tipo, ClienteProveedor.nombre,ClienteProveedor.cedula,ClienteProveedor.email,ClienteProveedor.telfono))
        return datos


class Ajuste(BaseModel):
    id = Auto(mostrar_Tree=False, mostrar_Form=False, help_text="ID")
    key = Char(help_text="Nombre", mostrar_Tree=True, mostrar_Form=True)
    valor = Char(help_text="Valor", mostrar_Tree=True, mostrar_Form=True,null=True)


db.connect()
db.create_tables([User,ClienteProveedor,Impuesto,Ajuste])

default_user = {
    "email": "admin",
    "nombre": "Administrador",
    "cedula": "00000000",
    "password": encriptar_password("admin"),
    "permisos": json.dumps({"admin": True})
}

default_Ajuste = [
    {
        "key": 'color.fondo',
        "valor": '#F8F9FA',
    },
    {
        "key": 'color.frame',
        "valor": '#FEFEFF',
    },
    {
        "key": 'color.btn.1',
        "valor": '#05d7ff',
    },
    {
        "key": 'color.btn.2',
        "valor": 'BLACK',
    },
    {
        "key": 'color.btn.3',
        "valor": '#65e7ff',
    },
    {
        "key": 'color.btn.4',
        "valor": 'WHITE',
    },
    {
        "key": 'img.logo',
        "valor": 'assets/images/img_login_sing.png',
    },
    {
        "key": 'smtp.servidor',
        "valor": 'smtp.gmail.com',
    },
    {
        "key": 'smtp.puerto',
        "valor": '465',
    },
    {
        "key": 'smtp.usuario',
        "valor": 'algo@gmail.com',
    },
    {
        "key": 'smtp.contrasena',
        "valor": 'AAAAA',
    },

]

if not User.select().where(User.email == default_user["email"]).exists():
    User.create(**default_user)

for ajsute in default_Ajuste:
    if not Ajuste.select().where(Ajuste.key == ajsute["key"]).exists():
        Ajuste.create(**ajsute)
