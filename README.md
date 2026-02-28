# Curso de Algoritmos Cuánticos

Curso de algoritmos cuánticos con implementaciones prácticas en **Qiskit 2.2.x**, organizado por secciones y temas. Cada tema incluye teoría y código ejecutable en notebooks de Jupyter (Python).

## Contenido del curso

El material está estructurado en módulos progresivos, desde fundamentos hasta algoritmos avanzados:

| Sección | Temas | Descripción |
|---------|-------|-------------|
| **1. Introducción** | Qiskit | Fundamentos de programación en Qiskit: circuitos, puertas, mediciones y visualización |
| **2. Primeros algoritmos** | Teleportación, Errores, Deutsch-Jozsa | Protocolos básicos y corrección de errores cuánticos |
| **3. Algoritmos de estimación** | Hadamard Test, SWAP Test, QPE, HOLCUS | Técnicas para estimar amplitudes y fases |
| **4. Búsqueda** | Grover | Algoritmo de búsqueda en base de datos no estructurada |
| **5. Transformaciones** | QFT | Transformada Cuántica de Fourier |
| **6. Sistemas lineales** | LCU, HHL | Combinación lineal de unitarias y algoritmo HHL |
| **7. Factorización** | Shor | Algoritmo de Shor y variante 2n+3 qubits |

## Requisitos

- **Python** 3.10+
- **Qiskit** 2.2.x (el curso usa 2.2.3)
- **qiskit-aer** para simulación local

> **Nota:** Qiskit 2.2 introdujo cambios importantes respecto a versiones anteriores. Muchos tutoriales antiguos no son compatibles. Usa la versión indicada para seguir los ejemplos correctamente.

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd Curso_Cuantica

# Crear entorno virtual (recomendado)
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

1. Activa el entorno virtual.
2. Inicia Jupyter:
   ```bash
   jupyter notebook
   ```
3. Abre los notebooks en orden según la numeración de carpetas y temas.

## Estructura del repositorio

```
Curso_Cuantica/
├── 1_introduction/
│   └── qiskit_introduction.ipynb
├── 2_first_step_algorithms/
│   ├── 1_quantum_teleportation.ipynb
│   ├── 2_quantum_errors.ipynb
│   └── 3_deutsch_jozsa.ipynb
├── 3_estimation_algorithms/
│   ├── 4_hadamard_test.ipynb
│   ├── 5_swap_test.ipynb
│   ├── 8_quantum_phase_estimation.ipynb
│   └── 11_holcus.ipynb
├── 4_search_algorithms/
│   └── 6_grover_algorithm.ipynb
├── 5_transformations/
│   └── 7_quantum_fourier_transform.ipynb
├── 6_linear_systems/
│   ├── 9_linear_combination_unitaries.ipynb
│   └── 10_hhl_algorithm.ipynb
├── 7_factorization_algorithms/
│   ├── 12_shor_algorithm.ipynb
│   └── 13_shor_2n_plus_3.ipynb
├── requirements.txt
└── README.md
```

## Recursos

- [Documentación oficial de Qiskit](https://www.ibm.com/quantum/qiskit)
- [Qiskit GitHub](https://github.com/Qiskit/qiskit)

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
