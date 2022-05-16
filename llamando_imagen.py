#llamamos librerias
from tkinter import *
import tkinter

# creamos la ventana
ventana = Tk()
# le ponemos titulo a la ventana
ventana.title('Presenta')

img1 = tkinter.PhotoImage(file="logo v1.png")

# para mostrarla usamos label
label1 = tkinter.Label(ventana, image=img1)
label1.pack()

ventana.mainloop()
