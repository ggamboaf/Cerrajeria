import os
import smtplib
import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
from utils.ajuste import ParametroAjuste
from utils.crear import Crear
from PIL import Image, ImageTk


class ViewAjuste(tk.Frame):
    def __init__(self, master=None):
        self.smtp_contrasena = None
        self.smtp_usuario = None
        self.smtp_puerto = None
        self.smtp_servidor = None
        self.marco_servidor_correo = None
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.marco_logo = None
        self.marco_botones = None
        self.marco_general = None
        self.Guardado = False
        self.pack(fill=tk.BOTH, expand=True)
        self.frame_contenido_header = self.crear_area_contenido_header()
        self.frame_contenido = self.crear_area_contenido()
        self.crear_header()
        self.crear_form()

    def crear_area_contenido_header(self):
        frame_contenido_header = tk.Frame(self, height=100, bg=self.ParametroAjuste.color_frame)
        frame_contenido_header.pack(side="top", fill="x")
        return frame_contenido_header

    def crear_area_contenido(self):
        frame_contenido = tk.Frame(self, bg=self.ParametroAjuste.color_frame)
        frame_contenido.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
        return frame_contenido

    def crear_header(self):
        btn_Guardar = Crear.crear_btn(self.Crear,text="Guardar",ajsutes=self.ParametroAjuste)
        btn_Guardar.place(x=150, y=50,in_=self.frame_contenido_header)
        btn_Guardar.config(command=self.guardar)

    def crear_form(self):
        self.crear_labelframe()
        espaciador = tk.Frame(self.frame_contenido, width=200, height=100, bg=self.ParametroAjuste.color_frame)
        espaciador.grid(row=0, column=0)
        espaciador = tk.Frame(self.frame_contenido, width=200, height=100, bg=self.ParametroAjuste.color_frame)
        espaciador.grid(row=0, column=1)

        label = tk.Label(self.marco_general, text="Color de fondo", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        cuadro_color_fondo = tk.Label(self.marco_general, width=5, height=2, bg=self.ParametroAjuste.color_fondo, relief="solid", bd=1)
        cuadro_color_fondo.grid(row=1, column=3, padx=10, pady=5, sticky="ew")
        entry = Crear.crear_btn(self.Crear,text="Cambiar",ajsutes=self.ParametroAjuste)
        entry.config(command=lambda: self.elegir_color("color_fondo",cuadro_color_fondo))
        entry.grid(row=1, column=2, padx=10, pady=5, sticky="ew",in_=self.marco_general)

        label = tk.Label(self.marco_general, text="Color de frame", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        cuadro_color_frame = tk.Label(self.marco_general, width=5, height=2, bg=self.ParametroAjuste.color_frame, relief="solid", bd=1)
        cuadro_color_frame.grid(row=2, column=3, padx=10, pady=5, sticky="ew")
        entry = Crear.crear_btn(self.Crear,text="Cambiar",ajsutes=self.ParametroAjuste)
        entry.config(command=lambda: self.elegir_color("color_frame", cuadro_color_frame))
        entry.grid(row=2, column=2, padx=10, pady=5, sticky="ew",in_=self.marco_general)

        label = tk.Label(self.marco_botones, text="Color de fondo del botón", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        cuadro_color_btn_1 = tk.Label(self.marco_botones, width=5, height=2, bg=self.ParametroAjuste.color_btn_1, relief="solid", bd=1)
        cuadro_color_btn_1.grid(row=1, column=3, padx=10, pady=5, sticky="ew")
        entry = Crear.crear_btn(self.Crear,text="Cambiar",ajsutes=self.ParametroAjuste)
        entry.config(command=lambda: self.elegir_color("color_btn_1", cuadro_color_btn_1))
        entry.grid(row=1, column=2, padx=10, pady=5, sticky="ew",in_=self.marco_botones)


        label = tk.Label(self.marco_botones, text="Color del texto", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        cuadro_color_btn_2 = tk.Label(self.marco_botones, width=5, height=2, bg=self.ParametroAjuste.color_btn_2, relief="solid", bd=1)
        cuadro_color_btn_2.grid(row=2, column=3, padx=10, pady=5, sticky="ew")
        entry = Crear.crear_btn(self.Crear,text="Cambiar",ajsutes=self.ParametroAjuste)
        entry.config(command=lambda: self.elegir_color("color_btn_2", cuadro_color_btn_2))
        entry.grid(row=2, column=2, padx=10, pady=5, sticky="ew",in_=self.marco_botones)

        label = tk.Label(self.marco_botones, text="Color de fondo del botón cuando está activo", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        cuadro_color_btn_3 = tk.Label(self.marco_botones, width=5, height=2, bg=self.ParametroAjuste.color_btn_3, relief="solid", bd=1)
        cuadro_color_btn_3.grid(row=3, column=3, padx=10, pady=5, sticky="ew")
        entry = Crear.crear_btn(self.Crear,text="Cambiar",ajsutes=self.ParametroAjuste)
        entry.config(command=lambda: self.elegir_color("color_btn_1", cuadro_color_btn_3))
        entry.grid(row=3, column=2, padx=10, pady=5, sticky="ew",in_=self.marco_botones)

        label = tk.Label(self.marco_botones, text="Color del texto cuando el botón está activo", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        cuadro_color_btn_4 = tk.Label(self.marco_botones, width=5, height=2, bg=self.ParametroAjuste.color_btn_4, relief="solid", bd=1)
        cuadro_color_btn_4.grid(row=4, column=3, padx=10, pady=5, sticky="ew")
        entry = Crear.crear_btn(self.Crear,text="Cambiar",ajsutes=self.ParametroAjuste)
        entry.config(command=lambda: self.elegir_color("color_btn_4", cuadro_color_btn_4))
        entry.grid(row=4, column=2, padx=10, pady=5, sticky="ew",in_=self.marco_botones)



        frame = tk.Frame(self.marco_logo, width=200, height=200, bg="gray")
        frame.grid(row=2, column=2, padx=10, pady=5, sticky="ew")
        label_imagen = tk.Label(frame)
        label_imagen.pack()
        imagen = Image.open(self.ParametroAjuste.img_logo)
        imagen.thumbnail((200, 200))
        imagen_actual = ImageTk.PhotoImage(imagen)
        label_imagen.config(image=imagen_actual)
        label_imagen.image = imagen_actual
        entry = Crear.crear_btn(self.Crear,text="Cambiar",ajsutes=self.ParametroAjuste)
        entry.config(command=lambda: self.cambiar_imagen("img_login_sing",label_imagen))
        entry.grid(row=1, column=2, padx=10, pady=5, sticky="ew",in_=self.marco_logo)


        label = tk.Label(self.marco_servidor_correo, text="Servidor SMTP", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.smtp_servidor = ttk.Entry(self.marco_servidor_correo,width=50, font=('Arial', 12, 'bold'))
        self.smtp_servidor.grid(row=2, column=3, padx=10, pady=5, sticky="ew")
        self.smtp_servidor.insert(0,self.ParametroAjuste.smtp_servidor)

        label = tk.Label(self.marco_servidor_correo, text="Puerto SMTP", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        self.smtp_puerto = ttk.Entry(self.marco_servidor_correo,width=50, font=('Arial', 12, 'bold'))
        self.smtp_puerto.grid(row=3, column=3, padx=10, pady=5, sticky="ew")
        self.smtp_puerto.insert(0,self.ParametroAjuste.smtp_puerto)

        label = tk.Label(self.marco_servidor_correo, text="Nombre de usuario", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=4, column=2, padx=10, pady=5, sticky="w")
        self.smtp_usuario = ttk.Entry(self.marco_servidor_correo,width=50, font=('Arial', 12, 'bold'))
        self.smtp_usuario.grid(row=4, column=3, padx=10, pady=5, sticky="ew")
        self.smtp_usuario.insert(0,self.ParametroAjuste.smtp_usuario)

        label = tk.Label(self.marco_servidor_correo, text="Contraseña", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'))
        label.grid(row=5, column=2, padx=10, pady=5, sticky="w")
        self.smtp_contrasena = ttk.Entry(self.marco_servidor_correo,width=50, font=('Arial', 12, 'bold'), show="*")
        self.smtp_contrasena.grid(row=5, column=3, padx=10, pady=5, sticky="ew")
        self.smtp_contrasena.insert(0,self.ParametroAjuste.smtp_contrasena)

        btn_probar_coneccion = Crear.crear_btn(self.Crear,text="Probar la conexión SMTP",ajsutes=self.ParametroAjuste)
        btn_probar_coneccion.grid(row=6, column=2, padx=10, pady=5, sticky="w",in_=self.marco_servidor_correo)
        btn_probar_coneccion.config(command=self.guardar)



    def crear_labelframe(self):
        self.frame_contenido.grid_columnconfigure(2, weight=1)
        self.frame_contenido.grid_columnconfigure(3, weight=1)
        self.frame_contenido.grid_rowconfigure(1, weight=1)
        self.frame_contenido.grid_rowconfigure(2, weight=1)
        style = ttk.Style()
        style.configure("Custom.TLabelframe.Label", foreground=self.ParametroAjuste.color_frame)
        style.configure("Custom.TLabelframe", background=self.ParametroAjuste.color_frame)

        self.marco_general = ttk.LabelFrame(self.frame_contenido, text="Datos", style="Custom.TLabelframe")
        titulo = tk.Label(self.marco_general, text="Datos", fg="black", bg=self.ParametroAjuste.color_frame, font=("Arial", 12, "bold"))
        self.marco_general.configure(labelwidget=titulo)
        self.marco_general.grid(row=1,column=1, padx=10, pady=10, sticky="nsew")

        self.marco_botones = ttk.LabelFrame(self.frame_contenido, text="Datos", style="Custom.TLabelframe")
        titulo = tk.Label(self.marco_botones, text="Datos", fg="black", bg=self.ParametroAjuste.color_frame, font=("Arial", 12, "bold"))
        self.marco_botones.configure(labelwidget=titulo)
        self.marco_botones.grid(row=1,column=2, padx=10, pady=10, sticky="nsew")

        self.marco_logo = ttk.LabelFrame(self.frame_contenido, text="Datos", style="Custom.TLabelframe")
        titulo = tk.Label(self.marco_logo, text="Datos", fg="black", bg=self.ParametroAjuste.color_frame, font=("Arial", 12, "bold"))
        self.marco_logo.configure(labelwidget=titulo)
        self.marco_logo.grid(row=2,column=1, padx=10, pady=10, sticky="nsew")

        self.marco_servidor_correo = ttk.LabelFrame(self.frame_contenido, text="Datos", style="Custom.TLabelframe")
        titulo = tk.Label(self.marco_servidor_correo, text="Datos", fg="black", bg=self.ParametroAjuste.color_frame, font=("Arial", 12, "bold"))
        self.marco_servidor_correo.configure(labelwidget=titulo)
        self.marco_servidor_correo.grid(row=2,column=2, padx=10, pady=10, sticky="nsew")

    def elegir_color(self,ajuste,cuadro_color_fondo):
        color = colorchooser.askcolor(title="Selecciona un color")
        if color[1]:
            cuadro_color_fondo.config(bg=color[1])
            setattr(self.ParametroAjuste, ajuste, color[1])

    def cambiar_imagen(self,ajuste,label_imagen):
        ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif")])
        if ruta:
            imagen = Image.open(ruta)
            imagen.thumbnail((200, 200))
            imagen_actual = ImageTk.PhotoImage(imagen)
            label_imagen.config(image=imagen_actual)
            label_imagen.image = imagen_actual
            ruta_completa = os.path.join("assets/images/", f"{ajuste}.{imagen.format}")
            imagen.save(ruta_completa)

    def guardar(self):
        try:
            servidor = smtplib.SMTP_SSL(self.smtp_servidor.get(), int( self.smtp_puerto.get()))
            # servidor.starttls()
            servidor.login(self.smtp_usuario.get(), self.smtp_contrasena.get())
            servidor.quit()
            messagebox.showinfo("Éxito", "✅ Conexión SMTP exitosa.")
            setattr(self.ParametroAjuste, "smtp_servidor", self.smtp_servidor.get())
            setattr(self.ParametroAjuste, "smtp_puerto", self.smtp_puerto.get())
            setattr(self.ParametroAjuste, "smtp_usuario", self.smtp_usuario.get())
            setattr(self.ParametroAjuste, "smtp_contrasena", self.smtp_contrasena.get())
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"❌ Error al conectar con el servidor SMTP: \n {e}")

    def regresar(self):
        if self.ir_action_back:
            self.ir_action_back()







