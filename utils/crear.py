import tkinter as tk
from tkinter import ttk

class Crear:
    def crear_btn(self,text,ajsutes):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Custom.TButton",
            font=('Arial', 12, 'bold'),
            background=ajsutes.color_btn_1,
            foreground=ajsutes.color_btn_2,
            borderwidth=0,
            padding=10
        )

        style.map(
            "Custom.TButton",
            background=[("active", ajsutes.color_btn_3)],
            foreground=[("active", ajsutes.color_btn_4)],
            highlightcolor=[("focus", "WHITE")],
            highlightbackground=[("focus", ajsutes.color_btn_1)]
        )
        return ttk.Button(
            text=text,
            style="Custom.TButton"
        )

    def crear_btn_navegacion(self,text,ajsutes):
        return tk.Button(
            text=text,
            relief="flat",
            borderwidth=0,
            bg=ajsutes.color_frame,
            highlightthickness=0,
            fg="black",
            font=('Arial', 12, 'bold'),
        )