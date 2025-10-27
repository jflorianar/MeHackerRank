"""
Título: Simple Array Sum
Dificultad: Easy
URL: https://www.hackerrank.com/challenges/simple-array-sum

Descripción:
Dado un array de enteros, encuentra la suma de todos sus elementos.

Constraints:
- 0 < n ≤ 10000
- 0 < ar[i] ≤ 10000

Approach:
Usar la función built-in sum() de Python para sumar todos los elementos
del array. Alternativa: iterar sobre el array y acumular la suma.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def simpleArraySum(ar):
    """
    Calcula la suma de todos los elementos en un array.
    
    Args:
        ar: Lista de enteros
        
    Returns:
        int: La suma de todos los elementos
    """
    return sum(ar)

if __name__ == '__main__':
    # Lee el tamaño del array (n) y luego el array de enteros
    # Formato de entrada estándar de HackerRank:
    # Línea 1: n (número de elementos)
    # Línea 2: elementos del array separados por espacios
    n = int(input())
    ar = list(map(int, input().split()))
    result = simpleArraySum(ar)
    print(result)
