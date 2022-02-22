from distutils.archive_util import make_archive
import os, shutil 

#sorts the files
def sort():

    #gets user and sets the working dir to downloads
    user = os.getlogin()
    main_dir = r"C:\Users\{}\{}".format(user, directoryInput.get()) 
    #directoryInput.get() instead of variable with the value because the value isn't constantly updated but .get() is
    
    os.chdir(main_dir)

    #gets each file in the working dir 
    for file in os.listdir():
        file = file.lower()
        file_extension = os.path.splitext(file)[1]

        #switch check of the extensions
        match file_extension:
            case ".mp3":
                if check_for_mp3.get() == 1:
                    #if user checks for mp3 the value of check_for_mp3 = 1
                    #creates folder within working directory if it doesnt exist already for the extension type
                    move_to_sound_folder_path = r"C:\Users\{}\Downloads\sound".format(user)
                    if not os.path.exists(move_to_sound_folder_path):
                        os.makedirs(move_to_sound_folder_path)
                    #location of where the file being worked with is
                    source_path = r"C:\Users\{}\Downloads\{}".format(user, file)
                    #sets the created folder path as the location of where the file is to be moved
                    destination_path = r"C:\Users\{}\Downloads\sound\{}".format(user, file)
                    print("{} has been moved to sound folder".format(file))
                    #moves the file 
                    shutil.move(source_path, destination_path)
            case ".pdf":
                if check_for_pdf.get() == 1: 
                    #checks if keyword is in file title and moves to unique folder from pdf
                    for word in ["css", "fafsa", "tax", "reciept", "wang", "nj", "aid"]:
                        if word in file:
                            move_to_finance_folder_path = r"C:\Users\{}\Downloads\finance".format(user)
                            if not os.path.exists(move_to_finance_folder_path):
                                os.makedirs(move_to_finance_folder_path)
                            source_path = r"C:\Users\{}\Downloads\{}".format(user, file)
                            destination_path = r"C:\Users\{}\Downloads\finance\{}".format(user, file)
                            shutil.move(source_path, destination_path)
                            print("{} has been moved to finance folder".format(file))
                            break 
                    else:
                        move_to_pdf_folder_path = r"C:\Users\{}\Downloads\pdf".format(user)
                        if not os.path.exists(move_to_pdf_folder_path):
                            os.makedirs(move_to_pdf_folder_path)
                        source_path = r"C:\Users\{}\Downloads\{}".format(user, file)
                        destination_path = r"C:\Users\{}\Downloads\pdf\{}".format(user, file)
                        shutil.move(source_path, destination_path)
                        print("{} has been moved to pdf folder".format(file))
            case ".jpg":
                if check_for_jpg.get() == 1: 
                    move_to_jpg_folder_path = r"C:\Users\{}\Downloads\jpg".format(user)
                    if not os.path.exists(move_to_jpg_folder_path):
                        os.makedirs(move_to_jpg_folder_path)
                    source_path = r"C:\Users\{}\Downloads\{}".format(user, file)
                    destination_path = r"C:\Users\{}\Downloads\jpg\{}".format(user, file)
                    print("{} has been moved to jpg folder".format(file))
                    shutil.move(source_path, destination_path)
            case ".png":
                if check_for_png.get() == 1:
                    source_path = r"C:\Users\{}\Downloads\{}".format(user, file)
                    destination_path = r"C:\Users\{}\Downloads\jpg\{}".format(user, file)
                    print("{} has been moved to jpg folder".format(file))
                    shutil.move(source_path, destination_path)
            case ".docx":
                if check_for_docx.get() == 1:
                    move_to_docx_folder_path = r"C:\Users\{}\Downloads\docx".format(user)
                    if not os.path.exists(move_to_docx_folder_path):
                        os.makedirs(move_to_docx_folder_path)
                    source_path = r"C:\Users\{}\Downloads\{}".format(user, file)
                    destination_path = r"C:\Users\{}\Downloads\docx\{}".format(user, file)
                    print("{} has been moved to docx folder".format(file))
                    shutil.move(source_path, destination_path)

#user interface
import tkinter as tk
from tkinter import CENTER, filedialog, Text

#creates main window 
window = tk.Tk()
window.title("File Sorter")
canvas = tk.Canvas(window, height = 300, width = 300, bg = "#C2C2C2")
canvas.pack()

#creates variables for checkbox inputs
check_for_mp3 = tk.IntVar()
check_for_pdf = tk.IntVar()
check_for_jpg = tk.IntVar()
check_for_png = tk.IntVar()
check_for_docx = tk.IntVar()

#creates checkboxes
check_mp3 = tk.Checkbutton(window, text="mp3", variable = check_for_mp3, onvalue = 1, offvalue = 0)
check_pdf = tk.Checkbutton(window, text="pdf", variable = check_for_pdf, onvalue = 1, offvalue = 0)
check_jpg = tk.Checkbutton(window, text="jpg", variable = check_for_jpg, onvalue = 1, offvalue = 0)
check_png = tk.Checkbutton(window, text="png", variable = check_for_png, onvalue = 1, offvalue = 0)
check_docx = tk.Checkbutton(window, text="docx", variable = check_for_docx, onvalue = 1, offvalue = 0)
check_mp3.place(x=25,y=200)
check_pdf.place(x=75,y=200)
check_jpg.place(x=125,y=200)
check_png.place(x=175,y=200)
check_docx.place(x=225,y=200)

#creates sort button 
sortButton = tk.Button(window, text = "Sort", padx = 10, pady = 10, fg = 'Black', bg = '#C2C2C2', command = sort)
sortButton.place(relx = 0.5, rely = 0.5, anchor=CENTER)

#creates intake box
directoryInput = tk.Entry(window)
canvas.create_window(150, 100, window = directoryInput)

#runs the tkinter window 
window.mainloop()