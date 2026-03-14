*This project has been created as part of the 42 curriculum by laviles.*

<p align="center">
    <img src="https://img.shields.io/badge/Score-Pending-yellow?style=for-the-badge&logo=42" alt="Score Pending">
    <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" alt="Language Python">
    <img src="https://img.shields.io/badge/Status-In_Construction-orange?style=for-the-badge" alt="Status In Construction">
</p>

<details>
<summary>🇪🇸 <b>Leer en Español (Versión en Castellano)</b></summary>

## 🐍 Piscina de Python para Data Science @ 42

Este repositorio contiene el desarrollo integral de la **Piscina de Python de 42**. El programa está diseñado para transformar a un programador de sistemas en un desarrollador capaz de manipular datos, automatizar procesos y desplegar modelos de aprendizaje automático.

### 🏛️ Filosofía de Ingeniería: El Puente C -> Python
Como estudiante de 42 con base sólida en lenguaje C, este aprendizaje se aborda como un análisis de abstracción:
* **Gestión de Memoria:** Comparativa entre el `malloc/free` manual y el conteo de referencias/Garbage Collector de CPython.
* **Estructuras de Datos:** Análisis de la eficiencia de las colecciones de Python (Lists, Dicts, Sets) frente a las implementaciones manuales en C.
* **Encapsulación:** Evolución desde el uso de **static structs** y tipos opacos en C hacia el sistema de clases, visibilidad (`_` y `__`) y decoradores de Python.

### 📂 Roadmap de la Piscina
* **Módulo 00 - Starting:** Setup del entorno, manipulación de tipos básicos y lógica fundamental.
* **Módulo 01 - Array & OOP:** Programación Orientada a Objetos y computación vectorial inicial.
* **Módulo 02 - DataTable:** Análisis exploratorio de datos y manipulación de archivos CSV/Dataframes.
* **Módulo 03 - Matrix:** Matemáticas lineales y optimización de grandes volúmenes de datos.
* **Módulo 04 - Machine Learning:** Implementación de algoritmos predictivos (Regresión Lineal).
* **Módulo 05 - Handling & Logic:** Gestión avanzada de excepciones y lógica de control robusta.
* **Módulo 06 - Functional & Advanced:** Programación funcional (map, filter, reduce) y decoradores avanzados.

---
</details>

# 🐍 Python for Data Science Piscine @ 42

This repository hosts the complete journey through the **42 Python Piscine**. The curriculum is specifically engineered to bridge the gap between low-level systems programming and high-level data engineering and Machine Learning.

### 🏛️ Engineering Philosophy: The C to Python Bridge
Coming from a solid background in C, this project treats Python not just as a scripting tool, but as a powerful abstraction layer:
* **Memory Management:** Understanding CPython's reference counting and garbage collection vs. manual `malloc/free` logic.
* **Data Structures:** Evaluating the Big O complexity of Python's built-in collections compared to manual implementations in C.
* **Encapsulation:** Transitioning from **static structs** and opaque pointers in C to Python’s robust Class system and property decorators.

### 📂 Piscine Roadmap

| Module | Focus | Key Concepts |
| :--- | :--- | :--- |
| **Module 00** | **Starting** | Environment setup (`venv`), basic types, and Pythonic syntax (PEP 8). |
| **Module 01** | **OOP & Vector** | Classes, inheritance, and the transition to vector programming. |
| **Module 02** | **DataTable** | Data parsing, exploration, and visualization techniques. |
| **Module 03** | **Matrix** | Linear algebra implementations and optimized matrix operations. |
| **Module 04** | **Machine Learning** | Building predictive models (Linear Regression) from scratch. |
| **Module 05** | **Robustness** | Exception handling, context managers (`with`), and error logging. |
| **Module 06** | **Optimization** | Functional programming, closures, and advanced decorators. |

### 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/youruser/42-python-piscine.git](https://github.com/youruser/42-python-piscine.git) && cd 42-python-piscine
   ```

2. **Environment Setup (Python 3.10+):**
   ```bash
   # Create a virtual environment
   python3 -m venv venv
   
   # Activate it
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Running Exercises:**
   Each module is contained in its own directory. Navigate to the specific exercise and run the main script:
   ```bash
   python M01/ex02/simulator.py
   ```

4. **Code Quality:**
   Check compliance with the **flake8** linter (as required by 42 subjects):
   ```bash
   flake8 path/to/exercise.py
   ```

### 🤖 Methodology & AI Tutoring
The development process follows a **Technical Mentorship** model:
* **Deep Dive Research:** Using AI to analyze the C-source code of Python features (CPython) to understand performance implications.
* **Edge Case Identification:** Proactive searching for language limits and unexpected behaviors in production-like environments.
* **Strict Compliance:** All code is validated against **flake8** and utilizes full **type hinting**.

---

### 📚 Bibliography
* **Official Python 3.10+ Documentation.**
* **Fluent Python (Luciano Ramalho):** For advanced implementation patterns.
* **42 Subject Path:** The pedagogical guide for each module.

> "Abstraction is not about hiding complexity; it's about making it manageable."
