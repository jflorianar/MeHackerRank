# Python 🐍

Esta carpeta contiene soluciones a los desafíos específicos de Python en HackerRank.

## Subcategorías

### Introduction
Conceptos básicos de Python y sintaxis fundamental.

**Temas:**
- Print statements
- Condicionales (if-else)
- Operaciones aritméticas
- Divisiones
- Bucles

**Ejemplos de problemas:**
- Say "Hello, World!" With Python
- Python If-Else
- Arithmetic Operators
- Python: Division

### Basic Data Types
Tipos de datos fundamentales en Python.

**Temas:**
- Lists (listas)
- Tuples (tuplas)
- Sets (conjuntos)
- Dictionaries (diccionarios)

**Ejemplos de problemas:**
- List Comprehensions
- Find the Runner-Up Score
- Nested Lists
- Finding the percentage

### Strings
Manipulación y operaciones con cadenas de texto.

**Temas:**
- String slicing
- String methods
- String formatting
- Regex

**Ejemplos de problemas:**
- sWAP cASE
- String Split and Join
- What's Your Name?
- Mutations
- Find a String

### Sets
Operaciones con conjuntos.

**Temas:**
- Set operations (union, intersection, difference)
- Set methods
- Symmetric difference

**Ejemplos de problemas:**
- Introduction to Sets
- Set .add()
- Set .discard(), .remove() & .pop()
- Set Mutations

### Collections
Módulo collections de Python.

**Temas:**
- Counter
- DefaultDict
- OrderedDict
- Named Tuple
- Deque

**Ejemplos de problemas:**
- Collections.Counter()
- DefaultDict Tutorial
- Collections.namedtuple()
- Collections.OrderedDict()
- Collections.deque()

## Conceptos Clave de Python

### List Comprehensions
```python
# Básico
squares = [x**2 for x in range(10)]

# Con condición
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i+j for j in range(3)] for i in range(3)]
```

### String Methods
```python
s = "Hello World"
s.upper()           # "HELLO WORLD"
s.lower()           # "hello world"
s.capitalize()      # "Hello world"
s.split()           # ['Hello', 'World']
s.replace('o', '0') # "Hell0 W0rld"
```

### Collections
```python
from collections import Counter, defaultdict, deque

# Counter
count = Counter(['a', 'b', 'a', 'c'])  # Counter({'a': 2, 'b': 1, 'c': 1})

# DefaultDict
d = defaultdict(int)
d['key'] += 1  # No KeyError

# Deque
dq = deque([1, 2, 3])
dq.appendleft(0)  # deque([0, 1, 2, 3])
```

### Lambda Functions
```python
# Básico
square = lambda x: x**2

# Con sorted
sorted(items, key=lambda x: x[1])

# Con map
list(map(lambda x: x*2, [1, 2, 3]))  # [2, 4, 6]
```

## Trucos de Python Útiles

### Swap Variables
```python
a, b = b, a
```

### Reverse String/List
```python
s[::-1]
```

### Multiple Assignment
```python
a, b, c = 1, 2, 3
```

### Enumerate
```python
for i, value in enumerate(['a', 'b', 'c']):
    print(f"{i}: {value}")
```

### Zip
```python
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### Any/All
```python
any([False, True, False])  # True
all([True, True, True])    # True
```

## Recursos Recomendados

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python Tricks - Dan Bader](https://realpython.com/products/python-tricks-book/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)

## Tips para HackerRank Python

1. **Familiarízate con la biblioteca estándar** - HackerRank permite el uso de la mayoría de módulos estándar
2. **Usa comprehensions** - Son más pythonicas y a menudo más eficientes
3. **Conoce tus built-ins** - sum(), max(), min(), sorted(), etc.
4. **Maneja el input correctamente** - Usa strip(), split(), map() apropiadamente
5. **Practica con el formateo de strings** - f-strings, .format(), %

## Complejidad Común en Python

| Operación | List | Set | Dict |
|-----------|------|-----|------|
| Access | O(1) | - | O(1) |
| Search | O(n) | O(1) | O(1) |
| Insert | O(n) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |
