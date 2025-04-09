import time  # Importa el módulo 'time' pa' poder usar funciones de tiempo, como sleep

cadena = 'JuanPablo'  # Se define una cadena de texto con el nombre 'JuanPablo'

# Se recorre cada letra dentro de la cadena con un ciclo for
for letra in cadena:
    if letra == 'l':
        continue  # Si la letra es una 'l', se salta esa iteración y no se imprime (pasa a la siguiente vuelta)

    print(letra)  # Imprime la letra en pantalla si no es 'l'
    time.sleep(1)  # Hace una pausa de 1 segundo antes de imprimir la siguiente letra