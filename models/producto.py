import decimal

from . import *
from .base import BaseModel
from .custom_fields import *

class Producto(BaseModel):
    plantilla_Name = "Plantilla Productos.xlsx"
    xlsx_Name = "Productos.xlsx"
    descripcion = "Producto"
    grupo_nombres = ['Información general','Información financiera']
    cant_grupo = 2
    tipo_choices = (
        ('Producto', 'Producto'),
        ('Servicio', 'Servicio'),
    )
    accion_Config = {
        'reporte': False,
    }
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
