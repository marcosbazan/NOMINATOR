# NOMINATOR

Aplicación de escritorio en Python para la gestión de nóminas, altas/bajas y generación de informes, con interfaz gráfica desarrollada en Tkinter, y la base de datos desarrollada en SQLite.

---

## 🔍 Características principales

- Interfaz gráfica con **Tkinter** para facilitar la navegación entre funciones.  
- Menú principal (`PANTALLA_MENU.py`) para acceder a las distintas secciones.  
- Gestión de nóminas (`PANTALLA_NOMINAS.py`): creación, visualización y edición de nóminas.  
- Altas y bajas (`PANTALLA_DE_ALTAS.py` y `PANTALLA_BAJAS.py`): registro de nuevos empleados y eliminación de registros.  
- Informes (`PANTALLA_INFORMES.py`): generación de reportes sobre los datos almacenados.  
- Base de datos **SQLite** (`nominator.db`) para persistencia local de la información.  
- Uso de imágenes y recursos locales para la interfaz (ej. `nomina.png`).  

---

## ⚙️ Requisitos

- Python 3.x  
- Tkinter (normalmente incluido en Python estándar)  
- SQLite (normalmente incluido en Python estándar)  
- Dependencias adicionales si se agregan en el futuro  

---

## 🚀 Instalación y uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/marcos318888/NOMINATOR.git
   
2. Navega al directorio del proyecto:

  cd NOMINATOR

3. Ejecuta la aplicación iniciando la pantalla principal:
   
  python PANTALLA_MENU.py
