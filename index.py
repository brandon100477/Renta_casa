from tkinter import Tk, Label,Button, Entry
import Controller.backController as backController

window = Tk()
window.geometry("1366x768") # Creación de ventana
window.title("Inicio de sesión") #titulo

lbl = Label(window, text = 'Inicia sesión',font=("Arial", 28)) 
lbl.place(relx=0.41, y=22, relheight=0.05, relwidth=0.19) #Posición del titulo de entrada

#Label con sus estilos
lbl1 = backController.create_label('Documento', window) 
lbl1.place(relx=0.9, rely=0.2, relheight=0.05, relwidth=0.09)
#textbox con sus estilos
txt1 = Entry(window,bg="#CFCFCF")
txt1.place(relx=0.76, rely=0.24, relheight=0.05, relwidth=0.22)

#Label con sus estilos
lbl2 = backController.create_label('Password', window)
lbl2.place(relx=0.904, rely=0.6, relheight=0.05, relwidth=0.09)
#textbox con sus estilos
txt2 = Entry(window,bg="#CFCFCF")
txt2.place(relx=0.76, rely=0.64, relheight=0.05, relwidth=0.22)

#lambda:backController.fnSuma(txt1.get(), txt2.get())
btn = backController.create_Button('Ingresar', window)
btn.place(relx=0.22, rely=0.89, relheight=0.06, relwidth=0.12)

window.mainloop()