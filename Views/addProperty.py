from tkinter import Tk, Label, Entry, PhotoImage, Frame, IntVar, Radiobutton, Button
import Controller.backController as backController
import Controller.addController as addController
from PIL import Image, ImageTk  #Instalar la libreria de PIL
from customtkinter import CTk, CTkFrame #Instalar la libreria de customtkinter
import database.Connection as conect



class propet():
    
    def __init__(self):
        
        def focus_in(event):
            if self.txt1.get() == "Identificación":
                self.txt1.delete(0, 'end')
                self.txt1.config(fg=backController.negro)

        def focus_out(event):
            if self.txt1.get() == "":
                self.txt1.insert(0, 'Identificación')
                self.txt1.config(fg=backController.gris_claro)
                
        def focus_in2(event):
            if self.txt2.get() == "Correo electronico":
                self.txt2.delete(0, 'end')
                self.txt2.config(fg=backController.negro)

        def focus_out2(event):
            if self.txt2.get() == "":
                self.txt2.insert(0, 'Correo electronico')
                self.txt2.config(fg=backController.gris_claro)
        
        def focus_in3(event):
            if self.txt3.get() == "Nombre":
                self.txt3.delete(0, 'end')
                self.txt3.config(fg=backController.negro)

        def focus_out3(event):
            if self.txt3.get() == "":
                self.txt3.insert(0, 'Nombre')
                self.txt3.config(fg=backController.gris_claro)
                
        """ def focus_in4(event):
            if self.txt4.get() == "Apellido":
                self.txt4.delete(0, 'end')
                self.txt4.config(fg=backController.negro)

        def focus_out4(event):
            if self.txt4.get() == "":
                self.txt4.insert(0, 'Apellido')
                self.txt4.config(fg=backController.gris_claro) """
                
        
                
        self.window = Tk()
        self.window.geometry("1366x768+105+20") # Creación de ventana (1366x768)->Tamaño de la ventana (+105+20)posicion de la ventana
        self.window.title("Propietarios") #titulo
        self.window.configure(bg=backController.blanco) #Color de fondo de fondo
        #Se crea una instancia para el poner una imagen para el fondo
        header = Frame(self.window, bg=backController.azul, height=90)
        header.pack(fill="x")
        # Parte principal de la ventana dividida en izquierda y derecha
        main_frame = Frame(self.window, bg= backController.blanco)
        main_frame.pack(fill="both", expand=True)

        left_half = Frame(main_frame, bg=backController.azul)  
        left_half.place(relx=0.0, rely=0.0, relwidth=0.3, relheight=1)# width para en ancho y height para el alto del campo en azul
        
        lbl = backController.create_label2('Lista de Propietarios', self.window)#Titulo y estilos
        lbl.place(relx=0.41, y=22, relheight=0.05, relwidth=0.26) #Posición del titulo de entrada
        
        btn1 = backController.btn_inicio('Inicio', self.window, command=lambda: backController.rollback(self))
        btn1.place(relx=0.05, rely=0.15, relheight=0.06, relwidth=0.18)
        
        btn2 = backController.btn_inicio('Arrendatario', self.window, command=lambda:backController.aadd(self))
        btn2.place(relx=0.05, rely=0.30, relheight=0.06, relwidth=0.18)
        
        btn2 = backController.btn_inicio('Agregar Propietario', self.window, command=lambda:backController.aadd(self))
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

        """ lbl = Label(self.window, text = 'Propiedad',font=("Arial", 28), bg=backController.blanco)
        lbl.place(relx=0.55, rely=0.16, relheight=0.05, relwidth=0.19) #Posición del titulo de entrada
        #Label con sus estilos """

        #textbox con sus estilos
        self.txt1 = Entry(self.window,bg=backController.gris_oscuro, bd=0, highlightthickness=0, insertwidth=2, justify='center', font=("Arial", 18), fg=backController.gris_claro)
        self.txt1.place(relx=0.44, rely=0.50, relheight=0.05, relwidth=0.22)
        self.txt1.insert(0, "Direccion") #Implementacion de placeholder
        self.txt1.bind("<FocusIn>", focus_in) #Controlador de eventos
        self.txt1.bind("<FocusOut>",focus_out) #Controlador de eventos

        #textbox con sus estilos
        self.txt2 = Entry(self.window,bg=backController.gris_oscuro, bd=0, highlightthickness=0, insertwidth=2, justify='center', font=("Arial", 18),fg=backController.gris_claro)
        self.txt2.place(relx=0.68, rely=0.50, relheight=0.05, relwidth=0.22)
        self.txt2.insert(0, "Telefono") #Implementacion de placeholder
        self.txt2.bind("<FocusIn>", focus_in2) #Controlador de eventos
        self.txt2.bind("<FocusOut>",focus_out2) #Controlador de eventos
        
        #textbox con sus estilos
        self.txt3 = Entry(self.window,bg=backController.gris_oscuro, bd=0, highlightthickness=0, insertwidth=2, justify='center', font=("Arial", 18), fg=backController.gris_claro)
        self.txt3.place(relx=0.44, rely=0.40, relheight=0.05, relwidth=0.22)
        self.txt3.insert(0, "Precio") #Implementacion de placeholder
        self.txt3.bind("<FocusIn>", focus_in3) #Controlador de eventos
        self.txt3.bind("<FocusOut>",focus_out3) #Controlador de eventos
        
        
        btn = backController.create_Button1('Registrar', self.window, command=lambda: addController.registrar2(self))
        btn.place(relx=0.75, rely=0.85, relheight=0.06, relwidth=0.18) #Botón para cerrar sesión
        
        btn = backController.btn_inicio('Volver', self.window, command=lambda: backController.rollback(self))
        btn.place(relx=0.35, rely=0.85, relheight=0.06, relwidth=0.18) #Botón para cerrar sesión
        #Creacion del logo
        logo = PhotoImage(file= 'img/icon.png')
        self.window.call('wm', 'iconphoto', self.window, logo)
        
        