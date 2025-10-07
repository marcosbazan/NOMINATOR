from tkinter import Tk, Label, Button, ttk, Scrollbar, Frame
import sqlite3

def obtener_informes(treeview, label_mensaje):
    try:
        conexion = sqlite3.connect('nominator.db')
        cursor = conexion.cursor()

        # Obtenemos solo empleados activos (fecha_fin NULL)
        cursor.execute("SELECT codigo, nombre, fecha_inicio, fecha_fin FROM empleados WHERE fecha_fin IS NULL")
        datos = cursor.fetchall()
        conexion.close()

        # Limpiar tabla antes de insertar
        for item in treeview.get_children():
            treeview.delete(item)

        if datos:
            for fila in datos:
                # Reemplazamos None por cadena vacía y eliminamos espacios
                fila_corregida = [str(campo).strip() if campo is not None else "" for campo in fila]
                treeview.insert("", "end", values=fila_corregida)
            label_mensaje.config(text=f"Se han cargado {len(datos)} empleados activos.", fg="green")
        else:
            label_mensaje.config(text="No hay empleados activos.", fg="red")

    except sqlite3.Error as e:
        label_mensaje.config(text=f"Error al cargar los informes: {str(e)}", fg="red")

def ventana_informes():
    ventana = Tk()
    ventana.title("Informes de Empleados")
    ventana.geometry("900x500")
    ventana.configure(bg="#f0f4f7")

    # ---- CABECERA ----
    header = Frame(ventana, bg="#2c3e50", pady=15)
    header.pack(fill="x")
    Label(header, text="INFORMES DE EMPLEADOS", font=('Helvetica', 20, 'bold'),
          bg="#2c3e50", fg="white").pack()

    # ---- FRAME TABLA ----
    frame_tabla = Frame(ventana, bg="#f0f4f7")
    frame_tabla.pack(padx=15, pady=15, fill="both", expand=True)

    # Columnas que queremos mostrar
    columnas = ("Código", "Nombre", "Fecha Inicio", "Fecha Fin")
    treeview = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

    # Configuración de columnas
    for col in columnas:
        treeview.heading(col, text=col)
        treeview.column(col, anchor="center", width=200, stretch=True)

    # Scrollbar vertical
    scrollbar_y = Scrollbar(frame_tabla, orient="vertical", command=treeview.yview)
    treeview.configure(yscroll=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")
    treeview.pack(fill="both", expand=True, side="left")

    # ---- FRAME MENSAJE Y BOTONES ----
    frame_botones = Frame(ventana, bg="#f0f4f7", pady=10)
    frame_botones.pack(fill="x")

    label_mensaje = Label(frame_botones, text="", font=("Helvetica", 12, "bold"), bg="#f0f4f7", fg="red")
    label_mensaje.pack(pady=5)

    Button(frame_botones, text="CARGAR INFORMES", width=25, height=2,
           bg="#3498db", fg="white", font=("Helvetica", 12, "bold"),
           command=lambda: obtener_informes(treeview, label_mensaje)).pack(pady=5)

    ventana.mainloop()


if __name__ == "__main__":
    ventana_informes()
