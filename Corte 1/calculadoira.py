import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora ")
        self.master.geometry("400x500")  # Tamaño de la ventana
        self.master.config(bg="#2d3e50")  # Fondo de la ventana
        
        # Estilo de los widgets
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Times New Roman", 14), width=10, padding=10, relief="flat", background="#4CAF50", foreground="white")
        self.style.map("TButton", background=[("active", "#45a049")])
        
        self.style.configure("TLabel", font=("Times New Roman", 16), background="#2d3e50", foreground="white")

        # Etiquetas y entradas
        self.num1_label = ttk.Label(master, text="Número 1:")
        self.num1_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.num1_entry = ttk.Entry(master, font=("Times New Roman", 16))
        self.num1_entry.grid(row=0, column=1, padx=20, pady=10, ipadx=10, ipady=5)

        self.num2_label = ttk.Label(master, text="Número 2:")
        self.num2_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.num2_entry = ttk.Entry(master, font=("Times New Roman", 16))
        self.num2_entry.grid(row=1, column=1, padx=20, pady=10, ipadx=10, ipady=5)

        # Botones de operaciones
        self.sumar_btn = ttk.Button(master, text="Sumar", command=self.sumar)
        self.sumar_btn.grid(row=2, column=0, padx=10, pady=10)

        self.restar_btn = ttk.Button(master, text="Restar", command=self.restar)
        self.restar_btn.grid(row=2, column=1, padx=10, pady=10)

        self.multiplicar_btn = ttk.Button(master, text="Multiplicar", command=self.multiplicar)
        self.multiplicar_btn.grid(row=3, column=0, padx=10, pady=10)

        self.dividir_btn = ttk.Button(master, text="Dividir", command=self.dividir)
        self.dividir_btn.grid(row=3, column=1, padx=10, pady=10)

        # Etiqueta para mostrar el resultado
        self.resultado_label = ttk.Label(master, text="Resultado: ", font=("Times New Roman", 18), background="#2d3e50", foreground="white")
        self.resultado_label.grid(row=4, column=0, columnspan=2, pady=20)

    def get_inputs(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos como vas a ingresar letras wn, te falla???.")
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
            try:
                resultado = num1 / num2
                self.resultado_label.config(text=f"Resultado: {resultado}")
            except ZeroDivisionError:
                messagebox.showerror("Error", "No se puede dividir por cero eres retrasadito mental???.")


# Crear la ventana principal
root = tk.Tk()
app = Calculadora(root)

# Ejecutar la interfaz gráfica
root.mainloop()
