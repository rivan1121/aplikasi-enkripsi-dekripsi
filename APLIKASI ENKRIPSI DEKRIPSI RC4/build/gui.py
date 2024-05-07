import tkinter as tk
from tkinter import ttk

def RC4(key, text):
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    out = []
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(char ^ S[(S[i] + S[j]) % 256]))

    return ''.join(out)

def encrypt_decrypt():
    key = [ord(char) for char in key_entry.get()]
    text = [ord(char) for char in text_entry.get()]

    ciphertext = RC4(key, text)

    plaintext = RC4(key, [ord(char) for char in ciphertext])

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Ciphertext: {ciphertext}\nPlaintext: {plaintext}")

root = tk.Tk()
root.title("ENCRYPT/DECRYPT RC4")
root.geometry("450x350")
root.resizable(False, False)
root.configure(bg="#212121")

font = ("Monaco", 10)

style = ttk.Style()
style.configure("TButton", foreground="#212121", background="#4CAF50", font=font)
style.map("TButton", foreground=[('active', '#4CAF50'), ('pressed', '#4CAF50')])

title_label = ttk.Label(root, text="RC4 ENCRYPT/DECRYPT", font=("Roboto", 20), background="#212121", foreground="#4CAF50")
title_label.grid(row=0, column=0,pady=15, columnspan=2)

key_label = ttk.Label(root, text="KEY:", font=font, background="#212121", foreground="white")
key_label.grid(row=1, column=0, padx=10, pady=(20, 5), sticky="w")

key_entry = ttk.Entry(root, width=44, font=font)
key_entry.grid(row=1, column=1, padx=10, pady=(25, 5))

text_label = ttk.Label(root, text="TEXT:", font=font, background="#212121", foreground="white")
text_label.grid(row=2, column=0, padx=10, pady=(5, 5), sticky="w")

text_entry = ttk.Entry(root, width=44, font=font)
text_entry.grid(row=2, column=1, padx=10, pady=(5, 5))

button = ttk.Button(root, text="ENCRYPT/DECRYPT", command=encrypt_decrypt)
button.grid(row=3, column=1, padx=10, pady=15, sticky="e")

result_text = tk.Text(root, height=8, width=52, font=font)
result_text.configure(bg="#424242", fg="white")
result_text.grid(row=4, column=0, columnspan=2, padx=15, pady=0)
root.mainloop()
