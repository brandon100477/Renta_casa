from tkinter import Tk, Label,Button, Entry
from Views.sesion import inicio
from Views.view1 import welcome


global blanco, negro, gris, azul, log
blanco = '#FFFFFF'
gris = '#CFCFCF'
azul = '#3A94E7'

#función de prueba
def fnSuma(n1, n2):
    print(int(n1) + int(n2))
#Funcion para estilos de Label
def create_label(text, window):
    return Label(window, text=text, font=("Arial", 14), bg=blanco)
#Función de estilos de botón
def create_Button(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, background="#3A94E7")

def close_Button(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, background="#E73A3A")

def open1(self):
    self.window.destroy()
    welcome()
    
def open2(self):
    self.window2.destroy()
    inicio()