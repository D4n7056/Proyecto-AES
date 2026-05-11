#=================#
#       GUI       #
#=================#

import tkinter as tk
from tkinter import filedialog, messagebox
from aes.ecb import ecbEncrypt, ecbDecrypt

class App:
    def __init__(self, root):
        self.root = root
        root.title("AES-128 ECB")
        root.geometry("500x350")
        self.file = ""

        tk.Button(root, text="Seleccionar archivo", command=self.sel).pack(pady=10)
        self.label = tk.Label(root, text="Ninguno")
        self.label.pack()

        # ASCII key input
        tk.Label(root, text="Llave ASCII (16 chars)").pack()
        self.key_ascii = tk.Entry(root, width=30)
        self.key_ascii.pack()

        # HEX key input
        tk.Label(root, text="Llave HEX (ej: FF 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F)").pack()
        self.key_hex = tk.Entry(root, width=50)
        self.key_hex.pack()

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
        ascii_val = self.key_ascii.get().strip()
        hex_val = self.key_hex.get().strip()

        # Sólo se puede usar una caja
        if ascii_val and hex_val:
            messagebox.showerror("Error", "Usa solo ASCII o HEX")
            return None
        if not ascii_val and not hex_val:
            messagebox.showerror("Error", "Ingresa una llave")
            return None

        # Modo HEX 
        if hex_val:
            try:
                hex_str = hex_val.replace(" ", "")
                if len(hex_str) != 32:
                    messagebox.showerror("Error", "Llave HEX debe ser 16 bytes (32 caracteres hex)")
                    return None
                return bytes.fromhex(hex_str)
            except ValueError:
                messagebox.showerror("Error", "Formato HEX inválido")
                return None

        # Modo ASCII
        if len(ascii_val) != 16:
            messagebox.showerror("Error", "Llave ASCII debe ser 16 chars")
            return None
        try:
            return ascii_val.encode('ascii')
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
            out  = ecbEncrypt(data, key)
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
            out  = ecbDecrypt(data, key)
            name = self.file[:-4] if self.file.endswith('.enc') else "dec_" + self.file
            open(name, 'wb').write(out)
            messagebox.showinfo("OK", "Descifrado completo")
        except:
            messagebox.showerror("Error", "Llave incorrecta o archivo corrupto")
