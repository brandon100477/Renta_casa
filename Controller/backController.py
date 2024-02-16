from tkinter import Tk, Label,Button, Entry, messagebox
from Views.sesion import inicio
from Views.view1 import welcome
from Views.register import register
from Views.add import ade
import database.Connection as conect
import mysql.connector as mysql
import hashlib

#Variables de entorno
global blanco, negro, gris, azul, rojo, azul_fg, rojo_fg, gris_claro,gris_oscuro, verde, var
blanco = '#FFFFFF'
gris = '#CFCFCF'
azul = '#3A94E7'
azul_fg = '#004B90'
rojo = '#E73A3A'
rojo_fg = '#DE0000'
negro = '#000000'
gris_claro = '#FBFBFB'
gris_oscuro ='#B8B8B8'
verde ='#61C12E'
var = '#56a5c6'
#función de prueba
def fnSuma(n1, n2):
    print(int(n1) + int(n2))
#Funcion para estilos de Label
def create_label(text, window):
    return Label(window, text=text, font=("Arial", 14), bg=blanco) #Tipo parrafo

def create_label2(text, window):
    return Label(window, text=text, font=("Arial", 28), bg=azul, fg=blanco) #Tipo titulo

#Función de estilos de botón
def create_Button(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, bg=azul, fg=blanco) #Botón con fondo azul

def create_Button1(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, bg=verde, fg=blanco) #Botón con fondo verde

def btn_inicio(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, bg=azul_fg, fg=blanco)  #Botón con fondo azul oscuro

def close_Button(text, window, command):
    return Button(window, text=text, font=("Arial", 16),command=command, bg=rojo, fg= negro)  #Botón con fondo rojo

def encriptar(contrasena):
    hash_contrasena = hashlib.sha256(contrasena.encode("utf-8")).hexdigest()
    return hash_contrasena

def open1(self): #Función para loguearse
    documento = self.txt1.get()
    password = self.txt2.get()
    encriptada = (encriptar(password))
    modific = "('"+encriptada+"',)" #Modificación de la clave encriptada para ser comparada
    conexion_registro = conect.registro() #conexion a data base
    cursor = conexion_registro.conexion.cursor()
    encrip = cursor.execute("SELECT password FROM usuario WHERE documento = %s", (documento,)) #data base query
    row = cursor.fetchone() #query type tupla
    scrip = str(row) #tupla in string
    if modific == scrip: #comparation
        self.window.destroy()
        welcome()
    elif row is None and encrip is None:
        messagebox.showinfo("Error","Usuario no existe. Por favor registrarse") #Error alert
    elif modific !=scrip:
        messagebox.showinfo("Error","Contraseña incorrecta. Intente nuevamente")#Error alert

def open2(self):
    self.window.destroy()
    inicio()
    
def registrar(self):
    self.window.destroy()
    register()

def registrar2(self):
    # Recoge los valores de los campos de texto
    documento = self.txt1.get()
    password = encriptar(self.txt2.get())
    nombre = self.txt3.get()
    apellido = self.txt4.get()
    
    if(nombre == "Respuesta..." or apellido =="Respuesta..." or documento == "CC 000000000000" ):
        messagebox.showinfo("Error", "Lo sentimos. Algo salío mal en el registro. Verifica los campos y vuelve a intentarlo.")# Muestra un mensaje de éxito
    else:
        try:
            # Crea una instancia de la clase 'registro' que maneja la conexión
            conexion_registro = conect.registro()
            cursor = conexion_registro.conexion.cursor() #cursor para interactuar con la base de datos
            sql = "INSERT INTO usuario (nombre, apellido, documento, password) VALUES (%s, %s, %s, %s)"  # Define la consulta SQL para la inserción
            valores = (nombre, apellido, documento, password) # Define los valores a insertar en la base de datos
            cursor.execute(sql, valores)# Ejecuta la consulta
            conexion_registro.conexion.commit() #Confirma los cambios en la base de datos
            cursor.close()# Cierra el cursor y la conexión
            conexion_registro.conexion.close()
            messagebox.showinfo("Éxito", "Registro exitoso")# Muestra un mensaje de éxito
            self.window.destroy()
            inicio()
        except mysql.Error as err:
            messagebox.showerror("Error", f"Error en la base de datos: {err}")# Muestra un mensaje de error si hay un problema con la base de datos
def aadd(self):
    self.window.destroy()
    ade()
    
def rollback(self):
    self.window.destroy()
    welcome()