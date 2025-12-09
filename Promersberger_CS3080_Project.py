import string
import secrets
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, symbols=True, mixed=True):
    chars=string.digits
    chars+=string.ascii_letters if mixed else string.ascii_lowercase
    if symbols:
        chars+=string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def generate_and_show():
    length=int(length_input.get())
    symbols=symbols_var.get()
    mixed=mixed_var.get()
    password=generate_password(length, symbols, mixed)

    popup=tk.Toplevel(root)
    popup.title("Password Generator")
    popup_width,popup_height= 300,150
    root_x=root.winfo_rootx()+100
    root_y=root.winfo_rooty()+100
    root_width = root.winfo_width()
    root_height = root.winfo_height()

    x = root_x + root_width - popup_width
    y = root_y + root_height - popup_height
    popup.geometry(f"{popup_width}x{popup_height}+{x+100}+{y}")

    tk.Label(popup, text="Your Password:", font=("Times New Roman", 15, "bold")).pack(pady=(10,0))
    tk.Label(popup, text=password, font=("Times New Roman", 17)).pack(padx=20, pady=10)
    
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(password)
        # Keeps clipboard content after window closes
        root.update()
    
    tk.Button(popup, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
    tk.Button(popup, text="Close", command=popup.destroy).pack(pady=5)

root = tk.Tk()
root.title("CS3080 Password Generator")
root.geometry("300x150")
root.resizable(True,True)

tk.Label(root, text="Password Length:").pack()
length_input = tk.Entry(root)
length_input.insert(0, "12")
length_input.pack()

symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w")

mixed_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Mixed Case", variable=mixed_var).pack(anchor="w")

tk.Button(root, text="Generate Password", command=generate_and_show).pack()

root.mainloop()

