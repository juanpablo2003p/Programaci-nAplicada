import time  # Importamos 'time' pa' medir cuánto se demora todo el proceso

# Definimos una función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False  # Los menores que 2 no son primos
    # Solo comprobamos divisores desde 2 hasta la raíz cuadrada del número
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False  # Si encuentra un divisor, no es primo
    return True  # Si no se encontró ningún divisor, es primo

inicio = time.time()  # Registramos el tiempo de inicio

# Recorremos los números del 1 al 30
for i in range(1, 31):
    if es_primo(i):  # Si el número es primo según la función...
        print(f'{i} es un primo\n')  # ...lo imprimimos con un salto de línea

fin = time.time()  # Registramos el tiempo de fin

# Mostramos cuánto se demoró todo el proceso, en milisegundos
print("t =", (fin - inicio) * 1000, "ms")
