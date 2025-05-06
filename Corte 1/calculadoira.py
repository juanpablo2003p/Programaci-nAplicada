import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        
        # Crear los campos de entrada
        self.num1_label = tk.Label(master, text="Número 1:")
        self.num1_label.grid(row=0, column=0)

        self.num1_entry = tk.Entry(master)
        self.num1_entry.grid(row=0, column=1)

        self.num2_label = tk.Label(master, text="Número 2:")
        self.num2_label.grid(row=1, column=0)

        self.num2_entry = tk.Entry(master)
        self.num2_entry.grid(row=1, column=1)

        # Crear los botones
        self.sumar_btn = tk.Button(master, text="Sumar", command=self.sumar)
        self.sumar_btn.grid(row=2, column=0)

        self.restar_btn = tk.Button(master, text="Restar", command=self.restar)
        self.restar_btn.grid(row=2, column=1)

        self.multiplicar_btn = tk.Button(master, text="Multiplicar", command=self.multiplicar)
        self.multiplicar_btn.grid(row=3, column=0)

        self.dividir_btn = tk.Button(master, text="Dividir", command=self.dividir)
        self.dividir_btn.grid(row=3, column=1)

        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(master, text="Resultado: ")
        self.resultado_label.grid(row=4, column=0, columnspan=2)

    def get_inputs(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")
            return None, None

    def sumar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            resultado = num1 + num2
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def restar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            resultado = num1 - num2
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def multiplicar(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            resultado = num1 * num2
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def dividir(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            if num2 != 0:
                resultado = num1 / num2
                self.resultado_label.config(text=f"Resultado: {resultado}")
            else:
                messagebox.showerror("Error", "No se puede dividir por cero.")


# Crear la ventana principal
root = tk.Tk()
app = Calculadora(root)

# Ejecutar la interfaz gráfica
root.mainloop()
