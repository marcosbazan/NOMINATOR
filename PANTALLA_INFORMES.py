import sqlite3
from tkinter import Tk, Label


def obtener_total_empleados():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para obtener el total de empleados
        cursor.execute("SELECT COUNT(*) FROM Empleados")
        total_empleados = cursor.fetchone()[0]

            # Cerrar la conexión
        conexion.close()

        return total_empleados

    except sqlite3.Error as e:
        print(f"Error al obtener el total de empleados: {str(e)}")
        return None

def contar_empleados_sin_fecha_fin():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para contar empleados con FechaFin vacío
        cursor.execute("SELECT COUNT(*) FROM Empleados WHERE FechaFin = ''")
        cantidad_empleados = cursor.fetchone()[0]

            # Cerrar la conexión
        conexion.close()

        return cantidad_empleados

    except sqlite3.Error as e:
        print(f"Error al contar empleados: {str(e)}")
        return None

def contar_empleados_con_fecha_fin():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para contar empleados con FechaFin no vacío
        cursor.execute("SELECT COUNT(*) FROM Empleados WHERE FechaFin != ''")
        cantidad_empleados = cursor.fetchone()[0]

            # Cerrar la conexión
        conexion.close()

        return cantidad_empleados

    except sqlite3.Error as e:
        print(f"Error al contar empleados con FechaFin: {str(e)}")
        return None

def contar_empleados_femeninos_sin_fecha_fin():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para contar empleados femeninos sin FechaFin
        cursor.execute("SELECT COUNT(*) FROM Empleados WHERE Genero = 'Femenino' AND FechaFin = ''")
        cantidad_empleados_femeninos_sin_fecha_fin = cursor.fetchone()[0]

            # Cerrar la conexión
        conexion.close()

        return cantidad_empleados_femeninos_sin_fecha_fin

    except sqlite3.Error as e:
        print(f"Error al contar empleados femeninos sin FechaFin: {str(e)}")
        return None

def contar_empleados_masculinos_sin_fecha_fin():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para contar empleados masculinos sin FechaFin
        cursor.execute("SELECT COUNT(*) FROM Empleados WHERE Genero = 'Masculino' AND FechaFin = ''")
        cantidad_empleados_masculinos_sin_fecha_fin = cursor.fetchone()[0]

            # Cerrar la conexión
        conexion.close()

        return cantidad_empleados_masculinos_sin_fecha_fin 

    except sqlite3.Error as e:
        print(f"Error al contar empleados masculinos sin FechaFin: {str(e)}")
        return None

def contar_empleados_masculinos_con_fecha_fin():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para contar empleados masculinos con FechaFin no vacío
        cursor.execute("SELECT COUNT(*) FROM Empleados WHERE Genero = 'Masculino' AND FechaFin != ''")
        cantidad_empleados_masculinos_con_fecha_fin = cursor.fetchone()[0]

            # Cerrar la conexión
        conexion.close()

        return cantidad_empleados_masculinos_con_fecha_fin

    except sqlite3.Error as e:
        print(f"Error al contar empleados masculinos con FechaFin: {str(e)}")
        return None
        
def contar_empleados_femeninos_con_fecha_fin():
        
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para contar empleados femeninos con FechaFin no vacío
        cursor.execute("SELECT COUNT(*) FROM Empleados WHERE Genero = 'Femenino' AND FechaFin != ''")
        cantidad_empleados_femeninos_con_fecha_fin = cursor.fetchone()[0]

            # Cerrar la conexión
        conexion.close()

        return cantidad_empleados_femeninos_con_fecha_fin

    except sqlite3.Error as e:
        print(f"Error al contar empleados femeninos con FechaFin: {str(e)}")
        return None
        
def calcular_retribucion_media():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para obtener la suma de salarios y el número total de empleados
        cursor.execute("SELECT SUM(SalarioMensual), COUNT(*) FROM Empleados")
        resultado = cursor.fetchone()
        suma_salarios, total_empleados = resultado[0], resultado[1]

            # Cerrar la conexión
        conexion.close()

            # Calcular la retribución media
        if total_empleados > 0:
            retribucion_media = suma_salarios / total_empleados
            return retribucion_media
        else:
            print("No hay empleados en la base de datos.")
            return None

    except sqlite3.Error as e:
        print(f"Error al calcular la retribución media: {str(e)}")
        return None
            
