import tkinter as tk
import socket
import sys
from views.view_login import ViewLogin
from views.view_principal import ViewPrincipal

def verificar_instancia_unica(puerto=65432):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("localhost", puerto))
    except socket.error:
        print("Ya hay una instancia del programa en ejecución.")
        sys.exit()

socket_bloqueo = verificar_instancia_unica()

def start():
    login_root = tk.Tk()
    ViewLogin(login_root, on_success=mostrar_ventana_principal,on_reset=start)
    login_root.mainloop()

def mostrar_ventana_principal(user):
    ViewPrincipal(tk.Tk(),user)

if __name__ == "__main__":
    start()
