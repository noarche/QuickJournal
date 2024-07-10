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
    text = textbox.get("1.0", tk.END).strip()
    if text:
        first_word = text.split()[0]
        filename = now.strftime('%B %d %Y %I%M %p') + f' - {first_word}.txt'
        file_path = os.path.join(save_path, filename)
        footer_text = ""
        if os.path.exists('footer.txt'):
            with open('footer.txt', 'r') as footer_file:
                footer_text = "\n" + footer_file.read().strip()
        with open(file_path, 'w') as file:
            file.write(text + footer_text)
        messagebox.showinfo("QuickJournal", f'Text saved as {file_path}')
        textbox.delete("1.0", tk.END)  # Clear the textbox
    else:
        messagebox.showwarning("QuickJournal", "No text to save")

# Function to show about information
def show_about():
    messagebox.showinfo("About", "QuickJournal is a simple journaling application that allows you to write and save text entries with ease.\nVisit GitHub for more information and updates.\nhttps://github.com/noarche/QuickJournal\nBuild Date: July 10 2024\n\nChanging Save Directory\nCreate a file named config.txt in the same directory this app is located and paste the full path to save to.\n\nAdding a signature:\nCreate a file named footer.txt in the same directory this app is located and paste your signature. This will be automatically added to all saved files moving forward.")

# Create the main window
root = tk.Tk()
root.title('QuickJournal')
root.geometry('500x480')
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

# Create and place the about button
about_button = tk.Button(root, text='About', command=show_about, bg='#0F3460', fg='#FFFFFF')
about_button.pack(pady=10)

# Start the main event loop
root.mainloop()

