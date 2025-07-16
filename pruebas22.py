# Frame superior
self.frame_contenido_report = tk.Frame(self.frame_contenido_body, bg=self.ParametroAjuste.color_frame)
self.frame_contenido_report.pack(padx=10, pady=10, fill='x')

# Frame intermedio para la cuadrícula 2x2
frame_cuadricula = tk.Frame(self.frame_contenido_body, bg="white")
frame_cuadricula.pack(padx=10, pady=10, fill='both', expand=True)

# Configurar la cuadrícula 2x2
for i in range(2):
    frame_cuadricula.grid_rowconfigure(i, weight=1)
    frame_cuadricula.grid_columnconfigure(i, weight=1)

# Crear los 4 LabelFrames
for row in range(2):
    for col in range(2):
        lf = ttk.LabelFrame(frame_cuadricula, text=f"Sección {row*2 + col + 1}", padding=10)
        lf.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        ttk.Label(lf, text=f"Contenido {row*2 + col + 1}").pack()

# Frame inferior (si lo tienes)
self.frame_contenido_footer = tk.Frame(self.frame_contenido_body, bg=self.ParametroAjuste.color_frame)
self.frame_contenido_footer.pack(padx=10, pady=10, fill='x')
