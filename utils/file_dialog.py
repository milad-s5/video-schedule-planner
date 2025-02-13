import tkinter as tk
from tkinter import filedialog

class FileDialog:
    @staticmethod
    def select_directory():
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        return filedialog.askdirectory(title="Select Course Directory")
