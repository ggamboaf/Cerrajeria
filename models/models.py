# import decimal
# import json
# import datetime
#
# from babel.numbers import format_currency
# from peewee import *
# from decimal import Decimal
# from utils.utils import encriptar_password, verificar_password
#
#
# db = SqliteDatabase('cerrajeria.db')
#
# class Char(CharField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
# class Auto(AutoField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
# class Text(TextField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
# class Float(FloatField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
# class Decimal(DecimalField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
# class ForeignKey(ForeignKeyField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
# class Boolean(BooleanField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
# class Date(DateField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
# class Integer(IntegerField):
#     def __init__(self, *args, mostrar_Tree=True,mostrar_Form=True,nombre_default="",lectura=False,numero_Grupo=0,posicion=0,ochange=False,valor_maximo=None,campo_busqueda="",required=False,exportar=False,  **kwargs):
#         self.mostrar_Tree = mostrar_Tree
#         self.mostrar_Form = mostrar_Form
#         self.lectura = lectura
#         self.nombre_default = nombre_default
#         self.numero_Grupo = numero_Grupo
#         self.posicion = posicion
#         self.ochange = ochange
#         self.valor_maximo = valor_maximo
#         self.campo_busqueda = campo_busqueda
#         self.required = required
#         self.exportar = exportar
#         super().__init__(*args, **kwargs)
#
#
# class BaseModel(Model):
#     class Meta:
#         database = db
#
# class User(BaseModel):
#     id = Auto(mostrar_Tree=False,mostrar_Form=False)
#     nombre = Char(mostrar_Tree=True)
#     email = Char(unique=True,mostrar_Tree=True)
#     cedula = Char(mostrar_Tree=True)
#     password = Char(mostrar_Tree=False,mostrar_Form=False)
#     codigo = Char(mostrar_Tree=False,mostrar_Form=False,null=True)
#     permisos =  Text(default='{}',mostrar_Tree=False,mostrar_Form=True)
#
# class Cliente(BaseModel):
#     plantilla_Name = "Plantilla Clientes.xlsx"
#     xlsx_Name = "Clientes.xlsx"
#     descripcion = "Cliente"
#     grupo_nombres = ['Información general', 'Información financiera']
#     cant_grupo = 2
#     accion_Config = {
#         'reporte': False,
#         'crear_Modelo': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0,exportar=True)
#     cedula = Char(help_text="Identificación",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
#     email = Char(help_text="Correo",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0,exportar=True)
#     telfono = Char(help_text="Teléfono",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=1,exportar=True)
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == FloatField:
#                 return float(valor)
#             elif tipo == BooleanField:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for ClienteProveedor in cls._meta.sorted_fields:
#             datos.append(ClienteProveedor.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for registro in registros:
#             datos.append((registro.id,registro.nombre,registro.cedula,registro.email,registro.telfono))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
#     @classmethod
#     def eliminar_datos_models_rel(cls,id):
#         datos = []
#         if hasattr(cls, "models_Rels"):
#             for model_name in cls.models_Rels:
#                 model = globals()[model_name]
#                 descp = {
#                     'tab_Name': model.descripcion,
#                     'model': model,
#                     'model_name': model_name
#                 }
#                 campo_relacion = cls.obtener_campo_rel(model)
#                 registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#                 dataTupla = []
#                 for registro in registros:
#                     registro.delete_instance()
#
#     @classmethod
#     def obtener_datos_para_exportar(cls):
#         datos = {}
#         records = cls.select()
#         for field in cls._meta.sorted_fields:
#             if field.exportar:
#                 if isinstance(field, ForeignKey):
#                     datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
#                 else:
#                     datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]
#
#         return datos
#
# class Proveedor(BaseModel):
#     plantilla_Name = "Plantilla Provedores.xlsx"
#     xlsx_Name = "Provedores.xlsx"
#     descripcion = "Proveedor"
#     grupo_nombres = ['Información general', 'Información financiera']
#     cant_grupo = 2
#     accion_Config = {
#         'reporte': False,
#         'crear_Modelo': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0,exportar=True)
#     cedula = Char(help_text="Identificación",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
#     email = Char(help_text="Correo",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0,exportar=True)
#     telfono = Char(help_text="Teléfono",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=1,exportar=True)
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == FloatField:
#                 return float(valor)
#             elif tipo == BooleanField:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for registro in cls._meta.sorted_fields:
#             datos.append(registro.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for registro in registros:
#             datos.append((registro.id, registro.nombre,registro.cedula,registro.email,registro.telfono))
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_exportar(cls):
#         datos = {}
#         records = cls.select()
#         for field in cls._meta.sorted_fields:
#             if field.exportar:
#                 if isinstance(field, ForeignKey):
#                     datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
#                 else:
#                     datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]
#
#         return datos
#
# class ImpuestoVenta(BaseModel):
#     descripcion = "Impuesto de venta"
#     grupo_nombres = ['Información general', 'Información financiera']
#     cant_grupo = 2
#     accion_Config = {
#         'reporte': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,nombre_default="Impuesto",numero_Grupo=0,posicion=0)
#     importe = Float(help_text="Importe (%)",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0)
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == FloatField:
#                 return float(valor)
#             elif tipo == BooleanField:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for registro in cls._meta.sorted_fields:
#             datos.append(registro.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for registro in registros:
#             datos.append((registro.id, registro.nombre,registro.importe))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
#     @classmethod
#     def obtener_datos_para_exportar(cls):
#         datos = {}
#         records = cls.select()
#         for field in cls._meta.sorted_fields:
#             if field.exportar:
#                 if isinstance(field, ForeignKey):
#                     datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
#                 else:
#                     datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]
#
#         return datos
#
# class ImpuestoCompra(BaseModel):
#     descripcion = "Impuesto de compra"
#     grupo_nombres = ['Información general', 'Información financiera']
#     cant_grupo = 2
#     accion_Config = {
#         'reporte': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,nombre_default="Impuesto",numero_Grupo=0,posicion=0)
#     importe = Float(help_text="Importe (%)",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=0)
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == FloatField:
#                 return float(valor)
#             elif tipo == BooleanField:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for registro in cls._meta.sorted_fields:
#             datos.append(registro.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for registro in registros:
#             datos.append((registro.id, registro.nombre,registro.importe))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
#     @classmethod
#     def obtener_datos_para_exportar(cls):
#         datos = {}
#         records = cls.select()
#         for field in cls._meta.sorted_fields:
#             if field.exportar:
#                 if isinstance(field, ForeignKey):
#                     datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
#                 else:
#                     datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]
#
#         return datos
#
# class Producto(BaseModel):
#     plantilla_Name = "Plantilla Productos.xlsx"
#     xlsx_Name = "Productos.xlsx"
#     descripcion = "Producto"
#     grupo_nombres = ['Información general','Información financiera']
#     cant_grupo = 2
#     tipo_choices = (
#         ('Producto', 'Producto'),
#         ('Servicio', 'Servicio'),
#     )
#     accion_Config = {
#         'reporte': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0,exportar=True)
#     tipo = Char(choices=tipo_choices,help_text="Tipo",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1,exportar=True)
#     existencias = Float(help_text="Existencias", null=True,mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,exportar=True)
#     costo = Decimal(help_text="Costo", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1, decimal_places=2,exportar=True)
#     porcentaje_ganancia = Float(help_text="Porcentaje de Ganancia (%)",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=2,exportar=True)
#     precio_Venta = Decimal(help_text="Precio de venta",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=3, decimal_places=2,exportar=True)
#     precio_Compra = Decimal(help_text="Precio de compra",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=1,posicion=4, decimal_places=2,exportar=True)
#     impuesto_Venta = ForeignKey(ImpuestoVenta,backref='Venta',campo_busqueda="importe",help_text="Impuesto de venta",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,exportar=True)
#     impuesto_Compra = ForeignKey(ImpuestoCompra,backref='Compra',campo_busqueda="importe",help_text="Impuesto de compra",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=3,null=True,exportar=True)
#
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == Float:
#                 return float(valor)
#             elif tipo == Decimal:
#                 return round(decimal.Decimal(valor),campos[campo].decimal_places)
#             elif tipo == Boolean:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for model in cls._meta.sorted_fields:
#             datos.append(model.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for instancia in cls.select():
#             fila = []
#             for field in cls._meta.sorted_fields:
#                 valor = getattr(instancia, field.name)
#
#                 if isinstance(field, ForeignKeyField):
#                     valor = getattr(instancia, f"{field.name}")
#                     valor = valor.nombre if valor is not None else ''
#
#                 # Reemplazar None por cadena vacía
#                 fila.append(valor if valor is not None else '')
#
#             datos.append(tuple(fila))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
#     @classmethod
#     def obtener_datos_para_exportar(cls):
#         datos = {}
#         records = cls.select()
#         for field in cls._meta.sorted_fields:
#             if field.exportar:
#                 if isinstance(field, ForeignKey):
#                     datos[f"{field.help_text}"] = [getattr(record, field.name).nombre for record in records]
#                 else:
#                     datos[f"{field.help_text}"] = [getattr(record, field.name) for record in records]
#
#         return datos
#
#     def obtener_valor_maximo(self):
#         totalOrdenVenta = 0
#         totalOrdenCompra = 0
#         ordenVenta = OrdenVentaLine.select().where(OrdenVentaLine.producto == self.id)
#         ordenCompra = OrdenCompraLine.select().where(OrdenCompraLine.producto == self.id)
#
#         if len(ordenVenta) > 1:
#             totalOrdenVenta = sum(f.cantidad for f in ordenVenta if f.cantidad is not None)
#
#         if len(ordenCompra) > 0:
#             totalOrdenCompra = sum(f.cantidad for f in ordenCompra if f.cantidad is not None)
#
#         return totalOrdenCompra - totalOrdenVenta
#
# class OrdenVenta(BaseModel):
#     descripcion = "Orden de venta"
#     defalult_name = "FACTC #"
#     grupo_nombres = ['Información general', 'Información financiera']
#     cant_grupo = 2
#     auto_Guardar = True
#     models_Rels = ['OrdenVentaLine']
#     accion_Config = {
#         'reporte': True,
#         'reporte_Template': "factura_template.xml",
#         'correo_Template': "correo_reporte.xml",
#         'reporte_Correo': True,
#         'reporte_CorreoDescripcion': "Enviar factura al cliente",
#         'reporte_Descargar': True,
#         'reporte_DescargarDescripcion': "Descargar factura",
#         'crear_Modelo': True,
#         'crear_Modelo_Nombre': "FacturaCliente",
#         'crear_Modelo_Descripcion': " Crear Factura de Cliente",
#     }
#
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0)
#     terminada = Boolean(default=False,help_text="Terminada",mostrar_Tree=False,mostrar_Form=False)
#     cliente = ForeignKey(Cliente,null=True,required=True, backref='Cliente', help_text="Cliente", mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1)
#     fecha = Date(help_text="Fecha",default=datetime.date.today,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=0,posicion=2)
#     subtoal = Float(help_text="Subtotal",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=0,default=0)
#     descuento = Float(help_text="Descuento",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=1,default=0)
#     impuesto = Float(help_text="Impuesto",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=2,default=0)
#     total = Float(help_text="Total",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=3,default=0)
#     total_Adeudado = Float(help_text="Total adeudado",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=4,default=0)
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == FloatField:
#                 return float(valor)
#             elif tipo == BooleanField:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 seq = Secuencia.siguiente_valor(cls.__name__)
#                 if seq:
#                     datos_convertidos['nombre'] = seq
#                 return cls.create(**datos_convertidos)
#         else:
#             seq = Secuencia.siguiente_valor(cls.__name__)
#             if seq:
#                 datos_convertidos['nombre'] = seq
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for model in cls._meta.sorted_fields:
#             datos.append(model.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for instancia in cls.select():
#             fila = []
#             for field in cls._meta.sorted_fields:
#                 valor = getattr(instancia, field.name)
#
#                 if isinstance(field, ForeignKeyField):
#                     valor = getattr(instancia, f"{field.name}")
#                     valor = valor.nombre if valor is not None else ''
#
#                 # Reemplazar None por cadena vacía
#                 fila.append(valor if valor is not None else '')
#
#             datos.append(tuple(fila))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_datos_models_rel(cls,id):
#         datos = []
#         for model_name in cls.models_Rels:
#             model = globals()[model_name]
#             descp = {
#                 'tab_Name': model.descripcion,
#                 'model': model,
#                 'model_name': model_name
#             }
#             campo_relacion = cls.obtener_campo_rel(model)
#             registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#             dataTupla = []
#             for registro in registros:
#                 vals = []
#                 vals.append(registro.id)
#                 vals.append(registro.ordenventa_id.id)
#                 vals.append(registro.producto.nombre)
#                 vals.append(registro.cantidad)
#                 vals.append(registro.precio_Unitario)
#                 vals.append(registro.descuento_Porcentaje)
#                 vals.append(registro.descuento_Monto)
#                 vals.append(registro.impuesto.nombre)
#                 vals.append(registro.impuesto_Monto)
#                 vals.append(registro.subtoal)
#                 vals.append(registro.total)
#                 dataTupla.append(tuple(vals))
#             descp['records'] = dataTupla
#             datos.append(descp)
#         return datos
#
#     @classmethod
#     def eliminar_datos_models_rel(cls,id):
#         datos = []
#         for model_name in cls.models_Rels:
#             model = globals()[model_name]
#             descp = {
#                 'tab_Name': model.descripcion,
#                 'model': model,
#                 'model_name': model_name
#             }
#             campo_relacion = cls.obtener_campo_rel(model)
#             registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#             dataTupla = []
#             for registro in registros:
#                 registro.delete_instance()
#
#     @classmethod
#     def obtener_campo_rel(cls,modelrel):
#         campo_relacion = None
#         for field_name, field_obj in modelrel._meta.fields.items():
#             if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
#                 campo_relacion = getattr(modelrel, field_name).name
#                 break
#         return campo_relacion
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         model.get_totales()
#         return model
#
#     def get_totales(self):
#         model = globals()['OrdenVentaLine']
#         registros = model.select().where(model.ordenventa_id == self.id)
#         self.subtoal = sum(f.subtoal for f in registros if f.subtoal is not None)
#         self.descuento = sum(f.descuento_Monto for f in registros if f.descuento_Monto is not None)
#         self.impuesto = sum(f.impuesto_Monto for f in registros if f.impuesto_Monto is not None)
#         self.total = sum(f.total for f in registros if f.total is not None)
#         self.total_Adeudado = sum(f.total for f in registros if f.total is not None)
#
#     def get_contexto(self):
#         contexto = {}
#         contexto['cliente'] = {
#             "nombre": self.cliente.nombre,
#             "cedula": self.cliente.cedula,
#             "email": self.cliente.email,
#             "telfono": self.cliente.telfono,
#         }
#         contexto['factura'] = {
#             'nombre': self.nombre,
#             'fecha': self.fecha,
#             'subtoal':format_currency(self.subtoal, 'CRC', locale='es_CR'),
#             'descuento':format_currency(self.descuento, 'CRC', locale='es_CR'),
#             'impuesto':format_currency(self.impuesto, 'CRC', locale='es_CR'),
#             'total':format_currency(self.total, 'CRC', locale='es_CR'),
#         }
#         registros = OrdenVentaLine.select().where(OrdenVentaLine.ordenventa_id == self.id)
#         vals = []
#         for registro in registros:
#             vals.append({
#                 'producto': registro.producto.nombre,
#                 'cantidad': registro.cantidad,
#                 'precio_Unitario': format_currency(registro.precio_Unitario, 'CRC', locale='es_CR'),
#                 'descuento_Porcentaje': f"{registro.descuento_Porcentaje}%",
#                 'descuento_Monto':format_currency(registro.descuento_Monto, 'CRC', locale='es_CR'),
#                 'impuesto': registro.impuesto.nombre,
#                 'impuesto_Monto': format_currency(registro.impuesto_Monto, 'CRC', locale='es_CR'),
#                 'subtoal': format_currency(registro.subtoal, 'CRC', locale='es_CR'),
#                 'total': format_currency(registro.total, 'CRC', locale='es_CR'),
#             })
#         contexto['factura']['facturadetalle'] = vals
#         return contexto
#
#     def buscar_crear_model(self):
#         factura_id = FacturaCliente.get_or_none(FacturaCliente.ordenventa_id == self.id)
#         if factura_id is None:
#             datos_dict = self.__data__.copy()
#             del datos_dict['id']
#             datos_dict['ordenventa_id'] = self.id
#             factura_id = FacturaCliente.crear_actualizar_desde_dict(datos_dict)
#             datos_modelrel = self.obtener_datos_models_rel(self.id)
#             for dato_modelrel in datos_modelrel:
#                 ids = [item[0] for item in dato_modelrel['records']]
#                 records = OrdenVentaLine.select().where(OrdenVentaLine.id.in_(ids))
#                 for record in records:
#                     record_dict = record.__data__.copy()
#                     del record_dict['id']
#                     del record_dict['ordenventa_id']
#                     record_dict['factura_id'] = factura_id.id
#                     FacturaClienteLine.crear_actualizar_desde_dict(record_dict)
#         return factura_id
#
# class OrdenVentaLine(BaseModel):
#     descripcion = "Lineas de la factura"
#     grupo_nombres = ['Información general', 'Información financiera','Información financiera']
#     cant_grupo = 3
#     accion_Config = {
#         'reporte': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     ordenventa_id = ForeignKey(OrdenVenta, backref='OrdenVenta', help_text="OrdenVenta", mostrar_Tree=False, mostrar_Form=False)
#     producto = ForeignKey(Producto, backref='Producto',valor_maximo="cantidad", help_text="Producto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,ochange=True)
#     cantidad = Float(help_text="Cantidad", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=1,ochange=True)
#     precio_Unitario = Decimal(help_text="Precio", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,max_digits=10, decimal_places=2)
#     descuento_Porcentaje = Float(help_text="Procentaje de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,ochange=True,default=0)
#     descuento_Monto = Decimal(help_text="Monto de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,default=0,max_digits=10, decimal_places=2)
#     impuesto = ForeignKey(ImpuestoVenta, backref='ImpuestoVenta', help_text="Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=0,null=True)
#     impuesto_Monto = Decimal(help_text="Monto de Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=1,default=0,max_digits=10, decimal_places=2)
#     subtoal = Decimal(help_text="Subtoal",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=2,null=True,max_digits=10, decimal_places=2)
#     total = Decimal(help_text="Total",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=3,null=True,max_digits=10, decimal_places=2)
#
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == Float:
#                 return float(valor)
#             elif tipo == Decimal:
#                 return decimal.Decimal(valor)
#             elif tipo == Boolean:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     def crear_actualizar_desde_model(cls):
#         print('s')
#         cls.save()
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for field_name, field_obj in cls._meta.fields.items():
#             help_text = getattr(field_obj, 'help_text', None)
#             mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
#             datos.append((help_text,mostrar_Tree))
#         return tuple(datos)
#
#     @classmethod
#     def obtener_columnas_para_treeviewrel(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for field_name, field_obj in cls._meta.fields.items():
#             help_text = getattr(field_obj, 'help_text', None)
#             mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
#             datos.append((help_text,mostrar_Tree))
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append(
#                 (
#                     model.id,
#                     model.nombre,
#                     model.tipo,
#                     model.costo,
#                     model.porcentaje_ganancia,
#                     model.precio_Venta,
#                     model.precio_Compra,
#                     model.impuesto_Venta.nombre,
#                     model.impuesto_Compra.nombre,
#                 )
#             )
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_campos_ochange(cls):
#         campos = []
#         for nombre_campo, campo in cls._meta.fields.items():
#             if getattr(campo, 'ochange', None) == True:
#                 campos.append(f"{nombre_campo}_field")
#         return campos
#
#     @classmethod
#     def obtener_resultado_ochange(cls,datos):
#         datos['producto'] = Producto.get(Producto.id ==  datos['producto'])
#         datos['cantidad'] = float(datos['cantidad'])
#         datos['descuento_Porcentaje'] = float(datos['descuento_Porcentaje'])
#         datos['precio_Unitario'] = datos['producto'].precio_Venta
#         datos['impuesto'] = datos['producto'].impuesto_Venta
#         datos['subtoal'] =  datos['precio_Unitario'] * decimal.Decimal(datos['cantidad'])
#         if datos['descuento_Porcentaje'] > 0 and isinstance(datos['descuento_Porcentaje'], (int, float, str, bool, bytes)):
#             datos['descuento_Monto'] = datos['subtoal'] * (decimal.Decimal(datos['descuento_Porcentaje']) / 100)
#         else:
#             datos['descuento_Monto'] = 0
#             datos['descuento_Porcentaje'] = 0
#
#         if datos['impuesto']:
#             datos['impuesto_Monto'] = (datos['subtoal'] - datos['descuento_Monto']) * (decimal.Decimal(datos['impuesto'].importe) / 100)
#         else:
#             datos['impuesto_Monto'] = 0
#
#         datos['total'] = datos['subtoal'] - datos['descuento_Monto'] + datos['impuesto_Monto']
#
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
#     @classmethod
#     def obtener_valor_maximo(cls,id):
#         producto =  Producto.get(Producto.id == id)
#         return producto.obtener_valor_maximo()
#
# class FacturaCliente(BaseModel):
#     descripcion = "Facturas de Cliente"
#     defalult_name = "FACTC #"
#     grupo_nombres = ['Información general', 'Información financiera']
#     cant_grupo = 2
#     auto_Guardar = True
#     models_Rels = ['FacturaClienteLine']
#     accion_Config = {
#         'reporte': True,
#         'reporte_Template': "factura_template.xml",
#         'correo_Template': "correo_reporte.xml",
#         'reporte_Correo': True,
#         'reporte_CorreoDescripcion': "Enviar factura al cliente",
#         'reporte_Descargar': True,
#         'reporte_DescargarDescripcion': "Descargar factura",
#         'crear_Modelo': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     ordenventa_id = ForeignKey(OrdenVenta, backref='OrdenVenta', help_text="OrdenVenta", mostrar_Tree=False,mostrar_Form=False,null=True)
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0)
#     terminada = Boolean(default=False,help_text="Terminada",mostrar_Tree=False,mostrar_Form=False)
#     cliente = ForeignKey(Cliente,null=True,required=True, backref='Cliente', help_text="Cliente", mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1)
#     fecha = Date(help_text="Fecha",default=datetime.date.today,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=0,posicion=2)
#     subtoal = Float(help_text="Subtotal",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=0,default=0)
#     descuento = Float(help_text="Descuento",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=1,default=0)
#     impuesto = Float(help_text="Impuesto",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=2,default=0)
#     total = Float(help_text="Total",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=3,default=0)
#     total_Adeudado = Float(help_text="Total adeudado",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=4,default=0)
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == FloatField:
#                 return float(valor)
#             elif tipo == BooleanField:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 seq = Secuencia.siguiente_valor(cls.__name__)
#                 if seq:
#                     datos_convertidos['nombre'] = seq
#                 return cls.create(**datos_convertidos)
#         else:
#             seq = Secuencia.siguiente_valor(cls.__name__)
#             if seq:
#                 datos_convertidos['nombre'] = seq
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for model in cls._meta.sorted_fields:
#             datos.append(model.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for instancia in cls.select():
#             fila = []
#             for field in cls._meta.sorted_fields:
#                 valor = getattr(instancia, field.name)
#
#                 if isinstance(field, ForeignKeyField):
#                     valor = getattr(instancia, f"{field.name}")
#                     valor = valor.nombre if valor is not None else ''
#
#                 # Reemplazar None por cadena vacía
#                 fila.append(valor if valor is not None else '')
#
#             datos.append(tuple(fila))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_datos_models_rel(cls,id):
#         datos = []
#         for model_name in cls.models_Rels:
#             model = globals()[model_name]
#             descp = {
#                 'tab_Name': model.descripcion,
#                 'model': model,
#                 'model_name': model_name
#             }
#             campo_relacion = cls.obtener_campo_rel(model)
#             registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#             dataTupla = []
#             for registro in registros:
#                 vals = []
#                 vals.append(registro.id)
#                 vals.append(registro.factura_id.id)
#                 vals.append(registro.producto.nombre)
#                 vals.append(registro.cantidad)
#                 vals.append(registro.precio_Unitario)
#                 vals.append(registro.descuento_Porcentaje)
#                 vals.append(registro.descuento_Monto)
#                 vals.append(registro.impuesto.nombre)
#                 vals.append(registro.impuesto_Monto)
#                 vals.append(registro.subtoal)
#                 vals.append(registro.total)
#                 dataTupla.append(tuple(vals))
#             descp['records'] = dataTupla
#             datos.append(descp)
#         return datos
#
#     @classmethod
#     def eliminar_datos_models_rel(cls,id):
#         datos = []
#         for model_name in cls.models_Rels:
#             model = globals()[model_name]
#             descp = {
#                 'tab_Name': model.descripcion,
#                 'model': model,
#                 'model_name': model_name
#             }
#             campo_relacion = cls.obtener_campo_rel(model)
#             registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#             dataTupla = []
#             for registro in registros:
#                 registro.delete_instance()
#
#     @classmethod
#     def obtener_campo_rel(cls,modelrel):
#         campo_relacion = None
#         for field_name, field_obj in modelrel._meta.fields.items():
#             if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
#                 campo_relacion = getattr(modelrel, field_name).name
#                 break
#         return campo_relacion
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         model.get_totales()
#         return model
#
#     def get_totales(self):
#         model = globals()['FacturaClienteLine']
#         registros = model.select().where(model.factura_id == self.id)
#         self.subtoal = sum(f.subtoal for f in registros if f.subtoal is not None)
#         self.descuento = sum(f.descuento_Monto for f in registros if f.descuento_Monto is not None)
#         self.impuesto = sum(f.impuesto_Monto for f in registros if f.impuesto_Monto is not None)
#         self.total = sum(f.total for f in registros if f.total is not None)
#         self.total_Adeudado = sum(f.total for f in registros if f.total is not None)
#
#     def get_contexto(self):
#         contexto = {}
#         contexto['cliente'] = {
#             "nombre": self.cliente.nombre,
#             "cedula": self.cliente.cedula,
#             "email": self.cliente.email,
#             "telfono": self.cliente.telfono,
#         }
#         contexto['factura'] = {
#             'nombre': self.nombre,
#             'fecha': self.fecha,
#             'subtoal':format_currency(self.subtoal, 'CRC', locale='es_CR'),
#             'descuento':format_currency(self.descuento, 'CRC', locale='es_CR'),
#             'impuesto':format_currency(self.impuesto, 'CRC', locale='es_CR'),
#             'total':format_currency(self.total, 'CRC', locale='es_CR'),
#         }
#         registros = FacturaClienteLine.select().where(FacturaClienteLine.factura_id == self.id)
#         vals = []
#         for registro in registros:
#             vals.append({
#                 'producto': registro.producto.nombre,
#                 'cantidad': registro.cantidad,
#                 'precio_Unitario': format_currency(registro.precio_Unitario, 'CRC', locale='es_CR'),
#                 'descuento_Porcentaje': f"{registro.descuento_Porcentaje}%",
#                 'descuento_Monto':format_currency(registro.descuento_Monto, 'CRC', locale='es_CR'),
#                 'impuesto': registro.impuesto.nombre,
#                 'impuesto_Monto': format_currency(registro.impuesto_Monto, 'CRC', locale='es_CR'),
#                 'subtoal': format_currency(registro.subtoal, 'CRC', locale='es_CR'),
#                 'total': format_currency(registro.total, 'CRC', locale='es_CR'),
#             })
#         contexto['factura']['facturadetalle'] = vals
#         return contexto
#
# class FacturaClienteLine(BaseModel):
#     descripcion = "Lineas de la factura"
#     grupo_nombres = ['Información general', 'Información financiera','Información financiera']
#     cant_grupo = 3
#     accion_Config = {
#         'reporte': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     factura_id = ForeignKey(FacturaCliente, backref='FacturaCliente', help_text="FacturaCliente", mostrar_Tree=False, mostrar_Form=False)
#     producto = ForeignKey(Producto, backref='Producto',valor_maximo="cantidad", help_text="Producto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,ochange=True)
#     cantidad = Float(help_text="Cantidad", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=1,ochange=True)
#     precio_Unitario = Decimal(help_text="Precio", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,max_digits=10, decimal_places=2)
#     descuento_Porcentaje = Float(help_text="Procentaje de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,ochange=True,default=0)
#     descuento_Monto = Decimal(help_text="Monto de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,default=0,max_digits=10, decimal_places=2)
#     impuesto = ForeignKey(ImpuestoVenta, backref='ImpuestoVenta', help_text="Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=0,null=True)
#     impuesto_Monto = Decimal(help_text="Monto de Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=1,default=0,max_digits=10, decimal_places=2)
#     subtoal = Decimal(help_text="Subtoal",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=2,null=True,max_digits=10, decimal_places=2)
#     total = Decimal(help_text="Total",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=3,null=True,max_digits=10, decimal_places=2)
#
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == Float:
#                 return float(valor)
#             elif tipo == Decimal:
#                 return decimal.Decimal(valor)
#             elif tipo == Boolean:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     def crear_actualizar_desde_model(cls):
#         print('s')
#         cls.save()
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for field_name, field_obj in cls._meta.fields.items():
#             help_text = getattr(field_obj, 'help_text', None)
#             mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
#             datos.append((help_text,mostrar_Tree))
#         return tuple(datos)
#
#     @classmethod
#     def obtener_columnas_para_treeviewrel(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for field_name, field_obj in cls._meta.fields.items():
#             help_text = getattr(field_obj, 'help_text', None)
#             mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
#             datos.append((help_text,mostrar_Tree))
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append(
#                 (
#                     model.id,
#                     model.nombre,
#                     model.tipo,
#                     model.costo,
#                     model.porcentaje_ganancia,
#                     model.precio_Venta,
#                     model.precio_Compra,
#                     model.impuesto_Venta.nombre,
#                     model.impuesto_Compra.nombre,
#                 )
#             )
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_campos_ochange(cls):
#         campos = []
#         for nombre_campo, campo in cls._meta.fields.items():
#             if getattr(campo, 'ochange', None) == True:
#                 campos.append(f"{nombre_campo}_field")
#         return campos
#
#     @classmethod
#     def obtener_resultado_ochange(cls,datos):
#         datos['producto'] = Producto.get(Producto.id ==  datos['producto'])
#         datos['cantidad'] = float(datos['cantidad'])
#         datos['descuento_Porcentaje'] = float(datos['descuento_Porcentaje'])
#         datos['precio_Unitario'] = datos['producto'].precio_Venta
#         datos['impuesto'] = datos['producto'].impuesto_Venta
#         datos['subtoal'] =  datos['precio_Unitario'] * decimal.Decimal(datos['cantidad'])
#         if datos['descuento_Porcentaje'] > 0 and isinstance(datos['descuento_Porcentaje'], (int, float, str, bool, bytes)):
#             datos['descuento_Monto'] = datos['subtoal'] * (decimal.Decimal(datos['descuento_Porcentaje']) / 100)
#         else:
#             datos['descuento_Monto'] = 0
#             datos['descuento_Porcentaje'] = 0
#
#         if datos['impuesto']:
#             datos['impuesto_Monto'] = (datos['subtoal'] - datos['descuento_Monto']) * (decimal.Decimal(datos['impuesto'].importe) / 100)
#         else:
#             datos['impuesto_Monto'] = 0
#
#         datos['total'] = datos['subtoal'] - datos['descuento_Monto'] + datos['impuesto_Monto']
#
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
#     @classmethod
#     def obtener_valor_maximo(cls,id):
#         producto =  Producto.get(Producto.id == id)
#         return producto.obtener_valor_maximo()
#
# class OrdenCompra(BaseModel):
#     descripcion = "Orden de compra"
#     defalult_name = "FACTC #"
#     grupo_nombres = ['Información general', 'Información financiera']
#     cant_grupo = 2
#     auto_Guardar = True
#     models_Rels = ['OrdenCompraLine']
#     accion_Config = {
#         'reporte': True,
#         'reporte_Template': "factura_template.xml",
#         'correo_Template': "correo_reporte.xml",
#         'reporte_Correo': True,
#         'reporte_CorreoDescripcion': "Enviar factura al cliente",
#         'reporte_Descargar': True,
#         'reporte_DescargarDescripcion': "Descargar factura",
#         'crear_Modelo': True,
#         'crear_Modelo_Nombre': "FacturaProveedor",
#         'crear_Modelo_Descripcion': " Crear Factura de Proveedor",
#     }
#
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0)
#     terminada = Boolean(default=False,help_text="Terminada",mostrar_Tree=False,mostrar_Form=False)
#     proveedor = ForeignKey(Proveedor,null=True,required=True, backref='Proveedor', help_text="Proveedor", mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1)
#     fecha = Date(help_text="Fecha",default=datetime.date.today,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=0,posicion=2)
#     subtoal = Float(help_text="Subtotal",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=0,default=0)
#     descuento = Float(help_text="Descuento",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=1,default=0)
#     impuesto = Float(help_text="Impuesto",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=2,default=0)
#     total = Float(help_text="Total",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=3,default=0)
#     total_Adeudado = Float(help_text="Total adeudado",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=4,default=0)
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == FloatField:
#                 return float(valor)
#             elif tipo == BooleanField:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 seq = Secuencia.siguiente_valor(cls.__name__)
#                 if seq:
#                     datos_convertidos['nombre'] = seq
#                 return cls.create(**datos_convertidos)
#         else:
#             seq = Secuencia.siguiente_valor(cls.__name__)
#             if seq:
#                 datos_convertidos['nombre'] = seq
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for model in cls._meta.sorted_fields:
#             datos.append(model.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for instancia in cls.select():
#             fila = []
#             for field in cls._meta.sorted_fields:
#                 valor = getattr(instancia, field.name)
#
#                 if isinstance(field, ForeignKeyField):
#                     valor = getattr(instancia, f"{field.name}")
#                     valor = valor.nombre if valor is not None else ''
#
#                 # Reemplazar None por cadena vacía
#                 fila.append(valor if valor is not None else '')
#
#             datos.append(tuple(fila))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_datos_models_rel(cls,id):
#         datos = []
#         for model_name in cls.models_Rels:
#             model = globals()[model_name]
#             descp = {
#                 'tab_Name': model.descripcion,
#                 'model': model,
#                 'model_name': model_name
#             }
#             campo_relacion = cls.obtener_campo_rel(model)
#             registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#             dataTupla = []
#             for registro in registros:
#                 vals = []
#                 vals.append(registro.id)
#                 vals.append(registro.ordencompra_id.id)
#                 vals.append(registro.producto.nombre)
#                 vals.append(registro.cantidad)
#                 vals.append(registro.precio_Unitario)
#                 vals.append(registro.descuento_Porcentaje)
#                 vals.append(registro.descuento_Monto)
#                 vals.append(registro.impuesto.nombre)
#                 vals.append(registro.impuesto_Monto)
#                 vals.append(registro.subtoal)
#                 vals.append(registro.total)
#                 dataTupla.append(tuple(vals))
#             descp['records'] = dataTupla
#             datos.append(descp)
#         return datos
#
#     @classmethod
#     def eliminar_datos_models_rel(cls,id):
#         datos = []
#         for model_name in cls.models_Rels:
#             model = globals()[model_name]
#             descp = {
#                 'tab_Name': model.descripcion,
#                 'model': model,
#                 'model_name': model_name
#             }
#             campo_relacion = cls.obtener_campo_rel(model)
#             registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#             dataTupla = []
#             for registro in registros:
#                 registro.delete_instance()
#
#     @classmethod
#     def obtener_campo_rel(cls,modelrel):
#         campo_relacion = None
#         for field_name, field_obj in modelrel._meta.fields.items():
#             if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
#                 campo_relacion = getattr(modelrel, field_name).name
#                 break
#         return campo_relacion
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         model.get_totales()
#         return model
#
#     def get_totales(self):
#         model = globals()['OrdenCompraLine']
#         registros = model.select().where(model.ordencompra_id == self.id)
#         self.subtoal = sum(f.subtoal for f in registros if f.subtoal is not None)
#         self.descuento = sum(f.descuento_Monto for f in registros if f.descuento_Monto is not None)
#         self.impuesto = sum(f.impuesto_Monto for f in registros if f.impuesto_Monto is not None)
#         self.total = sum(f.total for f in registros if f.total is not None)
#         self.total_Adeudado = sum(f.total for f in registros if f.total is not None)
#
#     def get_contexto(self):
#         contexto = {}
#         contexto['cliente'] = {
#             "nombre": self.cliente.nombre,
#             "cedula": self.cliente.cedula,
#             "email": self.cliente.email,
#             "telfono": self.cliente.telfono,
#         }
#         contexto['factura'] = {
#             'nombre': self.nombre,
#             'fecha': self.fecha,
#             'subtoal':format_currency(self.subtoal, 'CRC', locale='es_CR'),
#             'descuento':format_currency(self.descuento, 'CRC', locale='es_CR'),
#             'impuesto':format_currency(self.impuesto, 'CRC', locale='es_CR'),
#             'total':format_currency(self.total, 'CRC', locale='es_CR'),
#         }
#         registros = OrdenCompraLine.select().where(OrdenCompraLine.OrdenCompra_id == self.id)
#         vals = []
#         for registro in registros:
#             vals.append({
#                 'producto': registro.producto.nombre,
#                 'cantidad': registro.cantidad,
#                 'precio_Unitario': format_currency(registro.precio_Unitario, 'CRC', locale='es_CR'),
#                 'descuento_Porcentaje': f"{registro.descuento_Porcentaje}%",
#                 'descuento_Monto':format_currency(registro.descuento_Monto, 'CRC', locale='es_CR'),
#                 'impuesto': registro.impuesto.nombre,
#                 'impuesto_Monto': format_currency(registro.impuesto_Monto, 'CRC', locale='es_CR'),
#                 'subtoal': format_currency(registro.subtoal, 'CRC', locale='es_CR'),
#                 'total': format_currency(registro.total, 'CRC', locale='es_CR'),
#             })
#         contexto['factura']['facturadetalle'] = vals
#         return contexto
#
#     def buscar_crear_model(self):
#         factura_id = FacturaCliente.get_or_none(FacturaCliente.OrdenCompra_id == self.id)
#         if factura_id is None:
#             datos_dict = self.__data__.copy()
#             del datos_dict['id']
#             datos_dict['OrdenCompra_id'] = self.id
#             factura_id = FacturaCliente.crear_actualizar_desde_dict(datos_dict)
#             datos_modelrel = self.obtener_datos_models_rel(self.id)
#             for dato_modelrel in datos_modelrel:
#                 ids = [item[0] for item in dato_modelrel['records']]
#                 records = OrdenCompraLine.select().where(OrdenCompraLine.id.in_(ids))
#                 for record in records:
#                     record_dict = record.__data__.copy()
#                     del record_dict['id']
#                     del record_dict['OrdenCompra_id']
#                     record_dict['factura_id'] = factura_id.id
#                     FacturaClienteLine.crear_actualizar_desde_dict(record_dict)
#         return factura_id
#
# class OrdenCompraLine(BaseModel):
#     descripcion = "Lineas de la factura"
#     grupo_nombres = ['Información general', 'Información financiera','Información financiera']
#     cant_grupo = 3
#     accion_Config = {
#         'reporte': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     ordencompra_id = ForeignKey(OrdenCompra, backref='OrdenCompra', help_text="OrdenCompra", mostrar_Tree=False, mostrar_Form=False)
#     producto = ForeignKey(Producto, backref='Producto', help_text="Producto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,ochange=True)
#     cantidad = Float(help_text="Cantidad", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=1,ochange=True)
#     precio_Unitario = Decimal(help_text="Precio", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,max_digits=10, decimal_places=2)
#     descuento_Porcentaje = Float(help_text="Procentaje de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,ochange=True,default=0)
#     descuento_Monto = Decimal(help_text="Monto de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,default=0,max_digits=10, decimal_places=2)
#     impuesto = ForeignKey(ImpuestoVenta, backref='ImpuestoVenta', help_text="Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=0,null=True)
#     impuesto_Monto = Decimal(help_text="Monto de Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=1,default=0,max_digits=10, decimal_places=2)
#     subtoal = Decimal(help_text="Subtoal",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=2,null=True,max_digits=10, decimal_places=2)
#     total = Decimal(help_text="Total",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=3,null=True,max_digits=10, decimal_places=2)
#
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == Float:
#                 return float(valor)
#             elif tipo == Decimal:
#                 return decimal.Decimal(valor)
#             elif tipo == Boolean:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     def crear_actualizar_desde_model(cls):
#         print('s')
#         cls.save()
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for field_name, field_obj in cls._meta.fields.items():
#             help_text = getattr(field_obj, 'help_text', None)
#             mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
#             datos.append((help_text,mostrar_Tree))
#         return tuple(datos)
#
#     @classmethod
#     def obtener_columnas_para_treeviewrel(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for field_name, field_obj in cls._meta.fields.items():
#             help_text = getattr(field_obj, 'help_text', None)
#             mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
#             datos.append((help_text,mostrar_Tree))
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append(
#                 (
#                     model.id,
#                     model.nombre,
#                     model.tipo,
#                     model.costo,
#                     model.porcentaje_ganancia,
#                     model.precio_Venta,
#                     model.precio_Compra,
#                     model.impuesto_Venta.nombre,
#                     model.impuesto_Compra.nombre,
#                 )
#             )
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_campos_ochange(cls):
#         campos = []
#         for nombre_campo, campo in cls._meta.fields.items():
#             if getattr(campo, 'ochange', None) == True:
#                 campos.append(f"{nombre_campo}_field")
#         return campos
#
#     @classmethod
#     def obtener_resultado_ochange(cls,datos):
#         datos['producto'] = Producto.get(Producto.id ==  datos['producto'])
#         datos['cantidad'] = float(datos['cantidad'])
#         datos['descuento_Porcentaje'] = float(datos['descuento_Porcentaje'])
#         datos['precio_Unitario'] = datos['producto'].precio_Venta
#         datos['impuesto'] = datos['producto'].impuesto_Venta
#         datos['subtoal'] =  datos['precio_Unitario'] * decimal.Decimal(datos['cantidad'])
#         if datos['descuento_Porcentaje'] > 0 and isinstance(datos['descuento_Porcentaje'], (int, float, str, bool, bytes)):
#             datos['descuento_Monto'] = datos['subtoal'] * (decimal.Decimal(datos['descuento_Porcentaje']) / 100)
#         else:
#             datos['descuento_Monto'] = 0
#             datos['descuento_Porcentaje'] = 0
#
#         if datos['impuesto']:
#             datos['impuesto_Monto'] = (datos['subtoal'] - datos['descuento_Monto']) * (decimal.Decimal(datos['impuesto'].importe) / 100)
#         else:
#             datos['impuesto_Monto'] = 0
#
#         datos['total'] = datos['subtoal'] - datos['descuento_Monto'] + datos['impuesto_Monto']
#
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
# class FacturaProveedor(BaseModel):
#     descripcion = "Facturas de proveedor"
#     defalult_name = "FACTC #"
#     grupo_nombres = ['Información general', 'Información financiera']
#     cant_grupo = 2
#     auto_Guardar = True
#     models_Rels = ['FacturaProveedorLine']
#     accion_Config = {
#         'reporte': True,
#         'reporte_Template': "factura_template.xml",
#         'correo_Template': "correo_reporte.xml",
#         'reporte_Correo': True,
#         'reporte_CorreoDescripcion': "Enviar factura al cliente",
#         'reporte_Descargar': True,
#         'reporte_DescargarDescripcion': "Descargar factura",
#         'crear_Modelo': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     ordencompra_id = ForeignKey(OrdenCompra, backref='OrdenCompra', help_text="OrdenCompra", mostrar_Tree=False,mostrar_Form=False,null=True)
#     nombre = Char(help_text="Nombre",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=0)
#     terminada = Boolean(default=False,help_text="Terminada",mostrar_Tree=False,mostrar_Form=False)
#     proveedor = ForeignKey(Proveedor,null=True,required=True, backref='Proveedor', help_text="Proveedor", mostrar_Tree=True,mostrar_Form=True,numero_Grupo=0,posicion=1)
#     fecha = Date(help_text="Fecha",default=datetime.date.today,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=0,posicion=2)
#     subtoal = Float(help_text="Subtotal",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=0,default=0)
#     descuento = Float(help_text="Descuento",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=1,default=0)
#     impuesto = Float(help_text="Impuesto",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=2,default=0)
#     total = Float(help_text="Total",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=3,default=0)
#     total_Adeudado = Float(help_text="Total adeudado",null=True,mostrar_Tree=True,mostrar_Form=True,lectura=True,numero_Grupo=1,posicion=4,default=0)
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == FloatField:
#                 return float(valor)
#             elif tipo == BooleanField:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 seq = Secuencia.siguiente_valor(cls.__name__)
#                 if seq:
#                     datos_convertidos['nombre'] = seq
#                 return cls.create(**datos_convertidos)
#         else:
#             seq = Secuencia.siguiente_valor(cls.__name__)
#             if seq:
#                 datos_convertidos['nombre'] = seq
#             return cls.create(**datos_convertidos)
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for model in cls._meta.sorted_fields:
#             datos.append(model.name)
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for instancia in cls.select():
#             fila = []
#             for field in cls._meta.sorted_fields:
#                 valor = getattr(instancia, field.name)
#
#                 if isinstance(field, ForeignKeyField):
#                     valor = getattr(instancia, f"{field.name}")
#                     valor = valor.nombre if valor is not None else ''
#
#                 # Reemplazar None por cadena vacía
#                 fila.append(valor if valor is not None else '')
#
#             datos.append(tuple(fila))
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_datos_models_rel(cls,id):
#         datos = []
#         for model_name in cls.models_Rels:
#             model = globals()[model_name]
#             descp = {
#                 'tab_Name': model.descripcion,
#                 'model': model,
#                 'model_name': model_name
#             }
#             campo_relacion = cls.obtener_campo_rel(model)
#             registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#             dataTupla = []
#             for registro in registros:
#                 vals = []
#                 vals.append(registro.id)
#                 vals.append(registro.factura_id.id)
#                 vals.append(registro.producto.nombre)
#                 vals.append(registro.cantidad)
#                 vals.append(registro.precio_Unitario)
#                 vals.append(registro.descuento_Porcentaje)
#                 vals.append(registro.descuento_Monto)
#                 vals.append(registro.impuesto.nombre)
#                 vals.append(registro.impuesto_Monto)
#                 vals.append(registro.subtoal)
#                 vals.append(registro.total)
#                 dataTupla.append(tuple(vals))
#             descp['records'] = dataTupla
#             datos.append(descp)
#         return datos
#
#     @classmethod
#     def eliminar_datos_models_rel(cls,id):
#         datos = []
#         for model_name in cls.models_Rels:
#             model = globals()[model_name]
#             descp = {
#                 'tab_Name': model.descripcion,
#                 'model': model,
#                 'model_name': model_name
#             }
#             campo_relacion = cls.obtener_campo_rel(model)
#             registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
#             dataTupla = []
#             for registro in registros:
#                 registro.delete_instance()
#
#     @classmethod
#     def obtener_campo_rel(cls,modelrel):
#         campo_relacion = None
#         for field_name, field_obj in modelrel._meta.fields.items():
#             if isinstance(field_obj, ForeignKeyField) and field_obj.rel_model == cls:
#                 campo_relacion = getattr(modelrel, field_name).name
#                 break
#         return campo_relacion
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         model.get_totales()
#         return model
#
#     def get_totales(self):
#         model = globals()['FacturaClienteLine']
#         registros = model.select().where(model.factura_id == self.id)
#         self.subtoal = sum(f.subtoal for f in registros if f.subtoal is not None)
#         self.descuento = sum(f.descuento_Monto for f in registros if f.descuento_Monto is not None)
#         self.impuesto = sum(f.impuesto_Monto for f in registros if f.impuesto_Monto is not None)
#         self.total = sum(f.total for f in registros if f.total is not None)
#         self.total_Adeudado = sum(f.total for f in registros if f.total is not None)
#
#     def get_contexto(self):
#         contexto = {}
#         contexto['cliente'] = {
#             "nombre": self.cliente.nombre,
#             "cedula": self.cliente.cedula,
#             "email": self.cliente.email,
#             "telfono": self.cliente.telfono,
#         }
#         contexto['factura'] = {
#             'nombre': self.nombre,
#             'fecha': self.fecha,
#             'subtoal':format_currency(self.subtoal, 'CRC', locale='es_CR'),
#             'descuento':format_currency(self.descuento, 'CRC', locale='es_CR'),
#             'impuesto':format_currency(self.impuesto, 'CRC', locale='es_CR'),
#             'total':format_currency(self.total, 'CRC', locale='es_CR'),
#         }
#         registros = FacturaClienteLine.select().where(FacturaClienteLine.factura_id == self.id)
#         vals = []
#         for registro in registros:
#             vals.append({
#                 'producto': registro.producto.nombre,
#                 'cantidad': registro.cantidad,
#                 'precio_Unitario': format_currency(registro.precio_Unitario, 'CRC', locale='es_CR'),
#                 'descuento_Porcentaje': f"{registro.descuento_Porcentaje}%",
#                 'descuento_Monto':format_currency(registro.descuento_Monto, 'CRC', locale='es_CR'),
#                 'impuesto': registro.impuesto.nombre,
#                 'impuesto_Monto': format_currency(registro.impuesto_Monto, 'CRC', locale='es_CR'),
#                 'subtoal': format_currency(registro.subtoal, 'CRC', locale='es_CR'),
#                 'total': format_currency(registro.total, 'CRC', locale='es_CR'),
#             })
#         contexto['factura']['facturadetalle'] = vals
#         return contexto
#
# class FacturaProveedorLine(BaseModel):
#     descripcion = "Lineas de la factura"
#     grupo_nombres = ['Información general', 'Información financiera','Información financiera']
#     cant_grupo = 3
#     accion_Config = {
#         'reporte': False,
#     }
#     id = Auto(mostrar_Tree=False,mostrar_Form=False,help_text="ID")
#     factura_id = ForeignKey(FacturaProveedor, backref='FacturaProveedor', help_text="FacturaProveedor", mostrar_Tree=False, mostrar_Form=False)
#     producto = ForeignKey(Producto, backref='Producto',valor_maximo="cantidad", help_text="Producto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=0,ochange=True)
#     cantidad = Float(help_text="Cantidad", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=1,ochange=True)
#     precio_Unitario = Decimal(help_text="Precio", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=0,posicion=2,null=True,max_digits=10, decimal_places=2)
#     descuento_Porcentaje = Float(help_text="Procentaje de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=0,ochange=True,default=0)
#     descuento_Monto = Decimal(help_text="Monto de descuento", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=1,posicion=1,default=0,max_digits=10, decimal_places=2)
#     impuesto = ForeignKey(ImpuestoVenta, backref='ImpuestoVenta', help_text="Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=0,null=True)
#     impuesto_Monto = Decimal(help_text="Monto de Impuesto", mostrar_Tree=True, mostrar_Form=True,numero_Grupo=2,posicion=1,default=0,max_digits=10, decimal_places=2)
#     subtoal = Decimal(help_text="Subtoal",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=2,null=True,max_digits=10, decimal_places=2)
#     total = Decimal(help_text="Total",mostrar_Tree=True,mostrar_Form=True,numero_Grupo=2,posicion=3,null=True,max_digits=10, decimal_places=2)
#
#
#     @classmethod
#     def crear_actualizar_desde_dict(cls, datos):
#         """
#         Crea o actualiza un registro a partir de un diccionario.
#         Convierte automáticamente los valores a sus tipos correctos.
#         """
#         campos = cls._meta.fields
#
#         def convertir_valor(campo, valor):
#             tipo = type(campos[campo])
#             if tipo == IntegerField:
#                 return int(valor)
#             elif tipo == Float:
#                 return float(valor)
#             elif tipo == Decimal:
#                 return decimal.Decimal(valor)
#             elif tipo == Boolean:
#                 return valor.lower() in ("1", "true", "yes", "on")
#             else:
#                 return valor  # CharField, TextField, etc.
#
#         datos_convertidos = {}
#         for campo, valor in datos.items():
#             if campo in campos and valor != "":
#                 try:
#                     datos_convertidos[campo] = convertir_valor(campo, valor)
#                 except Exception as e:
#                     raise ValueError(f"Error al convertir el campo '{campo}': {e}")
#
#         if 'id' in datos_convertidos:
#             try:
#                 instancia = cls.get_by_id(datos_convertidos['id'])
#                 for campo, valor in datos_convertidos.items():
#                     if campo != 'id':
#                         setattr(instancia, campo, valor)
#                 instancia.save()
#                 return instancia
#             except cls.DoesNotExist:
#                 datos_convertidos.pop('id')
#                 return cls.create(**datos_convertidos)
#         else:
#             return cls.create(**datos_convertidos)
#
#     def crear_actualizar_desde_model(cls):
#         print('s')
#         cls.save()
#
#     @classmethod
#     def obtener_columnas_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for field_name, field_obj in cls._meta.fields.items():
#             help_text = getattr(field_obj, 'help_text', None)
#             mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
#             datos.append((help_text,mostrar_Tree))
#         return tuple(datos)
#
#     @classmethod
#     def obtener_columnas_para_treeviewrel(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         datos = []
#         for field_name, field_obj in cls._meta.fields.items():
#             help_text = getattr(field_obj, 'help_text', None)
#             mostrar_Tree = getattr(field_obj, 'mostrar_Tree', None)
#             datos.append((help_text,mostrar_Tree))
#         return tuple(datos)
#
#     @classmethod
#     def obtener_datos_para_treeview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append(
#                 (
#                     model.id,
#                     model.nombre,
#                     model.tipo,
#                     model.costo,
#                     model.porcentaje_ganancia,
#                     model.precio_Venta,
#                     model.precio_Compra,
#                     model.impuesto_Venta.nombre,
#                     model.impuesto_Compra.nombre,
#                 )
#             )
#         return datos
#
#     @classmethod
#     def obtener_datos_para_atucompleteview(cls):
#         """
#         Devuelve una lista de tuplas con los datos de todos los usuarios,
#         lista para insertar en un ttk.Treeview.
#         """
#         registros = cls.select()
#         datos = []
#         for model in registros:
#             datos.append((model.id,model.nombre))
#         return datos
#
#     @classmethod
#     def obtener_campos_ochange(cls):
#         campos = []
#         for nombre_campo, campo in cls._meta.fields.items():
#             if getattr(campo, 'ochange', None) == True:
#                 campos.append(f"{nombre_campo}_field")
#         return campos
#
#     @classmethod
#     def obtener_resultado_ochange(cls,datos):
#         datos['producto'] = Producto.get(Producto.id ==  datos['producto'])
#         datos['cantidad'] = float(datos['cantidad'])
#         datos['descuento_Porcentaje'] = float(datos['descuento_Porcentaje'])
#         datos['precio_Unitario'] = datos['producto'].precio_Venta
#         datos['impuesto'] = datos['producto'].impuesto_Venta
#         datos['subtoal'] =  datos['precio_Unitario'] * decimal.Decimal(datos['cantidad'])
#         if datos['descuento_Porcentaje'] > 0 and isinstance(datos['descuento_Porcentaje'], (int, float, str, bool, bytes)):
#             datos['descuento_Monto'] = datos['subtoal'] * (decimal.Decimal(datos['descuento_Porcentaje']) / 100)
#         else:
#             datos['descuento_Monto'] = 0
#             datos['descuento_Porcentaje'] = 0
#
#         if datos['impuesto']:
#             datos['impuesto_Monto'] = (datos['subtoal'] - datos['descuento_Monto']) * (decimal.Decimal(datos['impuesto'].importe) / 100)
#         else:
#             datos['impuesto_Monto'] = 0
#
#         datos['total'] = datos['subtoal'] - datos['descuento_Monto'] + datos['impuesto_Monto']
#
#         return datos
#
#     @classmethod
#     def obtener_con_accion(cls, id):
#         model = cls.get(cls.id == id)
#         return model
#
#     @classmethod
#     def obtener_valor_maximo(cls,id):
#         producto =  Producto.get(Producto.id == id)
#         return producto.existencias
#
# class Secuencia(BaseModel):
#     nombre = Char(unique=True)
#     prefijo = Char(default="SEQ")
#     padding = Integer(default=4)
#     ultimo_numero = Integer(default=0)
#
#     @classmethod
#     def siguiente_valor(cls,model_name):
#         seqs = cls.select().where(cls.nombre == model_name)
#         for seq in seqs:
#             seq.ultimo_numero += 1
#             seq.save()
#
#             partes = [seq.prefijo]
#             partes.append(str(seq.ultimo_numero).zfill(seq.padding))
#             return "/".join(partes)
#         return False
#
# class Ajuste(BaseModel):
#     id = Auto(mostrar_Tree=False, mostrar_Form=False, help_text="ID")
#     key = Char(help_text="Nombre", mostrar_Tree=True, mostrar_Form=True)
#     valor = Char(help_text="Valor", mostrar_Tree=True, mostrar_Form=True,null=True)
#
#
# db.connect()
# db.create_tables(
#     [
#         User,
#         Cliente,
#         Proveedor,
#         Producto,
#         ImpuestoVenta,
#         ImpuestoCompra,
#         Ajuste,
#         OrdenVenta,
#         OrdenVentaLine,
#         FacturaCliente,
#         FacturaClienteLine,
#         OrdenCompra,
#         OrdenCompraLine,
#         FacturaProveedor,
#         FacturaProveedorLine,
#         Secuencia,
#
#     ])
#
# default_user = {
#     "email": "admin",
#     "nombre": "Administrador",
#     "cedula": "00000000",
#     "password": encriptar_password("admin"),
#     "permisos": json.dumps({"admin": True})
# }
#
# default_Ajuste = [
#     {
#         "key": 'color.fondo',
#         "valor": '#F8F9FA',
#     },
#     {
#         "key": 'color.frame',
#         "valor": '#FEFEFF',
#     },
#     {
#         "key": 'color.btn.1',
#         "valor": '#05d7ff',
#     },
#     {
#         "key": 'color.btn.2',
#         "valor": 'BLACK',
#     },
#     {
#         "key": 'color.btn.3',
#         "valor": '#65e7ff',
#     },
#     {
#         "key": 'color.btn.4',
#         "valor": 'WHITE',
#     },
#     {
#         "key": 'img.logo',
#         "valor": 'assets/images/img_login_sing.png',
#     },
#     {
#         "key": 'smtp.servidor',
#         "valor": 'smtp.gmail.com',
#     },
#     {
#         "key": 'smtp.puerto',
#         "valor": '465',
#     },
#     {
#         "key": 'smtp.usuario',
#         "valor": 'algo@gmail.com',
#     },
#     {
#         "key": 'smtp.contrasena',
#         "valor": 'AAAAA',
#     },
#     {
#         "key": 'empresa.nombre',
#         "valor": 'Empresa S.A',
#     },
#     {
#         "key": 'empresa.telefono',
#         "valor": '88888888',
#     },
#     {
#         "key": 'empresa.correo',
#         "valor": 'empresa@empresa.com',
#     },
#     {
#         "key": 'empresa.direccion',
#         "valor": 'Av. Central 123, Edificio Empresarial Colima, Piso 4, San José, Costa Rica',
#     },
#
# ]
#
# default_Seq = [
#     {
#         "nombre": 'FacturaCliente',
#         "prefijo": 'FACT',
#         "padding": 4,
#         "ultimo_numero": 0,
#     },
#     {
#         "nombre": 'OrdenVenta',
#         "prefijo": 'OV',
#         "padding": 4,
#         "ultimo_numero": 0,
#     },
#     {
#         "nombre": 'FacturaProveedor',
#         "prefijo": 'FACTP',
#         "padding": 4,
#         "ultimo_numero": 0,
#     },
#     {
#         "nombre": 'OrdenCompra',
#         "prefijo": 'OC',
#         "padding": 4,
#         "ultimo_numero": 0,
#     },
# ]
#
#
# if not User.select().where(User.email == default_user["email"]).exists():
#     User.create(**default_user)
#
# for ajsute in default_Ajuste:
#     if not Ajuste.select().where(Ajuste.key == ajsute["key"]).exists():
#         Ajuste.create(**ajsute)
#
# for seq in default_Seq:
#     if not Secuencia.select().where(Secuencia.nombre == seq["nombre"]).exists():
#         Secuencia.create(**seq)
#
