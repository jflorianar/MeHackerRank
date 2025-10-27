# Data Structures 📊

Esta carpeta contiene soluciones a problemas de estructuras de datos de HackerRank.

## Subcategorías

### Arrays
Estructuras de datos más fundamentales en programación.

**Dificultad:** Easy a Medium  
**Temas:** Manipulación de arrays, operaciones, rotaciones

**Problemas comunes:**
- Array reversal
- Left rotation / Right rotation
- Sparse arrays
- 2D arrays

### Linked Lists
Listas enlazadas simples y dobles.

**Dificultad:** Easy a Hard  
**Temas:** Inserción, eliminación, reversión, detección de ciclos

**Problemas comunes:**
- Insert node
- Delete node
- Reverse linked list
- Detect cycle

### Stacks
Estructura de datos LIFO (Last In, First Out).

**Dificultad:** Easy a Medium  
**Temas:** Balance de paréntesis, evaluación de expresiones

**Problemas comunes:**
- Balanced brackets
- Maximum element
- Simple text editor

### Queues
Estructura de datos FIFO (First In, First Out).

**Dificultad:** Easy to Medium  
**Temas:** Colas simples, colas de prioridad, deques

**Problemas comunes:**
- Queue using two stacks
- Priority queues

### Trees
Árboles binarios, BST, árboles de segmentos.

**Dificultad:** Medium a Hard  
**Temas:** Traversals (in-order, pre-order, post-order), BST, balanceo

**Problemas comunes:**
- Tree traversals
- Binary search tree operations
- Lowest common ancestor
- Height of tree

### Heaps
Montículos y colas de prioridad.

**Dificultad:** Medium a Hard  
**Temas:** Min heap, max heap, heapify

**Problemas comunes:**
- Find median
- Min/Max heap operations
- Qheap1

## Operaciones Comunes

### Arrays
```python
# Acceso: O(1)
element = arr[i]

# Búsqueda: O(n)
index = arr.index(value)

# Inserción: O(n)
arr.insert(i, value)

# Eliminación: O(n)
arr.pop(i)
```

### Linked Lists
```python
# Acceso: O(n)
# Inserción al inicio: O(1)
# Eliminación al inicio: O(1)
```

### Stacks
```python
stack = []
stack.append(item)  # push - O(1)
stack.pop()         # pop - O(1)
stack[-1]           # peek - O(1)
```

### Queues
```python
from collections import deque
queue = deque()
queue.append(item)   # enqueue - O(1)
queue.popleft()      # dequeue - O(1)
```

## Recursos Recomendados

- [VisuAlgo - Data Structures](https://visualgo.net/)
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [GeeksforGeeks - Data Structures](https://www.geeksforgeeks.org/data-structures/)
