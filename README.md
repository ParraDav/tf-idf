- `tf-idf.py` : Script principal que realiza los cálculos y genera el ranking.
- `documents.txt` (opcional) : Puedes reemplazar o agregar documentos en este archivo si deseas ampliar el corpus.

---

## Cómo usar

1. **Editar los documentos**  
   Dentro de `tf-idf.py`, la lista `documents` contiene los textos. Puedes agregar, eliminar o modificar documentos directamente en esa lista.

2. **Cambiar la consulta**  
   Modifica la variable `consulta` con la palabra o palabras que quieres buscar:

```python
consulta = "estudiante matrícula asistencia"
Ejecutar el script
python tf-idf.py
Ver los resultados
El script mostrará:
TF de cada término por documento
IDF de cada término
TF-IDF individual y suma por documento
Ranking final de documentos según relevancia

Ejemplo de ranking generado:

Posición	Documento	Suma TF-IDF
1	Documento 4	0.0511
2	Documento 3	0.0491
3	Documento 5	0.0358
…	…	…
<img width="512" height="791" alt="prueba1" src="https://github.com/user-attachments/assets/771a94d8-4dd7-4255-873e-1a3df440963f" />
<img width="559" height="841" alt="prueba2" src="https://github.com/user-attachments/assets/de5fd7dc-905d-4fa6-86ff-1d14ecdcfdca" />
<img width="569" height="848" alt="prueba3" src="https://github.com/user-attachments/assets/07ffe01f-b618-450c-8682-1ab0505d16f4" />
