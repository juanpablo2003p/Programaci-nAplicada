import random
from matplotlib import pyplot as plt

numbers_a = range(1, 13)
numbers_b = [random.randint(1, 1000) for i in range(12)]

plt.plot(numbers_a, numbers_b, marker='o', linestyle='-', color='blue')  # Con marcadores y color
plt.title("Gráfico de números aleatorios")  # Título del gráfico
plt.xlabel("Mes")  # Eje X (por ejemplo, meses del año)
plt.ylabel("Valor aleatorio")  # Eje Y
plt.grid(True)  # Agrega una rejilla
plt.show()