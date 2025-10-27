# 🚀 MeHackerRank

Repositorio personal para practicar y almacenar ejercicios de programación de HackerRank en Python.

## 📁 Estructura del Repositorio

```
MeHackerRank/
├── exercises/
│   ├── algorithms/          # Ejercicios de algoritmos
│   │   └── warmup/         # Problemas de calentamiento
│   ├── data-structures/    # Estructuras de datos
│   ├── mathematics/        # Problemas matemáticos
│   └── python/             # Track específico de Python
│       └── introduction/   # Introducción a Python
├── template.py             # Plantilla para nuevos ejercicios
└── README.md              # Este archivo
```

## 🎯 Cómo Usar Este Repositorio

### 1. Crear un Nuevo Ejercicio

1. Copia el archivo `template.py` a la carpeta correspondiente
2. Renombra el archivo con un nombre descriptivo del ejercicio
3. Completa la información del header (título, dificultad, URL)
4. Implementa tu solución
5. Haz commit y push de tus cambios

Ejemplo:
```bash
cp template.py exercises/algorithms/warmup/simple_array_sum.py
# Edita el archivo y resuelve el problema
git add exercises/algorithms/warmup/simple_array_sum.py
git commit -m "Add: Simple Array Sum solution"
git push
```

### 2. Organización de Ejercicios

Organiza tus ejercicios según la categoría de HackerRank:
- **algorithms/**: Ejercicios de algoritmos
  - warmup/, sorting/, search/, etc.
- **data-structures/**: Arrays, listas, árboles, etc.
- **python/**: Track específico de Python
- **mathematics/**: Problemas matemáticos

## 🔗 Cómo Vincular tu Cuenta de GitHub con HackerRank

### Opción 1: Conectar Directamente (Recomendado)

1. **Accede a tu perfil de HackerRank**
   - Ve a https://www.hackerrank.com
   - Haz clic en tu foto de perfil → Settings

2. **Conecta tu cuenta de GitHub**
   - En la sección "Social Networks" o "Linked Accounts"
   - Busca la opción de GitHub y haz clic en "Connect"
   - Autoriza a HackerRank para acceder a tu perfil público de GitHub

3. **Beneficios**
   - Tu perfil de HackerRank mostrará tu actividad de GitHub
   - Los reclutadores pueden ver ambos perfiles conectados

### Opción 2: Sincronización Manual

Si prefieres mantener tu código en GitHub sin conexión directa:

1. **Después de resolver un problema en HackerRank:**
   ```bash
   # Copia tu solución al archivo correspondiente
   # Ejemplo: exercises/python/introduction/hello_world.py
   
   git add .
   git commit -m "Add: [Nombre del Ejercicio] - [Dificultad]"
   git push origin main
   ```

2. **Incluye el link en tu commit:**
   ```bash
   git commit -m "Add: Two Sum problem - Easy" -m "URL: https://www.hackerrank.com/challenges/two-sum"
   ```

### Opción 3: GitHub en tu Perfil de HackerRank

1. Edita tu perfil de HackerRank
2. En la sección "About" o "Bio"
3. Añade el link a este repositorio: `https://github.com/[tu-usuario]/MeHackerRank`

## 🌟 Otras Plataformas Recomendadas

### Para Práctica de Algoritmos y Estructuras de Datos

1. **LeetCode** (https://leetcode.com)
   - 🎯 Ideal para: Preparación de entrevistas técnicas
   - ✅ Pros: Problemas similares a entrevistas de FAANG, discusiones de la comunidad
   - 📊 Niveles: Easy, Medium, Hard
   - 💡 Especialmente útil para: Entrevistas de trabajo

2. **Codeforces** (https://codeforces.com)
   - 🎯 Ideal para: Programación competitiva
   - ✅ Pros: Competencias regulares, rankings globales, editorial detallada
   - 📊 Niveles: Div 1, Div 2, Div 3, Div 4
   - 💡 Especialmente útil para: Mejorar velocidad y precisión

3. **CodeWars** (https://www.codewars.com)
   - 🎯 Ideal para: Aprender diferentes lenguajes
   - ✅ Pros: Sistema de "kata" gamificado, múltiples soluciones visibles
   - 📊 Niveles: 8 kyu (más fácil) a 1 kyu (más difícil)
   - 💡 Especialmente útil para: Aprender mejores prácticas

4. **AtCoder** (https://atcoder.jp)
   - 🎯 Ideal para: Programación competitiva estilo japonés
   - ✅ Pros: Problemas de alta calidad, competencias semanales
   - 📊 Niveles: Beginner, Regular, Grand
   - 💡 Especialmente útil para: Algoritmos avanzados

### Para Proyectos y Desarrollo Práctico

5. **Exercism** (https://exercism.org)
   - 🎯 Ideal para: Aprender nuevos lenguajes con mentoría
   - ✅ Pros: Feedback de mentores, 100% gratis
   - 💡 Especialmente útil para: Aprendizaje guiado de Python

6. **Project Euler** (https://projecteuler.net)
   - 🎯 Ideal para: Problemas matemáticos y algorítmicos
   - ✅ Pros: Enfoque en matemáticas y algoritmia
   - 💡 Especialmente útil para: Desarrollar pensamiento matemático

### Para Entrevistas Específicas

7. **Pramp** (https://www.pramp.com)
   - 🎯 Ideal para: Practicar entrevistas técnicas con pares
   - ✅ Pros: Entrevistas mock gratuitas, feedback en tiempo real

8. **Interview Cake** (https://www.interviewcake.com)
   - 🎯 Ideal para: Preparación estructurada para entrevistas
   - ✅ Pros: Explicaciones detalladas paso a paso

## 📈 Recomendaciones de Estudio

### Ruta Sugerida (Principiante → Avanzado)

1. **Semanas 1-2**: Python Basics en HackerRank
   - Complete el track "Python" → "Introduction"
   - Practique sintaxis básica

2. **Semanas 3-4**: Algoritmos Básicos
   - Warmup challenges
   - Implementation problems

3. **Semanas 5-8**: Estructuras de Datos
   - Arrays, Strings
   - Linked Lists, Stacks, Queues

4. **Semanas 9-12**: Algoritmos Intermedios
   - Sorting, Searching
   - Greedy, Dynamic Programming (básico)

5. **Después**: Alternar entre plataformas
   - HackerRank para variedad
   - LeetCode para entrevistas
   - Codeforces para competencias

## 💡 Consejos

- ✅ **Consistencia**: Resuelve al menos 1 problema al día
- ✅ **Revisa Soluciones**: Después de resolver, mira otras soluciones
- ✅ **Documenta**: Añade comentarios explicando tu razonamiento
- ✅ **Timing**: Intenta resolver problemas dentro de un tiempo límite
- ✅ **Variedad**: No te quedes solo en problemas fáciles

## 📝 Convenciones de Commits

Usa estos prefijos para tus commits:
- `Add:` - Nuevo ejercicio resuelto
- `Update:` - Mejora de solución existente
- `Fix:` - Corrección de error
- `Docs:` - Cambios en documentación

Ejemplo:
```bash
git commit -m "Add: Simple Array Sum - Easy"
git commit -m "Update: Binary Search - Optimized O(log n) solution"
```

## 🤝 Contribuir

Este es un repositorio personal, pero si quieres compartir tus soluciones o sugerencias, ¡siéntete libre de crear un fork!

## 📚 Recursos Adicionales

- [Python Documentation](https://docs.python.org/3/)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualgo - Algorithm Visualizations](https://visualgo.net/)

---

**¡Feliz Coding! 🎉**

*De la teoría a la práctica, un ejercicio a la vez.*