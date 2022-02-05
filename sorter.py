from distutils.archive_util import make_archive
import os, shutil 

def sort():
    os.chdir(r"C:\Users\charl\Downloads")

from distutils.archive_util import make_archive
import os, shutil 

def sort():
    os.chdir(r"C:\Users\charl\Downloads")

    move_to_sound_folder_path = r"C:\Users\charl\Downloads\sound"
    if not os.path.exists(move_to_sound_folder_path):
        os.makedirs(move_to_sound_folder_path)

    move_to_pdf_folder_path = r"C:\Users\charl\Downloads\pdf"
    if not os.path.exists(move_to_pdf_folder_path):
        os.makedirs(move_to_pdf_folder_path)

    move_to_finance_folder_path = r"C:\Users\charl\Downloads\finance"
    if not os.path.exists(move_to_finance_folder_path):
        os.makedirs(move_to_finance_folder_path)

    move_to_jpg_folder_path = r"C:\Users\charl\Downloads\jpg"
    if not os.path.exists(move_to_jpg_folder_path):
        os.makedirs(move_to_jpg_folder_path)

    move_to_docx_folder_path = r"C:\Users\charl\Downloads\docx"
    if not os.path.exists(move_to_docx_folder_path):
        os.makedirs(move_to_docx_folder_path)

    for file in os.listdir():
        file = file.lower()
        file_extension = os.path.splitext(file)[1]
        match file_extension:
            case ".mp3":
                source_path = r"C:\Users\charl\Downloads\{}".format(file)
                destination_path = r"C:\Users\charl\Downloads\sound\{}".format(file)
                print("{} has been moved to sound folder".format(file))
                shutil.move(source_path, destination_path)
            case ".pdf":
                if (word in file for word in ["css", "fafsa", "tax", "reciept", "wang"]):
                    source_path = r"C:\Users\charl\Downloads\{}".format(file)
                    destination_path = r"C:\Users\charl\Downloads\finance\{}".format(file)
                    print("{} has been moved to finance folder".format(file))
                    shutil.move(source_path, destination_path)
                else:
                    source_path = r"C:\Users\charl\Downloads\{}".format(file)
                    destination_path = r"C:\Users\charl\Downloads\pdf\{}".format(file)
                    print("{} has been moved to pdf folder".format(file))
                    shutil.move(source_path, destination_path)
            case ".jpg":
                source_path = r"C:\Users\charl\Downloads\{}".format(file)
                destination_path = r"C:\Users\charl\Downloads\jpg\{}".format(file)
                print("{} has been moved to jpg folder".format(file))
                shutil.move(source_path, destination_path)
            case ".png":
                source_path = r"C:\Users\charl\Downloads\{}".format(file)
                destination_path = r"C:\Users\charl\Downloads\jpg\{}".format(file)
                print("{} has been moved to jpg folder".format(file))
                shutil.move(source_path, destination_path)
            case ".docx":
                source_path = r"C:\Users\charl\Downloads\{}".format(file)
                destination_path = r"C:\Users\charl\Downloads\docx\{}".format(file)
                print("{} has been moved to docx folder".format(file))
                shutil.move(source_path, destination_path)

import tkinter as tk
from tkinter import CENTER, filedialog, Text

root = tk.Tk()

canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42")
canvas.pack()

sortButton = tk.Button(root, text = "Sort", padx = 10, pady = 10, fg = 'White', bg = '#263D42', command = sort)
sortButton.place(relx = 0.5, rely = 0.5, anchor=CENTER)


root.mainloop()