from tkinter import Tk, Label,Button, Entry
import Controller.backController as backController


class welcome():
    
    def __init__(self):
        self.window2 = Tk()
        self.window2.geometry("1366x768") # Creación de ventana
        self.window2.title("Bienvenid@") #titulo
        lbl = Label(self.window2, text = 'Bienvenido',font=("Arial", 28)) 
        lbl.place(relx=0.41, y=22, relheight=0.05, relwidth=0.19) #Posición del titulo de entrada
        btn = backController.close_Button('Cerrar sesión', self.window2, command=lambda: backController.open2(self))
        btn.place(relx=0.22, rely=0.89, relheight=0.06, relwidth=0.12)
        self.window2.mainloop()

