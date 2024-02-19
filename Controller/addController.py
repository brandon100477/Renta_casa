from tkinter import Tk, Label,Button, Entry, messagebox
from Views.addHome import home
from Views.addProperty import propet

from Views.view1 import welcome
from Views.register import register
import database.Connection as conect
import mysql.connector as mysql
import Controller.backController as backController



def house(self):
    self.window.destroy()
    home()
    
def prop(self):
    self.window.destroy()
    propet()


def registrar2(self):
    # Recoge los valores de los campos de texto
    documento = self.txt1.get()
    email= self.txt2.get()
    nombre = self.txt3.get()
    apellido = self.txt4.get()
    telefono = self.txt5.get()
    habilitar = 0
    
    if(documento == "Identificación" or email == "Correo electronico" or nombre == "Nombre" or apellido == "Apellido" or telefono == "Telefono"):
        messagebox.showerror("Error", "Lo sentimos. Algo salío mal en el registro. Verifica los campos y vuelve a intentarlo.")# Muestra un mensaje de éxito
    else:
        print(documento, email, nombre, apellido, telefono)
    try:
        # Crea una instancia de la clase 'registro' que maneja la conexión
        conexion_registro = conect.registro()
        cursor = conexion_registro.conexion.cursor() #cursor para interactuar con la base de datos
        sql = "INSERT INTO propietario (nombre, apellido, documento, telefono, email, habilitar) VALUES (%s, %s, %s, %s, %s, %s)"  # Define la consulta SQL para la inserción
        valores = (nombre, apellido, documento, telefono, email, habilitar) # Define los valores a insertar en la base de datos
        cursor.execute(sql, valores)# Ejecuta la consulta
        conexion_registro.conexion.commit() #Confirma los cambios en la base de datos
        cursor.close()# Cierra el cursor y la conexión
        conexion_registro.conexion.close()
        respuesta = messagebox.askquestion("Pregunta", "¿Quiere agregarle una propiedad?")# Muestra un mensaje de éxito
        if(respuesta =="yes"):
            self.window.destroy()
            home()
        else:
            messagebox.showinfo("Éxito", "Registro exitoso")# Muestra un mensaje de éxito
            self.window.destroy()
            welcome()
    except mysql.Error as err:
        messagebox.showerror("Error", f"Error en la base de datos: {err}")# Muestra un mensaje de error si hay un problema con la base de datos

def registrarhome(self):
    # Recoge los valores de los campos de texto
    documento = self.txt1.get()
    email= self.txt2.get()
    nombre = self.txt3.get()
    apellido = self.txt4.get()
    telefono = self.txt5.get()
    habilitar = 0
    
    if(documento == "Identificación" or email == "Correo electronico" or nombre == "Nombre" or apellido == "Apellido" or telefono == "Telefono"):
        messagebox.showerror("Error", "Lo sentimos. Algo salío mal en el registro. Verifica los campos y vuelve a intentarlo.")# Muestra un mensaje de éxito
    else:
        print(documento, email, nombre, apellido, telefono)
    try:
        # Crea una instancia de la clase 'registro' que maneja la conexión
        conexion_registro = conect.registro()
        cursor = conexion_registro.conexion.cursor() #cursor para interactuar con la base de datos
        sql = "INSERT INTO propietario (nombre, apellido, documento, telefono, email, habilitar) VALUES (%s, %s, %s, %s, %s, %s)"  # Define la consulta SQL para la inserción
        valores = (nombre, apellido, documento, telefono, email, habilitar) # Define los valores a insertar en la base de datos
        cursor.execute(sql, valores)# Ejecuta la consulta
        conexion_registro.conexion.commit() #Confirma los cambios en la base de datos
        cursor.close()# Cierra el cursor y la conexión
        conexion_registro.conexion.close()
        respuesta = messagebox.askquestion("Pregunta", "¿Quiere agregarle una propiedad?")# Muestra un mensaje de éxito
        if(respuesta =="yes"):
            
            print("dijo que si")
        else:
            messagebox.showinfo("Éxito", "Registro exitoso")# Muestra un mensaje de éxito
            self.window.destroy()
            welcome()
    except mysql.Error as err:
        messagebox.showerror("Error", f"Error en la base de datos: {err}")# Muestra un mensaje de error si hay un problema con la base de datos

def mostrarseleccionado(self):
            if self.txt4.get()==1:
                self.label1.configure(text="opcion seleccionada=Varon")
            if self.txt4.get()==2:
                self.label1.configure(text="opcion seleccionada=Mujer")