def calcular_retribucion_media_femenina():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para obtener la suma de salarios y el número total de empleados femeninos
        cursor.execute("SELECT SUM(SalarioMensual), COUNT(*) FROM Empleados WHERE Genero = 'Femenino'")
        resultado = cursor.fetchone()
        suma_salarios, total_empleados_femeninos = resultado[0], resultado[1]

            # Cerrar la conexión
        conexion.close()

            # Calcular la retribución media para empleados femeninos
        if total_empleados_femeninos > 0:
            retribucion_media_femenina = suma_salarios / total_empleados_femeninos
            return retribucion_media_femenina
        else:
            print("No hay empleadas femeninas en la base de datos.")
            return None

    except sqlite3.Error as e:
        print(f"Error al calcular la retribución media femenina: {str(e)}")
        return None
        


def calcular_retribucion_media_masculina():
    try:
            # Conectar a la base de datos
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

            # Realizar la consulta para obtener la suma de salarios y el número total de empleados femeninos
        cursor.execute("SELECT SUM(SalarioMensual), COUNT(*) FROM Empleados WHERE Genero = 'Masculino'")
        resultado = cursor.fetchone()
        suma_salarios, total_empleados_femeninos = resultado[0], resultado[1]

            # Cerrar la conexión
        conexion.close()

            # Calcular la retribución media para empleados femeninos
        if total_empleados_femeninos > 0:
            retribucion_media_masculina = suma_salarios / total_empleados_femeninos
            return retribucion_media_masculina
        else:
            print("No hay empleadas femeninas en la base de datos.")
            return None

    except sqlite3.Error as e:
        print(f"Error al calcular la retribución media femenina: {str(e)}")
        return None
        



