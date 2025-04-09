import time  # Importamos módulo para medir el tiempo
import math  # Importamos módulo para usar raíz cuadrada

# Función para determinar si un número es primo
def es_primo(num):
    if num < 2:
        return False  # 0 y 1 no son primos
    for divisor in range(2, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False  # Si encuentra un divisor, no es primo
    return True  # Si no encontró divisores, es primo

# Marcamos el tiempo de inicio
inicio = time.time()

# Recorremos del 0 al 30
for i in range(0, 31):
    if es_primo(i):  # Si la función dice que es primo...
        print(f"{i} es un primo")  # ...lo imprimimos

# Marcamos el tiempo final
fin = time.time()
print("t =", (fin - inicio) * 1000, "ms")  # Tiempo en milisegundos