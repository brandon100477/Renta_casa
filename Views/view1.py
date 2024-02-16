from tkinter import Tk, Label,Button, Entry, PhotoImage, Frame
import Controller.backController as backController
from PIL import Image, ImageTk  #Instalar la libreria de PIL
from customtkinter import CTk, CTkFrame #Instalar la libreria de customtkinter


class welcome():
    
    def __init__(self):
        
        def focus_in1(event):
            if self.search.get() == "Buscar...":
                self.search.delete(0, 'end')
                self.search.config(fg=backController.negro)

        def focus_out1(event):
            if self.search.get() == "":
                self.search.insert(0, 'Buscar...')
                self.search.config(fg=backController.gris_claro)
                
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
        
        
        self.search = Entry(self.window,bg=backController.gris_claro, bd=0.5, highlightthickness=0, insertwidth=2, justify='left', font=("Arial", 13), fg=backController.gris_oscuro)
        self.search.place(relx=0.35, rely=0.16, relheight=0.05, relwidth=0.6)
        self.search.insert(0, "Buscar...") #Implementacion de placeholder
        self.search.bind("<FocusIn>", focus_in1) #Controlador de eventos
        self.search.bind("<FocusOut>",focus_out1) #Controlador de eventos
        
        btn1 = backController.btn_inicio('Arrendatario', self.window, command=lambda: print("Arrendamiento"))
        btn1.place(relx=0.05, rely=0.15, relheight=0.06, relwidth=0.18)
        
        btn2 = backController.btn_inicio('Agregar Propietario', self.window, command=lambda:backController.aadd(self))
        btn2.place(relx=0.05, rely=0.30, relheight=0.06, relwidth=0.18)
        
        btn2 = backController.btn_inicio('Agregar Propiedad', self.window, command=lambda:backController.aadd(self))
        btn2.place(relx=0.05, rely=0.45, relheight=0.06, relwidth=0.18)
        
        btn3 = backController.btn_inicio('Ult. vez ingresado', self.window, command=lambda: print("Ult. vez ingresado"))
        btn3.place(relx=0.05, rely=0.60, relheight=0.06, relwidth=0.18)
        
        btn4 = backController.btn_inicio('Filtrar', self.window, command=lambda: print("Filtrar"))
        btn4.place(relx=0.05, rely=0.75, relheight=0.06, relwidth=0.18)
        
        
        btn = backController.close_Button('Cerrar sesión', self.window, command=lambda: backController.open2(self))
        btn.place(relx=0.05, rely=0.90, relheight=0.06, relwidth=0.18) #Botón para cerrar sesión
        #Creacion del logo
        logo = PhotoImage(file= 'img/icon.png')
        self.window.call('wm', 'iconphoto', self.window, logo)

