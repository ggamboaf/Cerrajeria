from peewee import *

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