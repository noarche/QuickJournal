import tkinter as tk
from tkinter import scrolledtext, messagebox
import datetime
import os

# Function to read the save path from config.txt
def get_save_path():
    config_file = 'config.txt'
    default_path = os.getcwd()  # Default to current working directory
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            path = file.readline().strip()
            if os.path.isdir(path):
                return path
    return default_path

# Get the save path from config.txt
save_path = get_save_path()

# Function to save the text to a file
def save_entry():
    now = datetime.datetime.now()
    filename = now.strftime('%B %d %Y %I%M %p') + '.txt'
    text = textbox.get("1.0", tk.END).strip()
    if text:
        file_path = os.path.join(save_path, filename)
        with open(file_path, 'w') as file:
            file.write(text)
        messagebox.showinfo("QuickJournal", f'Text saved as {file_path}')
    else:
        messagebox.showwarning("QuickJournal", "No text to save")

# Create the main window
root = tk.Tk()
root.title('QuickJournal')
root.geometry('500x430')
root.configure(bg='#1A1A2E')

# Create and place the text label
label = tk.Label(root, text='Enter your text below:', bg='#1A1A2E', fg='#FFFFFF')
label.pack(pady=10)

# Create and place the scrolled text box
textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, bg='#16213E', fg='#FFFFFF', insertbackground='#FFFFFF')
textbox.pack(pady=10, padx=10)

# Create and place the save button
save_button = tk.Button(root, text='Save Entry', command=save_entry, bg='#0F3460', fg='#FFFFFF')
save_button.pack(pady=10)

# Start the main event loop
root.mainloop()
