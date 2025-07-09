from .base import BaseModel
from .custom_fields import *

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

