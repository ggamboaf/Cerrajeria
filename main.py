import tkinter as tk
from views.view_login import ViewLogin
from views.view_principal import ViewPrincipal

def start():
    login_root = tk.Tk()
    ViewLogin(login_root, on_success=mostrar_ventana_principal,on_reset=start)
    login_root.mainloop()

def mostrar_ventana_principal(user):
    ViewPrincipal(tk.Tk(),user)

if __name__ == "__main__":
    start()
