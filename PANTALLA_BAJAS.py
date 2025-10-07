from tkinter import Tk, Label, Entry, Button, Frame
import sqlite3
from datetime import datetime


def buscar_codigo(codigo_empleado):
    try:
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Empleados WHERE Codigo = ?", (codigo_empleado,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado
    except sqlite3.Error as e:
        print(f"Error al buscar código: {str(e)}")
        return None


def validar_fecha(fecha):
    try:
        fecha_obj = datetime.strptime(fecha, '%d-%m-%Y')
        return fecha_obj.date() >= datetime.now().date()
    except ValueError:
        return False


def ejecutar_consulta(codigo_empleado, fecha_baja, label_mensaje):
    try:
        empleado_existente = buscar_codigo(codigo_empleado)

        if empleado_existente:
            if validar_fecha(fecha_baja):
                conexion = sqlite3.connect('nominator.db')
                cursor = conexion.cursor()
                cursor.execute("UPDATE Empleados SET FechaFin = ? WHERE Codigo = ?", (fecha_baja, codigo_empleado))
                conexion.commit()
                conexion.close()
                label_mensaje.config(text=f"✅ Fecha de baja actualizada para el código {codigo_empleado}", fg="green")
            else:
                label_mensaje.config(text="⚠️ La fecha de baja debe ser válida y posterior al día actual.", fg="red")
        else:
            label_mensaje.config(text=f"❌ El código {codigo_empleado} no existe en la base de datos.", fg="red")

    except sqlite3.Error as e:
        label_mensaje.config(text=f"Error al actualizar la base de datos: {str(e)}", fg="red")


def ventana_bajas():
    ventana = Tk()
    ventana.title("Gestión de Bajas")
    ventana.geometry('600x450')
    ventana.configure(bg="#f0f4f7")

    # ---- ENCABEZADO ----
    header = Frame(ventana, bg="#2c3e50", pady=15)
    header.pack(fill="x")

    Label(header, text="REGISTRO DE BAJAS", font=('Helvetica', 20, 'bold'),
          bg="#2c3e50", fg="white").pack()

    # ---- FORMULARIO ----
    form_frame = Frame(ventana, bg="#f0f4f7")
    form_frame.pack(pady=40)

    Label(form_frame, text='CÓDIGO EMPLEADO', font=('Helvetica', 12, 'bold'),
          bg="#f0f4f7", fg="#2c3e50").grid(row=0, column=0, padx=15, pady=10, sticky="e")
    entry_codigo = Entry(form_frame, justify="center", width=30, font=('Helvetica', 12))
    entry_codigo.grid(row=0, column=1, padx=10, pady=10)

    Label(form_frame, text='FECHA DE BAJA (dd-mm-YYYY)', font=('Helvetica', 12, 'bold'),
          bg="#f0f4f7", fg="#2c3e50").grid(row=1, column=0, padx=15, pady=10, sticky="e")
    entry_fecha_baja = Entry(form_frame, justify="center", width=30, font=('Helvetica', 12))
    entry_fecha_baja.grid(row=1, column=1, padx=10, pady=10)

    # ---- MENSAJE DE VALIDACIÓN ----
    label_mensaje = Label(ventana, text="", font=('Helvetica', 13, 'bold'),
                          bg="#f0f4f7", fg="red", pady=10)
    label_mensaje.pack(pady=10)

    # ---- BOTÓN ----
    button_style = {
        "height": 2,
        "width": 20,
        "bg": "#3498db",
        "fg": "white",
        "bd": 0,
        "activebackground": "#2980b9",
        "activeforeground": "white",
        "font": ('Helvetica', 12, 'bold'),
        "relief": "flat"
    }

    Button(ventana, text="CONFIRMAR BAJA",
           command=lambda: ejecutar_consulta(entry_codigo.get(), entry_fecha_baja.get(), label_mensaje),
           **button_style).pack(pady=20)

    ventana.mainloop()


if __name__ == "__main__":
    ventana_bajas()
