from tkinter import Tk, Label, Entry, PhotoImage
import Controller.backController as backController
from PIL import Image, ImageTk  #Instalar la libreria de PIL
from customtkinter import CTk, CTkFrame #Instalar la libreria de customtkinter
import database.Connection as conexion
class inicio():
    
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
        self.txt1 = Entry(self.window,bg=backController.gris, bd=0, highlightthickness=0, insertwidth=2, justify='center', font=("Arial", 13), fg=backController.gris_claro)
        self.txt1.place(relx=0.76, rely=0.24, relheight=0.05, relwidth=0.22)
        self.txt1.insert(0, "CC 000000000000") #Implementacion de placeholder
        self.txt1.bind("<FocusIn>", focus_in) #Controlador de eventos
        self.txt1.bind("<FocusOut>",focus_out) #Controlador de eventos
        
        #Label con sus estilos
        lbl2 = backController.create_label('Password', self.window)
        lbl2.place(relx=0.904, rely=0.6, relheight=0.05, relwidth=0.09)
        #textbox con sus estilos
        self.txt2 = Entry(self.window,bg=backController.gris, bd=0, highlightthickness=0, insertwidth=2, justify='center', show='*', font=("Arial", 18),fg=backController.gris_claro )
        self.txt2.place(relx=0.76, rely=0.64, relheight=0.05, relwidth=0.22)
        self.txt2.insert(0, "***********") #Implementacion de placeholder
        self.txt2.bind("<FocusIn>", focus_in2) #Controlador de eventos
        self.txt2.bind("<FocusOut>",focus_out2) #Controlador de eventos
        
        
        btn = backController.create_Button('Ingresar', self.window, command=lambda: backController.open1(self))
        btn.place(relx=0.22, rely=0.89, relheight=0.06, relwidth=0.12)
        #Creacion del logo
        logo = PhotoImage(file= 'img/icon.png')
        self.window.call('wm', 'iconphoto', self.window, logo ) #implementación del logo
        self.window.mainloop()
        
