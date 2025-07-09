
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ViewLogin:
    def __init__(self, master, on_success, on_reset):
        self.master = master
        self.on_success = on_success
        self.on_reset = on_reset

        self.master.title("Login")
        self.master.geometry("600x400")
        self.master.minsize(400, 300)

        self.frame = tk.Frame(master, bg="#f0f0f0")
        self.frame.pack(fill="both", expand=True)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.login_frame = tk.Frame(self.frame, bg="white", padx=20, pady=20, relief="groove", bd=2)
        self.login_frame.grid(row=0, column=0, sticky="nsew", padx=100, pady=50)

        for i in range(6):
            self.login_frame.rowconfigure(i, weight=1)
        self.login_frame.columnconfigure(0, weight=1)

        self.title_label = tk.Label(self.login_frame, text="Iniciar Sesión", font=("Arial", 16, "bold"), bg="white")
        self.title_label.grid(row=0, column=0, sticky="n", pady=(0, 10))

        self.email_label = tk.Label(self.login_frame, text="Correo Electrónico", bg="white", anchor="w")
        self.email_label.grid(row=1, column=0, sticky="ew", pady=(5, 0))

        self.email_entry = tk.Entry(self.login_frame)
        self.email_entry.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        self.password_label = tk.Label(self.login_frame, text="Contraseña", bg="white", anchor="w")
        self.password_label.grid(row=3, column=0, sticky="ew", pady=(5, 0))

        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=4, column=0, sticky="ew", pady=(0, 10))

        self.login_button = tk.Button(self.login_frame, text="Iniciar Sesión", command=self.verificar_user, bg="#4CAF50", fg="white")
        self.login_button.grid(row=5, column=0, sticky="ew", pady=(10, 5))

        self.reset_button = tk.Button(self.login_frame, text="Restablecer contraseña", command=self.envio_codigo, bg="#2196F3", fg="white")
        self.reset_button.grid(row=6, column=0, sticky="ew")

    def verificar_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        print(f"Verificando usuario: {email} con contraseña: {password}")
        self.master.destroy()
        self.on_success(email)

    def envio_codigo(self):
        print("Enviando código de restablecimiento...")
        self.master.destroy()
        self.on_reset()
