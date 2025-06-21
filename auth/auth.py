import json

from models.models import User
from utils.utils import encriptar_password, verificar_password
from tkinter import messagebox
from peewee import IntegrityError


def registar_user(email, name, password, permisos=None):
    if permisos is None:
        permisos = {}
    hashed_password = encriptar_password(password)
    try:
        User.create(email=email, nombre=nombre,cedula=cedula, password=hashed_password, permisos=json.dumps(permissions))
        messagebox.showinfo("Éxito", "¡Usuario registrado exitosamente!")
    except IntegrityError:
        messagebox.showerror("Error", "¡El correo electrónico ya está registrado!")

def authenticacion_user(email, password):
    try:
        user = User.get(User.email == email)
        if verificar_password(password, user.password):
            user.permisos = json.loads(user.permisos)
            return user
        else:
            messagebox.showerror("Error", "¡Contraseña incorrecta!")
    except User.DoesNotExist:
        messagebox.showerror("Error", "¡Usuario no encontrado!")

def restablecer_user(codigo, password):
    hashed_password = encriptar_password(password)
    try:
        user = User.get(User.codigo == codigo)
        user.codigo = None
        user.password = hashed_password
        user.save()
        messagebox.showinfo("Éxito", "¡Contraseña restablecida!")
    except IntegrityError:
        messagebox.showerror("Error", "¡El correo electrónico ya está registrado!")

