from tkinter import Tk, Label,Button, Entry, PhotoImage
import Controller.backController as backController
from PIL import Image, ImageTk  #Instalar la libreria de PIL
from customtkinter import CTk, CTkFrame #Instalar la libreria de customtkinter


class welcome():
    
    def __init__(self):
        self.window2 = Tk()
        self.window2.geometry("1366x768+105+20") # Creación de ventana
        self.window2.title("Bienvenid@") #titulo
        self.window2.configure(bg=backController.blanco) #Color de fondo de fondo
        lbl = Label(self.window2, text = 'Bienvenido',font=("Arial", 28), bg=backController.blanco) 
        lbl.place(relx=0.41, y=22, relheight=0.05, relwidth=0.19) #Posición del titulo de entrada
        btn = backController.close_Button('Cerrar sesión', self.window2, command=lambda: backController.open2(self))
        btn.place(relx=0.22, rely=0.89, relheight=0.06, relwidth=0.12)
        #Creacion del logo
        
        logo = PhotoImage(file= 'img/icon.png')
        self.window2.call('wm', 'iconphoto', self.window2, logo )

