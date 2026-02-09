# Ejercicios Básicos de Programación Científica en Python

## Resumen

El presente repositorio contiene una colección de programas desarrollados en lenguaje Python orientados a la resolución de problemas matemáticos, físicos y de análisis numérico. Los algoritmos implementados abarcan desde operaciones aritméticas fundamentales hasta métodos de integración numérica y cálculo simbólico, constituyendo una base sólida para el desarrollo de competencias en programación científica.

## Introducción

La programación científica representa una herramienta fundamental en el quehacer investigativo contemporáneo. El dominio de lenguajes de programación como Python, junto con sus bibliotecas especializadas, permite abordar problemas complejos de manera sistemática y reproducible. Este conjunto de ejercicios ha sido diseñado con el propósito de familiarizar al estudiante con los conceptos básicos de la programación aplicada a las ciencias exactas.

## Metodología

### Estructura del Repositorio

Los programas se encuentran organizados en cinco categorías funcionales, de acuerdo con su aplicación específica:

#### 1. Operaciones Matemáticas Básicas

Este módulo comprende implementaciones de calculadoras con diferentes niveles de complejidad:

- `calculadora.py`: Implementación de una calculadora integral que ejecuta operaciones aritméticas fundamentales (adición, sustracción, multiplicación, división) así como operaciones de potenciación y radicación.
- `exponentes.py`: Programa especializado en el cálculo de potencias y raíces enésimas.
- `bhaskara.py`: Algoritmo para la resolución de ecuaciones cuadráticas mediante la aplicación de la fórmula de Bhaskara-Sridhar, con validación de soluciones reales.
- `notacion_cientifica.py`: Convertidor automático de números decimales a notación científica normalizada.

#### 2. Geometría Analítica: Cálculo de Volúmenes

Se presentan cuatro implementaciones progresivas para el cálculo de volúmenes geométricos:

- `volumen.py`: Cálculo básico del volumen de prismas rectangulares.
- `volumen_mej.py`: Versión modularizada mediante el uso de funciones.
- `volumen_cono.py`: Implementación de la fórmula para el volumen de conos circulares rectos.
- `volumen_cono_mej.py`: Sistema completo que permite calcular cualquier parámetro del cono (volumen, altura o radio) a partir de los otros dos, mediante despeje algebraico de las fórmulas correspondientes.

#### 3. Análisis Numérico y Cálculo

Esta sección incluye implementaciones de métodos numéricos y simbólicos:

- `aproximación_pi.py`: Aproximación del valor de π mediante integración numérica de la función 4/(1+x²) en el intervalo [0,1], utilizando el método del trapecio.
- `simu.py`: Cálculo de la integral definida de sen(x) en el intervalo [0,π] mediante el método del trapecio con discretización de un millón de puntos.
- `simu_der_sen.py`: Diferenciación simbólica de la función seno utilizando la biblioteca SymPy.
- `simu_int_cos.py`: Integración simbólica de la función coseno empleando álgebra computacional.

#### 4. Tabulación de Funciones

Programas orientados a la generación de tablas de valores para funciones matemáticas:

- `tabular_seno.py`: Generación de 100 pares ordenados (x, sen(x)) en el intervalo [0, 2π].
- `tabular_coseno.py`: Generación de 100 pares ordenados (x, cos(x)) en el intervalo [0, π].
- `tres_cuatro.py`: Tabulación de la función exponencial e^x con 500 puntos en el intervalo [3,4].
- `ejercicio_auto.py`: Tabulación de una función lineal específica (y = -0.2222x + 60) para valores enteros de x en [0,100].

#### 5. Estructuras de Control de Flujo

Ejemplos didácticos de las estructuras iterativas fundamentales:

- `ciclo_for.py`: Implementación de bucle for determinista para la impresión de números consecutivos.
- `ciclo_while.py`: Implementación de bucle while condicional con contador incremental.

#### 6. Aplicaciones en Física

- `ejercicio_fis_1.py`: Programa para el cálculo del cambio de velocidad en sistemas mecánicos, aplicable a problemas de cinemática unidimensional.

## Requisitos del Sistema

### Dependencias

La ejecución de los programas requiere la instalación previa de las siguientes bibliotecas científicas de Python:

```bash
pip install numpy
pip install sympy
pip install tabulate
```

- **NumPy**: Biblioteca fundamental para computación científica que provee estructuras de datos eficientes y funciones matemáticas optimizadas.
- **SymPy**: Sistema de álgebra computacional que permite manipulación simbólica de expresiones matemáticas.
- **Tabulate**: Utilidad para el formateo de datos tabulares en diversos formatos de presentación.

### Versión de Python

Se recomienda utilizar Python 3.6 o versiones posteriores para garantizar la compatibilidad con todas las características del lenguaje empleadas en los programas.

## Procedimiento de Ejecución

Cada programa constituye una unidad ejecutable independiente. La ejecución se realiza mediante la invocación del intérprete de Python desde la línea de comandos:

```bash
python nombre_del_programa.py
```

La mayoría de las implementaciones siguen un paradigma de interacción usuario-programa, solicitando los parámetros necesarios mediante la función `input()` y presentando los resultados a través de la salida estándar.

### Ejemplos de Uso

**Resolución de ecuaciones cuadráticas:**
```bash
python bhaskara.py
```
El programa solicita los coeficientes a, b y c de la ecuación ax² + bx + c = 0 y retorna las raíces reales si existen.

**Aproximación numérica de π:**
```bash
python aproximación_pi.py
```
Ejecuta el algoritmo de integración numérica y presenta el valor aproximado de π con precisión determinada por el número de subdivisiones del intervalo.

**Cálculo de volumen de cono:**
```bash
python volumen_cono_mej.py
```
Sistema interactivo que permite calcular el parámetro desconocido del cono a partir de los dos parámetros conocidos.

## Resultados y Discusión

Los programas desarrollados demuestran la versatilidad de Python como lenguaje para computación científica. La utilización de bibliotecas especializadas como NumPy y SymPy permite implementar algoritmos numéricos y simbólicos con elevada precisión y eficiencia computacional.

La aproximación de π mediante integración numérica (programa `aproximación_pi.py`) ilustra la aplicación del teorema fundamental del cálculo, estableciendo que:

π = 4∫₀¹ dx/(1+x²)

El método del trapecio proporciona una aproximación cuya precisión mejora con el incremento del número de subdivisiones del intervalo de integración.

## Conclusiones

El conjunto de programas presentado constituye una introducción sistemática a la programación científica en Python. Los ejercicios abarcan conceptos fundamentales que van desde las estructuras de control básicas hasta la implementación de métodos numéricos avanzados. El dominio de estas técnicas representa un componente esencial en la formación de investigadores en ciencias exactas y naturales.

La modularización progresiva observada en algunos programas (por ejemplo, la evolución de `volumen.py` a `volumen_mej.py`) refleja buenas prácticas de ingeniería de software, promoviendo la reutilización de código y la legibilidad de las implementaciones.

## Referencias

Python Software Foundation. (2024). Python Language Reference, version 3.x. Disponible en: https://www.python.org

Harris, C. R., et al. (2020). Array programming with NumPy. *Nature*, 585(7825), 357-362.

Meurer, A., et al. (2017). SymPy: symbolic computing in Python. *PeerJ Computer Science*, 3:e103.

---

**Nota:** Los programas contenidos en este repositorio han sido desarrollados con fines exclusivamente educativos y didácticos en el contexto de la asignatura Redacción y Escritura de Textos Científicos I.
