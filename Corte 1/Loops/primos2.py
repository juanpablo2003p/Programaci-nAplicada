def es_primo(num):
    """Función que determina si un número es primo"""
    if num < 2:
        return False  # 0 y 1 no son primos
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False  # Si encuentra un divisor, no es primo
    return True  # Si no encontró ningún divisor, es primo

continuar = True  # Controla si seguimos pidiendo números

while continuar:
    # Pedimos el número al usuario
    entrada = input("Ingrese un número para saber si es primo: ")

    # Validamos que sea un número entero positivo
    if not entrada.isdigit():
        print("Eso no es un número válido, parcero. Intente otra vez.\n")
        continue

    numero = int(entrada)

    # Usamos la función para verificar si es primo
    if es_primo(numero):
        print(f"\n{numero} SÍ es un número primo 🔥\n")
    else:
        print(f"\n{numero} NOOO es un número primo 💀\n")

    # Preguntamos si quiere continuar
    respuesta = input("¿Quiere probar otro número? (Presione 1 para sí, cualquier otra tecla para salir): ")
    continuar = (respuesta == "1")  # Solo sigue si el usuario presiona 1

print("Gracias por usar el detector de primos, manito 😎👊")
