import tkinter as tk

from models.models import User
from utils.enviar_correo import EnviarCorreo
from datetime import datetime
from tkinter import messagebox, ttk
from auth.auth import authenticacion_user, restablecer_user
from PIL import Image, ImageTk
from utils.ajuste import ParametroAjuste
from utils.crear import Crear
import random
from models import *

class ViewLogin:
    def __init__(self, master, on_success, on_reset):
        self.usuario = None
        self.codigo_Entry = None
        self.master = master
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        self.master.title("Login")
        self.master.state('zoomed')
        self.on_success = on_success
        self.on_reset = on_reset
        self.canvas = None

        self.show_login()

    def clear_canvas(self):
        if self.canvas:
            self.canvas.destroy()
            self.canvas = None

    def show_login(self):
        self.clear_canvas()

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        self.canvas = tk.Canvas(self.master, width=screen_width, height=screen_height, bg=self.ParametroAjuste.color_fondo)
        self.canvas.pack(fill="both", expand=True)

        frame_width = min(400, screen_width // 3)
        frame_height = min(600, screen_height // 2)
        frame_x = (screen_width - frame_width) // 2
        frame_y = (screen_height - frame_height) // 2

        login_frame = tk.Frame(self.canvas, bg=self.ParametroAjuste.color_frame, bd=2, relief="groove")
        self.canvas.create_window(frame_x, frame_y, window=login_frame, anchor="nw", width=frame_width, height=frame_height)

        for i in range(8):
            login_frame.rowconfigure(i, weight=1)
        login_frame.columnconfigure(0, weight=1)
        login_frame.columnconfigure(1, weight=4)

        # Logo
        try:
            image = Image.open(self.ParametroAjuste.img_logo)
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image = image.resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
        except Exception:
            photo = None
        img_login_sing = tk.Label(login_frame, image=photo, bg=self.ParametroAjuste.color_frame)
        img_login_sing.image = photo
        img_login_sing.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Correo Electrónico
        correo_Label = tk.Label(login_frame, text="Correo Electrónico", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        correo_Label.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 0))

        self.correo_Entry = ttk.Entry(login_frame, font=('Arial', 12, 'bold'))
        self.correo_Entry.grid(row=2, column=1, sticky="ew", padx=(0, 40), pady=(2, 0))

        try:
            usuario_icon_img = Image.open("assets/images/usuario_icon.png")
            usuario_icon_photo = ImageTk.PhotoImage(usuario_icon_img)
        except Exception:
            usuario_icon_photo = None
        usuario_icon = tk.Label(login_frame, image=usuario_icon_photo, bg=self.ParametroAjuste.color_frame)
        usuario_icon.image = usuario_icon_photo
        usuario_icon.grid(row=2, column=0, sticky="e", padx=(10, 0))

        # Contraseña
        password_Label = tk.Label(login_frame, text="Contraseña", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        password_Label.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20, pady=(20, 0))

        self.password_Entry =  ttk.Entry(login_frame, font=('Arial', 12, 'bold'))
        self.password_Entry.grid(row=4, column=1, sticky="ew", padx=(0, 40), pady=(2, 0))

        try:
            password_icon_img = Image.open("assets/images/password_icon.png")
            password_icon_photo = ImageTk.PhotoImage(password_icon_img)
        except Exception:
            password_icon_photo = None
        password_icon = tk.Label(login_frame, image=password_icon_photo, bg=self.ParametroAjuste.color_frame)
        password_icon.image = password_icon_photo
        password_icon.grid(row=4, column=0, sticky="e", padx=(10, 0))

        # Botón Iniciar Sesión
        btn_Login = self.Crear.crear_btn(text="Iniciar Sesión", ajsutes=self.ParametroAjuste)
        btn_Login.config(command=self.verificar_User)
        btn_Login.grid(row=5, column=0, columnspan=2, sticky="ew", padx=20, pady=(30, 5),in_=login_frame)

        # Botón Restablecer contraseña
        btn_Restablecer = self.Crear.crear_btn_navegacion(text="Restablecer contraseña", ajsutes=self.ParametroAjuste)
        btn_Restablecer.config(command=self.envio_Codigo)
        btn_Restablecer.grid(row=6, column=0, columnspan=2, sticky="ew", padx=20, pady=(5, 15),in_=login_frame)

    def verificar_User(self):
        email = self.correo_Entry.get()
        password = self.password_Entry.get()
        self.usuario = authenticacion_user(email, password)
        if not  self.usuario.nuevo:
            self.master.destroy()
            self.on_success( self.usuario)
        else:
            self.nuevo(password)

    def envio_Codigo(self):
        self.clear_canvas()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        self.canvas = tk.Canvas(self.master, width=screen_width, height=screen_height, bg=self.ParametroAjuste.color_fondo)
        self.canvas.pack(fill="both", expand=True)

        frame_width = min(400, screen_width // 3)
        frame_height = min(180, screen_height // 5)
        frame_x = (screen_width - frame_width) // 2
        frame_y = (screen_height - frame_height) // 2

        login_frame = tk.Frame(self.canvas, bg=self.ParametroAjuste.color_frame, bd=2, relief="groove")
        self.canvas.create_window(frame_x, frame_y, window=login_frame, anchor="nw", width=frame_width, height=frame_height)

        for i in range(4):
            login_frame.rowconfigure(i, weight=1)
        login_frame.columnconfigure(0, weight=1)
        login_frame.columnconfigure(1, weight=4)

        # Correo Electrónico
        correo_Label = tk.Label(login_frame, text="Correo Electrónico", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        correo_Label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 0))

        self.correo_Entry =  ttk.Entry(login_frame, font=('Arial', 12, 'bold'))
        self.correo_Entry.grid(row=1, column=1, sticky="ew", padx=(0, 40), pady=(2, 0))

        try:
            usuario_icon_img = Image.open("assets/images/usuario_icon.png")
            usuario_icon_photo = ImageTk.PhotoImage(usuario_icon_img)
        except Exception:
            usuario_icon_photo = None
        usuario_icon = tk.Label(login_frame, image=usuario_icon_photo, bg=self.ParametroAjuste.color_frame)
        usuario_icon.image = usuario_icon_photo
        usuario_icon.grid(row=1, column=0, sticky="e", padx=(10, 0))

        # Botón Enviar código
        btn_Login = self.Crear.crear_btn(text="Enviar código", ajsutes=self.ParametroAjuste)
        btn_Login.config(command=self.enviar_Codigo)
        btn_Login.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=(20, 10),in_=login_frame)

    def enviar_Codigo(self):
        try:
            usuario = User.get(User.email == self.correo_Entry.get())
            codigo = random.randint(1000, 9999)
            contexto = {
                "nombre": usuario.nombre,
                "sistema": "Cerrajeria",
                "codigo": codigo,
                "anio": datetime.now().year
            }
            usuario.codigo = str(codigo)
            usuario.save()
            envio = EnviarCorreo.enviar_correo(EnviarCorreo(), usuario.email, "reiniciar_contrasena.xml", contexto)
            if envio:
                self.restablecer()
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"❌ No existe usuario con este correo asociado")

    def restablecer(self):
        self.clear_canvas()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        self.canvas = tk.Canvas(self.master, width=screen_width, height=screen_height, bg=self.ParametroAjuste.color_fondo)
        self.canvas.pack(fill="both", expand=True)

        frame_width = min(400, screen_width // 3)
        frame_height = min(260, screen_height // 4)
        frame_x = (screen_width - frame_width) // 2
        frame_y = (screen_height - frame_height) // 2

        login_frame = tk.Frame(self.canvas, bg=self.ParametroAjuste.color_frame, bd=2, relief="groove")
        self.canvas.create_window(frame_x, frame_y, window=login_frame, anchor="nw", width=frame_width, height=frame_height)

        for i in range(8):
            login_frame.rowconfigure(i, weight=1)
        login_frame.columnconfigure(0, weight=1)
        login_frame.columnconfigure(1, weight=4)

        # Código
        codigo_Label = tk.Label(login_frame, text="Código", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        codigo_Label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 0))

        self.codigo_Entry =  ttk.Entry(login_frame, font=('Arial', 12, 'bold'))
        self.codigo_Entry.grid(row=1, column=1, sticky="ew", padx=(0, 40), pady=(2, 0))

        try:
            usuario_icon_img = Image.open("assets/images/usuario_icon.png")
            usuario_icon_photo = ImageTk.PhotoImage(usuario_icon_img)
        except Exception:
            usuario_icon_photo = None
        usuario_icon = tk.Label(login_frame, image=usuario_icon_photo, bg=self.ParametroAjuste.color_frame)
        usuario_icon.image = usuario_icon_photo
        usuario_icon.grid(row=1, column=0, sticky="e", padx=(10, 0))

        # Contraseña (oculta inicialmente)
        self.password_Label = tk.Label(login_frame, text="Contraseña", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        self.password_Entry =  ttk.Entry(login_frame, font=('Arial', 12, 'bold'))
        try:
            password_icon_img = Image.open("assets/images/password_icon.png")
            password_icon_photo = ImageTk.PhotoImage(password_icon_img)
        except Exception:
            password_icon_photo = None
        self.password_icon = tk.Label(login_frame, image=password_icon_photo, bg=self.ParametroAjuste.color_frame)
        self.password_icon.image = password_icon_photo

        # Botón Verificar código
        btn_Verificar = self.Crear.crear_btn(text="Verificar código", ajsutes=self.ParametroAjuste)
        btn_Verificar.config(command=lambda: self.vrificar_Codigo(btn_Verificar, btn_Restablecer))
        btn_Verificar.grid(row=4, column=0, columnspan=2, sticky="ew", padx=20, pady=(20, 5),in_=login_frame)

        # Botón Restablecer contraseña (oculto inicialmente)
        btn_Restablecer = self.Crear.crear_btn(text="Restablecer contraseña", ajsutes=self.ParametroAjuste)
        btn_Restablecer.config(command=self.restablecer_Contrsena)

        # Guardar para mostrar/ocultar
        self.btn_Restablecer = btn_Restablecer
        self.login_frame = login_frame

    def nuevo(self,password):
        self.clear_canvas()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        self.canvas = tk.Canvas(self.master, width=screen_width, height=screen_height, bg=self.ParametroAjuste.color_fondo)
        self.canvas.pack(fill="both", expand=True)

        frame_width = min(400, screen_width // 3)
        frame_height = min(260, screen_height // 4)
        frame_x = (screen_width - frame_width) // 2
        frame_y = (screen_height - frame_height) // 2

        login_frame = tk.Frame(self.canvas, bg=self.ParametroAjuste.color_frame, bd=2, relief="groove")
        self.canvas.create_window(frame_x, frame_y, window=login_frame, anchor="nw", width=frame_width, height=frame_height)

        for i in range(8):
            login_frame.rowconfigure(i, weight=1)
        login_frame.columnconfigure(0, weight=1)
        login_frame.columnconfigure(1, weight=4)

        # Contraseña (oculta inicialmente)
        self.password_Label = tk.Label(login_frame, text="Contraseña", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        self.password_Label.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 0)
                                 )
        self.password_Entry =  ttk.Entry(login_frame, font=('Arial', 12, 'bold'))
        self.password_Entry.grid(row=3, column=1, sticky="ew", padx=(0, 40), pady=(2, 0))
        try:
            password_icon_img = Image.open("assets/images/password_icon.png")
            password_icon_photo = ImageTk.PhotoImage(password_icon_img)
        except Exception:
            password_icon_photo = None
        self.password_icon = tk.Label(login_frame, image=password_icon_photo, bg=self.ParametroAjuste.color_frame)
        self.password_icon.image = password_icon_photo
        self.password_icon.grid(row=3, column=0, sticky="e", padx=(10, 0))

        btn_Restablecer = self.Crear.crear_btn(text="Restablecer contraseña", ajsutes=self.ParametroAjuste)
        btn_Restablecer.grid(row=6, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 5), in_=login_frame)
        btn_Restablecer.config(command=self.cambio_contrasena)

    def vrificar_Codigo(self, btn_Verificar, btn_Restablecer):
        try:
            self.usuario = User.get(User.codigo == self.codigo_Entry.get())
            self.codigo_Entry.config(state="disabled")
            btn_Verificar.grid_remove()
            self.btn_Restablecer.grid(row=6, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 5),in_=self.login_frame)
            self.password_Label.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 0),in_=self.login_frame)
            self.password_Entry.grid(row=3, column=1, sticky="ew", padx=(0, 40), pady=(2, 0),in_=self.login_frame)
            self.password_icon.grid(row=3, column=0, sticky="e", padx=(10, 0),in_=self.login_frame)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"❌ El código no es valido")

    def restablecer_Contrsena(self):
        codigo = self.codigo_Entry.get()
        password = self.password_Entry.get()
        restablecer_user(codigo, password)
        self.master.destroy()
        self.on_reset()

    def cambio_contrasena(self):
        self.usuario.password = self.password_Entry.get()
        self.usuario.cambio_contrasena()
        if not self.usuario.nuevo:
            self.master.destroy()
            self.on_success(self.usuario)