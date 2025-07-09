from .base import BaseModel
from .custom_fields import *

class User(BaseModel):
    id = Auto(mostrar_Tree=False, mostrar_Form=False)
    nombre = Char(mostrar_Tree=True)
    email = Char(unique=True, mostrar_Tree=True)
    cedula = Char(mostrar_Tree=True)
    password = Char(mostrar_Tree=False, mostrar_Form=False)
    codigo = Char(mostrar_Tree=False, mostrar_Form=False, null=True)
    permisos = Text(default='{}', mostrar_Tree=False, mostrar_Form=True)
