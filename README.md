## sistema de gestion de encuestas
Sistema de Gestión de Encuestas
Este proyecto es una aplicación gráfica creada en Python utilizando Tkinter. Permite la creación, visualización, y respuesta de encuestas, ofreciendo una interfaz amigable y fácil de usar.

## Funcionalidades
### Crear Encuestas:

Añadir encuestas con un título y preguntas.
Guardar las encuestas en memoria.
Responder Encuestas:

Seleccionar una encuesta de una lista disponible.
Completar las respuestas y enviarlas para ser registradas.
Ver Resultados:

Revisar las preguntas y respuestas asociadas a cada encuesta.
Identificar encuestas sin respuestas.
Requisitos Previos
Python 3.8 o superior instalado en tu sistema.
Las siguientes librerías instaladas:
tkinter (incluido por defecto en Python)
pytest (opcional, si deseas ejecutar las pruebas unitarias)
Si no tienes pytest, puedes instalarlo con el siguiente comando:

### bash
Copiar código
pip install pytest
Instalación
Clona este repositorio o descarga los archivos en tu computadora.

Asegúrate de estar en el directorio raíz del proyecto.

## Si usas un entorno virtual, actívalo (opcional):

### bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate   # Windows
Instala las dependencias necesarias:

### bash
Copiar código
pip install -r requirements.txt
Si no hay un archivo requirements.txt, asegúrate de tener Python configurado para usar tkinter.

## Ejecución del Programa
Para ejecutar la aplicación, usa el siguiente comando:

### bash
Copiar código
python main.py
Esto abrirá la ventana principal del sistema de gestión de encuestas.

## Estructura del Proyecto

├── main.py                # Archivo principal para ejecutar la aplicación

├── create_survey.py       # Clase para crear encuestas

├── view_results.py        # Clase para ver resultados

├── answer_survey.py       # Clase para responder encuestas

├── README.md              # Este archivo

├── tests/                 # Carpeta para pruebas unitarias

│   ├── test_create_survey.py

│   ├── test_view_results.py

│   ├── test_answer_survey.py

## Pruebas
Si deseas ejecutar las pruebas unitarias, asegúrate de tener pytest instalado y ejecuta el siguiente comando en la raíz del proyecto:

### bash
Copiar código
pytest tests/
Esto ejecutará todos los archivos de prueba en la carpeta tests.

## Personalización
Puedes personalizar la apariencia de la interfaz gráfica modificando los valores en cada archivo correspondiente, como los colores, fuentes, o dimensiones de las ventanas.

## Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza los cambios necesarios y haz commit (git commit -m 'Añadida nueva funcionalidad').
Sube los cambios a tu rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.

Autor
Creado por: David Cuartas y Sebastian Beron

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.