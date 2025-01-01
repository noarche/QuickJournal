import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMenuBar, QFileDialog
from datetime import datetime
import configparser

# Configuration file path
CONFIG_FILE = 'config.ini'

def get_config():
    config = configparser.ConfigParser()
    if not os.path.exists(CONFIG_FILE):
        config['Paths'] = {'save_path': os.getcwd(), 'signatures_path': os.path.abspath('signatures')}
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(CONFIG_FILE)
    return config

def update_config(section, key, value):
    config = get_config()
    if section not in config:
        config[section] = {}
    config[section][key] = value
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def get_path(key):
    config = get_config()
    return config['Paths'].get(key, os.getcwd())

# Get paths from config.ini
save_path = get_path('save_path')
signatures_path = get_path('signatures_path')

# Function to save the text to a file
def save_entry(textbox, titlebox, signature_dropdown):
    text = textbox.toPlainText().strip()
    title = titlebox.text().strip()

    if text:
        if not title:
            title = datetime.now().strftime('%B.%d.%Y.%H.%M.%S')
        else:
            title = title.replace(' ', '.')

        if '/' in title or '\\' in title:
            dir_path, title = os.path.split(title)
            dir_path = os.path.join(save_path, dir_path)
            os.makedirs(dir_path, exist_ok=True)
        else:
            dir_path = save_path

        filename = f'{title}.txt'
        file_path = os.path.join(dir_path, filename)

        footer_text = ""
        selected_signature = signature_dropdown.currentText()
        if selected_signature != "No Signature":
            signature_path = os.path.join(signatures_path, selected_signature)
            if os.path.exists(signature_path):
                with open(signature_path, 'r', encoding='utf-8') as footer_file:
                    footer_text = "\n" + footer_file.read().strip()

        # Save content to the file
        content_to_save = text
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content_to_save + footer_text)

        QtWidgets.QMessageBox.information(None, "QuickJournal", f'Text saved as {file_path}')
        textbox.clear()
        titlebox.clear()
    else:
        QtWidgets.QMessageBox.warning(None, "QuickJournal", "No text to save")

# Function to show about information
def show_about():
    about_text = (
        "QuickJournal is a simple journaling application that allows you to write and save text entries with ease.\n"
        "Visit GitHub for more information and updates.\n"
        "https://github.com/noarche/QuickJournal\n"
        "Build Date: July 10 2024\n\n"
        "Updated: JAN 1 2025\n\n"
        "Configuration:\n"
        "The application supports multiple configurable paths in the config.ini file:\n"
        "  - save_path: The directory where journal entries are saved.\n"
        "  - signatures_path: The directory containing signature files.\n\n"
        "Use the File menu options to change these paths dynamically."
    )
    QtWidgets.QMessageBox.information(None, "About", about_text)

# Function to change save location
def change_save_location():
    new_path = QFileDialog.getExistingDirectory(None, "Select Save Directory", save_path)
    if new_path:
        update_config('Paths', 'save_path', new_path)
        QtWidgets.QMessageBox.information(None, "QuickJournal", f"Save directory updated to: {new_path}")

# Function to change signatures directory
def change_signatures_location():
    new_path = QFileDialog.getExistingDirectory(None, "Select Signatures Directory", signatures_path)
    if new_path:
        update_config('Paths', 'signatures_path', new_path)
        QtWidgets.QMessageBox.information(None, "QuickJournal", f"Signatures directory updated to: {new_path}")

# Function to show configuration info
def show_config_info():
    config = get_config()
    save_path = config['Paths'].get('save_path', 'Not Found')
    signatures_path = config['Paths'].get('signatures_path', 'Not Found')
    config_info_text = (
        f"Current Save Path: {save_path}\n"
        f"Signatures Directory: {signatures_path}"
    )
    QtWidgets.QMessageBox.information(None, "Configuration Info", config_info_text)

# Main application class
class QuickJournalApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QuickJournal")
        self.setGeometry(100, 100, 600, 500)

        self.setStyleSheet(
            "background-color: rgba(26, 26, 46, 180); color: #FFFFFF; font-family: Arial; font-size: 14px;"
        )

        layout = QtWidgets.QVBoxLayout()

        # Menu bar
        menu_bar = QMenuBar(self)
        file_menu = menu_bar.addMenu("File")

        about_action = QtWidgets.QAction("About", self)
        about_action.triggered.connect(show_about)
        file_menu.addAction(about_action)

        change_save_action = QtWidgets.QAction("Change Save Location", self)
        change_save_action.triggered.connect(change_save_location)
        file_menu.addAction(change_save_action)

        change_signatures_action = QtWidgets.QAction("Change Signatures Location", self)
        change_signatures_action.triggered.connect(change_signatures_location)
        file_menu.addAction(change_signatures_action)

        config_info_action = QtWidgets.QAction("Config Info", self)
        config_info_action.triggered.connect(show_config_info)
        file_menu.addAction(config_info_action)

        layout.setMenuBar(menu_bar)

        # Label
        label = QtWidgets.QLabel("Enter your text below:")
        label.setStyleSheet("background-color: rgba(26, 26, 46, 150);")
        layout.addWidget(label)

        # Textbox
        self.textbox = QtWidgets.QPlainTextEdit()
        self.textbox.setStyleSheet("background-color: rgba(22, 33, 62, 180); color: #FFFFFF;")
        layout.addWidget(self.textbox)

        # Title input
        self.titlebox = QtWidgets.QLineEdit()
        self.titlebox.setPlaceholderText("Enter file title (optional)")
        self.titlebox.setStyleSheet("background-color: rgba(22, 33, 62, 180); color: #FFFFFF;")
        layout.addWidget(self.titlebox)

        # Signature dropdown
        self.signature_dropdown = QtWidgets.QComboBox()
        self.signature_dropdown.addItem("No Signature")
        if os.path.exists(signatures_path):
            for filename in os.listdir(signatures_path):
                if filename.endswith('.txt'):
                    self.signature_dropdown.addItem(filename)
        self.signature_dropdown.setStyleSheet("background-color: rgba(22, 33, 62, 180); color: #FFFFFF;")
        layout.addWidget(self.signature_dropdown)

        # Save button
        save_button = QtWidgets.QPushButton("Save Entry")
        save_button.clicked.connect(lambda: save_entry(self.textbox, self.titlebox, self.signature_dropdown))
        save_button.setStyleSheet("background-color: rgba(15, 52, 96, 180); color: #FFFFFF;")
        layout.addWidget(save_button)

        self.setLayout(layout)

# Run the application
def main():
    app = QtWidgets.QApplication([])
    window = QuickJournalApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
