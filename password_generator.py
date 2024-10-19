import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())  # Get password length
        if length <= 0:
            raise ValueError("Password length must be positive")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid password length")
        return

    include_upper = uppercase_var.get()
    include_lower = lowercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    char_set = ''
    if include_upper:
        char_set += string.ascii_uppercase
    if include_lower:
        char_set += string.ascii_lowercase
    if include_digits:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation

    if not char_set:
        messagebox.showerror("Error", "No character set selected!")
        return

    password = ''.join(random.choice(char_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("PASSWORD GENERATOR")
root.geometry("350x500")
root.configure(bg='#262C33')  # Dark background color

# Load the background image
background_image = Image.open("background1.jpg")  # Use your background image
bg = ImageTk.PhotoImage(background_image)

# Create a Label widget to display the background image
background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1) 

# Password Length Input
Password_Length = tk.Label(root, text="Password Length", font=("Arial", 12), fg='white', bg='#262C33', bd=0)
Password_Length.pack(pady=10)


length_entry = tk.Entry(root)
length_entry.pack(pady=15)


#label
title_label=tk.Label(root,text="PASSWORD GENERATOR TOOL",font=("times new roman",17,"bold"),fg="blue",bg="white")
title_label.place(x=0,y=700,width=1600)



# Character options
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w')

# Password output
#tk.Label(root, text="Generated Password:").pack(pady=10)
Generated_Password=tk.Label(root, text="Generated Password:", font=("Arial", 12), fg='white', bg='#262C33', bd=0)
Generated_Password.pack(pady=10)
password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=10)



# Buttons for generation and clipboard
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
# Run the application
root.mainloop()
