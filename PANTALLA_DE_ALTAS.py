from tkinter import *
import sqlite3

# ---------------- VALIDACIONES ----------------
def validar_genero(genero):
    return genero.capitalize() in ["Masculino", "Femenino"]

def validar_ccc(ccc):
    try:
        ccc = ccc.replace(" ", "")
        if len(ccc) != 20 or not ccc.isdigit():
            return False
        entidad = ccc[:4]
        oficina = ccc[4:8]
        control = ccc[8:10]
        cuenta = ccc[10:]

        def calcular_dc(digitos):
            pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
            suma = sum(int(d) * p for d, p in zip(digitos, pesos[-len(digitos):]))
            dc = 11 - (suma % 11)
            if dc == 11:
                dc = 0
            elif dc == 10:
                dc = 1
            return dc

        dc1 = calcular_dc("00" + entidad + oficina)
        dc2 = calcular_dc(cuenta)
        return int(control[0]) == dc1 and int(control[1]) == dc2

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

# ---------------- VENTANA DE ALTAS ----------------
def ventana_altas():
    altas = Tk()
    altas.title("Altas de Empleado")
    altas.geometry("800x650")
    altas.configure(bg="#f0f4f7")

    # ---- CABECERA ----
    header = Frame(altas, bg="#2c3e50", pady=15)
    header.pack(fill="x")
    Label(header, text="REGISTRO DE ALTAS", font=('Helvetica', 20, 'bold'),
          bg="#2c3e50", fg="white").pack()

    # ---- VARIABLES ----
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

    # ---- FUNCIÓN INSERTAR ----
    def insertar():
        if not Entry_codigo.get() or not Entry_Nombre.get():
            mensaje_aviso.set("⚠️ Código y Nombre son obligatorios.")
            return
        if Entry_Nif.get() and not validar_dni(Entry_Nif.get()):
            mensaje_aviso.set("❌ NIF incorrecto.")
            return
        if Entry_DatosBancarios.get() and not validar_ccc(Entry_DatosBancarios.get()):
            mensaje_aviso.set("❌ CCC incorrecto.")
            return
        if Entry_Genero.get() and not validar_genero(Entry_Genero.get()):
            mensaje_aviso.set("❌ Género debe ser Masculino o Femenino.")
            return

        try:
            conexion = sqlite3.connect("nominator.db")
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                              (codigo text, nombre text, fecha_inicio text, fecha_fin text,
                               direccion text, nif text, datos_bancarios text,
                               numero_afiliacion text, genero text, departamento text,
                               puesto text, telefono text, salario_mensual text, irpf text,
                               email text, pagas_extras text, seg_social text)''')

            datos = (Entry_codigo.get(), Entry_Nombre.get(), Entry_FechaInicio.get(), Entry_FechaFin.get(),
                     Entry_Direccion.get(), Entry_Nif.get(), Entry_DatosBancarios.get(), Entry_NumeroAfiliado.get(),
                     Entry_Genero.get(), Entry_Departamento.get(), Entry_Puesto.get(), Entry_Telefono.get(),
                     Entry_SalarioMensual.get(), Entry_Irpf.get(), Entry_Email.get(),
                     Entry_PagasExtras.get(), Entry_SegSocial.get())

            cursor.execute("INSERT INTO empleados VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", datos)
            conexion.commit()
            mensaje_aviso.set("✅ Empleado insertado correctamente.")
        except Exception as e:
            mensaje_aviso.set(f"❌ Error al insertar: {e}")
        finally:
            cursor.close()
            conexion.close()

    # ---- SECCIONES ----
    def crear_seccion(frame_padre, titulo, campos):
        frame = LabelFrame(frame_padre, text=titulo, padx=15, pady=10,
                           font=('Helvetica', 11, 'bold'), bg="#f0f4f7", fg="#2c3e50", labelanchor="n")
        frame.pack(fill="both", expand="yes", padx=15, pady=5)
        for i, (texto, variable) in enumerate(campos):
            Label(frame, text=texto, bg="#f0f4f7", fg="#2c3e50",
                  font=('Helvetica', 10, 'bold')).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            Entry(frame, textvariable=variable, font=('Helvetica', 10),
                  width=40, justify="left", relief="solid", bd=1).grid(row=i, column=1, padx=10, pady=5, sticky=W)
        return frame

    # ---- SECCIONES DE FORMULARIO ----
    crear_seccion(altas, "Datos Personales", [
        ("Código", Entry_codigo),
        ("Nombre y Apellidos", Entry_Nombre),
        ("Dirección", Entry_Direccion),
        ("Teléfono", Entry_Telefono),
        ("Email", Entry_Email)
    ])

    crear_seccion(altas, "Información Laboral", [
        ("Fecha de Inicio", Entry_FechaInicio),
        ("Fecha de Fin", Entry_FechaFin),
        ("Departamento", Entry_Departamento),
        ("Puesto", Entry_Puesto),
        ("Salario Mensual", Entry_SalarioMensual),
        ("IRPF (%)", Entry_Irpf),
        ("Pagas Extras", Entry_PagasExtras)
    ])

    crear_seccion(altas, "Datos Adicionales", [
        ("NIF", Entry_Nif),
        ("Número de Afiliación SS", Entry_NumeroAfiliado),
        ("Género", Entry_Genero),
        ("Datos Bancarios", Entry_DatosBancarios),
        ("Seguridad Social", Entry_SegSocial)
    ])

    # ---- BOTÓN Y MENSAJE ----
    frame_botones = Frame(altas, pady=15, bg="#f0f4f7")
    frame_botones.pack()
    Label(frame_botones, textvariable=mensaje_aviso, fg="red",
          bg="#f0f4f7", font=('Helvetica', 13, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    Button(frame_botones, text="INSERTAR EMPLEADO",
           command=insertar,
           height=2, width=25,
           bg="#3498db", fg="white", bd=0,
           activebackground="#2980b9", activeforeground="white",
           font=('Helvetica', 12, 'bold'), relief="flat").grid(row=1, column=0, pady=10)

    altas.mainloop()

# Ejecutar ventana
if __name__ == "__main__":
    ventana_altas()
