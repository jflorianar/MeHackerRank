"""
Título: Arrays - DS
Dificultad: Easy
Categoría: Data Structures - Arrays
URL: https://www.hackerrank.com/challenges/arrays-ds

Descripción:
Un array es un tipo de estructura de datos que almacena elementos del mismo tipo
en ubicaciones de memoria contiguas. Dado un array de enteros, imprímelo en orden inverso.

Ejemplo:
arr = [1, 4, 3, 2]
Retorna: [2, 3, 4, 1]

Enfoque:
Usar slicing de Python arr[::-1] o el método reverse().

Complejidad:
- Tiempo: O(n)
- Espacio: O(n) para el array invertido

Fecha: 2024-01-01
"""

def reverseArray(a):
    """
    Invierte un array.
    
    Argumentos:
    a -- lista de enteros
    
    Retorna:
    El array en orden inverso
    """
    return a[::-1]


if __name__ == '__main__':
    # Ejemplo de uso
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))
    
    res = reverseArray(arr)
    print(' '.join(map(str, res)))
