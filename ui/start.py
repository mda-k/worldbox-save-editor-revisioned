#imports
import customtkinter as ctk
from PIL import Image, ImageTk
import os
from tkinter import messagebox, filedialog
import zlib
from pathlib import Path
import time
import sys
cdir = Path(__file__).resolve().parent
rdir = cdir.parent / "compilation"
if str(rdir) not in sys.path:
    sys.path.insert(0, str(rdir))
from decompile import *

#the main function that main.py calls
def choose_ui():
    #basics
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
       #smooth exit
    def FUCKMYLIFE():
        app.quit()
        app.destroy()
    app.protocol("WM_DELETE_WINDOW", FUCKMYLIFE)
    def choosefile():
        decompile()
        FUCKMYLIFE()
    
            
            
    #window config
    app.title("unprofessional worldbox save editor")
    app.geometry("672x300")
    app.resizable(False, False)
    app.configure(fg_color="black")
    
    #hover events
    def hov0(event):
        welcome.configure(text_color="#960101")
    def hov1(event):
        welcome.configure(text_color="#3e0000")
    def hov2(event):
        choosefilebutton.configure(text_color="#960101")
        choosefilebutton.configure(border_color="#960101")
        choosefilebutton.configure(fg_color="#1a1a1a")
    def hov3(event):
        choosefilebutton.configure(text_color="#3e0000")
        choosefilebutton.configure(border_color="#3e0000")
        choosefilebutton.configure(fg_color="#000000")
    #path stuff and hover events that require them
    fold0 = os.path.dirname(__file__)
    fold1 = os.path.join(fold0, "uwse_logo_fixed_resized.png")
    fold2 = os.path.join(fold0, "icon_new.ico")
    fold3 = os.path.join(fold0, "uwse_logo_hover.png")
    def hov4(event):
        try:
            pillow_imgh = Image.open(fold3)
        except FileNotFoundError:
            messagebox.showerror("mild error i guess", "the unprofessional branding image's hover version (/ui/uwse_logo_hover.png) is missing.")
            pillow_imgh = Image.new("RGB", (200, 200), color="black")
        top.configure(light_image=pillow_imgh)
        top.configure(dark_image=pillow_imgh)
        
    #the logo and icon
    try:
        app.iconbitmap(fold2)
    except Exception:
        messagebox.showerror("mild error i guess", "the unprofessional branding icon (/ui/icon_new.ico) is missing i think.")
    try:
        pillow_img = Image.open(fold1)
    except FileNotFoundError:
        messagebox.showerror("mild error i guess", "the unprofessional branding image (/ui/uwse_logo_fixed_resized.png) is missing i think.")
        pillow_img = Image.new("RGB", (200, 200), color="black")
    def hov5(event):
        top.configure(light_image=pillow_img)
        top.configure(dark_image=pillow_img)
    top = ctk.CTkImage(light_image=pillow_img, dark_image=pillow_img, size=(672, 186))
    packertop = ctk.CTkLabel(master=app, image=top, text="")
    packertop.pack()
    packertop.bind("<Enter>", hov4)
    packertop.bind("<Leave>", hov5)
    
    #content
    welcome = ctk.CTkLabel(master=app, wraplength=650, justify="left", text_color="#3e0000", text="welcome to the unprofessional worldbox save editor by md! this beginner inefficient, inconvenient program will decompile your .wbox save to a readable. json file. to start, this piece of shit program needs you to choose a .wbox file.", font=("Consolas", 16, "bold"))
    welcome.pack()
    welcome.bind("<Enter>", hov0)
    welcome.bind("<Leave>", hov1)
    choosefilebutton = ctk.CTkButton(master=app, corner_radius=8, fg_color="black", text_color="#3e0000", border_color="#3e0000", border_width=2, text="choose your savefile", command=lambda:choosefile(), font=("Consolas", 16, "bold"))
    choosefilebutton.pack()
    choosefilebutton.bind("<Enter>", hov2)
    choosefilebutton.bind("<Leave>", hov3)
    app.mainloop()
    
    
