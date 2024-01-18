from tkinter import Tk, Label,Button, Entry, PhotoImage, Frame, Canvas
import Controller.backController as backController
from PIL import Image, ImageTk  #Instalar la libreria de PIL
from customtkinter import CTk, CTkFrame #Instalar la libreria de customtkinter


class welcome():
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1366x768+105+20") # Creación de ventana
        self.window.title("Bienvenid@") #titulo
        self.window.configure(bg=backController.blanco) #Color de fondo de fondo
        
        header = Frame(self.window, bg=backController.azul, height=90)
        header.pack(fill="x")

                # Parte principal de la ventana dividida en izquierda y derecha
        main_frame = Frame(self.window, bg= backController.blanco)
        main_frame.pack(fill="both", expand=True)

        left_half = Frame(main_frame, bg=backController.azul)  
        left_half.place(relx=0.0, rely=0.0, relwidth=0.3, relheight=1)# width para en ancho y height para el alto del campo en azul
        
        lbl = backController.create_label2('Bienvenido', self.window)#Titulo y estilos
        lbl.place(relx=0.41, y=22, relheight=0.05, relwidth=0.19) #Posición del titulo de entrada
        
        
        search = Entry(self.window,bg=backController.gris_claro)
        search.place(relx=0.35, rely=0.16, relheight=0.05, relwidth=0.6)
        
        
        btn1 = backController.btn_inicio('Arrendatario', self.window, command=lambda: print("Arrendamiento"))
        btn1.place(relx=0.05, rely=0.2, relheight=0.06, relwidth=0.18)
        
        btn2 = backController.btn_inicio('Agregar', self.window, command=lambda: print("Agregar"))
        btn2.place(relx=0.05, rely=0.35, relheight=0.06, relwidth=0.18)
        
        btn3 = backController.btn_inicio('Ult. vez ingresado', self.window, command=lambda: print("Ult. vez ingresado"))
        btn3.place(relx=0.05, rely=0.5, relheight=0.06, relwidth=0.18)
        
        btn4 = backController.btn_inicio('Filtrar', self.window, command=lambda: print("Filtrar"))
        btn4.place(relx=0.05, rely=0.65, relheight=0.06, relwidth=0.18)
        
        
        btn = backController.close_Button('Cerrar sesión', self.window, command=lambda: backController.open2(self))
        btn.place(relx=0.05, rely=0.8, relheight=0.06, relwidth=0.18) #Botón para cerrar sesión
        #Creacion del logo
        logo = PhotoImage(file= 'img/icon.png')
        self.window.call('wm', 'iconphoto', self.window, logo)

