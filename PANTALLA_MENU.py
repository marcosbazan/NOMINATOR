from tkinter import *
from PANTALLA_BAJAS import *
from PANTALLA_DE_ALTAS import *
from PANTALLA_INFORMES import *
from PANTALLA_NOMINAS import *

class Navegador:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Gestión de Nóminas')
        self.wind.geometry('650x650')
        self.wind.configure(bg="#f0f4f7")  # Fondo suave

        # ---- Encabezado ----
        header_frame = Frame(self.wind, bg="#2c3e50", pady=15)
        header_frame.pack(fill="x")

        label_texto = Label(
            header_frame,
            text="GESTIÓN DE NÓMINAS",
            font=('Helvetica', 20, 'bold'),
            bg="#2c3e50",
            fg="white"
        )
        label_texto.pack()

        # ---- Imagen ----
        try:
            img = PhotoImage(file="nomina.gif")  # debe estar en misma carpeta
            label_img = Label(self.wind, image=img, bg="#f0f4f7")
            label_img.image = img  # evitar que se libere
            label_img.pack(pady=20)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        # ---- Botonera ----
        button_frame = Frame(self.wind, bg="#f0f4f7")
        button_frame.pack(pady=20)

        button_style = {
            "height": 3,
            "width": 20,
            "bg": "#3498db",   # azul moderno
            "fg": "white",
            "bd": 0,
            "activebackground": "#2980b9",
            "activeforeground": "white",
            "font": ('Helvetica', 12, 'bold'),
            "relief": "flat"
        }

        # Boton Ventana ALTAS
        button1 = Button(button_frame, text="ALTAS", command=ventana_altas, **button_style)
        button1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Boton Ventana BAJAS
        button2 = Button(button_frame, text="BAJAS", command=ventana_bajas, **button_style)
        button2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Boton Ventana INFORMES
        button3 = Button(button_frame, text="INFORMES", command=ventana_informes, **button_style)
        button3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Boton Ventana NÓMINAS
        button4 = Button(button_frame, text="NÓMINAS", command=ventana_nominas, **button_style)
        button4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Expansión de botones en la cuadrícula
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)


if __name__ == '__main__':
    Window = Tk()
    application = Navegador(Window)
    Window.mainloop()
