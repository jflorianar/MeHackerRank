# MeHackerRank 🚀

Repositorio personal para practicar y almacenar soluciones de ejercicios de HackerRank en Python.

## 📋 Tabla de Contenidos

- [Estructura del Repositorio](#-estructura-del-repositorio)
- [Cómo Usar Este Repositorio](#-cómo-usar-este-repositorio)
- [Vincular GitHub con HackerRank](#-vincular-github-con-hackerrank)
- [Formato de Soluciones](#-formato-de-soluciones)
- [Categorías de Problemas](#-categorías-de-problemas)
- [Plataformas Recomendadas](#-plataformas-recomendadas)
- [Recursos de Aprendizaje](#-recursos-de-aprendizaje)

## 📁 Estructura del Repositorio

```
MeHackerRank/
│
├── algorithms/                    # Algoritmos
│   ├── warmup/                   # Problemas de calentamiento
│   ├── strings/                  # Manipulación de cadenas
│   ├── sorting/                  # Algoritmos de ordenamiento
│   ├── search/                   # Algoritmos de búsqueda
│   ├── dynamic_programming/      # Programación dinámica
│   ├── greedy/                   # Algoritmos voraces
│   ├── graphs/                   # Teoría de grafos
│   └── implementation/           # Problemas de implementación
│
├── data_structures/              # Estructuras de datos
│   ├── arrays/                   # Arreglos
│   ├── linked_lists/             # Listas enlazadas
│   ├── stacks/                   # Pilas
│   ├── queues/                   # Colas
│   ├── trees/                    # Árboles
│   └── heaps/                    # Montículos
│
├── mathematics/                  # Matemáticas
│   ├── fundamentals/             # Fundamentos
│   └── number_theory/            # Teoría de números
│
├── python/                       # Desafíos específicos de Python
│   ├── introduction/             # Introducción
│   ├── basic_data_types/         # Tipos de datos básicos
│   ├── strings/                  # Cadenas
│   ├── sets/                     # Conjuntos
│   └── collections/              # Colecciones
│
├── sql/                          # Desafíos SQL
│   ├── basic_select/             # Consultas básicas
│   └── advanced_select/          # Consultas avanzadas
│
└── interview_preparation/        # Preparación para entrevistas
```

## 🚀 Cómo Usar Este Repositorio

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/jflorianar/MeHackerRank.git
   cd MeHackerRank
   ```

2. **Crea un entorno virtual (recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Resuelve un problema y guarda tu solución**:
   - Navega a la carpeta correspondiente
   - Crea un archivo con un nombre descriptivo
   - Incluye el código y documentación

4. **Sube tus cambios**:
   ```bash
   git add .
   git commit -m "Añadir solución: [nombre del problema]"
   git push origin main
   ```

## 🔗 Vincular GitHub con HackerRank

HackerRank te permite vincular tu cuenta de GitHub para mostrar tus logros:

### Método 1: Vinculación Directa (Recomendado)

1. **Inicia sesión en HackerRank** ([hackerrank.com](https://www.hackerrank.com))

2. **Ve a tu perfil**:
   - Haz clic en tu avatar (esquina superior derecha)
   - Selecciona "Settings" o "Configuración"

3. **Conecta GitHub**:
   - En la sección "Social Networks" o "Redes Sociales"
   - Busca el icono de GitHub
   - Haz clic en "Connect" o "Conectar"
   - Autoriza a HackerRank para acceder a tu cuenta de GitHub

4. **Verifica la conexión**:
   - Una vez conectado, verás tu nombre de usuario de GitHub
   - Tus certificados y logros de HackerRank aparecerán en tu perfil de GitHub

### Método 2: Sincronización Manual de Soluciones

Para guardar automáticamente tus soluciones de HackerRank en GitHub:

1. **Resuelve el problema en HackerRank**

2. **Copia tu solución**

3. **Crea un archivo en este repositorio**:
   ```bash
   # Ejemplo para un problema de strings
   cd algorithms/strings
   touch two_strings.py
   ```

4. **Agrega tu código con documentación**:
   ```python
   """
   Problema: Two Strings
   Dificultad: Easy
   URL: https://www.hackerrank.com/challenges/two-strings
   
   Descripción:
   [Descripción breve del problema]
   
   Complejidad:
   - Tiempo: O(n)
   - Espacio: O(1)
   """
   
   def twoStrings(s1, s2):
       # Tu solución aquí
       pass
   ```

5. **Commit y push**:
   ```bash
   git add .
   git commit -m "Solución: Two Strings (Easy)"
   git push origin main
   ```

### Método 3: Badge de HackerRank en el README

Muestra tu perfil de HackerRank en este README:

```markdown
[![HackerRank](https://img.shields.io/badge/-HackerRank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)](https://www.hackerrank.com/tu_usuario)
```

## 📝 Formato de Soluciones

Cada solución debe incluir:

```python
"""
Título: [Nombre del Problema]
Dificultad: [Easy/Medium/Hard]
Categoría: [Algorithms/Data Structures/etc.]
URL: [Link al problema en HackerRank]

Descripción:
[Explicación breve del problema]

Enfoque:
[Estrategia utilizada para resolver el problema]

Complejidad:
- Tiempo: O(?)
- Espacio: O(?)

Fecha: [YYYY-MM-DD]
"""

# Solución
def nombre_funcion(parametros):
    """
    Argumentos:
    parametros -- descripción
    
    Retorna:
    descripción del valor de retorno
    """
    # Implementación
    pass

# Tests (opcional)
if __name__ == '__main__':
    # Casos de prueba
    print(nombre_funcion(test_input))
```

## 📚 Categorías de Problemas

### Algoritmos
- **Warmup**: Problemas de calentamiento para principiantes
- **Implementation**: Problemas de implementación básica
- **Strings**: Manipulación y procesamiento de cadenas
- **Sorting**: Algoritmos de ordenamiento
- **Search**: Algoritmos de búsqueda
- **Dynamic Programming**: Programación dinámica
- **Greedy**: Algoritmos voraces
- **Graphs**: Teoría de grafos y recorridos

### Estructuras de Datos
- **Arrays**: Arreglos y operaciones
- **Linked Lists**: Listas enlazadas
- **Stacks**: Pilas
- **Queues**: Colas
- **Trees**: Árboles binarios, BST, etc.
- **Heaps**: Montículos y colas de prioridad

### Python
- **Introduction**: Conceptos básicos de Python
- **Basic Data Types**: Listas, tuplas, diccionarios
- **Strings**: Manipulación de cadenas en Python
- **Sets**: Operaciones con conjuntos
- **Collections**: Módulo collections

## 🌟 Plataformas Recomendadas

Además de HackerRank, aquí hay otras excelentes plataformas para practicar:

### Para Algoritmos y Estructuras de Datos:
1. **LeetCode** ([leetcode.com](https://leetcode.com))
   - Excelente para preparación de entrevistas
   - Enfoque en empresas FAANG
   - Tiene discusiones de la comunidad

2. **CodeWars** ([codewars.com](https://www.codewars.com))
   - Sistema de ranking por "kyu"
   - Comunidad muy activa
   - Múltiples lenguajes de programación

3. **Exercism** ([exercism.org](https://exercism.org))
   - Mentoría gratuita
   - Track específico para Python
   - Enfoque en mejores prácticas

4. **AtCoder** ([atcoder.jp](https://atcoder.jp))
   - Competencias regulares
   - Problemas de alta calidad
   - Fuerte en algoritmos

5. **Codeforces** ([codeforces.com](https://codeforces.com))
   - Competencias programadas regularmente
   - Sistema de rating ELO
   - Excelente para programación competitiva

### Para Desarrollo de Proyectos:
6. **Frontend Mentor** ([frontendmentor.io](https://www.frontendmentor.io))
   - Proyectos de frontend con diseños reales
   - Enfoque en HTML/CSS/JavaScript

7. **CodeCrafters** ([codecrafters.io](https://codecrafters.io))
   - Construye tus propias herramientas (Git, Docker, etc.)
   - Aprendizaje profundo de sistemas

### Para SQL y Bases de Datos:
8. **SQLZoo** ([sqlzoo.net](https://sqlzoo.net))
   - Tutoriales interactivos de SQL
   - Desde básico hasta avanzado

9. **Mode Analytics SQL Tutorial** ([mode.com/sql-tutorial](https://mode.com/sql-tutorial/))
   - SQL para análisis de datos
   - Casos de uso reales

### Para Preparación de Entrevistas:
10. **Pramp** ([pramp.com](https://www.pramp.com))
    - Práctica de entrevistas peer-to-peer
    - Gratis y con retroalimentación en tiempo real

11. **AlgoExpert** ([algoexpert.io](https://www.algoexpert.io))
    - Curso completo de algoritmos
    - Videos explicativos detallados
    - (De pago)

## 📖 Recursos de Aprendizaje

### Libros Recomendados:
- "Cracking the Coding Interview" - Gayle Laakmann McDowell
- "Introduction to Algorithms" - CLRS
- "Python Cookbook" - David Beazley
- "Fluent Python" - Luciano Ramalho

### Cursos Online:
- [Python for Everybody - Coursera](https://www.coursera.org/specializations/python)
- [Algorithms Specialization - Stanford (Coursera)](https://www.coursera.org/specializations/algorithms)
- [CS50 - Harvard](https://cs50.harvard.edu/)

### Documentación:
- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)

## 📊 Seguimiento de Progreso

Mantén un registro de tu progreso:

| Categoría | Problemas Resueltos | Objetivo | Progreso |
|-----------|---------------------|----------|----------|
| Algorithms | 0 | 50 | █░░░░░░░░░ 0% |
| Data Structures | 0 | 30 | █░░░░░░░░░ 0% |
| Python | 0 | 40 | █░░░░░░░░░ 0% |
| SQL | 0 | 20 | █░░░░░░░░░ 0% |

## 🎯 Metas

- [ ] Resolver al menos 1 problema al día
- [ ] Completar el track de Python en HackerRank
- [ ] Dominar algoritmos de ordenamiento
- [ ] Aprender programación dinámica
- [ ] Participar en un HackerRank challenge mensual

## 📝 Notas

- Siempre intenta optimizar tu solución después de que funcione
- Revisa las soluciones de otros para aprender diferentes enfoques
- Documenta tu proceso de pensamiento
- No te rindas si un problema parece difícil, toma descansos

## 🤝 Contribuciones

Este es un repositorio personal, pero siéntete libre de:
- Sugerir mejoras en las soluciones
- Compartir enfoques alternativos
- Reportar errores

## 📄 Licencia

Este repositorio es de uso personal y educativo.

---

**¡Feliz Coding! 💻✨**

*Recuerda: La práctica constante es la clave del éxito en programación.*