import tkinter as tk
from tkinter import ttk, messagebox
from ciphers.caesar import caesar_encrypt, caesar_decrypt
from ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from ciphers.playfair import playfair_encrypt, playfair_decrypt

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Select Cipher:")
        self.label.pack(pady=10)

        self.cipher_var = tk.StringVar(value="Caesar")
        self.cipher_menu = ttk.Combobox(self.root, textvariable=self.cipher_var, values=["Caesar", "Vigenère", "Playfair"])
        self.cipher_menu.pack(pady=10)

        self.input_label = ttk.Label(self.root, text="Input Text:")
        self.input_label.pack(pady=10)
        self.input_entry = ttk.Entry(self.root, width=50)
        self.input_entry.pack(pady=10)

        self.key_label = ttk.Label(self.root, text="Key:")
        self.key_label.pack(pady=10)
        self.key_entry = ttk.Entry(self.root, width=50)
        self.key_entry.pack(pady=10)

        self.encrypt_button = ttk.Button(self.root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack(pady=10)
        self.decrypt_button = ttk.Button(self.root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack(pady=10)

        self.result_label = ttk.Label(self.root, text="Result:")
        self.result_label.pack(pady=10)
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)

    def run(self):
        self.root.mainloop()

    def encrypt(self):
        cipher = self.cipher_var.get()
        text = self.input_entry.get()
        key = self.key_entry.get()

        try:
            if cipher == "Caesar":
                shift = int(key)
                result = caesar_encrypt(text, shift)
            elif cipher == "Vigenère":
                result = vigenere_encrypt(text, key)
            elif cipher == "Playfair":
                result = playfair_encrypt(text, key)
            else:
                raise ValueError("Invalid cipher selected.")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        cipher = self.cipher_var.get()
        text = self.input_entry.get()
        key = self.key_entry.get()

        try:
            if cipher == "Caesar":
                shift = int(key)
                result = caesar_decrypt(text, shift)
            elif cipher == "Vigenère":
                result = vigenere_decrypt(text, key)
            elif cipher == "Playfair":
                result = playfair_decrypt(text, key)
            else:
                raise ValueError("Invalid cipher selected.")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
