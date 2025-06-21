import tkinter as tk
from utils.enviar_correo import EnviarCorreo
from datetime import datetime
from tkinter import messagebox, Frame
from auth.auth import authenticacion_user, restablecer_user
from PIL import Image, ImageTk
from utils.ajuste import ParametroAjuste
from utils.crear import Crear
import random
from models.models import *


class ViewLogin:
    def __init__(self, master, on_success,on_reset):
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

        try:
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()

            self.canvas = tk.Canvas(self.master, width=screen_width, height=screen_height,bg=self.ParametroAjuste.color_fondo)
            self.canvas.pack(fill="both", expand=True)

            frame_width = 300
            frame_height = 600
            frame_x = (screen_width - frame_width) // 2
            frame_y = (screen_height - frame_height) // 2

            login_frame = tk.Frame(self.canvas, bg=self.ParametroAjuste.color_frame, bd=2, relief="groove")
            self.canvas.create_window(frame_x, frame_y, window=login_frame, anchor="nw", width=frame_width, height=frame_height)

            image = Image.open(self.ParametroAjuste.img_logo)
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image = image.resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            img_login_sing = tk.Label(login_frame, image=photo, bg=self.ParametroAjuste.color_frame)
            img_login_sing.image = photo
            img_login_sing.place(x=100, y=50)

            correo_Label = tk.Label(login_frame, text="Correo Electrónico", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
            correo_Label.place(x=75, y=200)

            self.correo_Entry = tk.Entry(login_frame, highlightthickness=0, relief=tk.FLAT, bg=self.ParametroAjuste.color_frame, fg="#6b6a69", font=("TkTextFont ", 12, "bold"), insertbackground='#6b6a69')
            self.correo_Entry.place(x=100, y=235, width=150)

            correo_Line = tk.Canvas(login_frame, width=175, height=2.0, bg="#bdb9b1", highlightthickness=0)
            correo_Line.place(x=75, y=259)

            image = Image.open("assets/images/usuario_icon.png")
            photo = ImageTk.PhotoImage(image)
            usuario_icon = tk.Label(login_frame, image=photo, bg=self.ParametroAjuste.color_frame)
            usuario_icon.image = photo
            usuario_icon.place(x=75, y=232)

            password_Label = tk.Label(login_frame, text="Contraseña", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
            password_Label.place(x=75, y=280)

            self.password_Entry = tk.Entry(login_frame, highlightthickness=0, relief=tk.FLAT, bg=self.ParametroAjuste.color_frame, fg="#6b6a69", font=("TkTextFont ", 12, "bold"), show="*", insertbackground='#6b6a69')
            self.password_Entry.place(x=100, y=316, width=150)

            password_Line = tk.Canvas(login_frame, width=175, height=2.0, bg="#bdb9b1", highlightthickness=0)
            password_Line.place(x=75, y=340)

            image = Image.open("assets/images/password_icon.png")
            photo = ImageTk.PhotoImage(image)
            password_icon = tk.Label(login_frame, image=photo, bg=self.ParametroAjuste.color_frame)
            password_icon.image = photo
            password_icon.place(x=75, y=314)

            btn_Login = Crear.crear_btn(self.Crear, text="Iniciar Sesión", ajsutes=self.ParametroAjuste)
            btn_Login.config(command=self.verificar_User)
            btn_Login.place(x=75, y=360,in_=login_frame,width=175)

            btn_Login = Crear.crear_btn_navegacion(self.Crear, text="Restablecer contraseña", ajsutes=self.ParametroAjuste)
            btn_Login.config(command=self.envio_Codigo)
            btn_Login.place(x=60, y=410,in_=login_frame,width=200)


        except Exception as e:
            print("No se pudo cargar la imagen de fondo:", e)

    def verificar_User(self):
        email = self.correo_Entry.get()
        password = self.password_Entry.get()
        user = authenticacion_user(email, password)
        if user:
            self.master.destroy()
            self.on_success(user)

    def envio_Codigo(self):
        self.canvas.destroy()

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        self.canvas = tk.Canvas(self.master, width=screen_width, height=screen_height, bg=self.ParametroAjuste.color_fondo)
        self.canvas.pack(fill="both", expand=True)

        frame_width = 400
        frame_height = 150
        frame_x = (screen_width - frame_width) // 2
        frame_y = (screen_height - frame_height) // 2

        login_frame = tk.Frame(self.canvas, bg=self.ParametroAjuste.color_frame, bd=2, relief="groove")
        self.canvas.create_window(frame_x, frame_y, window=login_frame, anchor="nw", width=frame_width, height=frame_height)

        correo_Label = tk.Label(login_frame, text="Correo Electrónico", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        correo_Label.place(x=130, y=10)

        self.correo_Entry = tk.Entry(login_frame, highlightthickness=0, relief=tk.FLAT, bg=self.ParametroAjuste.color_frame, fg="#6b6a69", font=("TkTextFont ", 12, "bold"), insertbackground='#6b6a69')
        self.correo_Entry.place(x=155, y=40, width=175)

        correo_Line = tk.Canvas(login_frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        correo_Line.place(x=130, y=66)

        image = Image.open("assets/images/usuario_icon.png")
        photo = ImageTk.PhotoImage(image)
        usuario_icon = tk.Label(login_frame, image=photo, bg=self.ParametroAjuste.color_frame)
        usuario_icon.image = photo
        usuario_icon.place(x=130, y=40)

        btn_Login = Crear.crear_btn(self.Crear, text="Enviar código", ajsutes=self.ParametroAjuste)
        btn_Login.config(command=self.enviar_Codigo)
        btn_Login.place(x=140, y=90, in_=login_frame, width=175)


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
        self.canvas.destroy()

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        self.canvas = tk.Canvas(self.master, width=screen_width, height=screen_height, bg=self.ParametroAjuste.color_fondo)
        self.canvas.pack(fill="both", expand=True)

        frame_width = 400
        frame_height = 220
        frame_x = (screen_width - frame_width) // 2
        frame_y = (screen_height - frame_height) // 2

        login_frame = tk.Frame(self.canvas, bg=self.ParametroAjuste.color_frame, bd=2, relief="groove")
        self.canvas.create_window(frame_x, frame_y, window=login_frame, anchor="nw", width=frame_width, height=frame_height)

        codigo_Label = tk.Label(login_frame, text="Código", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        codigo_Label.place(x=130, y=10)

        self.codigo_Entry = tk.Entry(login_frame, highlightthickness=0, relief=tk.FLAT, bg=self.ParametroAjuste.color_frame, fg="#6b6a69", font=("TkTextFont ", 12, "bold"), insertbackground='#6b6a69')
        self.codigo_Entry.place(x=155, y=40, width=175)

        codigo_Line = tk.Canvas(login_frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        codigo_Line.place(x=130, y=66)

        image = Image.open("assets/images/usuario_icon.png")
        photo = ImageTk.PhotoImage(image)
        usuario_icon = tk.Label(login_frame, image=photo, bg=self.ParametroAjuste.color_frame)
        usuario_icon.image = photo
        usuario_icon.place(x=130, y=40)

        password_Label = tk.Label(login_frame, text="Contraseña", bg=self.ParametroAjuste.color_frame, font=('TkTextFont', 13, 'bold'), fg='#4f4e4d')
        password_Label.place(x=-500, y=-500)

        self.password_Entry = tk.Entry(login_frame, highlightthickness=0, relief=tk.FLAT, bg=self.ParametroAjuste.color_frame, fg="#6b6a69", font=("TkTextFont ", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_Entry.place(x=-500, y=-500, width=175)

        password_Line = tk.Canvas(login_frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        password_Line.place(x=-500, y=-500)

        image = Image.open("assets/images/password_icon.png")
        photo = ImageTk.PhotoImage(image)
        password_icon = tk.Label(login_frame, image=photo, bg=self.ParametroAjuste.color_frame)
        password_icon.image = photo
        password_icon.place(x=-500, y=-500)

        btn_Verificar = Crear.crear_btn(self.Crear, text="Verificar código", ajsutes=self.ParametroAjuste)
        btn_Verificar.config(command=lambda: self.vrificar_Codigo(btn_Verificar,btn_Restablecer,password_Label,password_Line,password_icon))
        btn_Verificar.place(x=140, y=160, in_=login_frame, width=175)

        btn_Restablecer = Crear.crear_btn(self.Crear, text="Restablecer contraseña", ajsutes=self.ParametroAjuste)
        btn_Restablecer.config(command=self.restablecer_Contrsena)
        btn_Restablecer.place(x=-500, y=-500, in_=login_frame, width=175)

    def vrificar_Codigo(self,btn_Verificar,btn_Restablecer,password_Label,password_Line,password_icon):
        try:
            self.usuario = User.get(User.codigo == self.codigo_Entry.get())
            self.codigo_Entry.config(state="disabled")
            btn_Verificar.place(x=-500, y=-500)
            btn_Restablecer.place(x=140, y=160)
            password_Label.place(x=130, y=80)
            self.password_Entry.place(x=155, y=110)
            password_Line.place(x=130, y=136)
            password_icon.place(x=130, y=110)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"❌ El código no es valido")

    def restablecer_Contrsena(self):
        codigo = self.codigo_Entry.get()
        password = self.password_Entry.get()
        restablecer_user(codigo, password)
        self.master.destroy()
        self.on_reset()




