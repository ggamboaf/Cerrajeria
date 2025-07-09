from . import *
from .base import BaseModel
from .custom_fields import *

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


