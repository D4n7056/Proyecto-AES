#=================#
#       GUI       #
#=================#

import tkinter as tk
from tkinter import filedialog, messagebox
from aes.cbc import cbcEncrypt, cbcDecrypt

class App:
    def __init__(self, root):
        self.root = root
        root.title("AES-128 CBC")
        root.geometry("500x300")
        self.file = ""

        tk.Button(root, text="Seleccionar archivo", command=self.sel).pack(pady=10)
        self.label = tk.Label(root, text="Ninguno")
        self.label.pack()

        tk.Label(root, text="Llave (16 chars ASCII)").pack()
        self.key = tk.Entry(root, width=30)
        self.key.pack()

        tk.Button(root, text="Cifrar",    bg="green", command=self.enc).pack(pady=10)
        tk.Button(root, text="Descifrar", bg="blue",  command=self.dec).pack()

    #------------------------#
    # sel                    #
    #------------------------#
    def sel(self):
        f = filedialog.askopenfilename()
        if f:
            self.file = f
            self.label.config(text=f)

    #------------------------#
    # getkey                 #
    #------------------------#
    def getkey(self):
        k = self.key.get()
        if len(k) != 16:
            messagebox.showerror("Error", "Llave debe ser 16 chars")
            return None
        try:
            return k.encode('ascii')
        except:
            messagebox.showerror("Error", "ASCII solamente")
            return None

    #------------------------#
    # enc                    #
    #------------------------#
    def enc(self):
        key = self.getkey()
        if not key or not self.file: return
        try:
            data = open(self.file, 'rb').read()
            out  = cbcEncrypt(data, key)
            open(self.file + '.enc', 'wb').write(out)
            messagebox.showinfo("OK", "Cifrado completo")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    #------------------------#
    # dec                    #
    #------------------------#
    def dec(self):
        key = self.getkey()
        if not key or not self.file: return
        try:
            data = open(self.file, 'rb').read()
            out  = cbcDecrypt(data, key)
            name = self.file[:-4] if self.file.endswith('.enc') else "dec_" + self.file
            open(name, 'wb').write(out)
            messagebox.showinfo("OK", "Descifrado completo")
        except:
            messagebox.showerror("Error", "Llave incorrecta o archivo corrupto")