def ventana_informes():
    total_empleados = obtener_total_empleados()
    cantidad_sin_fecha_fin = contar_empleados_sin_fecha_fin()
    cantidad_con_fecha_fin = contar_empleados_con_fecha_fin()
    cantidad_femeninos_sin_fecha_fin = contar_empleados_femeninos_sin_fecha_fin()
    cantidad_empleados_masculinos_sin_fecha_fin = contar_empleados_masculinos_sin_fecha_fin()
    cantidad_empleados_masculinos_con_fecha_fin = contar_empleados_masculinos_con_fecha_fin()
    cantidad_empleados_femeninos_con_fecha_fin = contar_empleados_femeninos_con_fecha_fin()
    retribucion_media_total =calcular_retribucion_media()
    retribucion_media_femenina=calcular_retribucion_media_femenina()
    retribucion_media_masculina=calcular_retribucion_media_masculina()

    if total_empleados is not None and cantidad_sin_fecha_fin is not None and cantidad_con_fecha_fin  is not None and cantidad_femeninos_sin_fecha_fin is not None and cantidad_empleados_masculinos_sin_fecha_fin is not None and cantidad_empleados_masculinos_con_fecha_fin  is not None and cantidad_empleados_femeninos_con_fecha_fin is not None and calcular_retribucion_media is not None and calcular_retribucion_media_femenina is not None and calcular_retribucion_media_masculina is not None:
        texto_resultado_sin_fecha_fin.config(text=f" {cantidad_sin_fecha_fin}")
        texto_resultado_con_fecha_fin.config(text=f" {cantidad_con_fecha_fin}")
            # % mujeres sin fecha fin
        porcentaje_femenino = (cantidad_femeninos_sin_fecha_fin / cantidad_sin_fecha_fin) * 100
        texto_porcentaje_femenino.config(text=f"{porcentaje_femenino:.2f}%")

            # % hombres sin fecha fin
        porcentaje_masculino_sin_fecha_fin = (cantidad_empleados_masculinos_sin_fecha_fin / cantidad_sin_fecha_fin) * 100
        texto_porcentaje_masculino_sin_fecha_fin.config(text=f"{porcentaje_masculino_sin_fecha_fin:.2f}%")

            # %mujeres con fecha fin 
        porcentaje_femenino_con_fecha_fin = (cantidad_empleados_femeninos_con_fecha_fin / cantidad_con_fecha_fin) * 100
        texto_porcentaje_femenino_con_fecha_fin.config(text=f"{porcentaje_femenino_con_fecha_fin:.2f}%")

            #%hombers con fecha fin
        porcentaje_femenino_con_fecha_fin = (cantidad_empleados_masculinos_con_fecha_fin / cantidad_con_fecha_fin) * 100
        texto_porcentaje_masculino_con_fecha_fin.config(text=f"{porcentaje_femenino_con_fecha_fin:.2f}%")

            #RETRIBUCION MEDIA 
        texto_retribucion_media_total.config(text=f" {round(retribucion_media_total)} €")


            #RETRIBUCION MEDIA MUJERES
        texto_calcular_retribucion_media_femenina.config(text=f" {retribucion_media_femenina} €")

            #RETRIBUCION MEDIA HOMBRESç

        texto_calcular_retribucion_media_masculina.config(text=f" {retribucion_media_masculina} €")

        # Establecer una actualización automática cada 5000 milisegundos (5 segundos)
        ventana.after(5000, ventana_informes)


    if __name__ == "__main__":
        ventana = Tk()
        ventana.title("INFORMES")
        ventana.geometry('420x300')
        ventana.resizable(0,0)
        
        # EMPLEADOS ALTA
        Label(ventana, text=' EMPLEADOS\nALTA', font=('Helvetica', 10, 'bold')).grid(row=0, column=0, pady=10)

        texto_resultado_sin_fecha_fin = Label(ventana, text='', font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=35)
        texto_resultado_sin_fecha_fin.grid(row=1, column=0, pady=5)

        # EMPELADOS BAJA
        Label(ventana, text='EMPLEADOS\nBAJA', font=('Helvetica', 10,'bold')).grid(row=0, column=1, pady=10)

        texto_resultado_con_fecha_fin = Label(ventana, text='', font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=35)
        texto_resultado_con_fecha_fin.grid(row=1, column=1, pady=5)

        # %MUJERES ALTA
        Label(ventana, text='  % MUJERES', font=('Helvetica', 10)).grid(row=2, column=0, pady=5)

        texto_porcentaje_femenino = Label(ventana, text='', font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=15)
        texto_porcentaje_femenino.grid(row=3, column=0, pady=5)

        # %HOMBRES ALTA
        Label(ventana, text='  % HOMBRES', font=('Helvetica', 10)).grid(row=4, column=0, pady=5)
        texto_porcentaje_masculino_sin_fecha_fin = Label(ventana, text='', font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=15)
        texto_porcentaje_masculino_sin_fecha_fin.grid(row=5, column=0, pady=5)


        # %MUJERES BAJA
        Label(ventana, text='  % MUJERES', font=('Helvetica', 10)).grid(row=2, column=1, pady=5)
        texto_porcentaje_femenino_con_fecha_fin = Label(ventana, text='', font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=15)
        texto_porcentaje_femenino_con_fecha_fin.grid(row=3, column=1, pady=5)

        # %HOMBRES BAJA
        Label(ventana, text='  % HOMBRES', font=('Helvetica', 10)).grid(row=4, column=1, pady=5)
        texto_porcentaje_masculino_con_fecha_fin = Label(ventana, text='', font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=15)
        texto_porcentaje_masculino_con_fecha_fin.grid(row=5, column=1, pady=5)


        #ESPACIO ENTRE LABELS
        Label(ventana, text='', font=('Helvetica', 10)).grid(row=0, column=2, pady=5)
        wew = Label(ventana, font=('Helvetica', 12), pady=5, padx=15)
        wew.grid(row=1, column=2, pady=5)


        #MEDIA EDADES
        Label(ventana, text=' MEDIA\nEDADES', font=('Helvetica', 10,'bold')).grid(row=0, column=3, pady=5)
        edades = Label(ventana, font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=35)
        edades.grid(row=1, column=3, pady=5)

    #MEDIA EDADES MUEJERES
        Label(ventana, text=' MUJERES', font=('Helvetica', 10)).grid(row=2, column=3, pady=5)
        Label(ventana, font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=35).grid(row=3, column=3, pady=5)

        #MEDIA EDADES HOMBRES
        Label(ventana, text=' HOMBRES', font=('Helvetica', 10)).grid(row=4, column=3, pady=5)
        Label(ventana, font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=35).grid(row=5, column=3, pady=5)


        #RETRIBUCION MEDIA
        Label(ventana, text=' RETRIBUCION\nMEDIA', font=('Helvetica', 10, 'bold'), fg='dark blue').grid(row=0, column=4, pady=5)
        texto_retribucion_media_total = Label(ventana, font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=20)
        texto_retribucion_media_total.grid(row=1, column=4, pady=5)


        # RETRIBUCION MUJERES
        Label(ventana, text=' MUJERES', font=('Helvetica', 10), fg='blue').grid(row=2, column=4, pady=5)
        texto_calcular_retribucion_media_femenina=Label(ventana, font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=20)
        texto_calcular_retribucion_media_femenina.grid(row=3, column=4, pady=20)

        # RETRIBUCION HOMBRES
        Label(ventana, text=' HOMBRES', font=('Helvetica', 10), fg='blue').grid(row=4, column=4, pady=5)
        texto_calcular_retribucion_media_masculina=Label(ventana, font=('Helvetica', 12), bd=2, relief="solid", pady=5, padx=20)
        texto_calcular_retribucion_media_masculina.grid(row=5, column=4, pady=20)

        # Iniciar la consulta y mostrar el resultado automáticamente
        ventana_informes()

        ventana.mainloop()
