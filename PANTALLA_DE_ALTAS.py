from tkinter import *
import sqlite3


# Funciones de validación (sin cambios)
def validar_genero(genero):
    return genero.capitalize() in ["Masculino", "Femenino"]


def validar_ccc(ccc):
    try:
        ccc = ccc.replace(" ", "")  # Elimina espacios en blanco
        entidad = int(ccc[:4])
        oficina = int(ccc[4:8])
        cuenta = int(ccc[10:20])
        control = int(ccc[8:10])

        suma = (entidad // 10 * 1 + entidad % 10 * 2 +
                oficina // 10 * 3 + oficina % 10 * 4 +
                cuenta // 10000 * 5 + cuenta % 10000 // 1000 * 6 +
                cuenta % 1000 // 100 * 7 + cuenta % 100 // 10 * 8 +
                cuenta % 10 * 9) % 11

        digito_control = 11 - suma
        if digito_control == 11:
            digito_control = 0
        elif digito_control == 10:
            digito_control = 1

        return digito_control == control

    except ValueError:
        return False


def validar_dni(dni):
    tabla_asignacion = "TRWAGMYFPDXBNJZSQVHLCKE"
    try:
        numero = int(dni[:-1])
        letra = dni[-1].upper()
        resto = numero % 23
        letra_calculada = tabla_asignacion[resto]
        return letra == letra_calculada
    except ValueError:
        return False


def ventana_altas():
    altas = Tk()
    altas.title("Altas de Empleado")
    altas.geometry("800x600")

    # Variables asociadas a las entradas
    Entry_codigo = StringVar()
    Entry_Nombre = StringVar()
    Entry_FechaInicio = StringVar()
    Entry_FechaFin = StringVar()
    Entry_Direccion = StringVar()
    Entry_Nif = StringVar()
    Entry_DatosBancarios = StringVar()
    Entry_NumeroAfiliado = StringVar()
    Entry_Genero = StringVar()
    Entry_Departamento = StringVar()
    Entry_Puesto = StringVar()
    Entry_Telefono = StringVar()
    Entry_SalarioMensual = StringVar()
    Entry_Irpf = StringVar()
    Entry_Email = StringVar()
    Entry_PagasExtras = StringVar()
    Entry_SegSocial = StringVar()
    mensaje_aviso = StringVar()
    def insertar():
        try:
            conexion = sqlite3.connect("nominator.db")
            cursor = conexion.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                            (codigo text, nombre text, fecha_inicio text, fecha_fin text,
                            direccion text, nif text, datos_bancarios text, numero_afiliacion text,
                            genero text, departamento text, puesto text, telefono text, 
                            salario_mensual text, irpf text, email text, pagas_extras text,
                            seg_social text)''')

            datos = (Entry_codigo.get(), Entry_Nombre.get(), Entry_FechaInicio.get(), Entry_FechaFin.get(),
                    Entry_Direccion.get(), Entry_Nif.get(), Entry_DatosBancarios.get(), Entry_NumeroAfiliado.get(),
                    Entry_Genero.get(), Entry_Departamento.get(), Entry_Puesto.get(), Entry_Telefono.get(),
                    Entry_SalarioMensual.get(), Entry_Irpf.get(), Entry_Email.get(),
                    Entry_PagasExtras.get(), Entry_SegSocial.get())

            cursor.execute("""
            INSERT INTO empleados VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", datos)
            conexion.commit()

            mensaje_aviso.set("Empleado insertado correctamente.")
        except Exception as e:
            mensaje_aviso.set(f"Error: {e}")
        finally:
            cursor.close()
            conexion.close()


# Configuración principal de la ventana
 

# Función para crear una sección
    def crear_seccion(frame_padre, titulo, campos):
        frame = LabelFrame(frame_padre, text=titulo, padx=10, pady=10, font=('Helvetica', 10, 'bold'))
        frame.pack(fill="both", expand="yes", padx=10, pady=5)
        for i, (texto, variable) in enumerate(campos):
            Label(frame, text=texto).grid(row=i, column=0, sticky=W, pady=5)
            Entry(frame, textvariable=variable).grid(row=i, column=1, padx=5, pady=5, sticky=W)
        return frame


# Sección de datos personales
    crear_seccion(altas, "Datos Personales", [
        ("Código", Entry_codigo),
        ("Nombre y Apellidos", Entry_Nombre),
        ("Dirección", Entry_Direccion),
        ("Teléfono", Entry_Telefono),
        ("Email", Entry_Email)
    ])

    # Sección de información laboral
    crear_seccion(altas, "Información Laboral", [
        ("Fecha de Inicio", Entry_FechaInicio),
        ("Fecha de Fin", Entry_FechaFin),
        ("Departamento", Entry_Departamento),
        ("Puesto", Entry_Puesto),
        ("Salario Mensual", Entry_SalarioMensual),
        ("IRPF (%)", Entry_Irpf),
        ("Pagas Extras", Entry_PagasExtras)
    ])

    # Sección de datos adicionales
    crear_seccion(altas, "Datos Adicionales", [
        ("NIF", Entry_Nif),
        ("Número de Afiliación SS", Entry_NumeroAfiliado),
        ("Género", Entry_Genero),
        ("Datos Bancarios", Entry_DatosBancarios),
        ("Seguridad Social", Entry_SegSocial)
    ])

    # Botón para insertar datos
    frame_botones = Frame(altas, pady=10)
    frame_botones.pack()
    Label(frame_botones, textvariable=mensaje_aviso, fg="red").grid(row=0, column=0, columnspan=2)
    Button(frame_botones, text="Insertar", command=insertar, bg="yellow").grid(row=1, column=0, pady=10)

    altas.mainloop()
