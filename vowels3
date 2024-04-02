import re
import tkinter as tk
from tkinter import filedialog

def remove_vowels(file_path, output_path):
    vowels = 'aeiouAEIOU'
    with open(file_path, 'r') as file:
        text = file.read()
        modified_text = re.sub(r'\b[aeiouAEIOU]\b', "''", text)
        modified_text = ''.join(char for char in modified_text if char not in vowels)
        print("Modified string:")
        print(modified_text)
        save_to_file(modified_text, output_path)

def save_to_file(text, output_path):
    with open(output_path, 'w') as file:
        file.write(text)
    print(f"Output saved to {output_path}")

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    input_file_path = filedialog.askopenfilename()
    if input_file_path:
        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if output_file_path:
            remove_vowels(input_file_path, output_file_path)
        else:
            print("No output file selected.")
    else:
        print("No input file selected.")

if __name__ == "__main__":
    open_file_dialog()
