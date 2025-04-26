import tkinter as tk
from tkinter import font, filedialog, messagebox
import backend
import os
import winreg
import sys

# missing_files = []
# frontend.py

REG_PATH = r"Software\MyTkApp"
REG_VALUE_NAME = "TextboxValue"
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def save_to_registry():
    """
    I have never experience winreg so this part is written by Bing Copilot:
    Save the content of the textbox to the Windows registry.
    """
    text_value = textbox_omsi_path.get()
    try:
        # Open or create the registry key where you want to save your value
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        # Save the value (REG_SZ for a string)
        winreg.SetValueEx(key, REG_VALUE_NAME, 0, winreg.REG_SZ, text_value)
        winreg.CloseKey(key)
        print("OMSI Path saved successfully!")
    except Exception as e:
        print("Error", f"Failed to save data: {e}")

def load_from_registry():
    """
    Load the content from the Windows registry, if it exists, and set it in the textbox.
    """
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, REG_VALUE_NAME)
        winreg.CloseKey(key)
        textbox_omsi_path.delete(0, tk.END)
        textbox_omsi_path.insert(0, value)
    except Exception as e:
        # If the key/value is not found, skip loading.
        print("No registry value to load:", e)

def read_omsi_path_frontend():
    omsi_path = textbox_omsi_path.get()
    backend.read_omsi_path(omsi_path)

def read_zip_file_name_frontend():
    zip_name = textbox_packed_file_name.get()
    backend.read_zip_file_name(zip_name)

def read_missing_files_list_frontend():
    missing_files_list = textbox_missing_objects.get("1.0", tk.END).strip()
    backend.read_missing_files(missing_files_list)

def call_all_command():
    save_to_registry()
    read_missing_files_list_frontend()
    read_omsi_path_frontend()
    read_zip_file_name_frontend()
    textbox_not_found_files.config(state="normal")
    # global missing_files
    # Call the pack_files function with the collected parameters
    missing_files = backend.pack_files(backend.source_directory, backend.output_zip_file, backend.file_paths)
    textbox_not_found_files.delete("1.0", tk.END)
    for file in missing_files:
        textbox_not_found_files.insert(tk.END, file)
    messagebox.showinfo("Finished packing", f"Your file is packed as {backend.output_zip_file}")
    textbox_not_found_files.config(state="disabled")


def browse_path():
    chosen_path = filedialog.askdirectory(title="Select Path")
    if chosen_path:  # If a valid directory was selected
        textbox_omsi_path.delete(0, tk.END)
        textbox_omsi_path.insert(0, chosen_path)

# Create the main window
root = tk.Tk()
root.title("OMSI Missing File Packer")
root.iconbitmap(resource_path('omsi-file-packer-logo.ico'))

# Set initial window size to full screen
root.state('zoomed')  # For Windows
# root.attributes('-zoomed', True)  # For Linux

# Create font objects
segoe_font = font.Font(family="Segoe UI", size=16)
segoe_font_small = font.Font(family="Segoe UI", size=10)

# Configure root grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

# Create left and right frames
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

# Configure left frame
left_frame.columnconfigure(0, weight=1)
left_frame.rowconfigure(1, weight=0)

# OMSI Path elements
label_omsi_path = tk.Label(left_frame, text="Input your OMSI2 path", font=segoe_font)
label_omsi_path.grid(row=0, column=0, sticky="nsew", pady=5)

textbox_omsi_path = tk.Entry(left_frame, font=segoe_font_small)
textbox_omsi_path.grid(row=1, column=0, sticky="ew", pady=5)
# current_path = os.getcwd()
# textbox_omsi_path.insert(0, current_path)

browse_button = tk.Button(left_frame, text="Browse", command=browse_path)
browse_button.grid(row=1, column=1, padx=5)

label_packed_file_name = tk.Label(left_frame, text="Name the Zip file", font=segoe_font)
label_packed_file_name.grid(row=2, column=0, sticky="nsew", pady=5)

textbox_packed_file_name = tk.Entry(left_frame, font=segoe_font_small)
textbox_packed_file_name.grid(row=3, column=0, sticky="ew", pady=5)

label_not_found_files = tk.Label(left_frame, text="Not found files", font=segoe_font)
label_not_found_files.grid(row=4, column=0, sticky="nsew", pady=5)

textbox_not_found_files = tk.Text(left_frame, font=segoe_font_small, wrap=tk.WORD, height=80)
textbox_not_found_files.grid(row=5, column=0, sticky="nsew", pady=5)
textbox_not_found_files.config(state="disabled")


# Configure right frame
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(1, weight=1)

# Missing Files elements
label_missing_objects = tk.Label(right_frame, text="Input missing objects", font=segoe_font)
label_missing_objects.grid(row=0, column=0, sticky="nsew", pady=5)

textbox_missing_objects = tk.Text(right_frame, font=segoe_font_small, wrap=tk.WORD)
textbox_missing_objects.grid(row=1, column=0, sticky="nsew", pady=5)

# Add scrollbar for text widget
scrollbar = tk.Scrollbar(right_frame, command=textbox_missing_objects.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
textbox_missing_objects.config(yscrollcommand=scrollbar.set)

# Pack button at the bottom
button = tk.Button(root, text="Pack", font=segoe_font, command=call_all_command)
button.grid(row=1, column=0, columnspan=2, pady=20, sticky="")

# Run the application
load_from_registry()
root.mainloop()