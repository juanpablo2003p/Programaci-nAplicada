# Punto 9: Imprimir los números primos existentes entre 0 y 30 (sin optimización)

tope_rango = 30  # Límite superior del rango
n = 0  # Comenzamos desde 0

while n < tope_rango:
    primo = True  # Suponemos que el número es primo (se reinicia en cada ciclo)
    
    # Verificamos si el número tiene algún divisor aparte de 1 y él mismo
    for div in range(2, n):
        if n % div == 0:
            primo = False  # Si encontramos un divisor, ya no es primo
    
    if primo:
        print(n)  # Si es primo, lo mostramos
    
    n += 1  # Pasamos al siguiente número
# Punto 10: Misma idea pero optimizando con 'break'

n = 0  # Reiniciamos n

while n < tope_rango:
    primo = True  # Suponemos que es primo
    
    for div in range(2, n):
        if n % div == 0:
            primo = False
            break  # Nos salimos del ciclo apenas encontramos un divisor
    
    if primo:
        print(n)  # Si sigue siendo primo, lo imprimimos
    
    n += 1
# Punto 11: Comparar cuántos ciclos se ejecutan sin usar 'break'

ciclos_sin_break = 0  # Contador de iteraciones del ciclo interno
n = 0

while n < tope_rango:
    primo = True  # Reiniciamos el flag

    for div in range(2, n):
        ciclos_sin_break += 1  # Contamos la iteración
        if n % div == 0:
            primo = False  # No es primo
    
    if primo:
        print(n)
    
    n += 1

print('Cantidad de ciclos SIN break: ' + str(ciclos_sin_break))
# Misma comparación pero ahora usando 'break' para optimizar

ciclos_con_break = 0  # Contador de iteraciones con break
n = 0

while n < tope_rango:
    primo = True

    for div in range(2, n):
        ciclos_con_break += 1  # Contamos cada intento de división
        if n % div == 0:
            primo = False
            break  # Cortamos el ciclo apenas detectamos que no es primo
    
    if primo:
        print(n)
    
    n += 1

print('Cantidad de ciclos CON break: ' + str(ciclos_con_break))

# Cálculo de optimización: cuántos ciclos se usaron en proporción
optimizado = ciclos_con_break / ciclos_sin_break * 100
print(f'Se optimizó a un {optimizado:.2f}% de los ciclos usando break')
