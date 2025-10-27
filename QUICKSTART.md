# Guía Rápida de Inicio ⚡

## Configuración Inicial (5 minutos)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/jflorianar/MeHackerRank.git
cd MeHackerRank
```

### 2. Configurar Entorno Virtual (Opcional pero Recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar (Linux/Mac)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate
```

## Workflow Diario

### Resolver un Problema en HackerRank

1. **Lee y resuelve el problema** en HackerRank
2. **Copia tu solución** que pasó todos los tests
3. **Crea el archivo** en la carpeta correcta:
   ```bash
   cd algorithms/warmup
   touch nombre_problema.py
   ```
4. **Usa la plantilla TEMPLATE.py** del repositorio
5. **Pega tu código** y completa la documentación
6. **Prueba localmente**:
   ```bash
   python nombre_problema.py
   ```
7. **Guarda en Git**:
   ```bash
   git add .
   git commit -m "Solución: Nombre del Problema (Dificultad)"
   git push origin main
   ```

## Estructura de Carpetas

```
Problema de Warmup       → algorithms/warmup/
Problema de Strings      → algorithms/strings/
Problema de Arrays       → data_structures/arrays/
Problema de Python       → python/introduction/
Problema de SQL          → sql/basic_select/
```

## Plantilla Rápida

```python
"""
Título: [Nombre]
Dificultad: [Easy/Medium/Hard]
URL: [link]
"""

def solution(params):
    # tu código
    pass

if __name__ == '__main__':
    # input/output
    pass
```

## Comandos Git Útiles

```bash
# Ver estado
git status

# Agregar archivos
git add .

# Commit con mensaje
git commit -m "Mensaje descriptivo"

# Subir cambios
git push origin main

# Ver historial
git log --oneline

# Ver cambios no guardados
git diff
```

## Vincular con HackerRank

1. Ir a [HackerRank Settings](https://www.hackerrank.com/settings)
2. Buscar sección "Social Networks"
3. Click en "Connect" junto a GitHub
4. Autorizar la conexión

## Tips Rápidos

✅ **DO:**
- Resolver problemas Easy primero
- Documentar tu código
- Probar localmente antes de commit
- Usar nombres descriptivos para archivos
- Especificar complejidad temporal/espacial

❌ **DON'T:**
- Copiar soluciones sin entender
- Hacer commit sin probar
- Usar nombres genéricos (solution.py, test.py)
- Olvidar la URL del problema

## Atajos de Teclado Python

```python
# Invertir string/lista
s[::-1]

# List comprehension
[x*2 for x in range(10)]

# Múltiple asignación
a, b = 1, 2

# F-strings
f"Resultado: {variable}"

# Lambda
sorted(items, key=lambda x: x[1])
```

## Recursos Rápidos

- **Documentación Python**: https://docs.python.org/3/
- **Big-O Cheat Sheet**: https://www.bigocheatsheet.com/
- **VisuAlgo**: https://visualgo.net/
- **Python Tutor**: https://pythontutor.com/

## Metas Sugeridas

- [ ] 1 problema al día durante 30 días
- [ ] Completar todo Warmup (Easy)
- [ ] 10 problemas de cada categoría
- [ ] Participar en 1 competencia mensual

## Problemas para Empezar (Fáciles)

1. Solve Me First
2. Simple Array Sum
3. Compare the Triplets
4. A Very Big Sum
5. Diagonal Difference
6. Plus Minus
7. Staircase
8. Mini-Max Sum
9. Birthday Cake Candles
10. Time Conversion

## ¿Necesitas Ayuda?

- Revisa `CONTRIBUTING.md` para guidelines detalladas
- Consulta `README.md` para información completa
- Usa `TEMPLATE.py` como plantilla para nuevas soluciones

---

**¡Empieza ahora! Resuelve tu primer problema y súbelo al repo.** 🚀
