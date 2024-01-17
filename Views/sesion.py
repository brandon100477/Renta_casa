from tkinter import Tk, Label, Entry, PhotoImage
import Controller.backController as backController
from PIL import Image, ImageTk  #Instalar la libreria de PIL
from customtkinter import CTk, CTkFrame #Instalar la libreria de customtkinter

class inicio():
    
    def __init__(self):
         
        
        self.window = Tk()
        self.window.geometry("1366x768+105+20") # Creación de ventana (1366x768)->Tamaño de la ventana (+105+20)posicion de la ventana
        self.window.title("Inicio de sesión") #titulo
        self.window.configure(bg=backController.blanco) #Color de fondo de fondo
        imag = Image.open("img/image.png")
        #Estilos e implementacion de imagen
        photo = ImageTk.PhotoImage(imag)
        background_label = Label(self.window, image=photo)
        background_label.place(relx=0.2, rely=0.35, relwidth=0.16, relheight=0.3)

        lbl = Label(self.window, text = 'Inicia sesión',font=("Arial", 28), bg=backController.blanco)
        lbl.place(relx=0.41, y=22, relheight=0.05, relwidth=0.19) #Posición del titulo de entrada
        #Label con sus estilos
        lbl1 = backController.create_label('Documento', self.window) 
        lbl1.place(relx=0.9, rely=0.2, relheight=0.05, relwidth=0.09)
        #textbox con sus estilos
        txt1 = Entry(self.window,bg=backController.gris)
        txt1.place(relx=0.76, rely=0.24, relheight=0.05, relwidth=0.22)
        #Label con sus estilos
        lbl2 = backController.create_label('Password', self.window)
        lbl2.place(relx=0.904, rely=0.6, relheight=0.05, relwidth=0.09)
        #textbox con sus estilos
        txt2 = Entry(self.window,bg=backController.gris)
        txt2.place(relx=0.76, rely=0.64, relheight=0.05, relwidth=0.22)
        #lambda:backController.fnSuma(txt1.get(), txt2.get())
        btn = backController.create_Button('Ingresar', self.window, command=lambda: backController.open1(self))
        btn.place(relx=0.22, rely=0.89, relheight=0.06, relwidth=0.12)
        #Creacion del logo
        logo = PhotoImage(file= 'img/icon.png')
        self.window.call('wm', 'iconphoto', self.window, logo ) #implementación del logo
        self.window.mainloop()
        
