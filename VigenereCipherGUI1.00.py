import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

def encrypt(text: str, keyphrase: str) -> str:
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyphrase[key_index]) - ord('A')
            new_char = chr(((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
            result.append(new_char)
            key_index = (key_index + 1) % len(keyphrase)
        else:
            result.append(char)
    return "".join(result)

def decrypt(cipher_text: str, keyphrase: str) -> str:
    result = []
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            shift = ord(keyphrase[key_index]) - ord('A')
            new_char = chr(((ord(char.upper()) - ord('A') - shift + 26) % 26) + ord('A'))
            result.append(new_char)
            key_index = (key_index + 1) % len(keyphrase)
        else:
            result.append(char)
    return "".join(result)

def paste_from_clipboard(widget):
    try:
        text = root.clipboard_get()
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, text)
    except tk.TclError:
        messagebox.showerror("Error", "No text in clipboard!")

def paste_to_entry(widget):
    try:
        text = root.clipboard_get()
        widget.delete(0, tk.END)
        widget.insert(0, text)
    except tk.TclError:
        messagebox.showerror("Error", "No text in clipboard!")

def copy_to_clipboard(widget):
    text = widget.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")
    else:
        messagebox.showerror("Error", "No text to copy!")

def show_frame(frame):
    for f in (main_menu_frame, encryption_frame, decryption_frame):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

def perform_encryption():
    text = encrypt_input.get("1.0", tk.END).strip()
    keyphrase = encrypt_key_entry.get().replace(" ", "").upper()
    
    if not any(c.isalpha() for c in text):
        messagebox.showerror("Error", "Text must contain at least one alphabetic character.")
        return
    if not keyphrase.isalpha() or keyphrase == "":
        messagebox.showerror("Error", "Keyphrase must consist of alphabetic characters only.")
        return
    
    result = encrypt(text.upper(), keyphrase)
    encrypt_output.config(state=tk.NORMAL)
    encrypt_output.delete("1.0", tk.END)
    encrypt_output.insert(tk.END, result)
    encrypt_output.config(state=tk.DISABLED)

def perform_decryption():
    text = decrypt_input.get("1.0", tk.END).strip()
    keyphrase = decrypt_key_entry.get().replace(" ", "").upper()
    
    if not any(c.isalpha() for c in text):
        messagebox.showerror("Error", "Text must contain at least one alphabetic character.")
        return
    if not keyphrase.isalpha() or keyphrase == "":
        messagebox.showerror("Error", "Keyphrase must consist of alphabetic characters only.")
        return
    
    result = decrypt(text, keyphrase)
    decrypt_output.config(state=tk.NORMAL)
    decrypt_output.delete("1.0", tk.END)
    decrypt_output.insert(tk.END, result)
    decrypt_output.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Encryption Tool")

main_menu_frame = tk.Frame(root)
encryption_frame = tk.Frame(root)
decryption_frame = tk.Frame(root)

monospace = tkFont.Font(family="Courier", size=10)
ascii_art = """\
██╗   ██╗██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ ███████╗
██║   ██║██║██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝
██║   ██║██║██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝█████╗  
╚██╗ ██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝  
 ╚████╔╝ ██║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗
  ╚═══╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                               
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗                     
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗                    
██║     ██║██████╔╝███████║█████╗  ██████╔╝                    
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗                    
╚██████╗██║██║     ██║  ██║███████╗██║  ██║                    
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝          
"""
tk.Label(main_menu_frame, text=ascii_art, font=monospace, fg="red", justify="left").pack(padx=10, pady=5)
tk.Label(main_menu_frame, text="By Joshua M Clatney - Ethical Pentesting Enthusiast.", font=("Arial", 10), fg="blue").pack(pady=5)
tk.Label(main_menu_frame, text="Options:", font=("Arial", 12, "bold")).pack(pady=(5, 10))
tk.Button(main_menu_frame, text="Encrypt Text", width=20, command=lambda: show_frame(encryption_frame)).pack(pady=5)
tk.Button(main_menu_frame, text="Decrypt Text", width=20, command=lambda: show_frame(decryption_frame)).pack(pady=5)

frame_encrypt_input = tk.Frame(encryption_frame)
frame_encrypt_input.pack(fill="x", padx=10, pady=(10, 0))
tk.Label(frame_encrypt_input, text="Enter text to encrypt:").pack(side=tk.LEFT)
tk.Button(frame_encrypt_input, text="Paste", command=lambda: paste_from_clipboard(encrypt_input)).pack(side=tk.RIGHT)
encrypt_input = tk.Text(encryption_frame, height=5, width=60)
encrypt_input.pack(padx=10, pady=5)

tk.Label(encryption_frame, text="Enter keyphrase:").pack(anchor="w", padx=10, pady=(10, 0))
encrypt_key_entry = tk.Entry(encryption_frame, width=60)
encrypt_key_entry.pack(padx=10, pady=5)

button_frame_enc = tk.Frame(encryption_frame)
button_frame_enc.pack(pady=5)
tk.Button(button_frame_enc, text="Paste Keyphrase", command=lambda: paste_to_entry(encrypt_key_entry)).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame_enc, text="Encrypt", command=perform_encryption).pack(side=tk.LEFT, padx=5)

frame_encrypt_output = tk.Frame(encryption_frame)
frame_encrypt_output.pack(fill="x", padx=10, pady=(10, 0))
tk.Label(frame_encrypt_output, text="Encrypted text:").pack(side=tk.LEFT)
tk.Button(frame_encrypt_output, text="Copy", command=lambda: copy_to_clipboard(encrypt_output)).pack(side=tk.RIGHT)
encrypt_output = tk.Text(encryption_frame, height=5, width=60, state=tk.DISABLED)
encrypt_output.pack(padx=10, pady=5)

tk.Button(encryption_frame, text="Return to Main Menu", command=lambda: show_frame(main_menu_frame)).pack(pady=10)

frame_decrypt_input = tk.Frame(decryption_frame)
frame_decrypt_input.pack(fill="x", padx=10, pady=(10, 0))
tk.Label(frame_decrypt_input, text="Enter text to decrypt:").pack(side=tk.LEFT)
tk.Button(frame_decrypt_input, text="Paste", command=lambda: paste_from_clipboard(decrypt_input)).pack(side=tk.RIGHT)
decrypt_input = tk.Text(decryption_frame, height=5, width=60)
decrypt_input.pack(padx=10, pady=5)

tk.Label(decryption_frame, text="Enter keyphrase:").pack(anchor="w", padx=10, pady=(10, 0))
decrypt_key_entry = tk.Entry(decryption_frame, width=60)
decrypt_key_entry.pack(padx=10, pady=5)

button_frame_dec = tk.Frame(decryption_frame)
button_frame_dec.pack(pady=5)
tk.Button(button_frame_dec, text="Paste Keyphrase", command=lambda: paste_to_entry(decrypt_key_entry)).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame_dec, text="Decrypt", command=perform_decryption).pack(side=tk.LEFT, padx=5)

frame_decrypt_output = tk.Frame(decryption_frame)
frame_decrypt_output.pack(fill="x", padx=10, pady=(10, 0))
tk.Label(frame_decrypt_output, text="Decrypted text:").pack(side=tk.LEFT)
tk.Button(frame_decrypt_output, text="Copy", command=lambda: copy_to_clipboard(decrypt_output)).pack(side=tk.RIGHT)
decrypt_output = tk.Text(decryption_frame, height=5, width=60, state=tk.DISABLED)
decrypt_output.pack(padx=10, pady=5)

tk.Button(decryption_frame, text="Return to Main Menu", command=lambda: show_frame(main_menu_frame)).pack(pady=10)

show_frame(main_menu_frame)
root.mainloop()