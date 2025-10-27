"""
Título: Simple Array Sum
Dificultad: Easy
Categoría: Algorithms - Warmup
URL: https://www.hackerrank.com/challenges/simple-array-sum

Descripción:
Dada una matriz de enteros, encuentra la suma de sus elementos.

Ejemplo:
ar = [1, 2, 3]
Retorna: 6

Enfoque:
Iterar sobre el array y sumar todos los elementos, o usar la función sum() de Python.

Complejidad:
- Tiempo: O(n) donde n es el tamaño del array
- Espacio: O(1)

Fecha: 2024-01-01
"""

def simpleArraySum(ar):
    """
    Calcula la suma de todos los elementos en un array.
    
    Argumentos:
    ar -- lista de enteros
    
    Retorna:
    La suma total de los elementos
    """
    return sum(ar)


if __name__ == '__main__':
    # Ejemplo de uso
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    
    result = simpleArraySum(ar)
    print(result)
