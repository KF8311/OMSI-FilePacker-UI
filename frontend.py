import tkinter as tk
from tkinter import font
import backend2

def read_omsi_path_frontend():
    omsi_path = textbox_omsi_path.get()
    backend2.read_omsi_path(omsi_path)

def read_missing_files_list_frontend():
    missing_files_list = textbox_missing_objects.get("1.0", tk.END).strip()
    backend2.read_missing_files(missing_files_list)

def call_all_command():
    read_missing_files_list_frontend()
    read_omsi_path_frontend()

# Create the main window
root = tk.Tk()
root.title("OMSI Missing File Packer")

# Set the window size to the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Create font objects
segoe_font = font.Font(family="Segoe UI", size=12)
segoe_font_small = font.Font(family="Segoe UI", size=8)

# Create and place the "Input your OMSI2 path" label and textbox
label_omsi_path = tk.Label(root, text="Input your OMSI2 path", font=segoe_font)
label_omsi_path.grid(row=0, column=0, padx=10, pady=10, sticky='w')

textbox_omsi_path = tk.Entry(root, width=100, font=segoe_font_small)
textbox_omsi_path.grid(row=1, column=0, padx=10, pady=10, sticky='nw')

# Create and place the "Input missing objects" label and textbox
label_missing_objects = tk.Label(root, text="Input missing objects", font=segoe_font)
label_missing_objects.grid(row=0, column=1, padx=10, pady=10, sticky='e')

textbox_missing_objects = tk.Text(root, width=100, height=10, font=segoe_font_small)
textbox_missing_objects.grid(row=1, column=1, padx=10, pady=10, sticky='e')

# Create and place the button
button = tk.Button(root, text="Pack", font=segoe_font, command=call_all_command)
button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
