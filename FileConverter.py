import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("File Converter")

def openfile():
    file = askopenfile(filetypes = [('Word Files', '*.docx')])
    convert(file.name,'/convert.pdf')
    showinfo("Done","File Succesfully Converted")

label = tk.Label(root, text= "Select Word File:- ")
label.grid(row=0, column=0, padx=10,pady=10)

button = ttk.Button(root, text="Select", width=30, command=openfile)
button.grid(row=0, column=1, padx=5,pady=5)

root.mainloop()