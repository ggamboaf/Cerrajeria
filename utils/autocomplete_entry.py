import tkinter as tk

class AutocompleteEntry(tk.Entry):
    def __init__(self, data_list, *args, **kwargs):
        """
        data_list: lista de tuplas (id, nombre)
        """
        super().__init__(*args, **kwargs)
        self.data_list = data_list
        self.filtered_data = []
        self.listbox = None
        self.x = 0
        self.y = 0
        self.bind("<KeyRelease>", self.check_input)

    def check_input(self, event):
        typed = self.get()
        self.x = event.x_root
        self.y = event.y_root
        if typed == "":
            self.hide_listbox()
        else:
            # Filtrar por coincidencia tipo LIKE
            self.filtered_data = [
                (id_, name) for id_, name in self.data_list if typed.lower() in name.lower()
            ]
            if self.filtered_data:
                self.show_listbox()
            else:
                self.hide_listbox()

    def show_listbox(self):
        if self.listbox:
            self.listbox.destroy()
        self.listbox = tk.Listbox()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        for _, name in self.filtered_data:
            self.listbox.insert(tk.END, name)
        gg =self.winfo_x()
        gkg =self.winfo_y()
        self.listbox.place(x= self.x, y=self.y + self.winfo_height())

    def hide_listbox(self):
        if self.listbox:
            self.listbox.destroy()
            self.listbox = None

    def on_select(self, event):
        if self.listbox:
            index = self.listbox.curselection()[0]
            selected_id, selected_name = self.filtered_data[index]
            self.delete(0, tk.END)
            self.insert(0, selected_name)
            self.hide_listbox()
            print(f"Seleccionaste: {selected_name} (ID: {selected_id})")