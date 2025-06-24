import json

from peewee import *
from utils.utils import encriptar_password, verificar_password

db = SqliteDatabase('cerrajeria.db')

class Char(CharField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="", **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.nombre_default = nombre_default
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

class ForeignKey(ForeignKeyField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,campo_busqueda="", **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.campo_busqueda = campo_busqueda
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

class Cliente(BaseModel):
    plantilla_Name = "Plantilla Clientes.xlsx"
    descripcion = "Cliente"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
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
    def obtener_datos_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select()
        datos = []
        for registro in registros:
            datos.append((registro.id,registro.nombre,registro.cedula,registro.email,registro.telfono))
        return datos

class Proveedor(BaseModel):
    plantilla_Name = "Plantilla Proveedores.xlsx"
    descripcion = "Proveedor"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
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
        for registro in cls._meta.sorted_fields:
            datos.append(registro.name)
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select()
        datos = []
        for registro in registros:
            datos.append((registro.id, registro.nombre,registro.cedula,registro.email,registro.telfono))
        return datos

class ImpuestoVenta(BaseModel):
    descripcion = "Impuesto de venta"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,nombre_default="Impuesto")
    importe = Float(help_text="Importe (%)",mostrar_Tree=True,mostrar_Form=True)

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
    def obtener_datos_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select()
        datos = []
        for registro in registros:
            datos.append((registro.id, registro.nombre,registro.importe))
        return datos

    @classmethod
    def obtener_datos_para_atucompleteview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select()
        datos = []
        for model in registros:
            datos.append((model.id,model.nombre))
        return datos

class ImpuestoCompra(BaseModel):
    descripcion = "Impuesto de compra"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,nombre_default="Impuesto")
    importe = Float(help_text="Importe (%)",mostrar_Tree=True,mostrar_Form=True)

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
    def obtener_datos_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select()
        datos = []
        for registro in registros:
            datos.append((registro.id, registro.nombre,registro.importe))
        return datos

    @classmethod
    def obtener_datos_para_atucompleteview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select()
        datos = []
        for model in registros:
            datos.append((model.id,model.nombre))
        return datos

class Producto(BaseModel):
    plantilla_Name = "Plantilla Productos.xlsx"
    descripcion = "Producto"
    tipo_choices = (
        ('Producto', 'Producto'),
        ('Servicio', 'Servicio'),
    )
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True)
    tipo = Char(choices=tipo_choices,help_text="Tipo",mostrar_Tree=True,mostrar_Form=True)
    costo = Float(help_text="Costo", mostrar_Tree=True, mostrar_Form=True)
    porcentaje_ganancia = Float(help_text="Porcentaje de Ganancia (%)",mostrar_Tree=True,mostrar_Form=True)
    precio_Venta = Float(help_text="Precio de venta",mostrar_Tree=True,mostrar_Form=True)
    precio_Compra = Float(help_text="Precio de compra",mostrar_Tree=True,mostrar_Form=True)
    impuesto_Venta = ForeignKey(ImpuestoVenta,backref='Venta',help_text="Impuesto de venta",mostrar_Tree=True,mostrar_Form=True,campo_busqueda="importe")
    impuesto_Compra = ForeignKey(ImpuestoCompra,backref='Compra',help_text="Impuesto de compra",mostrar_Tree=True,mostrar_Form=True,campo_busqueda="importe")


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
        for model in cls._meta.sorted_fields:
            datos.append(model.name)
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select()
        datos = []
        for model in registros:
            datos.append(
                (
                    model.id,
                    model.nombre,
                    model.tipo,
                    model.costo,
                    model.porcentaje_ganancia,
                    model.precio_Venta,
                    model.precio_Compra,
                    model.impuesto_Venta.nombre,
                    model.impuesto_Compra.nombre,
                )
            )
        return datos

    @classmethod
    def obtener_datos_para_atucompleteview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        registros = cls.select()
        datos = []
        for model in registros:
            datos.append(
                (
                    model.id,
                    model.nombre,
                    model.tipo,
                    model.costo,
                    model.precio_Venta,
                    model.precio_Compra,
                    model.impuesto_Venta,
                    model.impuesto_Compra,
                )
            )
        return datos


class Ajuste(BaseModel):
    id = Auto(mostrar_Tree=False, mostrar_Form=False, help_text="ID")
    key = Char(help_text="Nombre", mostrar_Tree=True, mostrar_Form=True)
    valor = Char(help_text="Valor", mostrar_Tree=True, mostrar_Form=True,null=True)


db.connect()
db.create_tables(
    [
        User,
        Cliente,
        Proveedor,
        Producto,
        ImpuestoVenta,
        ImpuestoCompra,
        Ajuste,
    ])

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
