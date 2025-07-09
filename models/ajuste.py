from . import *
from .base import BaseModel
from .custom_fields import *

class Ajuste(BaseModel):
    id = Auto(mostrar_Tree=False, mostrar_Form=False, help_text="ID")
    key = Char(help_text="Nombre", mostrar_Tree=True, mostrar_Form=True)
    valor = Char(help_text="Valor", mostrar_Tree=True, mostrar_Form=True,null=True)




