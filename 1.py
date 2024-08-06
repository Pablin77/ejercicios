"""
1 - Create a function that takes a list representation of a Minesweeper board, and returns another
board where the value of each cell is the amount of its neighbouring mines.

Version de Python: Python 3.10.9
"""
import numpy as np

def get_input(prompt):
    """
    Solicito al usuario un numero entero positivo.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("El numero debe ser entero positivo. Intentelo de nuevo.")
            else:
                return value
        except ValueError:
            print("Por favor, ingrese un numero entero valido.")


def recorro(matriz):
    """
    Recorro matriz, busco los 1 y reemplazo por 9. Calculo los 1 al rededor de los 0.
    """
    for i in range(0, filas):
        for j in range(0,columnas):
            if matriz[i, j] == 1:
                solucion[i, j] = 9
            else:
                contador = 0
                for x in range(max(0, i-1), min(filas, i+2)):
                    for z in range(max(0, j-1), min(columnas, j+2)):
                        if matriz[x, z] == 1:
                            contador += 1
                solucion[i, j] = contador
    return solucion



if __name__ == "__main__":
    filas = get_input("Ingrese el número de filas: ")
    columnas = get_input("Ingrese el número de columnas: ")
    
    print('Buscaminas: ')
    matriz  =np.random.randint(0,2,(filas,columnas))
    print(matriz)

    solucion = np.zeros((filas, columnas), dtype=int)

    print('Solucion: ')
    print(recorro(matriz))


