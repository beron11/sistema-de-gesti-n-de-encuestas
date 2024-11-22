## Requerimientos del Sistema de Gestión de Encuestas
Este archivo describe las dependencias necesarias para ejecutar el Sistema de Gestión de Encuestas y cómo configurar el entorno de desarrollo.

## Requisitos de Software
Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes herramientas:

Python 3.8 o superior

Python es el lenguaje de programación utilizado en este proyecto. Asegúrate de tener la versión 3.8 o superior instalada en tu sistema.
Instalación:

## Descargar Python
Tkinter (para interfaces gráficas)

Tkinter es la biblioteca estándar de Python utilizada para crear la interfaz gráfica del usuario (GUI) en este proyecto.
### Nota: Tkinter viene preinstalado con la mayoría de las distribuciones de Python, por lo que no es necesario instalarlo manualmente.
pytest (opcional para pruebas unitarias)

pytest es una herramienta para realizar pruebas automatizadas en el código.
Dependencias
El proyecto requiere las siguientes dependencias que deben ser instaladas mediante pip:

pytest - Para pruebas unitarias.

## Instalación:

Puedes instalar pytest utilizando el archivo requirements.txt o directamente con el siguiente comando:

### bash
Copiar código
pip install pytest
Versión recomendada: >=7.4.0

### Instalación del Proyecto
Sigue los siguientes pasos para instalar y ejecutar el proyecto en tu máquina local:

## Paso 1: Clonar el Repositorio
Primero, clona el repositorio desde GitHub:

### bash
Copiar código
git clone <URL_DEL_REPOSITORIO>
cd sistema-gestion-encuestas
## Paso 2: Crear un Entorno Virtual (opcional)
Es recomendable crear un entorno virtual para manejar las dependencias del proyecto sin afectar tu instalación global de Python.

### Para crear y activar un entorno virtual:

Linux/macOS:

### bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Windows:

### bash
Copiar código
python -m venv venv
venv\Scripts\activate
## Paso 3: Instalar Dependencias
Con el entorno virtual activado, instala las dependencias necesarias utilizando el archivo requirements.txt:

### bash
Copiar código
pip install -r requirements.txt
Esto instalará todas las bibliotecas requeridas, incluyendo pytest.

## Paso 4: Ejecutar el Proyecto
Para ejecutar la aplicación, ejecuta el siguiente comando:

### bash
Copiar código
python main.py
Uso de Pruebas Unitarias
El proyecto incluye pruebas unitarias utilizando pytest para verificar el funcionamiento correcto del sistema. Para ejecutar las pruebas, asegúrate de tener pytest instalado y luego ejecuta:

### bash
Copiar código
pytest tests/
Estructura del Proyecto

## La estructura del proyecto es la siguiente:

### Copiar código
sistema-gestion-encuestas/
├── main.py                # Archivo principal para ejecutar el programa

├── create_survey.py       # Módulo para la creación de encuestas

├── answer_survey.py       # Módulo para responder encuestas

├── view_results.py        # Módulo para ver resultados

├── tests/                 # Carpeta con pruebas unitarias

│   ├── test_create_survey.py

│   ├── test_answer_survey.py

│   └── test_view_results.py

├── docs/                  # Carpeta de documentación

│   ├── user_guide.md

│   ├── system_design.md

│   └── faq.md

├── requirements.txt       # Archivo con dependencias necesarias

└── README.md              # Este archivo

## Contacto
Si tienes preguntas o sugerencias sobre este proyecto, no dudes en ponerte en contacto con nosotros:

Correo electrónico: juans-beronl@unilibre.edu.co -- David-cuartash@unilibre.edu.co