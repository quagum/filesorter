from distutils.archive_util import make_archive
import os, shutil 

user = os.getlogin()
main_dir = r"C:\Users\{}\Downloads".format(user)
os.chdir(main_dir)

def sort():
    for file in os.listdir():
        file = file.lower()
        file_extension = os.path.splitext(file)[1]

        match file_extension:
            case ".mp3":
                if check_for_mp3.get() == 1:
                    move_to_sound_folder_path = r"C:\Users\quagu\Downloads\sound"
                    if not os.path.exists(move_to_sound_folder_path):
                        os.makedirs(move_to_sound_folder_path)
                    source_path = r"C:\Users\quagu\Downloads\{}".format(file)
                    destination_path = r"C:\Users\quagu\Downloads\sound\{}".format(file)
                    print("{} has been moved to sound folder".format(file))
                    shutil.move(source_path, destination_path)
            case ".pdf":
                if check_for_pdf.get() == 1: 
                    for word in ["css", "fafsa", "tax", "reciept", "wang", "nj", "aid"]:
                        if word in file:
                            move_to_finance_folder_path = r"C:\Users\quagu\Downloads\finance"
                            if not os.path.exists(move_to_finance_folder_path):
                                os.makedirs(move_to_finance_folder_path)
                            source_path = r"C:\Users\quagu\Downloads\{}".format(file)
                            destination_path = r"C:\Users\quagu\Downloads\finance\{}".format(file)
                            shutil.move(source_path, destination_path)
                            print("{} has been moved to finance folder".format(file))
                            break 
                    else:
                        move_to_pdf_folder_path = r"C:\Users\quagu\Downloads\pdf"
                        if not os.path.exists(move_to_pdf_folder_path):
                            os.makedirs(move_to_pdf_folder_path)
                        source_path = r"C:\Users\quagu\Downloads\{}".format(file)
                        destination_path = r"C:\Users\quagu\Downloads\pdf\{}".format(file)
                        shutil.move(source_path, destination_path)
                        print("{} has been moved to pdf folder".format(file))
            case ".jpg":
                if check_for_jpg.get() == 1: 
                    move_to_jpg_folder_path = r"C:\Users\quagu\Downloads\jpg"
                    if not os.path.exists(move_to_jpg_folder_path):
                        os.makedirs(move_to_jpg_folder_path)
                    source_path = r"C:\Users\quagu\Downloads\{}".format(file)
                    destination_path = r"C:\Users\quagu\Downloads\jpg\{}".format(file)
                    print("{} has been moved to jpg folder".format(file))
                    shutil.move(source_path, destination_path)
            case ".png":
                if check_for_png.get() == 1:
                    source_path = r"C:\Users\quagu\Downloads\{}".format(file)
                    destination_path = r"C:\Users\quagu\Downloads\jpg\{}".format(file)
                    print("{} has been moved to jpg folder".format(file))
                    shutil.move(source_path, destination_path)
            case ".docx":
                if check_for_docx.get() == 1:
                    move_to_docx_folder_path = r"C:\Users\quagu\Downloads\docx"
                    if not os.path.exists(move_to_docx_folder_path):
                        os.makedirs(move_to_docx_folder_path)
                    source_path = r"C:\Users\quagu\Downloads\{}".format(file)
                    destination_path = r"C:\Users\quagu\Downloads\docx\{}".format(file)
                    print("{} has been moved to docx folder".format(file))
                    shutil.move(source_path, destination_path)

import tkinter as tk
from tkinter import CENTER, filedialog, Text

window = tk.Tk()
canvas = tk.Canvas(window, height = 700, width = 700, bg = "#263D42")
canvas.pack()


check_for_mp3 = tk.IntVar()
check_for_pdf = tk.IntVar()
check_for_jpg = tk.IntVar()
check_for_png = tk.IntVar()
check_for_docx = tk.IntVar()

check_mp3 = tk.Checkbutton(window, text="mp3", variable = check_for_mp3, onvalue = 1, offvalue = 0)
check_pdf = tk.Checkbutton(window, text="pdf", variable = check_for_pdf, onvalue = 1, offvalue = 0)
check_jpg = tk.Checkbutton(window, text="jpg", variable = check_for_jpg, onvalue = 1, offvalue = 0)
check_png = tk.Checkbutton(window, text="png", variable = check_for_png, onvalue = 1, offvalue = 0)
check_docx = tk.Checkbutton(window, text="docx", variable = check_for_docx, onvalue = 1, offvalue = 0)
check_mp3.pack()
check_pdf.pack()
check_jpg.pack()
check_png.pack()
check_docx.pack()


sortButton = tk.Button(window, text = "Sort", padx = 10, pady = 10, fg = 'White', bg = '#263D42', command = sort)
sortButton.place(relx = 0.5, rely = 0.5, anchor=CENTER)

window.mainloop()

