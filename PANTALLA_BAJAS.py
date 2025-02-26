from tkinter import Tk, Label, Entry, Button
import sqlite3
from datetime import datetime



def buscar_codigo(codigo_empleado):
    try:
            # Conectamos a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Consultamos si el código de empleado existe en la base de datos
        cursor.execute("SELECT * FROM Empleados WHERE Codigo = ?", (codigo_empleado,))
        resultado = cursor.fetchone()

            # Cerramos la conexión
        conexion.close()

        return resultado  # Devolvemos el resultado de la consulta

    except sqlite3.Error as e:
        print(f"Error al buscar código no existe: {str(e)}")
        return None



def validar_fecha(fecha):
        try:
            # Intentamos convertir la fecha a un objeto datetime
            fecha_obj = datetime.strptime(fecha, '%d-%m-%Y')
            
            # Validamos que la fecha sea posterior al día actual
            if fecha_obj.date() >= datetime.now().date():
                return True
            else:
                return False
        except ValueError:
            return False
        
        

def ejecutar_consulta(codigo_empleado, fecha_baja, label_mensaje):
        try:
            # Verificamos si el código de empleado existe
            empleado_existente = buscar_codigo(codigo_empleado)

            if empleado_existente:
                # Validamos la fecha
                if validar_fecha(fecha_baja):
                    # Conectamos a la base de datos
                    conexion = sqlite3.connect('nominator.db')
                    cursor = conexion.cursor()

                    # Insertamos la fecha de baja en la tabla de empleados
                    cursor.execute("UPDATE Empleados SET FechaFin = ? WHERE Codigo = ?", (fecha_baja, codigo_empleado))
                    conexion.commit()
                    conexion.close()

                    # Actualizamos el mensaje
                    mensaje = f"Fecha de baja actualizada para el código {codigo_empleado}"
                    label_mensaje.config(text=mensaje)
                else:
                    mensaje = "La fecha de baja debe ser válida y posterior al día actual."
                    label_mensaje.config(text=mensaje)

            else:
                # Si el código de empleado no existe, mostramos un mensaje de error
                mensaje = f"El código de empleado {codigo_empleado} no existe en la base de datos"
                label_mensaje.config(text=mensaje)

        except sqlite3.Error as e:
            # En caso de error, actualizamos el mensaje de error
            mensaje = f"Error al actualizar fecha de baja: {str(e)}"
            label_mensaje.config(text=mensaje)



def ventana_bajas():
        ventana = Tk()
        ventana.title("Ejemplo de pantalla")
        ventana.geometry('570x450')

        Label(ventana, text='CÓDIGO EMPLEADO', width=20, anchor="ne", font=('Helvetica', 12)).grid(row=0, column=0, padx=10, pady=10)
        entry_codigo = Entry(ventana, justify="center", width=30, font="Arial")
        entry_codigo.grid(row=1, column=0, padx=5, pady=10)

        Label(ventana, text='FECHA DE BAJA', width=20, anchor="ne", font=('Helvetica', 12)).grid(row=0, column=1, padx=10, pady=10)
        entry_fecha_baja = Entry(ventana, justify="center", width=30, font="Arial")
        entry_fecha_baja.grid(row=1, column=1, padx=5, pady=10)

        # Cuadro de mensaje
        label_mensaje = Label(ventana, text="MENSAJES DE VALIDACION",foreground="red",font=('Helvetica', 14) ,padx=10, pady=10)
        label_mensaje.grid(row=4, columnspan=2, pady=20)

        # Botón
        Label(ventana, text='', pady=20).grid(row=5, column=0)

        button1 = Button(ventana, text="CONFIRMAR", height=3, width=25, bg='#FDFD96', fg='black', bd=2, font=('Helvetica', 12, 'bold'), command=lambda: ejecutar_consulta(entry_codigo.get(), entry_fecha_baja.get(), label_mensaje))
        button1.grid(row=6, column=0, columnspan=2, pady=5) 


        ventana.mainloop()
    

if __name__ == "__main__":
        ventana_bajas()