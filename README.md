Proyecto TF-IDF para Documentos Académicos
Descripción

Este proyecto implementa un sistema de cálculo de TF-IDF (Term Frequency – Inverse Document Frequency) para un conjunto de documentos académicos.

El código permite:

Calcular la frecuencia de términos (TF) en cada documento.
Calcular la relevancia de los términos en el corpus (IDF).
Generar un score TF-IDF para consultas de usuario.
Identificar los documentos más relevantes según la consulta.

El proyecto está diseñado como un script en Python y se ejecuta desde la consola.

Requisitos
Python 3.10 o superior
Biblioteca NumPy

Instalar NumPy desde la terminal:

pip install numpy
Ejecución

Para ejecutar el proyecto, abrir la terminal y ejecutar:

python tfidf_proyecto.py

El sistema pedirá ingresar una consulta (palabras clave) y mostrará:

TF de cada término en cada documento
IDF de cada término
TF-IDF por término
Score final de cada documento
Ranking de los documentos según relevancia
Uso
Modificar el conjunto de documentos dentro del archivo tfidf_proyecto.py si se desea.
Definir la consulta de búsqueda en la variable consulta.
Ejecutar el script y revisar los resultados en la consola.