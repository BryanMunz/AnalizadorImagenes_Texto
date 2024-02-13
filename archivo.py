import random
import string
from tabulate import tabulate


def cifrar_mensaje(n, oracion):
    alfabeto = string.ascii_uppercase
    matriz = []

    for _ in range(n):
        fila = [" " for _ in range(n)]
        matriz.append(fila)

    indices_vacios = [0, 2, 9, 13, 21]

    # Eliminar los espacios de la oración
    oracion = oracion.replace(" ", "")
    # Dividir la oración en grupos de 5 letras
    grupos_letras = [oracion[i:i + 5] for i in range(0, len(oracion), 5)]

    # Asignar las primeras letras a los espacios vacíos iniciales de la matriz original
    for i, indice in enumerate(indices_vacios):
        fila = indice // n
        columna = indice % n
        letra = grupos_letras[0][i]
        matriz[fila][columna] = letra

    # Imprimir la matriz con el mensaje inicial
    # print("Matriz con el mensaje inicial:")
    # tabla_inicial = tabulate(matriz, tablefmt="fancy_grid")
    # print(tabla_inicial)

    # Girar la matriz y asignar las letras restantes hasta completar la oración
    letra_actual = 5
    for grupo in grupos_letras[1:]:
        # Girar la matriz hacia la derecha
        matriz = list(zip(*matriz[::-1]))
        matriz = [list(fila) for fila in matriz]  # Convertir las tuplas en listas



        # Asignar las letras del grupo a los espacios vacíos de la matriz girada
        for i, letra in enumerate(grupo):
            if letra_actual < len(oracion):
                indice = indices_vacios[i]
                fila = indice // n
                columna = indice % n
                if matriz[fila][columna] == " ":
                    matriz[fila][columna] = letra
                else:
                    matriz[fila][columna] = oracion[letra_actual]
                letra_actual += 1

        # Imprimir la matriz después del giro
        print("Mensaje oculto")
        tabla_giro = tabulate(matriz, tablefmt="fancy_grid")
        print(tabla_giro)

    # Llenar los espacios restantes de la matriz con letras aleatorias
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == " ":
                matriz[i][j] = random.choice(alfabeto)

    # Imprimir la matriz final
    print("Matriz cifrada")
    tabla_final = tabulate(matriz, tablefmt="fancy_grid")
    print(tabla_final)

    return matriz


def descifrar_mensaje(matriz):
    indices_vacios = [0, 2, 9, 13, 21]
    cadena_indices_vacios = ''.join(str(indice) for indice in indices_vacios)
    clave = input("Ingrese la clave: ")
    if clave == cadena_indices_vacios:
        mensaje_descifrado = ""

        grupos_letras = len(indices_vacios)  # Número de grupos de 5 letras en el mensaje original

        for _ in range(grupos_letras):
            for indice in indices_vacios:
                fila = indice // len(matriz)
                columna = indice % len(matriz)
                letra = matriz[fila][columna]
                mensaje_descifrado += letra

            # Girar la matriz hacia la izquierda
            # matriz = [list(fila) for fila in zip(*matriz[::-1])]

            matriz = list(zip(*matriz[::-1]))
            matriz = [list(fila) for fila in matriz]

            # Imprimir la matriz después del giro hacia la izquierda
            print("\nGiro hacia la izquierda:")
            tabla_giro = tabulate(matriz, tablefmt="fancy_grid")
            print(tabla_giro)

        # return mensaje_descifrado

    else:
        print("La clave es incorrecta, vuelve a intentarlo")


# Solicitar el tamaño de la matriz y la oración al usuario
n = 5
oracion = input("Ingrese el mensaje: ")
oracion = oracion.upper()
print("\n>>>>> PROCESO DE CIFRADO <<<<<")
# Crear la matriz
matriz_resultante = cifrar_mensaje(n, oracion)
texto_resultante = ''.join([''.join(fila) for fila in matriz_resultante])

print("\nMensaje cifrado:")
print(texto_resultante)

print("\n\n>>>>> PROCESO DE DECIFRADO <<<<<")

mensaje_descifrado = descifrar_mensaje(matriz_resultante)

print("\nMensaje decifrado:")

# print(mensaje_descifrado)
# Eliminar los espacios de la oración
oracion = oracion.replace(" ", "")
print(oracion)