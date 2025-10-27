# 🤝 Guía de Contribución

## Cómo Añadir Tus Soluciones

### 1. Formato de Archivos

Cada solución debe seguir esta estructura:

```python
"""
Título: [Nombre del Ejercicio]
Dificultad: [Easy/Medium/Hard]
URL: [Link al problema en HackerRank]

Descripción:
[Descripción breve del problema]

Constraints:
[Restricciones del problema]

Approach:
[Explica tu enfoque para resolver el problema]

Time Complexity: O(?)
Space Complexity: O(?)
"""

def solution():
    """
    Implementa tu solución aquí
    """
    pass

if __name__ == '__main__':
    # Tu código principal aquí
    pass
```

### 2. Nomenclatura de Archivos

- Usa snake_case: `simple_array_sum.py`
- Nombres descriptivos: `two_sum.py` en vez de `problem1.py`
- Sin espacios ni caracteres especiales

### 3. Organización por Categorías

Coloca tu archivo en la carpeta correcta según el tipo de problema:

```
exercises/
├── algorithms/
│   ├── warmup/
│   ├── implementation/
│   ├── sorting/
│   ├── search/
│   ├── dynamic-programming/
│   └── greedy/
├── data-structures/
│   ├── arrays/
│   ├── linked-lists/
│   ├── trees/
│   └── stacks-queues/
├── mathematics/
└── python/
    ├── introduction/
    ├── basic-data-types/
    └── strings/
```

### 4. Mejores Prácticas

#### Código

- ✅ Escribe código limpio y legible
- ✅ Usa nombres de variables descriptivos
- ✅ Añade comentarios para lógica compleja
- ✅ Incluye docstrings en funciones
- ✅ Sigue PEP 8 (estilo de Python)

#### Documentación

- ✅ Completa el header con toda la información
- ✅ Explica tu approach (enfoque)
- ✅ Indica complejidad temporal y espacial
- ✅ Añade ejemplos si es necesario

#### Testing

```python
# Opcional: añade casos de prueba
def test_solution():
    assert solution([1, 2, 3]) == 6
    assert solution([]) == 0
    print("All tests passed!")

if __name__ == '__main__':
    test_solution()
```

### 5. Commits

Formato recomendado:
```
[Categoría] Título del Problema - Dificultad

Ejemplos:
Add: [Python] Hello World - Easy
Update: [Algorithms] Binary Search - Optimized solution
Fix: [Data Structures] Linked List - Edge case handling
```

### 6. Pull Request (Si haces fork)

Si decides hacer fork de este repo y quieres contribuir:

1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/nuevo-ejercicio`
3. Haz tus cambios
4. Commit: `git commit -m 'Add: [Categoría] Problema'`
5. Push: `git push origin feature/nuevo-ejercicio`
6. Crea un Pull Request

### 7. Múltiples Soluciones

Si tienes varias soluciones para el mismo problema:

```
exercises/algorithms/sorting/
├── merge_sort_v1.py          # Solución recursiva
├── merge_sort_v2.py          # Solución iterativa
└── merge_sort_optimized.py   # Solución optimizada
```

O dentro del mismo archivo:

```python
def solution_v1():
    """Approach: Brute force - O(n²)"""
    pass

def solution_v2():
    """Approach: Optimized with hash map - O(n)"""
    pass
```

### 8. Checklist Antes de Commit

- [ ] El código funciona correctamente
- [ ] Incluye el header completo
- [ ] Explica el approach
- [ ] Indica complejidades (tiempo/espacio)
- [ ] Sigue PEP 8
- [ ] Nombre de archivo descriptivo
- [ ] En la carpeta correcta
- [ ] Commit message claro

---

¡Gracias por contribuir! 🎉
