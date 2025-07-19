import calendar
import decimal
import inspect
import random
import string
import datetime

from babel.numbers import format_currency
from peewee import *
from peewee import fn
from decimal import Decimal
import pandas as pd
from utils.utils import encriptar_password


db = SqliteDatabase('cerrajeria.db')

class Char(CharField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class Auto(AutoField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class Text(TextField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class Float(FloatField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class Decimal(DecimalField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class ForeignKey(ForeignKeyField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class Boolean(BooleanField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class Date(DateField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class Integer(IntegerField):
    def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
        self.mostrar_Tree = mostrar_Tree
        self.mostrar_Form = mostrar_Form
        self.lectura = lectura
        self.nombre_default = nombre_default
        self.numero_Grupo = numero_Grupo
        self.posicion = posicion
        self.ochange = ochange
        self.valor_maximo = valor_maximo
        self.campo_busqueda = campo_busqueda
        self.required = required
        self.exportar = exportar
        super().__init__(*args, **kwargs)

class BaseModel(Model):
    class Meta:
        database = db

class Modelo(BaseModel):
    descripcion = "Permisos"
    grupo_nombres = ['Información general', 'Permisos']
    cant_grupo = 0
    accion_Config = {
        'reporte': False,
        'crear_Modelo': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    modelo = Char(help_text="Modelo",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    menu_root_index = Integer(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    menu_root_nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    menu_parent_index = Integer(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    menu_parent_nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    menu_index = Integer(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    menu_nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    icon_path = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True,default="")

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

    @classmethod
    def obtener_datos_menu(cls,usuario):
        usuarioPermisos = None
        if not usuario.admin:
            usuarioPermisos = UserPermisos.select(UserPermisos.modelo_id).where(UserPermisos.usuario_id == usuario.id and UserPermisos.lectura == True)
            usuarioPermisos = [permiso.modelo_id.modelo for permiso in usuarioPermisos]
        else:
            usuarioPermisos =  cls.select(cls.modelo)
            usuarioPermisos =  [permiso.modelo for permiso in usuarioPermisos]
        dic = {}
        menu_Principal = cls.select(cls.menu_root_nombre,cls.icon_path).where((cls.menu_root_nombre != "") & (cls.modelo.in_(usuarioPermisos))).order_by(cls.menu_root_index).distinct()
        dic['menu_Principal'] = {record.menu_root_nombre: record.icon_path for record in menu_Principal}
        dic['menu_Parent'] = dic['menu_Principal'].copy()
        for campo,valor in dic['menu_Parent'].items():
            menus_parents = cls.select(cls.menu_parent_nombre).where((cls.menu_root_nombre == campo) & (cls.modelo.in_(usuarioPermisos))).order_by(cls.menu_parent_index).distinct()
            menus_parents =  [menu.menu_parent_nombre for menu in menus_parents]
            dic['menu_Parent'][campo] = {item: None for item in menus_parents}
            for campo_menu, valor_menu in dic['menu_Parent'][campo].items():
                menus = cls.select(cls.menu_nombre).where((cls.menu_parent_nombre == campo_menu) & (cls.modelo.in_(usuarioPermisos))).order_by( cls.menu_index).distinct()
                dic['menu_Parent'][campo][campo_menu] = [menu.menu_nombre for menu in menus]
        return dic

    @classmethod
    def obtener_modelo(cls,menu):
        models = cls.select(cls.modelo).where(cls.menu_nombre == menu).distinct()
        for model in models:
            return globals()[model.modelo]

    @classmethod
    def obtener_modelo_nombre(cls,modelo):
        return globals()[modelo]


    @classmethod
    def obtener_dashboard(cls):
        modelos = [
            modelo_clase.dashboard for m in cls.select(cls.modelo).distinct()
            if (modelo_clase := globals().get(m.modelo)) and isinstance(getattr(modelo_clase, 'dashboard', None),dict)
        ]
        return sorted(modelos, key=lambda x: x["index"])


class User(BaseModel):
    descripcion = "Usuarios"
    grupo_nombres = ['Información general', 'Información general','Permisos']
    cant_grupo = 2
    models_Rels = ['UserPermisos']
    accion_Config = {
        'reporte': False,
        'crear_Modelo': False,
        'correo_Template': "envio_credenciales.xml",
        'otras_acciones':[
            {
                'accion_Nombre': 'Enviar credenciales',
                'metodo': 'enviar_credenciales',
            }
        ]
    }
    menu_root_index = 3
    menu_root_nombre = 'Configuración'
    menu_parent_index = 0
    menu_parent_nombre = 'Configuración'
    menu_index = 1
    menu_nombre = "Usuarios"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    email = Char(help_text="Correo",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=2,exportar=True)
    cedula = Char(help_text="Identificación",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0,exportar=True)
    puesto = Char(help_text="Puesto",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=1,exportar=True)
    admin = Boolean(default=False, help_text="Administrador", mostrar_Tree=True, mostrar_Form=True, numero_Grupo=1,posicion=2, exportar=True)
    password = Char(help_text="Contraseña",mostrar_Tree=False,mostrar_Form=False,numero_Grupo=0,posicion=0,exportar=False)
    codigo = Char(help_text="Código",null=True,mostrar_Tree=False,mostrar_Form=False,numero_Grupo=0,posicion=0,exportar=False)
    nuevo = Boolean(default=False, help_text="Nuevo", mostrar_Tree=False, mostrar_Form=False)

    @classmethod
    def crear_actualizar_desde_dict(cls, datos):
        campos = cls._meta.fields
        instancia = None
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
                instancia = cls.create(**datos_convertidos)
        else:
            instancia = cls.create(**datos_convertidos)

        return instancia

    def enviar_credenciales(self):
        from  utils.enviar_correo import EnviarCorreo
        self.password = self.generar_contrasena()
        EnviarCorreo.enviar_correo(EnviarCorreo(), model=self)
        self.password = encriptar_password(self.password)
        self.nuevo = True
        self.save()

    def get_contexto(self):
        return {
            'usuario': {
                'nombre': self.nombre,
                'email': self.email,
                'password': self.password,
            }
        }

    def cambio_contrasena(self):
        self.password = encriptar_password(self.password)
        self.nuevo = False
        self.save()
    def generar_contrasena(self):
        letras = random.choices(string.ascii_letters, k=3)  # Letras aleatorias (mayúsculas y minúsculas)
        numeros = random.choices(string.digits, k=4)  # Dígitos aleatorios
        combinacion = letras + numeros
        random.shuffle(combinacion)  # Mezclar el orden
        return ''.join(combinacion)

    @classmethod
    def obtener_datos_para_treeview(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def eliminar_datos_models_rel(cls,id):
        datos = []
        if hasattr(cls, "models_Rels"):
            for model_name in cls.models_Rels:
                model = globals()[model_name]
                descp = {
                    'tab_Name': model.descripcion,
                    'model': model,
                    'model_name': model_name
                }
                campo_relacion = cls.obtener_campo_rel(model)
                registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
                dataTupla = []
                for registro in registros:
                    registro.delete_instance()

    @classmethod
    def obtener_datos_para_exportar(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if field.exportar:
                if isinstance(field, ForeignKey):
                    datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
                else:
                    datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]

        return datos

    @classmethod
    def obtener_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            records = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            vals = {}
            for field in model._meta.sorted_fields:
                if isinstance(field, ForeignKey):
                    vals[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records] if isinstance(id,int) else []
                elif isinstance(field, Boolean):
                    vals[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records] if isinstance(id,int) else []
                else:
                    vals[f"{field.help_text}"] = [getattr(record, field.name) for record in records] if isinstance(id,int) else []
            descp['datos'] = vals
            datos.append(descp)
        return datos

    @classmethod
    def obtener_campo_rel(cls,modelrel):
        campo_relacion = None
        for field_name, field_obj in modelrel._meta.fields.items():
            if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
                campo_relacion = getattr(modelrel, field_name).name
                break
        return campo_relacion

    def get_permiso(self,modelo):
        if self.admin:
            return {
                "lectura": True,
                "escritura": True,
                "creacion": True,
                "eliminacion": True,
            }
        else:
            if not isinstance(modelo, type):
                modelo = modelo.__class__
            modelo = modelo.__name__
            modelo = Modelo.get(Modelo.modelo == modelo)
            permiso = UserPermisos.get_or_none((UserPermisos.usuario_id == self.id) & (UserPermisos.modelo_id == modelo.id))
            if permiso:
                return dict(permiso.__data__)
            else:
                return {
                    "lectura": False,
                    "escritura": False,
                    "creacion": False,
                    "eliminacion": False,
                }

class UserPermisos(BaseModel):
    descripcion = "Permisos"
    grupo_nombres = ['Información general','Permisos']
    cant_grupo = 2
    accion_Config = {
        'reporte': False,
        'crear_Modelo': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    usuario_id = ForeignKey(User, backref='Usuario', help_text="Usuario", mostrar_Tree=False, mostrar_Form=False)
    modelo_id = ForeignKey(Modelo, backref='Modelo', help_text="Modelo", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,exportar=True)
    lectura = Boolean(default=False, help_text="Lectura", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,exportar=True)
    escritura = Boolean(default=False, help_text="Escritura", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,exportar=True)
    creacion = Boolean(default=False, help_text="Creación", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=2,exportar=True)
    eliminacion = Boolean(default=False, help_text="Eliminación", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=3,exportar=True)

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
    def obtener_datos_para_treeview(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def eliminar_datos_models_rel(cls,id):
        datos = []
        if hasattr(cls, "models_Rels"):
            for model_name in cls.models_Rels:
                model = globals()[model_name]
                descp = {
                    'tab_Name': model.descripcion,
                    'model': model,
                    'model_name': model_name
                }
                campo_relacion = cls.obtener_campo_rel(model)
                registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
                dataTupla = []
                for registro in registros:
                    registro.delete_instance()

    @classmethod
    def obtener_datos_para_exportar(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if field.exportar:
                if isinstance(field, ForeignKey):
                    datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
                else:
                    datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]

        return datos

class Cliente(BaseModel):
    plantilla_Name = "Plantilla Clientes.xlsx"
    xlsx_Name = "Clientes.xlsx"
    descripcion = "Cliente"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
    accion_Config = {
        'reporte': False,
        'crear_Modelo': False,
    }
    menu_root_index = 2
    menu_root_nombre = 'Contabilidad'
    menu_parent_index = 0
    menu_parent_nombre = 'Clientes'
    menu_index = 2
    menu_nombre = "Clientes"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0,exportar=True)
    cedula = Char(help_text="Identificación",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    email = Char(help_text="Correo",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0,exportar=True)
    telfono = Char(help_text="Teléfono",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=1,exportar=True)

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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def eliminar_datos_models_rel(cls,id):
        datos = []
        if hasattr(cls, "models_Rels"):
            for model_name in cls.models_Rels:
                model = globals()[model_name]
                descp = {
                    'tab_Name': model.descripcion,
                    'model': model,
                    'model_name': model_name
                }
                campo_relacion = cls.obtener_campo_rel(model)
                registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
                dataTupla = []
                for registro in registros:
                    registro.delete_instance()

    @classmethod
    def obtener_datos_para_exportar(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if field.exportar:
                if isinstance(field, ForeignKey):
                    datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
                else:
                    datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]

        return datos

class Proveedor(BaseModel):
    plantilla_Name = "Plantilla Provedores.xlsx"
    xlsx_Name = "Provedores.xlsx"
    descripcion = "Proveedor"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
    accion_Config = {
        'reporte': False,
        'crear_Modelo': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0,exportar=True)
    cedula = Char(help_text="Identificación",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    email = Char(help_text="Correo",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0,exportar=True)
    telfono = Char(help_text="Teléfono",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=1,exportar=True)
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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


        return datos

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

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

    @classmethod
    def obtener_datos_para_exportar(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if field.exportar:
                if isinstance(field, ForeignKey):
                    datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
                else:
                    datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]

        return datos

class ImpuestoVenta(BaseModel):
    descripcion = "Impuesto de venta"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
    accion_Config = {
        'reporte': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,nombre_default="Impuesto",numero_Grupo=0,posicion=0)
    importe = Float(help_text="Importe (%)",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0)

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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def obtener_datos_para_exportar(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if field.exportar:
                if isinstance(field, ForeignKey):
                    datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
                else:
                    datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]

        return datos

class ImpuestoCompra(BaseModel):
    descripcion = "Impuesto de compra"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
    accion_Config = {
        'reporte': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,nombre_default="Impuesto",numero_Grupo=0,posicion=0)
    importe = Float(help_text="Importe (%)",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0)

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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def obtener_datos_para_exportar(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if field.exportar:
                if isinstance(field, ForeignKey):
                    datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
                else:
                    datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]

        return datos

class Producto(BaseModel):
    plantilla_Name = "Plantilla Productos.xlsx"
    xlsx_Name = "Productos.xlsx"
    descripcion = "Producto"
    grupo_nombres = ['Información general','Información financiera']
    cant_grupo = 2
    dashboard = {
        'index': 0,
        'index_nombre': 'Productos',
        'modelo': 'Producto',
        'tipo': [
            {
                'titulo': 'Existencias de productos',
                'filtro': True,
                'filtro_conf': {
                    'tipo': 'valor_unico',
                    'entrada': 'entry',
                    'valores_defecto': 'obtener_productos_menor_valor',
                    'tipo_valor': float,
                    'textos': ['Productos menores a'],
                },
                'grafico':False,
                'grafico_conf': {},
                'tabla':True,
                'tabla_conf': {
                    'metodo': 'obtener_productos_menor',
                    'redirige': True,
                },
            },
            {
                'titulo': 'Venta de productos',
                'filtro': True,
                'filtro_conf': {
                    'tipo': 'rango',
                    'entrada': 'date',
                    'valores_defecto': 'obtener_venta_valor',
                    'tipo_valor': datetime.date,
                    'textos': ['Desde', 'Hasta'],
                },
                'grafico': True,
                'grafico_conf': {
                    'tipo': 'barn',
                    'metodo': 'obtener_venta_grafico'
                },
                'tabla': True,
                'tabla_conf': {
                    'metodo': 'obtener_venta_tabla',
                    'redirige': True,
                },
            }
        ]
    }
    tipo_choices = (
        ('Producto', 'Producto'),
        ('Servicio', 'Servicio'),
    )
    accion_Config = {
        'reporte': False,
    }
    menu_root_index = 2
    menu_root_nombre = 'Contabilidad'
    menu_parent_index = 0
    menu_parent_nombre = 'Clientes'
    menu_index = 1
    menu_nombre = "Productos"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0,exportar=True)
    tipo = Char(choices=tipo_choices,help_text="Tipo",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
    existencias = Float(help_text="Existencias", null=True,mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,exportar=True)
    costo = Decimal(help_text="Costo", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1, decimal_places=2,exportar=True)
    porcentaje_ganancia = Float(help_text="Porcentaje de Ganancia (%)",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=2,exportar=True)
    precio_Venta = Decimal(help_text="Precio de venta",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=3, decimal_places=2,exportar=True)
    precio_Compra = Decimal(help_text="Precio de compra",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=4, decimal_places=2,exportar=True)
    impuesto_Venta = ForeignKey(ImpuestoVenta,backref='Venta',campo_busqueda="importe",help_text="Impuesto de venta",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,exportar=True)
    impuesto_Compra = ForeignKey(ImpuestoCompra,backref='Compra',campo_busqueda="importe",help_text="Impuesto de compra",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=3,null=True,exportar=True)


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
            elif tipo == Float:
                return float(valor)
            elif tipo == Decimal:
                return round(decimal.Decimal(valor),campos[campo].decimal_places)
            elif tipo == Boolean:
                return valor.lower() in ("1", "true", "yes", "on")
            else:
                return valor

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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def obtener_datos_para_exportar(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if field.exportar:
                if isinstance(field, ForeignKey):
                    datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
                else:
                    datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]

        return datos

    @classmethod
    def obtener_productos_menor_valor(cls):
        return [5]

    @classmethod
    def obtener_venta_valor(cls):
        return [False,False]

    @classmethod
    def obtener_productos_menor(cls,valores_defecto=False):
        if not valores_defecto:
            valores_defecto = 5
        datos = {}
        productos = cls.select(cls.id,cls.nombre,cls.existencias).where(cls.existencias < valores_defecto)
        datos['MODEL'] = ['Producto' for producto in productos]
        datos['ID'] = [producto.id for producto in productos]
        datos['Producto'] = [producto.nombre for producto in productos]
        datos['Existencias'] = [producto.existencias for producto in productos]

        return datos

    @classmethod
    def obtener_venta_tabla(cls,desde=False,hasta=False):
        datos = {}
        if desde and hasta:
            query = (FacturaClienteLine
                     .select(Producto.id.alias('ID'),Producto.nombre.alias('Producto'), fn.SUM(FacturaClienteLine.cantidad).alias('Total'))
                     .join(Producto)
                     .switch(FacturaClienteLine)
                     .join(FacturaCliente)
                     .where(FacturaCliente.fecha.between(desde, hasta))
                     .group_by(FacturaClienteLine.producto))
        else:
            query = (FacturaClienteLine
                     .select(Producto.id.alias('ID'),Producto.nombre.alias('Producto'), fn.SUM(FacturaClienteLine.cantidad).alias('Total'))
                     .join(Producto)
                     .group_by(FacturaClienteLine.producto))

        if query.count() > 0:
            lista_productos = list(query.dicts())
            datos['MODEL'] = ['Producto' for producto in lista_productos]
            datos['ID'] = [producto["ID"] for producto in lista_productos]
            datos['Producto'] = [producto["Producto"] for producto in lista_productos]
            datos['Total'] = [producto["Total"] for producto in lista_productos]
            df = pd.DataFrame(datos)
            df_ordenado = df.sort_values(by='Total', ascending=False).reset_index(drop=True)
            percentil_33 = df_ordenado['Total'].quantile(0.33)
            percentil_66 = df_ordenado['Total'].quantile(0.66)

            def clasificar(cantidad):
                if cantidad >= percentil_66:
                    return 'Más vendidos'
                elif cantidad >= percentil_33:
                    return 'Ventas medias'
                else:
                    return 'Menos vendidos'

            df_ordenado['Clasificación'] = df_ordenado['Total'].apply(clasificar)
            return df_ordenado
        else:
            return {}

    @classmethod
    def obtener_venta_grafico(cls,desde=False,hasta=False):
        if desde and hasta:
            query = (FacturaClienteLine
                     .select(Producto.nombre.alias('Producto'), fn.SUM(FacturaClienteLine.cantidad).alias('Total'))
                     .join(Producto)
                     .switch(FacturaClienteLine)
                     .join(FacturaCliente)
                     .where(FacturaCliente.fecha.between(desde, hasta))
                     .group_by(FacturaClienteLine.producto))
        else:
            query = (FacturaClienteLine
                     .select(Producto.nombre.alias('Producto'), fn.SUM(FacturaClienteLine.cantidad).alias('Total'))
                     .join(Producto)
                     .group_by(FacturaClienteLine.producto))
        if query.count() > 0:
            lista_productos = list(query.dicts())
            x = [producto["Producto"] for producto in lista_productos]
            y = [producto["Total"] for producto in lista_productos]
            return x,y
        else:
            return [],[]

    def obtener_valor_maximo(self):
        totalOrdenVenta = 0
        totalOrdenCompra = 0
        ordenVenta = OrdenVentaLine.select().where(OrdenVentaLine.producto == self.id)
        ordenCompra = OrdenCompraLine.select().where(OrdenCompraLine.producto == self.id)

        if len(ordenVenta) > 1:
            totalOrdenVenta = sum(f.cantidad for f in ordenVenta if f.cantidad is not None)

        if len(ordenCompra) > 0:
            totalOrdenCompra = sum(f.cantidad for f in ordenCompra if f.cantidad is not None)

        return totalOrdenCompra - totalOrdenVenta

class OrdenVenta(BaseModel):
    descripcion = "Orden de venta"
    defalult_name = "FACTC #"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
    dashboard = {
        'index': 1,
        'index_nombre': 'Ordenes de venta',
        'modelo': 'OrdenVenta',
        'tipo': [
            {
                'titulo': 'Ordenes de venta sin facturar',
                'filtro': True,
                'filtro_conf': {
                    'tipo': 'rango',
                    'entrada': 'date',
                    'tipo_valor': datetime.date,
                    'valores_defecto': 'obtener_ordenes_sin_factura_valor',
                    'textos': ['Desde','Hasta'],
                },
                'grafico':False,
                'grafico_conf': {},
                'tabla':True,
                'tabla_conf': {
                    'metodo': 'obtener_ordenes_sin_factura',
                    'redirige': True,
                },
            },
            {
                'titulo': 'Utilidad ordenes de venta',
                'filtro': True,
                'filtro_conf': {
                    'tipo': 'rango',
                    'entrada': 'date',
                    'tipo_valor': datetime.date,
                    'valores_defecto': 'obtener_ordenes_sin_factura_valor',
                    'textos': ['Desde', 'Hasta'],
                },
                'grafico': True,
                'grafico_conf': {
                    'tipo': 'plot',
                    'metodo': 'obtener_venta_grafico'
                },
                'tabla': True,
                'tabla_conf': {
                    'metodo': 'obtener_venta_tabla',
                    'redirige': False,
                },
            },
        ]
    }
    auto_Guardar = True
    models_Rels = ['OrdenVentaLine']
    accion_Config = {
        'reporte': True,
        'reporte_Template': "factura_template.xml",
        'correo_Template': "correo_reporte.xml",
        'reporte_Correo': True,
        'reporte_CorreoDescripcion': "Enviar factura al cliente",
        'reporte_Descargar': True,
        'reporte_DescargarDescripcion': "Descargar factura",
        'crear_Modelo': True,
        'crear_Modelo_Nombre': "FacturaCliente",
        'crear_Modelo_Descripcion': " Crear Factura de Cliente",
    }
    menu_root_index = 0
    menu_root_nombre = 'Ventas'
    menu_parent_index = 0
    menu_parent_nombre = 'Ventas'
    menu_index = 0
    menu_nombre = "Orden de venta"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0)
    terminada = Boolean(default=False,help_text="Terminada",mostrar_Tree=False,mostrar_Form=False)
    cliente = ForeignKey(Cliente,null=True,required=True, backref='Cliente', help_text="Cliente", mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1)
    fecha = Date(help_text="Fecha",default=datetime.date.today,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=0,posicion=2)
    subtoal = Float(help_text="Subtotal",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=0,default=0)
    descuento = Float(help_text="Descuento",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=1,default=0)
    impuesto = Float(help_text="Impuesto",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=2,default=0)
    total = Float(help_text="Total",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=3,default=0)
    total_Adeudado = Float(help_text="Total adeudado",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=4,default=0)

    @classmethod
    def crear_actualizar_desde_dict(cls, datos={}):
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
                seq = Secuencia.siguiente_valor(cls.__name__)
                if seq:
                    datos_convertidos['nombre'] = seq
                return cls.create(**datos_convertidos)
        else:
            seq = Secuencia.siguiente_valor(cls.__name__)
            if seq:
                datos_convertidos['nombre'] = seq
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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre if getattr(record, field.name) is not None else "" for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            records = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            vals = {}
            for field in model._meta.sorted_fields:
                if isinstance(field, ForeignKey):
                    vals[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records] if isinstance(id,int) else []
                elif isinstance(field, Boolean):
                    vals[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records] if isinstance(id,int) else []
                else:
                    vals[f"{field.help_text}"] = [getattr(record, field.name) for record in records] if isinstance(id,int) else []
            descp['datos'] = vals
            datos.append(descp)
        return datos

    @classmethod
    def eliminar_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            dataTupla = []
            for registro in registros:
                registro.delete_instance()

    @classmethod
    def obtener_campo_rel(cls,modelrel):
        campo_relacion = None
        for field_name, field_obj in modelrel._meta.fields.items():
            if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
                campo_relacion = getattr(modelrel, field_name).name
                break
        return campo_relacion

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        model.get_totales()
        return model

    @classmethod
    def obtener_ordenes_sin_factura_valor(cls):
        today = datetime.date.today()
        first_day = today.replace(day=1)
        last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])
        return first_day, last_day

    @classmethod
    def obtener_ordenes_sin_factura(cls,desde=False,hasta=False):
        datos = {}
        ordenes_ids = [id for (id,) in cls.select(cls.id).tuples()]
        ordenesFactura_ids = [id for (id,) in FacturaCliente.select(FacturaCliente.ordenventa_id).tuples()]
        ids = list(set(ordenes_ids) - set(ordenesFactura_ids))
        ordenes = cls.select(cls.id,cls.cliente,cls.nombre,cls.fecha).where(cls.id.in_(ids))
        datos['MODEL'] = ['OrdenVenta' for orden in ordenes]
        datos['ID'] = [orden.id for orden in ordenes]
        datos['Nombre'] = [orden.nombre   for orden in ordenes]
        datos['Cliente'] = [orden.cliente.nombre if orden.cliente is not None else "N/A" for orden in ordenes]
        datos['Fecha'] = [orden.fecha for orden in ordenes]
        return datos

    @classmethod
    def obtener_venta_tabla(cls,desde=False,hasta=False):
        datos = {}
        if desde and hasta:
            query = (OrdenVenta
                     .select(OrdenVenta.id.alias('ID'),OrdenVenta.fecha.alias('Fecha'), fn.SUM(OrdenVenta.total).alias('Total'))
                     .where(OrdenVenta.fecha.between(desde, hasta))
                     .group_by(OrdenVenta.fecha)
                     .order_by(OrdenVenta.fecha)
                     )
        else:
            query = (OrdenVenta
                     .select(OrdenVenta.id.alias('ID'),OrdenVenta.fecha.alias('Fecha'), fn.SUM(OrdenVenta.total).alias('Total'))
                     .group_by(OrdenVenta.fecha)
                     .order_by(OrdenVenta.fecha)
                     )
        if query.count() > 0:
            lista_records = list(query.dicts())
            datos['MODEL'] = ['OrdenVenta' for record in lista_records]
            datos['ID'] = [record["ID"] for record in lista_records]
            datos['Fecha'] = [record["Fecha"] for record in lista_records]
            datos['Total'] = [record["Total"] for record in lista_records]
            df = pd.DataFrame(datos)
            df_ordenado = df.sort_values(by='Total', ascending=False).reset_index(drop=True)
            return df_ordenado
        else:
            return {}

    @classmethod
    def obtener_venta_grafico(cls,desde=False,hasta=False):
        datos = {}
        if desde and hasta:
            query = (OrdenVenta
                     .select(OrdenVenta.id.alias('ID'),OrdenVenta.fecha.alias('Fecha'), fn.SUM(OrdenVenta.total).alias('Total'))
                     .where(OrdenVenta.fecha.between(desde, hasta))
                     .group_by(OrdenVenta.fecha)
                     .order_by(OrdenVenta.fecha)
                     )
        else:
            query = (OrdenVenta
                     .select(OrdenVenta.id.alias('ID'),OrdenVenta.fecha.alias('Fecha'), fn.SUM(OrdenVenta.total).alias('Total'))
                     .group_by(OrdenVenta.fecha)
                     .order_by(OrdenVenta.fecha)
                     )
        if query.count() > 0:
            lista_records = list(query.dicts())
            x = [record["Fecha"] for record in lista_records]
            y = [record["Total"] for record in lista_records]
            return x, y
        else:
            return [], []

    def get_totales(self):
        model = globals()['OrdenVentaLine']
        registros = model.select().where(model.ordenventa_id == self.id)
        self.subtoal = sum(f.subtoal for f in registros if f.subtoal is not None)
        self.descuento = sum(f.descuento_Monto for f in registros if f.descuento_Monto is not None)
        self.impuesto = sum(f.impuesto_Monto for f in registros if f.impuesto_Monto is not None)
        self.total = sum(f.total for f in registros if f.total is not None)
        self.total_Adeudado = sum(f.total for f in registros if f.total is not None)

    def get_contexto(self):
        contexto = {}
        contexto['cliente'] = {
            "nombre": self.cliente.nombre,
            "cedula": self.cliente.cedula,
            "email": self.cliente.email,
            "telfono": self.cliente.telfono,
        }
        contexto['factura'] = {
            'nombre': self.nombre,
            'fecha': self.fecha,
            'subtoal':format_currency(self.subtoal, 'CRC', locale='es_CR'),
            'descuento':format_currency(self.descuento, 'CRC', locale='es_CR'),
            'impuesto':format_currency(self.impuesto, 'CRC', locale='es_CR'),
            'total':format_currency(self.total, 'CRC', locale='es_CR'),
        }
        registros = OrdenVentaLine.select().where(OrdenVentaLine.ordenventa_id == self.id)
        vals = []
        for registro in registros:
            vals.append({
                'producto': registro.producto.nombre,
                'cantidad': registro.cantidad,
                'precio_Unitario': format_currency(registro.precio_Unitario, 'CRC', locale='es_CR'),
                'descuento_Porcentaje': f"{registro.descuento_Porcentaje}%",
                'descuento_Monto':format_currency(registro.descuento_Monto, 'CRC', locale='es_CR'),
                'impuesto': registro.impuesto.nombre,
                'impuesto_Monto': format_currency(registro.impuesto_Monto, 'CRC', locale='es_CR'),
                'subtoal': format_currency(registro.subtoal, 'CRC', locale='es_CR'),
                'total': format_currency(registro.total, 'CRC', locale='es_CR'),
            })
        contexto['factura']['facturadetalle'] = vals
        return contexto

    def buscar_crear_model(self):
        factura_id = FacturaCliente.get_or_none(FacturaCliente.ordenventa_id == self.id)
        if factura_id is None:
            datos_dict = self.__data__.copy()
            del datos_dict['id']
            datos_dict['ordenventa_id'] = self.id
            factura_id = FacturaCliente.crear_actualizar_desde_dict(datos_dict)
            datos_modelrel = self.obtener_datos_models_rel(self.id)
            for dato_modelrel in datos_modelrel:
                ids = dato_modelrel['datos']['ID']
                records = OrdenVentaLine.select().where(OrdenVentaLine.id.in_(ids))
                for record in records:
                    record_dict = record.__data__.copy()
                    del record_dict['id']
                    del record_dict['ordenventa_id']
                    record_dict['factura_id'] = factura_id.id
                    FacturaClienteLine.crear_actualizar_desde_dict(record_dict)
        self.terminada = True
        self.save()
        return factura_id

class OrdenVentaLine(BaseModel):
    descripcion = "Lineas de la factura"
    grupo_nombres = ['Información general', 'Información financiera','Información financiera']
    cant_grupo = 3
    accion_Config = {
        'reporte': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    ordenventa_id = ForeignKey(OrdenVenta, backref='OrdenVenta', help_text="OrdenVenta", mostrar_Tree=False, mostrar_Form=False)
    producto = ForeignKey(Producto, backref='Producto',valor_maximo="cantidad", help_text="Producto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,ochange=True)
    cantidad = Float(help_text="Cantidad", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=1,ochange=True)
    precio_Unitario = Decimal(help_text="Precio", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,max_digits=10, decimal_places=2)
    descuento_Porcentaje = Float(help_text="Procentaje de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,ochange=True,default=0)
    descuento_Monto = Decimal(help_text="Monto de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,default=0,max_digits=10, decimal_places=2)
    impuesto = ForeignKey(ImpuestoVenta, backref='ImpuestoVenta', help_text="Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=0,null=True)
    impuesto_Monto = Decimal(help_text="Monto de Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=1,default=0,max_digits=10, decimal_places=2)
    subtoal = Decimal(help_text="Subtoal",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=2,null=True,max_digits=10, decimal_places=2)
    total = Decimal(help_text="Total",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=3,null=True,max_digits=10, decimal_places=2)


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
            elif tipo == Float:
                return float(valor)
            elif tipo == Decimal:
                return decimal.Decimal(valor)
            elif tipo == Boolean:
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

    def crear_actualizar_desde_model(cls):
        print('s')
        cls.save()

    @classmethod
    def obtener_columnas_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for field_name, field_obj in cls._meta.fields.items():
            help_text = getattr(field_obj, 'help_text', None)
            mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
            datos.append((help_text,mostrar_Tree))
        return tuple(datos)

    @classmethod
    def obtener_columnas_para_treeviewrel(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for field_name, field_obj in cls._meta.fields.items():
            help_text = getattr(field_obj, 'help_text', None)
            mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
            datos.append((help_text,mostrar_Tree))
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_campos_ochange(cls):
        campos = []
        for nombre_campo, campo in cls._meta.fields.items():
            if getattr(campo, 'ochange', None) == True:
                campos.append(f"{nombre_campo}_field")
        return campos

    @classmethod
    def obtener_resultado_ochange(cls,datos):
        datos['producto'] = Producto.get(Producto.id ==  datos['producto'])
        datos['cantidad'] = float(datos['cantidad'])
        datos['descuento_Porcentaje'] = float(datos['descuento_Porcentaje'])
        datos['precio_Unitario'] = datos['producto'].precio_Venta
        datos['impuesto'] = datos['producto'].impuesto_Venta
        datos['subtoal'] =  datos['precio_Unitario'] * decimal.Decimal(datos['cantidad'])
        if datos['descuento_Porcentaje'] > 0 and isinstance(datos['descuento_Porcentaje'], (int, float, str, bool, bytes)):
            datos['descuento_Monto'] = datos['subtoal'] * (decimal.Decimal(datos['descuento_Porcentaje']) / 100)
        else:
            datos['descuento_Monto'] = 0
            datos['descuento_Porcentaje'] = 0

        if datos['impuesto']:
            datos['impuesto_Monto'] = (datos['subtoal'] - datos['descuento_Monto']) * (decimal.Decimal(datos['impuesto'].importe) / 100)
        else:
            datos['impuesto_Monto'] = 0

        datos['total'] = datos['subtoal'] - datos['descuento_Monto'] + datos['impuesto_Monto']

        return datos

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def obtener_valor_maximo(cls,id):
        producto =  Producto.get(Producto.id == id)
        return producto.obtener_valor_maximo()

class FacturaCliente(BaseModel):
    descripcion = "Facturas de Cliente"
    defalult_name = "FACTC #"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
    auto_Guardar = True
    models_Rels = ['FacturaClienteLine']
    accion_Config = {
        'reporte': True,
        'reporte_Template': "factura_template.xml",
        'correo_Template': "correo_reporte.xml",
        'reporte_Correo': True,
        'reporte_CorreoDescripcion': "Enviar factura al cliente",
        'reporte_Descargar': True,
        'reporte_DescargarDescripcion': "Descargar factura",
        'crear_Modelo': False,
    }
    menu_root_index = 2
    menu_root_nombre = 'Contabilidad'
    menu_parent_index = 0
    menu_parent_nombre = 'Clientes'
    menu_index = 0
    menu_nombre = "Facturas"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    ordenventa_id = ForeignKey(OrdenVenta, backref='OrdenVenta', help_text="OrdenVenta", mostrar_Tree=False,mostrar_Form=False,null=True)
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0)
    terminada = Boolean(default=False,help_text="Terminada",mostrar_Tree=False,mostrar_Form=False)
    cliente = ForeignKey(Cliente,null=True,required=True, backref='Cliente', help_text="Cliente", mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1)
    fecha = Date(help_text="Fecha",default=datetime.date.today,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=0,posicion=2)
    subtoal = Float(help_text="Subtotal",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=0,default=0)
    descuento = Float(help_text="Descuento",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=1,default=0)
    impuesto = Float(help_text="Impuesto",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=2,default=0)
    total = Float(help_text="Total",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=3,default=0)
    total_Adeudado = Float(help_text="Total adeudado",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=4,default=0)

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
                seq = Secuencia.siguiente_valor(cls.__name__)
                if seq:
                    datos_convertidos['nombre'] = seq
                return cls.create(**datos_convertidos)
        else:
            seq = Secuencia.siguiente_valor(cls.__name__)
            if seq:
                datos_convertidos['nombre'] = seq
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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            records = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            vals = {}
            for field in model._meta.sorted_fields:
                if isinstance(field, ForeignKey):
                    vals[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records] if isinstance(id,int) else []
                elif isinstance(field, Boolean):
                    vals[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records] if isinstance(id,int) else []
                else:
                    vals[f"{field.help_text}"] = [getattr(record, field.name) for record in records] if isinstance(id,int) else []
            descp['datos'] = vals
            datos.append(descp)
        return datos

    @classmethod
    def eliminar_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            dataTupla = []
            for registro in registros:
                registro.delete_instance()

    @classmethod
    def obtener_campo_rel(cls,modelrel):
        campo_relacion = None
        for field_name, field_obj in modelrel._meta.fields.items():
            if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
                campo_relacion = getattr(modelrel, field_name).name
                break
        return campo_relacion

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        model.get_totales()
        return model

    def get_totales(self):
        model = globals()['FacturaClienteLine']
        registros = model.select().where(model.factura_id == self.id)
        self.subtoal = sum(f.subtoal for f in registros if f.subtoal is not None)
        self.descuento = sum(f.descuento_Monto for f in registros if f.descuento_Monto is not None)
        self.impuesto = sum(f.impuesto_Monto for f in registros if f.impuesto_Monto is not None)
        self.total = sum(f.total for f in registros if f.total is not None)
        self.total_Adeudado = sum(f.total for f in registros if f.total is not None)

    def get_contexto(self):
        contexto = {}
        contexto['cliente'] = {
            "nombre": self.cliente.nombre,
            "cedula": self.cliente.cedula,
            "email": self.cliente.email,
            "telfono": self.cliente.telfono,
        }
        contexto['factura'] = {
            'nombre': self.nombre,
            'fecha': self.fecha,
            'subtoal':format_currency(self.subtoal, 'CRC', locale='es_CR'),
            'descuento':format_currency(self.descuento, 'CRC', locale='es_CR'),
            'impuesto':format_currency(self.impuesto, 'CRC', locale='es_CR'),
            'total':format_currency(self.total, 'CRC', locale='es_CR'),
        }
        registros = FacturaClienteLine.select().where(FacturaClienteLine.factura_id == self.id)
        vals = []
        for registro in registros:
            vals.append({
                'producto': registro.producto.nombre,
                'cantidad': registro.cantidad,
                'precio_Unitario': format_currency(registro.precio_Unitario, 'CRC', locale='es_CR'),
                'descuento_Porcentaje': f"{registro.descuento_Porcentaje}%",
                'descuento_Monto':format_currency(registro.descuento_Monto, 'CRC', locale='es_CR'),
                'impuesto': registro.impuesto.nombre,
                'impuesto_Monto': format_currency(registro.impuesto_Monto, 'CRC', locale='es_CR'),
                'subtoal': format_currency(registro.subtoal, 'CRC', locale='es_CR'),
                'total': format_currency(registro.total, 'CRC', locale='es_CR'),
            })
        contexto['factura']['facturadetalle'] = vals
        return contexto

class FacturaClienteLine(BaseModel):
    descripcion = "Lineas de la factura"
    grupo_nombres = ['Información general', 'Información financiera','Información financiera']
    cant_grupo = 3
    accion_Config = {
        'reporte': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    factura_id = ForeignKey(FacturaCliente, backref='FacturaCliente', help_text="FacturaCliente", mostrar_Tree=False, mostrar_Form=False)
    producto = ForeignKey(Producto, backref='Producto',valor_maximo="cantidad", help_text="Producto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,ochange=True)
    cantidad = Float(help_text="Cantidad", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=1,ochange=True)
    precio_Unitario = Decimal(help_text="Precio", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,max_digits=10, decimal_places=2)
    descuento_Porcentaje = Float(help_text="Procentaje de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,ochange=True,default=0)
    descuento_Monto = Decimal(help_text="Monto de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,default=0,max_digits=10, decimal_places=2)
    impuesto = ForeignKey(ImpuestoVenta, backref='ImpuestoVenta', help_text="Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=0,null=True)
    impuesto_Monto = Decimal(help_text="Monto de Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=1,default=0,max_digits=10, decimal_places=2)
    subtoal = Decimal(help_text="Subtoal",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=2,null=True,max_digits=10, decimal_places=2)
    total = Decimal(help_text="Total",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=3,null=True,max_digits=10, decimal_places=2)


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
            elif tipo == Float:
                return float(valor)
            elif tipo == Decimal:
                return decimal.Decimal(valor)
            elif tipo == Boolean:
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

    def crear_actualizar_desde_model(cls):
        print('s')
        cls.save()

    @classmethod
    def obtener_columnas_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for field_name, field_obj in cls._meta.fields.items():
            help_text = getattr(field_obj, 'help_text', None)
            mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
            datos.append((help_text,mostrar_Tree))
        return tuple(datos)

    @classmethod
    def obtener_columnas_para_treeviewrel(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for field_name, field_obj in cls._meta.fields.items():
            help_text = getattr(field_obj, 'help_text', None)
            mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
            datos.append((help_text,mostrar_Tree))
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_campos_ochange(cls):
        campos = []
        for nombre_campo, campo in cls._meta.fields.items():
            if getattr(campo, 'ochange', None) == True:
                campos.append(f"{nombre_campo}_field")
        return campos

    @classmethod
    def obtener_resultado_ochange(cls,datos):
        datos['producto'] = Producto.get(Producto.id ==  datos['producto'])
        datos['cantidad'] = float(datos['cantidad'])
        datos['descuento_Porcentaje'] = float(datos['descuento_Porcentaje'])
        datos['precio_Unitario'] = datos['producto'].precio_Venta
        datos['impuesto'] = datos['producto'].impuesto_Venta
        datos['subtoal'] =  datos['precio_Unitario'] * decimal.Decimal(datos['cantidad'])
        if datos['descuento_Porcentaje'] > 0 and isinstance(datos['descuento_Porcentaje'], (int, float, str, bool, bytes)):
            datos['descuento_Monto'] = datos['subtoal'] * (decimal.Decimal(datos['descuento_Porcentaje']) / 100)
        else:
            datos['descuento_Monto'] = 0
            datos['descuento_Porcentaje'] = 0

        if datos['impuesto']:
            datos['impuesto_Monto'] = (datos['subtoal'] - datos['descuento_Monto']) * (decimal.Decimal(datos['impuesto'].importe) / 100)
        else:
            datos['impuesto_Monto'] = 0

        datos['total'] = datos['subtoal'] - datos['descuento_Monto'] + datos['impuesto_Monto']

        return datos

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def obtener_valor_maximo(cls,id):
        producto =  Producto.get(Producto.id == id)
        return producto.obtener_valor_maximo()

class OrdenCompra(BaseModel):
    descripcion = "Orden de compra"
    defalult_name = "FACTC #"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
    auto_Guardar = True
    models_Rels = ['OrdenCompraLine']
    accion_Config = {
        'reporte': True,
        'reporte_Template': "factura_template.xml",
        'correo_Template': "correo_reporte.xml",
        'reporte_Correo': True,
        'reporte_CorreoDescripcion': "Enviar factura al cliente",
        'reporte_Descargar': True,
        'reporte_DescargarDescripcion': "Descargar factura",
        'crear_Modelo': True,
        'crear_Modelo_Nombre': "FacturaProveedor",
        'crear_Modelo_Descripcion': " Crear Factura de Proveedor",
    }
    menu_root_index = 1
    menu_root_nombre = 'Compras'
    menu_parent_index = 0
    menu_parent_nombre = 'Compras'
    menu_index = 0
    menu_nombre = "Orden de compra"
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0)
    terminada = Boolean(default=False,help_text="Terminada",mostrar_Tree=False,mostrar_Form=False)
    proveedor = ForeignKey(Proveedor,null=True,required=True, backref='Proveedor', help_text="Proveedor", mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1)
    fecha = Date(help_text="Fecha",default=datetime.date.today,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=0,posicion=2)
    subtoal = Float(help_text="Subtotal",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=0,default=0)
    descuento = Float(help_text="Descuento",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=1,default=0)
    impuesto = Float(help_text="Impuesto",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=2,default=0)
    total = Float(help_text="Total",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=3,default=0)
    total_Adeudado = Float(help_text="Total adeudado",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=4,default=0)

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
                seq = Secuencia.siguiente_valor(cls.__name__)
                if seq:
                    datos_convertidos['nombre'] = seq
                return cls.create(**datos_convertidos)
        else:
            seq = Secuencia.siguiente_valor(cls.__name__)
            if seq:
                datos_convertidos['nombre'] = seq
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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            records = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            vals = {}
            for field in model._meta.sorted_fields:
                if isinstance(field, ForeignKey):
                    vals[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records] if isinstance(id,int) else []
                elif isinstance(field, Boolean):
                    vals[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records] if isinstance(id,int) else []
                else:
                    vals[f"{field.help_text}"] = [getattr(record, field.name) for record in records] if isinstance(id,int) else []
            descp['datos'] = vals
            datos.append(descp)
        return datos

    @classmethod
    def eliminar_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            dataTupla = []
            for registro in registros:
                registro.delete_instance()

    @classmethod
    def obtener_campo_rel(cls,modelrel):
        campo_relacion = None
        for field_name, field_obj in modelrel._meta.fields.items():
            if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
                campo_relacion = getattr(modelrel, field_name).name
                break
        return campo_relacion

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        model.get_totales()
        return model

    @classmethod
    def obtener_ordenes_sin_factura(cls):
        datos = {}
        ordenes_ids = [id for (id,) in cls.select(cls.id).tuples()]
        ordenesFactura_ids = [id for (id,) in FacturaProveedor.select(FacturaProveedor.ordencompra_id).tuples()]
        ids = list(set(ordenes_ids) - set(ordenesFactura_ids))
        ordenes = cls.select(cls.id,cls.proveedor,cls.nombre,cls.fecha).where(cls.id.in_(ids))
        datos['ID'] = [orden.id for orden in ordenes]
        datos['Nombre'] = [orden.nombre   for orden in ordenes]
        datos['Proveedor'] = [orden.proveedor.nombre if orden.proveedor is not None else "N/A" for orden in ordenes]
        datos['Fecha'] = [orden.fecha for orden in ordenes]
        return datos

    def get_totales(self):
        model = globals()['OrdenCompraLine']
        registros = model.select().where(model.ordencompra_id == self.id)
        self.subtoal = sum(f.subtoal for f in registros if f.subtoal is not None)
        self.descuento = sum(f.descuento_Monto for f in registros if f.descuento_Monto is not None)
        self.impuesto = sum(f.impuesto_Monto for f in registros if f.impuesto_Monto is not None)
        self.total = sum(f.total for f in registros if f.total is not None)
        self.total_Adeudado = sum(f.total for f in registros if f.total is not None)

    def get_contexto(self):
        contexto = {}
        contexto['cliente'] = {
            "nombre": self.cliente.nombre,
            "cedula": self.cliente.cedula,
            "email": self.cliente.email,
            "telfono": self.cliente.telfono,
        }
        contexto['factura'] = {
            'nombre': self.nombre,
            'fecha': self.fecha,
            'subtoal':format_currency(self.subtoal, 'CRC', locale='es_CR'),
            'descuento':format_currency(self.descuento, 'CRC', locale='es_CR'),
            'impuesto':format_currency(self.impuesto, 'CRC', locale='es_CR'),
            'total':format_currency(self.total, 'CRC', locale='es_CR'),
        }
        registros = OrdenCompraLine.select().where(OrdenCompraLine.OrdenCompra_id == self.id)
        vals = []
        for registro in registros:
            vals.append({
                'producto': registro.producto.nombre,
                'cantidad': registro.cantidad,
                'precio_Unitario': format_currency(registro.precio_Unitario, 'CRC', locale='es_CR'),
                'descuento_Porcentaje': f"{registro.descuento_Porcentaje}%",
                'descuento_Monto':format_currency(registro.descuento_Monto, 'CRC', locale='es_CR'),
                'impuesto': registro.impuesto.nombre,
                'impuesto_Monto': format_currency(registro.impuesto_Monto, 'CRC', locale='es_CR'),
                'subtoal': format_currency(registro.subtoal, 'CRC', locale='es_CR'),
                'total': format_currency(registro.total, 'CRC', locale='es_CR'),
            })
        contexto['factura']['facturadetalle'] = vals
        return contexto

    def buscar_crear_model(self):
        factura_id = FacturaCliente.get_or_none(FacturaCliente.OrdenCompra_id == self.id)
        if factura_id is None:
            datos_dict = self.__data__.copy()
            del datos_dict['id']
            datos_dict['OrdenCompra_id'] = self.id
            factura_id = FacturaCliente.crear_actualizar_desde_dict(datos_dict)
            datos_modelrel = self.obtener_datos_models_rel(self.id)
            for dato_modelrel in datos_modelrel:
                ids = [item[0] for item in dato_modelrel['records']]
                records = OrdenCompraLine.select().where(OrdenCompraLine.id.in_(ids))
                for record in records:
                    record_dict = record.__data__.copy()
                    del record_dict['id']
                    del record_dict['OrdenCompra_id']
                    record_dict['factura_id'] = factura_id.id
                    FacturaClienteLine.crear_actualizar_desde_dict(record_dict)
        return factura_id

class OrdenCompraLine(BaseModel):
    descripcion = "Lineas de la factura"
    grupo_nombres = ['Información general', 'Información financiera','Información financiera']
    cant_grupo = 3
    accion_Config = {
        'reporte': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    ordencompra_id = ForeignKey(OrdenCompra, backref='OrdenCompra', help_text="OrdenCompra", mostrar_Tree=False, mostrar_Form=False)
    producto = ForeignKey(Producto, backref='Producto', help_text="Producto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,ochange=True)
    cantidad = Float(help_text="Cantidad", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=1,ochange=True)
    precio_Unitario = Decimal(help_text="Precio", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,max_digits=10, decimal_places=2)
    descuento_Porcentaje = Float(help_text="Procentaje de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,ochange=True,default=0)
    descuento_Monto = Decimal(help_text="Monto de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,default=0,max_digits=10, decimal_places=2)
    impuesto = ForeignKey(ImpuestoVenta, backref='ImpuestoVenta', help_text="Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=0,null=True)
    impuesto_Monto = Decimal(help_text="Monto de Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=1,default=0,max_digits=10, decimal_places=2)
    subtoal = Decimal(help_text="Subtoal",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=2,null=True,max_digits=10, decimal_places=2)
    total = Decimal(help_text="Total",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=3,null=True,max_digits=10, decimal_places=2)


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
            elif tipo == Float:
                return float(valor)
            elif tipo == Decimal:
                return decimal.Decimal(valor)
            elif tipo == Boolean:
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

    def crear_actualizar_desde_model(cls):
        print('s')
        cls.save()

    @classmethod
    def obtener_columnas_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for field_name, field_obj in cls._meta.fields.items():
            help_text = getattr(field_obj, 'help_text', None)
            mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
            datos.append((help_text,mostrar_Tree))
        return tuple(datos)

    @classmethod
    def obtener_columnas_para_treeviewrel(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for field_name, field_obj in cls._meta.fields.items():
            help_text = getattr(field_obj, 'help_text', None)
            mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
            datos.append((help_text,mostrar_Tree))
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_campos_ochange(cls):
        campos = []
        for nombre_campo, campo in cls._meta.fields.items():
            if getattr(campo, 'ochange', None) == True:
                campos.append(f"{nombre_campo}_field")
        return campos

    @classmethod
    def obtener_resultado_ochange(cls,datos):
        datos['producto'] = Producto.get(Producto.id ==  datos['producto'])
        datos['cantidad'] = float(datos['cantidad'])
        datos['descuento_Porcentaje'] = float(datos['descuento_Porcentaje'])
        datos['precio_Unitario'] = datos['producto'].precio_Venta
        datos['impuesto'] = datos['producto'].impuesto_Venta
        datos['subtoal'] =  datos['precio_Unitario'] * decimal.Decimal(datos['cantidad'])
        if datos['descuento_Porcentaje'] > 0 and isinstance(datos['descuento_Porcentaje'], (int, float, str, bool, bytes)):
            datos['descuento_Monto'] = datos['subtoal'] * (decimal.Decimal(datos['descuento_Porcentaje']) / 100)
        else:
            datos['descuento_Monto'] = 0
            datos['descuento_Porcentaje'] = 0

        if datos['impuesto']:
            datos['impuesto_Monto'] = (datos['subtoal'] - datos['descuento_Monto']) * (decimal.Decimal(datos['impuesto'].importe) / 100)
        else:
            datos['impuesto_Monto'] = 0

        datos['total'] = datos['subtoal'] - datos['descuento_Monto'] + datos['impuesto_Monto']

        return datos

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

class FacturaProveedor(BaseModel):
    descripcion = "Facturas de proveedor"
    defalult_name = "FACTC #"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
    auto_Guardar = True
    models_Rels = ['FacturaProveedorLine']
    accion_Config = {
        'reporte': True,
        'reporte_Template': "factura_template.xml",
        'correo_Template': "correo_reporte.xml",
        'reporte_Correo': True,
        'reporte_CorreoDescripcion': "Enviar factura al cliente",
        'reporte_Descargar': True,
        'reporte_DescargarDescripcion': "Descargar factura",
        'crear_Modelo': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    ordencompra_id = ForeignKey(OrdenCompra, backref='OrdenCompra', help_text="OrdenCompra", mostrar_Tree=False,mostrar_Form=False,null=True)
    nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0)
    terminada = Boolean(default=False,help_text="Terminada",mostrar_Tree=False,mostrar_Form=False)
    proveedor = ForeignKey(Proveedor,null=True,required=True, backref='Proveedor', help_text="Proveedor", mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1)
    fecha = Date(help_text="Fecha",default=datetime.date.today,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=0,posicion=2)
    subtoal = Float(help_text="Subtotal",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=0,default=0)
    descuento = Float(help_text="Descuento",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=1,default=0)
    impuesto = Float(help_text="Impuesto",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=2,default=0)
    total = Float(help_text="Total",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=3,default=0)
    total_Adeudado = Float(help_text="Total adeudado",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=4,default=0)

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
                seq = Secuencia.siguiente_valor(cls.__name__)
                if seq:
                    datos_convertidos['nombre'] = seq
                return cls.create(**datos_convertidos)
        else:
            seq = Secuencia.siguiente_valor(cls.__name__)
            if seq:
                datos_convertidos['nombre'] = seq
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
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            records = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            vals = {}
            for field in model._meta.sorted_fields:
                if isinstance(field, ForeignKey):
                    vals[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records] if isinstance(id,int) else []
                elif isinstance(field, Boolean):
                    vals[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records] if isinstance(id,int) else []
                else:
                    vals[f"{field.help_text}"] = [getattr(record, field.name) for record in records] if isinstance(id,int) else []
            descp['datos'] = vals
            datos.append(descp)
        return datos

    @classmethod

    def eliminar_datos_models_rel(cls,id):
        datos = []
        for model_name in cls.models_Rels:
            model = globals()[model_name]
            descp = {
                'tab_Name': model.descripcion,
                'model': model,
                'model_name': model_name
            }
            campo_relacion = cls.obtener_campo_rel(model)
            registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            dataTupla = []
            for registro in registros:
                registro.delete_instance()

    @classmethod
    def obtener_campo_rel(cls,modelrel):
        campo_relacion = None
        for field_name, field_obj in modelrel._meta.fields.items():
            if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
                campo_relacion = getattr(modelrel, field_name).name
                break
        return campo_relacion

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        model.get_totales()
        return model

    def get_totales(self):
        model = globals()['FacturaClienteLine']
        registros = model.select().where(model.factura_id == self.id)
        self.subtoal = sum(f.subtoal for f in registros if f.subtoal is not None)
        self.descuento = sum(f.descuento_Monto for f in registros if f.descuento_Monto is not None)
        self.impuesto = sum(f.impuesto_Monto for f in registros if f.impuesto_Monto is not None)
        self.total = sum(f.total for f in registros if f.total is not None)
        self.total_Adeudado = sum(f.total for f in registros if f.total is not None)

    def get_contexto(self):
        contexto = {}
        contexto['cliente'] = {
            "nombre": self.cliente.nombre,
            "cedula": self.cliente.cedula,
            "email": self.cliente.email,
            "telfono": self.cliente.telfono,
        }
        contexto['factura'] = {
            'nombre': self.nombre,
            'fecha': self.fecha,
            'subtoal':format_currency(self.subtoal, 'CRC', locale='es_CR'),
            'descuento':format_currency(self.descuento, 'CRC', locale='es_CR'),
            'impuesto':format_currency(self.impuesto, 'CRC', locale='es_CR'),
            'total':format_currency(self.total, 'CRC', locale='es_CR'),
        }
        registros = FacturaClienteLine.select().where(FacturaClienteLine.factura_id == self.id)
        vals = []
        for registro in registros:
            vals.append({
                'producto': registro.producto.nombre,
                'cantidad': registro.cantidad,
                'precio_Unitario': format_currency(registro.precio_Unitario, 'CRC', locale='es_CR'),
                'descuento_Porcentaje': f"{registro.descuento_Porcentaje}%",
                'descuento_Monto':format_currency(registro.descuento_Monto, 'CRC', locale='es_CR'),
                'impuesto': registro.impuesto.nombre,
                'impuesto_Monto': format_currency(registro.impuesto_Monto, 'CRC', locale='es_CR'),
                'subtoal': format_currency(registro.subtoal, 'CRC', locale='es_CR'),
                'total': format_currency(registro.total, 'CRC', locale='es_CR'),
            })
        contexto['factura']['facturadetalle'] = vals
        return contexto

class FacturaProveedorLine(BaseModel):
    descripcion = "Lineas de la factura"
    grupo_nombres = ['Información general', 'Información financiera','Información financiera']
    cant_grupo = 3
    accion_Config = {
        'reporte': False,
    }
    id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
    factura_id = ForeignKey(FacturaProveedor, backref='FacturaProveedor', help_text="FacturaProveedor", mostrar_Tree=False, mostrar_Form=False)
    producto = ForeignKey(Producto, backref='Producto',valor_maximo="cantidad", help_text="Producto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,ochange=True)
    cantidad = Float(help_text="Cantidad", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=1,ochange=True)
    precio_Unitario = Decimal(help_text="Precio", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,max_digits=10, decimal_places=2)
    descuento_Porcentaje = Float(help_text="Procentaje de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,ochange=True,default=0)
    descuento_Monto = Decimal(help_text="Monto de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,default=0,max_digits=10, decimal_places=2)
    impuesto = ForeignKey(ImpuestoVenta, backref='ImpuestoVenta', help_text="Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=0,null=True)
    impuesto_Monto = Decimal(help_text="Monto de Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=1,default=0,max_digits=10, decimal_places=2)
    subtoal = Decimal(help_text="Subtoal",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=2,null=True,max_digits=10, decimal_places=2)
    total = Decimal(help_text="Total",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=3,null=True,max_digits=10, decimal_places=2)


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
            elif tipo == Float:
                return float(valor)
            elif tipo == Decimal:
                return decimal.Decimal(valor)
            elif tipo == Boolean:
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

    def crear_actualizar_desde_model(cls):
        print('s')
        cls.save()

    @classmethod
    def obtener_columnas_para_treeview(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for field_name, field_obj in cls._meta.fields.items():
            help_text = getattr(field_obj, 'help_text', None)
            mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
            datos.append((help_text,mostrar_Tree))
        return tuple(datos)

    @classmethod
    def obtener_columnas_para_treeviewrel(cls):
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for field_name, field_obj in cls._meta.fields.items():
            help_text = getattr(field_obj, 'help_text', None)
            mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
            datos.append((help_text,mostrar_Tree))
        return tuple(datos)

    @classmethod
    def obtener_datos_para_treeview(cls):
        datos = {}
        records = cls.select()
        for field in cls._meta.sorted_fields:
            if isinstance(field, ForeignKey):
                datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
            elif isinstance(field, Boolean):
                datos[f"{field.help_text}"] = ["SI" if getattr(record, field.name) else "NO" for record in records]
            else:
                datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]


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

    @classmethod
    def obtener_campos_ochange(cls):
        campos = []
        for nombre_campo, campo in cls._meta.fields.items():
            if getattr(campo, 'ochange', None) == True:
                campos.append(f"{nombre_campo}_field")
        return campos

    @classmethod
    def obtener_resultado_ochange(cls,datos):
        datos['producto'] = Producto.get(Producto.id ==  datos['producto'])
        datos['cantidad'] = float(datos['cantidad'])
        datos['descuento_Porcentaje'] = float(datos['descuento_Porcentaje'])
        datos['precio_Unitario'] = datos['producto'].precio_Venta
        datos['impuesto'] = datos['producto'].impuesto_Venta
        datos['subtoal'] =  datos['precio_Unitario'] * decimal.Decimal(datos['cantidad'])
        if datos['descuento_Porcentaje'] > 0 and isinstance(datos['descuento_Porcentaje'], (int, float, str, bool, bytes)):
            datos['descuento_Monto'] = datos['subtoal'] * (decimal.Decimal(datos['descuento_Porcentaje']) / 100)
        else:
            datos['descuento_Monto'] = 0
            datos['descuento_Porcentaje'] = 0

        if datos['impuesto']:
            datos['impuesto_Monto'] = (datos['subtoal'] - datos['descuento_Monto']) * (decimal.Decimal(datos['impuesto'].importe) / 100)
        else:
            datos['impuesto_Monto'] = 0

        datos['total'] = datos['subtoal'] - datos['descuento_Monto'] + datos['impuesto_Monto']

        return datos

    @classmethod
    def obtener_con_accion(cls, id):
        model = cls.get(cls.id == id)
        return model

    @classmethod
    def obtener_valor_maximo(cls,id):
        producto =  Producto.get(Producto.id == id)
        return producto.existencias

class Secuencia(BaseModel):
    nombre = Char(unique=True)
    prefijo = Char(default="SEQ")
    padding = Integer(default=4)
    ultimo_numero = Integer(default=0)

    @classmethod
    def siguiente_valor(cls,model_name):
        seqs = cls.select().where(cls.nombre == model_name)
        for seq in seqs:
            seq.ultimo_numero += 1
            seq.save()

            partes = [seq.prefijo]
            partes.append(str(seq.ultimo_numero).zfill(seq.padding))
            return "/".join(partes)
        return False

class Ajuste(BaseModel):
    descripcion  = 'Ajustes'
    menu_root_index = 3
    menu_root_nombre = 'Configuración'
    menu_parent_index = 0
    menu_parent_nombre = 'Configuración'
    menu_index = 0
    menu_nombre = "Ajustes"
    id = Auto(mostrar_Tree=False, mostrar_Form=False, help_text="ID")
    key = Char(help_text="Nombre", mostrar_Tree=True, mostrar_Form=True)
    valor = Char(help_text="Valor", mostrar_Tree=True, mostrar_Form=True,null=True)


db.connect()
db.create_tables(
    [
        User,
        UserPermisos,
        Modelo,
        Cliente,
        Proveedor,
        Producto,
        ImpuestoVenta,
        ImpuestoCompra,
        Ajuste,
        OrdenVenta,
        OrdenVentaLine,
        FacturaCliente,
        FacturaClienteLine,
        OrdenCompra,
        OrdenCompraLine,
        FacturaProveedor,
        FacturaProveedorLine,
        Secuencia,

    ])

default_user = {
    "email": "admin",
    "nombre": "Administrador",
    "cedula": "00000000",
    "puesto": "Gerente",
    "password": encriptar_password("admin"),
    "admin": True
}

default_Ajuste = [
    {
        "key": 'color.menu',
        "valor": '#555',
    },
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
    {
        "key": 'empresa.nombre',
        "valor": 'Empresa S.A',
    },
    {
        "key": 'empresa.telefono',
        "valor": '88888888',
    },
    {
        "key": 'empresa.correo',
        "valor": 'empresa@empresa.com',
    },
    {
        "key": 'empresa.direccion',
        "valor": 'Av. Central 123, Edificio Empresarial Colima, Piso 4, San José, Costa Rica',
    },

]

default_Seq = [
    {
        "nombre": 'FacturaCliente',
        "prefijo": 'FACT',
        "padding": 4,
        "ultimo_numero": 0,
    },
    {
        "nombre": 'OrdenVenta',
        "prefijo": 'OV',
        "padding": 4,
        "ultimo_numero": 0,
    },
    {
        "nombre": 'FacturaProveedor',
        "prefijo": 'FACTP',
        "padding": 4,
        "ultimo_numero": 0,
    },
    {
        "nombre": 'OrdenCompra',
        "prefijo": 'OC',
        "padding": 4,
        "ultimo_numero": 0,
    },
]
modelos_info = [
    {
        "modelo": name,
        "nombre": getattr(obj, "descripcion", ""),
        "menu_root_index": getattr(obj, "menu_root_index", 1000),
        "menu_root_nombre": getattr(obj, "menu_root_nombre", ""),
        "menu_parent_index": getattr(obj, "menu_parent_index",1000),
        "menu_parent_nombre": getattr(obj, "menu_parent_nombre", ""),
        "menu_index": getattr(obj, "menu_index", 1000),
        "menu_nombre": getattr(obj, "menu_nombre", ""),
        "icon_path": f"assets/icon/{getattr(obj, "menu_root_nombre", "")}.png",
    }
    for name, obj in globals().items()
    if inspect.isclass(obj) and issubclass(obj, Model) and obj is not Model and name not in ("BaseModel","Modelo")
]

for modelo in modelos_info:
    if not Modelo.select().where(Modelo.modelo == modelo["modelo"]).exists():
        Modelo.create(**modelo)

if not User.select().where(User.email == default_user["email"]).exists():
    User.create(**default_user)

for ajsute in default_Ajuste:
    if not Ajuste.select().where(Ajuste.key == ajsute["key"]).exists():
        Ajuste.create(**ajsute)

for seq in default_Seq:
    if not Secuencia.select().where(Secuencia.nombre == seq["nombre"]).exists():
        Secuencia.create(**seq)

