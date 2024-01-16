from tkinter import Tk, Label,Button, Entry
import backController

window = Tk()
window.geometry("1366x768")
window.title("Inicio de sesión")

lbl = Label(window, text = 'Inicia sesión')
lbl.place(relx=0.44, y=22, relheight=0.05, relwidth=0.09)

lbl1 = Label(window, text = 'suma1')
lbl1.place(relx=0.9, rely=0.2, relheight=0.05, relwidth=0.09)
txt1 = Entry(window,bg="gray")
txt1.place(relx=0.747, rely=0.24, relheight=0.05, relwidth=0.22)

lbl2 = Label(window, text = 'suma2')
lbl2.place(relx=0.9, rely=0.6, relheight=0.05, relwidth=0.09)
txt2 = Entry(window,bg="gray")
txt2.place(relx=0.747, rely=0.64, relheight=0.05, relwidth=0.22)




btn = Button(window, text ='button firts', command=lambda:backController.fnSuma(txt1.get(), txt2.get()))
btn.place(relx=0.22, rely=0.89, relheight=0.05, relwidth=0.09)


window.mainloop()
