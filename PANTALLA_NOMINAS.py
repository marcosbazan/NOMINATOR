from tkinter import *
import sqlite3

def ventana_nominas():
    # ---- Ventana principal ----
    nominas = Tk()
    nominas.title("Gestión de Nóminas")
    nominas.geometry("800x700")
    nominas.configure(bg="#f0f4f7")

    # ---- VARIABLES ----
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

    # ---- CABECERA ----
    header = Frame(nominas, bg="#2c3e50", pady=15)
    header.pack(fill="x")

    Label(header, text="GESTIÓN DE NÓMINAS",
          font=('Helvetica', 20, 'bold'),
          bg="#2c3e50", fg="white").pack(expand=True)  # centrado horizontal

    # ---- CANVAS SCROLLABLE ----
    main_frame = Frame(nominas, bg="#f0f4f7")
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame, bg="#f0f4f7", highlightthickness=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    second_frame = Frame(canvas, bg="#f0f4f7")
    canvas.create_window((0, 0), window=second_frame, anchor="nw")

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    second_frame.bind("<Configure>", update_scrollregion)

    # ---- FUNCIONES ----
    def consultar_empleado():
        codigo_consulta = Entry_codigo_consulta.get().strip()
        if not codigo_consulta:
            mensaje_aviso.set("⚠️ El código de empleado es obligatorio.")
            return
        try:
            conexion = sqlite3.connect("nominator.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM empleados WHERE codigo=?", (codigo_consulta,))
            empleado = cursor.fetchone()
            if empleado:
                Entry_Nombre.set(empleado[1])
                Entry_FechaInicio.set(empleado[2])
                Entry_FechaFin.set(empleado[3])
                Entry_Direccion.set(empleado[4])
                Entry_Nif.set(empleado[5])
                Entry_DatosBancarios.set(empleado[6])
                Entry_NumeroAfiliado.set(empleado[7])
                Entry_Irpf.set(empleado[13])
                Entry_SegSocial.set(empleado[16])
                mensaje_aviso.set("✅ Empleado encontrado correctamente.")
            else:
                limpiar_campos()
                mensaje_aviso.set("❌ Empleado no encontrado.")
        except Exception as e:
            mensaje_aviso.set(f"❌ Error: {e}")
        finally:
            cursor.close()
            conexion.close()

    def limpiar_campos():
        for var in [Entry_Nombre, Entry_FechaInicio, Entry_FechaFin, Entry_Direccion,
                    Entry_Nif, Entry_DatosBancarios, Entry_NumeroAfiliado,
                    Entry_Irpf, Entry_SegSocial]:
            var.set("")
        mensaje_aviso.set("")

    # ---- SECCIÓN CONSULTA ----
    frame_consulta = LabelFrame(second_frame, text="Consulta de Empleado",
                                font=('Helvetica', 11, 'bold'),
                                bg="#f0f4f7", fg="#2c3e50",
                                padx=15, pady=10, labelanchor="n")
    frame_consulta.pack(fill="x", padx=15, pady=10)

    Label(frame_consulta, text="Código de Empleado:",
          bg="#f0f4f7", fg="#2c3e50", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, pady=5, sticky=W)
    Entry(frame_consulta, textvariable=Entry_codigo_consulta,
          font=('Helvetica', 10), width=25, relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5, sticky=W)
    Button(frame_consulta, text="CONSULTAR", command=consultar_empleado,
           bg="#3498db", fg="white", font=('Helvetica', 10, 'bold'),
           activebackground="#2980b9", activeforeground="white",
           relief="flat", width=15).grid(row=0, column=2, padx=10, pady=5)

    # ---- SECCIÓN DATOS ----
    def crear_seccion(frame_padre, titulo, campos):
        frame = LabelFrame(frame_padre, text=titulo, padx=15, pady=10,
                           font=('Helvetica', 11, 'bold'), bg="#f0f4f7", fg="#2c3e50", labelanchor="n")
        frame.pack(fill="both", expand="yes", padx=15, pady=5)
        for i, (texto, variable) in enumerate(campos):
            Label(frame, text=texto, bg="#f0f4f7", fg="#2c3e50",
                  font=('Helvetica', 10, 'bold')).grid(row=i, column=0, sticky=W, pady=5, padx=5)
            Entry(frame, textvariable=variable, font=('Helvetica', 10),
                  width=40, justify="left", relief="solid", bd=1, state="readonly").grid(row=i, column=1, padx=10, pady=5, sticky=W)
        return frame

    crear_seccion(second_frame, "Datos del Empleado", [
        ("Nombre", Entry_Nombre),
        ("Fecha de Inicio", Entry_FechaInicio),
        ("Fecha de Fin", Entry_FechaFin),
        ("Dirección", Entry_Direccion),
        ("NIF", Entry_Nif),
        ("Datos Bancarios", Entry_DatosBancarios),
        ("Nº Afiliación SS", Entry_NumeroAfiliado),
        ("% IRPF", Entry_Irpf),
        ("Seguridad Social", Entry_SegSocial)
    ])

    # ---- MENSAJES Y BOTONES ----
    frame_botones = Frame(second_frame, pady=15, bg="#f0f4f7")
    frame_botones.pack()
    Label(frame_botones, textvariable=mensaje_aviso, fg="red",
          bg="#f0f4f7", font=('Helvetica', 13, 'bold')).grid(row=0, column=0, columnspan=3, pady=10)

    Button(frame_botones, text="LIMPIAR",
           command=limpiar_campos, width=15,
           bg="#e67e22", fg="white", font=('Helvetica', 11, 'bold'),
           activebackground="#d35400", relief="flat").grid(row=1, column=0, padx=10, pady=10)

    Button(frame_botones, text="SALIR",
           command=nominas.destroy, width=15,
           bg="#c0392b", fg="white", font=('Helvetica', 11, 'bold'),
           activebackground="#922b21", relief="flat").grid(row=1, column=1, padx=10, pady=10)

    nominas.mainloop()


if __name__ == "__main__":
    ventana_nominas()
