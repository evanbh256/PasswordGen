import os
import random
import string
import tkinter as tk
import pyperclip
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle



def generate_password(length, file_path):
    if length <= 4:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if length > 4 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
            break
        elif length <= 4:
            break
    pyperclip.copy(password)
    message_label.config(text="Copied to Clipboard", fg="green")
    if not file_path:
        message_label.config(text="Location not entered", fg="red")
    elif os.path.exists(file_path):
        with open(file_path, "a") as f:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{now}: {password}\n")
    else:
        with open(file_path, "w") as f:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{now}: {password}\n")
        

def generate_password_callback(event=None):
    try:
        length = int(length_entry.get())
        file_path = file_entry.get()
        generate_password(length, file_path)
        
        password_entry.delete(0, tk.END)
        password_entry.insert(0, pyperclip.paste())
        
    except ValueError:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Invalid length value")
        message_label.config(text="")

    file_entry.focus_set()

def copy_password_callback():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        message_label.config(text="Copied to Clipboard", fg="green")
    else:
        message_label.config(text="No password generated", fg="red")

root = tk.Tk()
root.geometry("400x350")
root.title("Password Generator")

style = ThemedStyle(root)
style.set_theme("blue")


length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=(10,0))

length_entry = tk.Entry(root)
length_entry.pack()

file_label = tk.Label(root, text="Enter file path:")
file_label.pack(pady=(10,0))

file_entry = tk.Entry(root, width=40)
file_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_callback)
generate_button.pack(pady=(10,0))

password_entry = tk.Entry(root, show="")
password_entry.pack()

copy_button = tk.Button(root, text="Copy Password", command=lambda: copy_password_callback())
copy_button.pack(pady=(10,0))

message_label = tk.Label(root, text="", font=("Arial", 10))
message_label.pack(pady=(5,0))

# Bind the Enter key to the generate_password_callback function for length_entry
length_entry.bind('<Return>', lambda event: file_entry.focus_set())

# Bind the Enter key to the generate_password_callback function for file_entry
file_entry.bind('<Return>', lambda event: generate_password_callback())

root.mainloop()
