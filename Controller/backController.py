from tkinter import Tk, Label,Button, Entry

#función de prueba
def fnSuma(n1, n2):
    print(int(n1) + int(n2))
#Funcion para estilos de Label
def create_label(text, window):
    return Label(window, text=text, font=("Arial", 14))
#Función de estilos de botón
def create_Button(text, window):
    return Button(window, text=text, font=("Arial", 16),command=lambda: print("Hello word!"), background="#3A94E7")