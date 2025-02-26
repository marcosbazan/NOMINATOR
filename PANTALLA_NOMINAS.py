from tkinter import *
import sqlite3

def ventana_nominas():
    
    def consultar_empleado():
        try:
            codigo_consulta = Entry_codigo_consulta.get()
            conexion = sqlite3.connect("nominator.db")
            cursor = conexion.cursor()

            # Consultar los datos del empleado por código
            cursor.execute("SELECT * FROM Empleados WHERE Codigo=?", (codigo_consulta,))
            empleado = cursor.fetchone()

            if empleado:
                # Mostrar los datos del empleado en las entradas correspondientes
                Entry_Nombre.set(empleado[1])
                Entry_FechaInicio.set(empleado[2])
                Entry_FechaFin.set(empleado[3])
                Entry_Direccion.set(empleado[4])
                Entry_Nif.set(empleado[5])
                Entry_DatosBancarios.set(empleado[6])
                Entry_NumeroAfiliado.set(empleado[7])
                Entry_Irpf.set(empleado[8])
                Entry_SegSocial.set(empleado[9])

                mensaje_aviso.set("Datos del empleado encontrados.")
            else:
                mensaje_aviso.set("Empleado no encontrado.")
                limpiar_campos()

        except Exception as e:
            mensaje_aviso.set(f"Error al consultar empleado: {str(e)}")

        finally:
            cursor.close()
            conexion.close()


    def limpiar_campos():
        """Limpia todos los campos."""
        Entry_Nombre.set("")
        Entry_FechaInicio.set("")
        Entry_FechaFin.set("")
        Entry_Direccion.set("")
        Entry_Nif.set("")
        Entry_DatosBancarios.set("")
        Entry_NumeroAfiliado.set("")
        Entry_Irpf.set("")
        Entry_SegSocial.set("")


    # Configuración de la ventana principal
    nominas = Tk()
    nominas.title("Gestión de Empleados")
    nominas.geometry("600x400")

    # Variables asociadas a las entradas
    Entry_codigo_consulta = StringVar()
    Entry_Nombre = StringVar()
    Entry_FechaInicio = StringVar()
    Entry_FechaFin = StringVar()
    Entry_Direccion = StringVar()
    Entry_Nif = StringVar()
    Entry_DatosBancarios = StringVar()
    Entry_NumeroAfiliado = StringVar()
    Entry_Irpf = StringVar()
    Entry_SegSocial = StringVar()
    mensaje_aviso = StringVar()

    # Título
    Label(nominas, text="Gestión de Empleados", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    # Campo de consulta
    Label(nominas, text="Código de Empleado").grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_codigo_consulta).grid(row=1, column=1, padx=10, pady=5)
    Button(nominas, text="Consultar", command=consultar_empleado).grid(row=1, column=2, padx=10, pady=5)

    # Datos del empleado
    Label(nominas, text="Nombre").grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_Nombre, state="disabled").grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky=EW)

    Label(nominas, text="Fecha Inicio").grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_FechaInicio, state="disabled").grid(row=3, column=1, padx=10, pady=5)

    Label(nominas, text="Fecha Fin").grid(row=3, column=2, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_FechaFin, state="disabled").grid(row=3, column=3, padx=10, pady=5)

    Label(nominas, text="Dirección").grid(row=4, column=0, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_Direccion, state="disabled").grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky=EW)

    Label(nominas, text="NIF").grid(row=5, column=0, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_Nif, state="disabled").grid(row=5, column=1, padx=10, pady=5)

    Label(nominas, text="Datos Bancarios").grid(row=5, column=2, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_DatosBancarios, state="disabled").grid(row=5, column=3, padx=10, pady=5)

    Label(nominas, text="Número Afiliación SS").grid(row=6, column=0, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_NumeroAfiliado, state="disabled").grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky=EW)

    Label(nominas, text="% IRPF").grid(row=7, column=0, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_Irpf, state="disabled").grid(row=7, column=1, padx=10, pady=5)

    Label(nominas, text="Seguridad Social").grid(row=7, column=2, sticky=W, padx=10, pady=5)
    Entry(nominas, textvariable=Entry_SegSocial, state="disabled").grid(row=7, column=3, padx=10, pady=5)

    # Mensaje de aviso
    Label(nominas, textvariable=mensaje_aviso, fg="red").grid(row=8, column=0, columnspan=4, pady=10,)

    # Botones de acción
    Button(nominas, text="Limpiar", command=limpiar_campos).grid(row=9, column=1, pady=10)
    Button(nominas, text="Salir", command=nominas.quit).grid(row=9, column=2, pady=10)
    nominas.mainloop()
