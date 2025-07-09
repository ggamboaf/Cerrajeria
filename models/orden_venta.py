import datetime
import decimal

from babel.numbers import format_currency

from . import *
from .base import BaseModel
from .custom_fields import *


class OrdenVenta(BaseModel):
    descripcion = "Orden de venta"
    defalult_name = "FACTC #"
    grupo_nombres = ['Información general', 'Información financiera']
    cant_grupo = 2
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
        """
        Devuelve una lista de tuplas con los datos de todos los usuarios,
        lista para insertar en un ttk.Treeview.
        """
        datos = []
        for instancia in cls.select():
            fila = []
            for field in cls._meta.sorted_fields:
                valor = getattr(instancia, field.name)

                if isinstance(field, ForeignKeyField):
                    valor = getattr(instancia, f"{field.name}")
                    valor = valor.nombre if valor is not None else ''

                # Reemplazar None por cadena vacía
                fila.append(valor if valor is not None else '')

            datos.append(tuple(fila))
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
            registros = model.select().where(getattr(model, campo_relacion)== id).order_by(model.id)
            dataTupla = []
            for registro in registros:
                vals = []
                vals.append(registro.id)
                vals.append(registro.ordenventa_id.id)
                vals.append(registro.producto.nombre)
                vals.append(registro.cantidad)
                vals.append(registro.precio_Unitario)
                vals.append(registro.descuento_Porcentaje)
                vals.append(registro.descuento_Monto)
                vals.append(registro.impuesto.nombre)
                vals.append(registro.impuesto_Monto)
                vals.append(registro.subtoal)
                vals.append(registro.total)
                dataTupla.append(tuple(vals))
            descp['records'] = dataTupla
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
                ids = [item[0] for item in dato_modelrel['records']]
                records = OrdenVentaLine.select().where(OrdenVentaLine.id.in_(ids))
                for record in records:
                    record_dict = record.__data__.copy()
                    del record_dict['id']
                    del record_dict['ordenventa_id']
                    record_dict['factura_id'] = factura_id.id
                    FacturaClienteLine.crear_actualizar_desde_dict(record_dict)
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



