"""
Título: Solve Me First
Dificultad: Easy
Categoría: Algorithms - Warmup
URL: https://www.hackerrank.com/challenges/solve-me-first

Descripción:
Completa la función solveMeFirst para calcular la suma de dos enteros.

Ejemplo:
a = 2
b = 3
Retorna: 5

Enfoque:
Simple suma de dos números enteros.

Complejidad:
- Tiempo: O(1)
- Espacio: O(1)

Fecha: 2024-01-01
"""

def solveMeFirst(a, b):
    """
    Suma dos enteros.
    
    Argumentos:
    a -- primer entero
    b -- segundo entero
    
    Retorna:
    La suma de a y b
    """
    return a + b


if __name__ == '__main__':
    # Ejemplo de uso
    num1 = int(input())
    num2 = int(input())
    res = solveMeFirst(num1, num2)
    print(res)
