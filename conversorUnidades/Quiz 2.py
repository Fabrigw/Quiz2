import tkinter as tk
from tkinter import messagebox

# Tasa de conversión fija
TASA_CONVERSION = 51747

# Función para realizar la conversión
def convertir():
    try:
        # Obtener el valor de entrada
        valor_usd = float(entry_usd.get())
        # Calcular el valor en CRC
        valor_crc = valor_usd * TASA_CONVERSION
        # Mostrar el resultado
        label_resultado.config(text=f"{valor_crc:.2f} CRC")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Función para limpiar los campos
def limpiar():
    entry_usd.delete(0, tk.END)
    label_resultado.config(text="")

# Función para confirmar salida
def confirmar_salida():
    if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Moneda USD a CRC")
root.geometry("300x200")

# Etiqueta y campo de entrada para USD
label_usd = tk.Label(root, text="Ingrese monto en USD:")
label_usd.grid(row=0, column=0, padx=10, pady=10)

entry_usd = tk.Entry(root)
entry_usd.grid(row=0, column=1, padx=10, pady=10)

# Botón para convertir
boton_convertir = tk.Button(root, text="Convertir", command=convertir)
boton_convertir.grid(row=1, column=0, columnspan=2, pady=10)

# Botón para limpiar
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=2, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="")
label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Evento para confirmar salida
root.protocol("WM_DELETE_WINDOW", confirmar_salida)

# Iniciar el bucle principal
root.mainloop()