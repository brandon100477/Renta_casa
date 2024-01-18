from tkinter import Tk, Label,Button, Entry
from Views.sesion import inicio
from Views.view1 import welcome


global blanco, negro, gris, azul, rojo, azul_fg, rojo_fg, gris_claro,gris_oscuro
blanco = '#FFFFFF'
gris = '#CFCFCF'
azul = '#3A94E7'
azul_fg = '#004B90'
rojo = '#E73A3A'
rojo_fg = '#DE0000'
negro = '#000000'
gris_claro = '#FBFBFB'
gris_oscuro ='#B8B8B8'
#función de prueba
def fnSuma(n1, n2):
    print(int(n1) + int(n2))
#Funcion para estilos de Label
def create_label(text, window):
    return Label(window, text=text, font=("Arial", 14), bg=blanco)

def create_label2(text, window):
    return Label(window, text=text, font=("Arial", 28), bg=azul, fg=blanco)

#Función de estilos de botón
def create_Button(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, bg=azul, fg=blanco)

def btn_inicio(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, bg=azul, fg=blanco)

def close_Button(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, bg=rojo, fg= negro)

def open1(self):
    self.window.destroy()
    welcome()
    
def open2(self):
    self.window.destroy()
    inicio()