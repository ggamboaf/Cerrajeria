import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


# Ejemplo de uso
root = tk.Tk()
root.title("Frame con Scroll Vertical")

scroll_frame = ScrollableFrame(root)
scroll_frame.pack(fill="both", expand=True)

# Agregar muchos widgets para probar el scroll
for i in range(50):
    ttk.Label(scroll_frame.scrollable_frame, text=f"Etiqueta {i+1}").pack()

root.mainloop()
