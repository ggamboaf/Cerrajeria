from models.models import *

class ParametroAjuste:
    def __init__(self):
        self._valores = {
            "color_fondo": Ajuste.get(Ajuste.key == "color.fondo").valor,
            "color_frame": Ajuste.get(Ajuste.key == "color.frame").valor,
            "color_btn_1": Ajuste.get(Ajuste.key == "color.btn.1").valor,
            "color_btn_2": Ajuste.get(Ajuste.key == "color.btn.2").valor,
            "color_btn_3": Ajuste.get(Ajuste.key == "color.btn.3").valor,
            "color_btn_4": Ajuste.get(Ajuste.key == "color.btn.4").valor,
            "img_logo": Ajuste.get(Ajuste.key == "img.logo").valor,
            "smtp_servidor": Ajuste.get(Ajuste.key == "smtp.servidor").valor,
            "smtp_puerto": Ajuste.get(Ajuste.key == "smtp.puerto").valor,
            "smtp_usuario": Ajuste.get(Ajuste.key == "smtp.usuario").valor,
            "smtp_contrasena": Ajuste.get(Ajuste.key == "smtp.contrasena").valor,
            "empresa_nombre": Ajuste.get(Ajuste.key == "empresa.nombre").valor,
            "empresa_telefono": Ajuste.get(Ajuste.key == "empresa.telefono").valor,
            "empresa_correo": Ajuste.get(Ajuste.key == "empresa.correo").valor,
            "empresa_direccion": Ajuste.get(Ajuste.key == "empresa.direccion").valor,
        }

        # Asignar los valores iniciales sin disparar __setattr__
        for k, v in self._valores.items():
            super().__setattr__(k, v)

    def __setattr__(self, nombre, valor):
        if nombre in ["color_fondo", "color_frame", "color_btn_1", "color_btn_2", "color_btn_3", "color_btn_4","smtp_servidor","smtp_puerto","smtp_usuario","smtp_contrasena"]:
            print(f"Se cambió '{nombre}' a {valor}")
            self.cambiar_color(nombre, valor)
        super().__setattr__(nombre, valor)

    def cambiar_color(self, nombre, valor):
        ajsute = Ajuste.get(Ajuste.key == nombre.replace("_","."))
        ajsute.valor = valor
        ajsute.save()

    def get_contexto_empresa(self,contexto):
        contexto['logo'] = self._valores["empresa_nombre"]
        contexto['informacionEmpresa'] = {
            'nombre': self._valores["empresa_nombre"],
            'email': self._valores["empresa_correo"],
            'telfono': self._valores["empresa_telefono"],
            'direccion': self._valores["empresa_direccion"],
        }
        return contexto
