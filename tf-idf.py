import numpy as np

# Documentos (los mismos que ya tienes)
documents = [
    """La Institución podrá ofrecer programas académicos en todos los
niveles formales de la educación superior establecidos por la ley:
técnico profesional, tecnológico, profesional universitario,
especialización, maestría y doctorado.""",
    """La Institución podrá desarrollar programas de educación informal,
los cuales no conducirán a la obtención de títulos profesionales ni a
certificaciones de aptitud ocupacional. Estos programas serán
denominados programas de educación o formación continuada.
PARÁGRAFO: Los programas de educación o formación
continuada se podrán desarrollar en las modalidades presencial, a
distancia, virtual o en combinaciones de estas, de acuerdo con las
disposiciones vigentes.""",
    """Cada periodo académico tendrá una duración definida en semanas,
conforme lo reglamente el Consejo Académico, considerando las
características de los planes de estudio de los programas académicos,
las Resoluciones de Registro Calificado y la normativa nacional
vigente.
PARÁGRAFO: La hora académica con acompañamiento directo del
docente (sincrónico, ya sea presencial o remoto) tendrá una duración
establecida según el nivel de formación y el tipo de espacio
formativo, sin que ello limite la programación de bloques de dos o
más horas continuas, cuando sea necesario.""",
    """La matrícula es el acto mediante el cual la Institución reconoce
formalmente a una persona como estudiante. Al aceptar esta
condición, el estudiante se compromete a cumplir con los Estatutos
y reglamentos de la Institución. Esta calidad entra en vigor a partir
del pago de los derechos pecuniarios, el registro de asignaturas o
créditos académicos del programa y la suscripción del acta de
matrícula que se realiza a través de los medios dispuestos para tal
fin.""",
    """La matrícula se cancela:
1. Por decisión voluntaria del estudiante, comunicada a través del
trámite académico establecido y dentro de los plazos fijados por la
Institución.
2. Por las causales de pérdida de la calidad de estudiante,
contempladas en el presente Reglamento.
PARÁGRAFO: En el caso de la cancelación de matrícula por decisión
voluntaria, se activará automáticamente el proceso de reserva de
cupo.""",
    """La asistencia de los estudiantes es obligatoria, toda vez que el
programa académico al que está matriculado disponga de espacios
formativos que impliquen presencialidad o mediación tecnológica de
esta. La participación presencial y/o sincrónica remota de los
estudiantes constituye una responsabilidad y compromiso del
estudiante.""",
    """Cuando la inasistencia a una asignatura iguale o
supere el porcentaje anteriormente señalado, la asignatura se califica
con cero (0), y el sistema la registrará como reprobada por
inasistencia, caso en el cual el estudiante deberá registrarla y cursarla
nuevamente como repitente. El estudiante que pierda la asignatura
por ausencias podrá continuar asistiendo a dicha asignatura y
presentando evaluaciones que permitan realimentar
cualitativamente su desempeño sin que implique una calificación
formal.""",
    """Es compromiso del estudiante ingresar oportunamente al aula física
o virtual, según el caso. Si por inconvenientes no previstos, el
estudiante llega tarde, el ingreso no ocurrirá después de
transcurridos los primeros quince (15) minutos de la hora de clase,
asumiendo que en su ausencia las actividades académicas
evaluativas no podrán realizarse posteriormente y su nota será cero
(0), a excepción de tener una excusa avalada por el programa; así
mismo, los contenidos tratados durante su ausencia se dan por
vistos""",
    """La valoración del alcance de los resultados de aprendizaje por parte
del estudiante será permanente durante todo el proceso formativo.
Al iniciar cada asignatura el profesor informará a los estudiantes
sobre las actividades y procedimientos evaluativos que se van a
emplear, así como su peso ponderado; esta información estará
registrada en el plan analítico de cada asignatura. Lo anterior, sin
perjuicio de la implementación de actividades que, a juicio docente,
sean pertinentes en el marco de los objetivos académicos.""",
    """Se denominan pruebas de evaluación parcial y qüices, las pruebas
orales o escritas que cada profesor realiza en el marco de la
asignatura durante el periodo lectivo y antes de que este finalice, y
que son calificadas conforme a una pauta de evaluación o rúbrica.
Los docentes deben utilizar diferentes formas de evaluación durante
el periodo académico."""
]

# Función para TF
def tf(term, document):
    palabras = document.lower().split()
    return palabras.count(term.lower()) / len(palabras)

# Función para IDF
def idf(term, documents):
    N = len(documents)
    df = sum(1 for doc in documents if term.lower() in doc.lower())
    if df == 0:
        return 0
    return np.log(N / df)

# Función para TF-IDF
def tf_idf(term, document, documents):
    return tf(term, document) * idf(term, documents)

# Consulta
consulta = "estudiante"

# Dividir términos
terms = consulta.split()

# Listas para almacenar resultados
tf_list = []
idf_list = []
tf_idf_list = []

print(f"\nResultados para la consulta: {consulta}\n")

# Calcular TF, IDF y TF-IDF para cada documento y cada término
for i, doc in enumerate(documents):
    tf_doc = []
    idf_doc = []
    tf_idf_doc = []
    for term in terms:
        tf_val = tf(term, doc)
        idf_val = idf(term, documents)
        tf_idf_val = tf_val * idf_val
        tf_doc.append(round(float(tf_val),4))
        idf_doc.append(round(float(idf_val),4))
        tf_idf_doc.append(round(float(tf_idf_val),4))
    tf_list.append(tf_doc)
    idf_list.append(idf_doc)
    tf_idf_list.append(tf_idf_doc)
    print(f"Documento {i}:")
    print(f"  TF     : {tf_doc}")
    print(f"  IDF    : {idf_doc}")
    print(f"  TF-IDF : {tf_idf_doc}")
    print(f"  Suma TF-IDF: {sum(tf_idf_doc):.4f}\n")

# Ranking por suma de TF-IDF
ranking = sorted(enumerate([sum(doc) for doc in tf_idf_list]), key=lambda x: x[1], reverse=True)
print("Ranking de documentos según TF-IDF total:")
for rank, (idx, score) in enumerate(ranking, 1):
    print(f"{rank} - Documento {idx} : {score:.4f}")