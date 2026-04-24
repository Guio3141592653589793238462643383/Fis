# 📚 Proyecto de Fundamentos en Python

Repositorio de práctica con **Python** enfocado en:

- 🧠 Fundamentos del lenguaje  
- 🔢 Matemáticas y cálculo  
- ⚛️ Física clásica  
- 📊 Visualización de datos  

Incluye ejercicios y scripts que combinan cálculo simbólico, numérico y gráficas.

---

## 📁 Estructura del proyecto

```
├── calculo
├── ejercicios_basicos
├── fisica_clasica
├── fundamentos_python
├── matematicas
└── visualizacion
```

### 🔹 Descripción

- **calculo** → Derivadas, integrales, funciones
- **ejercicios_basicos** → Lógica y estructuras básicas
- **fisica_clasica** → Fórmulas y simulaciones simples
- **fundamentos_python** → Sintaxis y bases del lenguaje
- **matematicas** → Álgebra y funciones
- **visualizacion** → Gráficas con datos

---

## ⚙️ Requisitos

- Python 3.8+

### 📦 Librerías usadas

```
pip install sympy numpy matplotlib tabulate
```

---

## 🚀 Ejemplo de uso

```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

x = sp.symbols('x')
y = sp.sin(x)

f = sp.lambdify(x, y, 'numpy')

x_vals = np.linspace(0, 8*np.pi, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.title("Gráfica de sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()

filas = [[xv, yv] for xv, yv in zip(x_vals, y_vals)]
print(tabulate(filas, headers=["x", "y"], tablefmt="grid"))
```

---

## 🚀 Cómo ejecutar

```
git clone <URL_DEL_REPO>
cd <PROYECTO>
python ruta/al/script.py
```

---

## 🎯 Objetivo

Este proyecto sirve para:

- Practicar Python de forma aplicada  
- Entender matemáticas con código  
- Visualizar funciones y datos  
- Explorar ideas de física y cálculo  

---

## 📌 Notas

- Los scripts son independientes (puedes correrlos por separado)
- Puedes modificar funciones y rangos para experimentar

---

## 🤝 Contribuciones

1. Fork  
2. Nueva rama  
3. Pull request  

---

## 📄 Licencia

Uso libre con fines educativos
