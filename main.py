'''
Attach any additional dependencies or packages required for your Python project
1. pip install torch
2. pip install torchvision
3. pip install pyinstaller
4. pip install rembg

and run this file command is
>>>python gopal_jogi.py
'''

#!/usr/bin/env python3

import io
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image
from rembg.bg import remove
import os

class GopalJogi:
    def __init__(self, root):
        root.title("GopalJogi")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text='Input Image').grid(column=1, row=1, sticky=(N, E))

        self.input_path = StringVar()
        ttk.Button(mainframe, text="Select", command=self.get_inputfilename).grid(column=2, row=1, sticky=(N, E))

        ttk.Label(mainframe, text='Output Image').grid(column=1, row=2, sticky=(N, E))

        self.output_path = StringVar()
        ttk.Entry(mainframe, textvariable=self.output_path, state='readonly').grid(column=2, row=2, sticky=(N, E))
        ttk.Button(mainframe, text="Select", command=self.get_outputfilename).grid(column=3, row=2, sticky=(N, E))

        ttk.Button(mainframe, text="Process", command=self.process).grid(column=2, row=3, sticky=(N, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind("<Return>", self.process)

    def get_inputfilename(self, *args):
        self.input_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]))
        self.generate_default_output_filename()

    def get_outputfilename(self, *args):
        self.output_path.set(filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")]))
    
    def generate_default_output_filename(self):
        input_file_path = self.input_path.get()
        if input_file_path:
            input_file_name = os.path.basename(input_file_path)
            root, ext = os.path.splitext(input_file_name)
            default_output_file_name = f"{root}_output.png"
            self.output_path.set(os.path.join(os.path.dirname(input_file_path), default_output_file_name))

    def process(self, *args):
        try:
            input_file_path = self.input_path.get()
            output_file_path = self.output_path.get()
            
            with open(input_file_path, 'rb') as input_file:
                input_content = input_file.read()
                
            result = remove(input_content)
            img = Image.open(io.BytesIO(result)).convert("RGBA")
            img.save(output_file_path)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    root = Tk()
    GopalJogi(root)
    root.mainloop()
