import socket
import sys
import tkinter as tk

def check_if_running(port=65432):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("localhost", port))
    except socket.error:
        print("La aplicación ya está en ejecución.")
        sys.exit()
    return s

sock = check_if_running()

root = tk.Tk()
root.title("App con Socket")

label = tk.Label(root, text="Aplicación única en ejecución")
label.pack()

root.mainloop()
sock.close()
