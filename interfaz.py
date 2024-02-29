from tkinter import scrolledtext
import tkinter as tk
from V3 import analizar_entrada  # Asegúrate de que esta función esté definida y ajustada correctamente en `analizador.py`

def analizar():
    entrada = txt_entrada.get("1.0", tk.END).strip()
    resultado = analizar_entrada(entrada)
    txt_resultado.delete("1.0", tk.END)
    txt_resultado.insert(tk.INSERT, resultado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Sintáctico")

# Crear el widget de entrada
lbl_entrada = tk.Label(ventana, text="Texto a analizar:")
lbl_entrada.pack()

txt_entrada = scrolledtext.ScrolledText(ventana, width=40, height=10)
txt_entrada.pack()
txt_entrada.insert(tk.INSERT, "function nombre(var variable: boolean; otro: boolean;)")


# Crear el botón para analizar
btn_analizar = tk.Button(ventana, text="Analizar", command=analizar)
btn_analizar.pack()

# Crear el widget de salida para resultados
lbl_resultado = tk.Label(ventana, text="Resultado del análisis:")
lbl_resultado.pack()

txt_resultado = scrolledtext.ScrolledText(ventana, width=40, height=15)
txt_resultado.pack()

# Iniciar el loop principal
ventana.mainloop()
