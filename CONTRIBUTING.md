# Guía de Contribución 🤝

Esta guía te ayudará a agregar nuevas soluciones a este repositorio de manera organizada y consistente.

## 📋 Antes de Empezar

1. Asegúrate de haber resuelto el problema en HackerRank
2. Verifica que tu solución pase todos los casos de prueba
3. Entiende la complejidad temporal y espacial de tu solución

## 🗂️ Estructura de Archivos

### Nombrado de Archivos

- Usa **snake_case** para nombres de archivo (minúsculas con guiones bajos)
- El nombre debe ser descriptivo del problema
- Ejemplo: `two_strings.py`, `simple_array_sum.py`

### Ubicación de Archivos

Coloca tu solución en la carpeta correspondiente según la categoría:

```
algorithms/
├── warmup/              # Problemas de calentamiento
├── implementation/      # Implementación
├── strings/            # Strings
├── sorting/            # Ordenamiento
├── search/             # Búsqueda
├── dynamic_programming/# Programación Dinámica
├── greedy/             # Algoritmos Voraces
└── graphs/             # Grafos

data_structures/
├── arrays/             # Arreglos
├── linked_lists/       # Listas Enlazadas
├── stacks/             # Pilas
├── queues/             # Colas
├── trees/              # Árboles
└── heaps/              # Montículos

python/
├── introduction/       # Introducción a Python
├── basic_data_types/   # Tipos de Datos Básicos
├── strings/            # Strings en Python
├── sets/               # Conjuntos
└── collections/        # Colecciones

sql/
├── basic_select/       # SELECT básico
└── advanced_select/    # SELECT avanzado
```

## 📝 Plantilla de Solución

Cada solución debe seguir esta plantilla:

```python
"""
Título: [Nombre Exacto del Problema]
Dificultad: [Easy/Medium/Hard]
Categoría: [Categoría Principal - Subcategoría]
URL: [Link completo al problema en HackerRank]

Descripción:
[Breve descripción del problema en 2-3 líneas]

Ejemplo:
[Un ejemplo del input y output esperado]

Enfoque:
[Explica tu estrategia para resolver el problema]
[Por qué elegiste este enfoque]
[Consideraciones especiales]

Complejidad:
- Tiempo: O(?)
- Espacio: O(?)

Fecha: [YYYY-MM-DD]
Autor: [Tu nombre] (opcional)
"""

# Imports necesarios (si aplica)
import module

def nombre_funcion(parametros):
    """
    Descripción breve de la función.
    
    Argumentos:
    parametro1 -- descripción del parámetro
    parametro2 -- descripción del parámetro
    
    Retorna:
    descripción del valor de retorno
    """
    # Tu implementación aquí
    pass


# Bloque principal (para testing local)
if __name__ == '__main__':
    # Código para leer input y producir output
    # según el formato de HackerRank
    pass
```

## ✅ Checklist para Agregar una Solución

- [ ] El archivo está en la carpeta correcta
- [ ] El nombre del archivo usa snake_case
- [ ] Incluye el docstring completo al inicio
- [ ] El código está comentado cuando es necesario
- [ ] Incluye la URL del problema
- [ ] Especifica la complejidad temporal y espacial
- [ ] El código sigue las convenciones de Python (PEP 8)
- [ ] Funciona con el formato de input/output de HackerRank
- [ ] Has probado la solución localmente

## 🎨 Estilo de Código

Sigue las convenciones de Python ([PEP 8](https://pep8.org/)):

### Nombres de Variables y Funciones
- **snake_case** para variables y funciones: `my_variable`, `calculate_sum()`
- **PascalCase** para clases: `MyClass`
- **UPPER_CASE** para constantes: `MAX_SIZE = 100`

### Indentación y Espaciado
```python
# Bueno ✓
def function_name(param1, param2):
    if condition:
        do_something()
    return result

# Evitar ✗
def function_name(param1,param2):
  if condition:
        do_something()
  return result
```

### Imports
```python
# Bueno ✓
import os
import sys
from collections import defaultdict

# Evitar ✗
from collections import *
```

### Comentarios
```python
# Usa comentarios para explicar el "por qué", no el "qué"
# Bueno ✓
# Usamos binary search porque el array está ordenado
result = binary_search(arr, target)

# Evitar ✗
# Llama a binary search
result = binary_search(arr, target)
```

## 🚀 Proceso de Adición

1. **Crear el archivo**
   ```bash
   cd algorithms/warmup
   touch nuevo_problema.py
   ```

2. **Escribir la solución** usando la plantilla

3. **Probar localmente**
   ```bash
   python nuevo_problema.py
   ```

4. **Agregar al repositorio**
   ```bash
   git add algorithms/warmup/nuevo_problema.py
   git commit -m "Añadir solución: [Nombre del Problema] ([Dificultad])"
   git push origin main
   ```

## 💡 Consejos

### Para Principiantes
- Empieza con problemas "Easy"
- No te preocupes por la optimización al principio, primero haz que funcione
- Lee las soluciones de otros después de resolver el problema

### Para Avanzados
- Incluye múltiples enfoques si existen (fuerza bruta vs. optimizado)
- Agrega análisis de trade-offs entre diferentes soluciones
- Contribuye con explicaciones detalladas para ayudar a otros

## 📊 Ejemplos de Buenos Commits

```bash
# Bueno ✓
git commit -m "Añadir solución: Two Strings (Easy)"
git commit -m "Optimizar solución de Array Manipulation (Hard)"
git commit -m "Agregar enfoque alternativo para Queens Attack II"

# Evitar ✗
git commit -m "update"
git commit -m "fix"
git commit -m "nuevo archivo"
```

## 🐛 Reporte de Errores

Si encuentras un error en alguna solución:

1. Verifica que el error sea reproducible
2. Identifica el caso de prueba que falla
3. Si es tu solución, corrígela
4. Haz commit con un mensaje descriptivo: `"Corregir edge case en [nombre del problema]"`

## 📚 Recursos Útiles

- [PEP 8 - Style Guide for Python](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python - Code Style](https://realpython.com/python-code-quality/)

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar librerías externas?**
R: Preferiblemente usa la biblioteca estándar de Python. HackerRank tiene limitaciones en las librerías disponibles.

**P: ¿Qué hago si hay múltiples formas de resolver un problema?**
R: Incluye la solución más eficiente en la función principal. Puedes agregar enfoques alternativos como comentarios o funciones adicionales.

**P: ¿Debo incluir todos los casos de prueba?**
R: No es necesario. Incluye 1-2 ejemplos representativos en el docstring.

**P: ¿Puedo reorganizar la estructura de carpetas?**
R: Sí, pero mantén consistencia y actualiza el README.md en consecuencia.

## 🎯 Metas de Calidad

Aspira a:
- ✅ Código limpio y legible
- ✅ Documentación clara
- ✅ Soluciones eficientes
- ✅ Manejo de edge cases
- ✅ Seguir las convenciones de Python

---

**¡Gracias por mantener este repositorio organizado y útil! 🌟**
