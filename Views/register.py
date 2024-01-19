from tkinter import Tk, Label, Entry, PhotoImage, Canvas
import Controller.backController as backController
from PIL import Image, ImageTk  #Instalar la libreria de PIL
from customtkinter import CTk, CTkFrame #Instalar la libreria de customtkinter
import database.Connection as conect



class register():
    
    def __init__(self):
         
        def focus_in(event):
            if self.txt1.get() == "CC 000000000000":
                self.txt1.delete(0, 'end')
                self.txt1.config(fg=backController.negro)

        def focus_out(event):
            if self.txt1.get() == "":
                self.txt1.insert(0, 'CC 000000000000')
                self.txt1.config(fg=backController.gris_claro)
                
        def focus_in2(event):
            if self.txt2.get() == "***********":
                self.txt2.delete(0, 'end')
                self.txt2.config(fg=backController.negro)

        def focus_out2(event):
            if self.txt2.get() == "":
                self.txt2.insert(0, '***********')
                self.txt2.config(fg=backController.gris_claro)
        
        def focus_in3(event):
            if self.txt3.get() == "Respuesta...":
                self.txt3.delete(0, 'end')
                self.txt3.config(fg=backController.negro)

        def focus_out3(event):
            if self.txt3.get() == "":
                self.txt3.insert(0, 'Respuesta...')
                self.txt3.config(fg=backController.gris_claro)
                
        def focus_in4(event):
            if self.txt4.get() == "Respuesta...":
                self.txt4.delete(0, 'end')
                self.txt4.config(fg=backController.negro)

        def focus_out4(event):
            if self.txt4.get() == "":
                self.txt4.insert(0, 'Respuesta...')
                self.txt4.config(fg=backController.gris_claro)
                
        self.window = Tk()
        self.window.geometry("1366x768+105+20") # Creación de ventana (1366x768)->Tamaño de la ventana (+105+20)posicion de la ventana
        self.window.title("Registro") #titulo
        #Se crea una instancia para el poner una imagen para el fondo
        self.canvas = Canvas(self.window, width=1366, height=768)
        self.canvas.pack()
        fondo_image = PhotoImage(file='img/fondo.png')# Cargar la imagen de fondo
        self.canvas.create_image(0, 0, anchor='nw', image=fondo_image)# Configurar la imagen de fondo en el Canvas
        self.fondo_image = fondo_image # Restricción de la imagen para que no sea eliminada por el recolector de basura


        lbl = Label(self.window, text = 'Registrarse',font=("Arial", 28), bg=backController.blanco)
        lbl.place(relx=0.41, y=22, relheight=0.05, relwidth=0.19) #Posición del titulo de entrada
        #Label con sus estilos
        
        
        lbl1 = backController.create_label('Documento', self.window) 
        lbl1.place(relx=0.11, rely=0.7, relheight=0.05, relwidth=0.09)
        #textbox con sus estilos
        self.txt1 = Entry(self.window,bg=backController.gris, bd=0, highlightthickness=0, insertwidth=2, justify='center', font=("Arial", 13), fg=backController.gris_claro)
        self.txt1.place(relx=0.12, rely=0.74, relheight=0.05, relwidth=0.22)
        self.txt1.insert(0, "CC 000000000000") #Implementacion de placeholder
        self.txt1.bind("<FocusIn>", focus_in) #Controlador de eventos
        self.txt1.bind("<FocusOut>",focus_out) #Controlador de eventos
        
        #Label con sus estilos
        lbl2 = backController.create_label('Password', self.window)
        lbl2.place(relx=0.104, rely=0.5, relheight=0.05, relwidth=0.09)
        #textbox con sus estilos
        self.txt2 = Entry(self.window,bg=backController.gris, bd=0, highlightthickness=0, insertwidth=2, justify='center', show='*', font=("Arial", 18),fg=backController.gris_claro )
        self.txt2.place(relx=0.12, rely=0.54, relheight=0.05, relwidth=0.22)
        self.txt2.insert(0, "***********") #Implementacion de placeholder
        self.txt2.bind("<FocusIn>", focus_in2) #Controlador de eventos
        self.txt2.bind("<FocusOut>",focus_out2) #Controlador de eventos
        
        
        lbl3 = backController.create_label('Nombre', self.window) 
        lbl3.place(relx=0.1, rely=0.1, relheight=0.05, relwidth=0.09)
        #textbox con sus estilos
        self.txt3 = Entry(self.window,bg=backController.gris, bd=0, highlightthickness=0, insertwidth=2, justify='center', font=("Arial", 13), fg=backController.gris_claro)
        self.txt3.place(relx=0.12, rely=0.14, relheight=0.05, relwidth=0.22)
        self.txt3.insert(0, "Respuesta...") #Implementacion de placeholder
        self.txt3.bind("<FocusIn>", focus_in3) #Controlador de eventos
        self.txt3.bind("<FocusOut>",focus_out3) #Controlador de eventos
        
        lbl4 = backController.create_label('Apellido', self.window) 
        lbl4.place(relx=0.1, rely=0.3, relheight=0.05, relwidth=0.09)
        #textbox con sus estilos
        self.txt4 = Entry(self.window,bg=backController.gris, bd=0, highlightthickness=0, insertwidth=2, justify='center', font=("Arial", 13), fg=backController.gris_claro)
        self.txt4.place(relx=0.12, rely=0.34, relheight=0.05, relwidth=0.22)
        self.txt4.insert(0, "Respuesta...") #Implementacion de placeholder
        self.txt4.bind("<FocusIn>", focus_in4) #Controlador de eventos
        self.txt4.bind("<FocusOut>",focus_out4) #Controlador de eventos
        
        
        btn = backController.create_Button1('Iniciar sesión', self.window, command=lambda: backController.open2(self))
        btn.place(relx=0.75, rely=0.8, relheight=0.06, relwidth=0.18) #Botón para cerrar sesión
        
        btn = backController.btn_inicio('Registrar', self.window, command=lambda: backController.registrar2(self))
        btn.place(relx=0.55, rely=0.8, relheight=0.06, relwidth=0.18) #Botón para cerrar sesión
        #Creacion del logo
        logo = PhotoImage(file= 'img/icon.png')
        self.window.call('wm', 'iconphoto', self.window, logo)