from tkinter import *
from PANTALLA_BAJAS import *
from PANTALLA_DE_ALTAS import *
from PANTALLA_INFORMES import *
from PANTALLA_NOMINAS import *

class Navegador:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Navegator')
        self.wind.geometry('600x600')

        # Crear un contenedor para el texto
        text_frame = Frame(self.wind, pady=20)  
        text_frame.grid(row=0, column=0, columnspan=2, pady=120)

        # Agregar un texto al contenedor
        texto = "NOMINATOR+"
        label_texto = Label(text_frame, text=texto, font=('Helvetica', 18, 'bold'))
        label_texto.grid(row=0, column=0, columnspan=2)

        try:
            img = PhotoImage(file="E:/python/NOMINATOR/nomina.gif")  # Cambia a un formato compatible (.gif)
            label_img = Label(text_frame, image=img)
            label_img.grid(row=1, column=0, columnspan=2)  # Mostrar la imagen
            label_img.image = img  # Guardar una referencia para evitar que la imagen se elimine
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            
        # Crear un contenedor para los botones
        button_frame = Frame(self.wind, pady=20)  
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)

        # Configurar las columnas para que se expandan y se centren
        self.wind.columnconfigure(0, weight=1)
        self.wind.columnconfigure(1, weight=1)
            # Puedes personalizar la nueva ventana aquí

        # Boton Ventana ALTA
        button1 = Button(button_frame, text="ALTAS", command=ventana_altas, height=3, width=25, bg='#FDFD96', fg='black', bd=2, font=('Helvetica', 12, 'bold'))
        button1.grid(row=0, column=0, padx=5, pady=5)

        # Boton Ventana BAJAS
        button2 = Button(button_frame, text="BAJAS", command=ventana_bajas, height=3, width=25, bg='#FDFD96', fg='black', bd=2, font=('Helvetica', 12, 'bold'))
        button2.grid(row=0, column=1, padx=5, pady=5)

        # Boton Ventana INFORMES
        button3 = Button(button_frame, text="INFORMES",command=ventana_informes, height=3, width=25, bg='#FDFD96', fg='black', bd=2, font=('Helvetica', 12, 'bold'))
        button3.grid(row=1, column=0, padx=5, pady=5)

        #Boton Ventana NÓMINAS
        button4 = Button(button_frame, text="NÓMINAS", command=ventana_nominas, height=3, width=25, bg='#FDFD96', fg='black', bd=2, font=('Helvetica', 12, 'bold'))
        button4.grid(row=1, column=1, padx=5, pady=5)



if __name__ == '__main__':
    Window = Tk()
    application = Navegador(Window)
    Window.mainloop()
