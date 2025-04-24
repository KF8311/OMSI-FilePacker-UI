import tkinter as tk
from tkinter import font
import backend2

def read_omsi_path_frontend():
    omsi_path = textbox_omsi_path.get()
    backend2.read_omsi_path(omsi_path)

def read_zip_file_name_frontend():
    zip_name = textbox_packed_file_name.get()
    backend2.read_zip_file_name(zip_name)

def read_missing_files_list_frontend():
    missing_files_list = textbox_missing_objects.get("1.0", tk.END).strip()
    backend2.read_missing_files(missing_files_list)

def update_missing_list():
    print()

def call_all_command():
    read_missing_files_list_frontend()
    read_omsi_path_frontend()
    read_zip_file_name_frontend()
    update_missing_list()

# Create the main window
root = tk.Tk()
root.title("OMSI Missing File Packer")

# Set initial window size to full screen
root.state('zoomed')  # For Windows
# root.attributes('-zoomed', True)  # For Linux

# Create font objects
segoe_font = font.Font(family="Segoe UI", size=12)
segoe_font_small = font.Font(family="Segoe UI", size=8)

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

label_packed_file_name = tk.Label(left_frame, text="Name the Zip file", font=segoe_font)
label_packed_file_name.grid(row=2, column=0, sticky="nsew", pady=5)

textbox_packed_file_name = tk.Entry(left_frame, font=segoe_font_small)
textbox_packed_file_name.grid(row=3, column=0, sticky="ew", pady=5)

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
root.mainloop()