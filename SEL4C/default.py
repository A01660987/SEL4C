from SEL4C.models import (
    User,
    Group,
    Institution,
    Discipline, 
    Degree,
    DiagnosisQuestion,
    Test,
    TrainingReagent,
)

administrator = User.objects.create(
    username="admin@tec.mx",
    name="José Carlos",
    first_lastname="Vázquez"
)

groups = Group.objects.bulk_create(
    [
        Group(name="Cátedra UNESCO-Invierno 2023"),
        Group(name="Grupo Prueba"),
        Group(name="Prueba Novus"),
    ]
)

institutions = Institution.objects.bulk_create(
    [
        Institution(name="Tecnológico de Monterrey"),
    ]
)

disciplines = Discipline.objects.bulk_create(
    [
        Discipline(
            name="Ingeniería y Ciencias"
        ),
        Discipline(
            name="Humanidades y Educación"
        ),
        Discipline(
            name="Ciencias Sociales"
        ),
        Discipline(
            name="Ciencias de la Salud"
        ),
        Discipline(
            name="Arquitectura, Arte y Diseño"
        ),
        Discipline(
            name="Negocios"
        ),
    ]
)

degrees = Degree.objects.bulk_create(
    [
        Degree(
            institution=institutions[0],
            discipline=disciplines[0],
            type="Pregrado",
        ),
        Degree(
            institution=institutions[0],
            discipline=disciplines[0],
            type="Posgrado",
        ),
        Degree(
            institution=institutions[0],
            discipline=disciplines[0],
            type="Educación continua",
        ),
    ]
)

"""
Estimado participante: el presente cuestionario tiene por objetivo medir tu percepción en cuanto al nivel de logro de las competencias de emprendimiento social y pensamiento complejo.

Se solicita tu valiosa colaboración y la disposición de 10 minutos para responder este test.  Los datos obtenidos serán usados con fines de investigación en innovación educativa. La información obtenida será estrictamente confidencial y  los datos personales serán protegidos de acuerdo con el aviso de privacidad y la ley de protección de datos personales del Tecnológico de Monterrey.

Al continuar, usted consciente que sus datos sean usados con fines de investigación. 

Por favor, registra los datos que se solicitan en la primera parte antes de responder el test.

Luego, lee detenidamente cada uno de los reactivos que se presentan y responde marcando la opción según el grado de acuerdo o desacuerdo, considerando la siguiente escala:

1: Nada de acuerdo.
2: Poco de acuerdo.
3: Ni de acuerdo ni desacuerdo.
4: De acuerdo.
5: Muy de acuerdo. 

¡Muchas gracias por tu participación!
"""

diagnosisQuestions = DiagnosisQuestion.objects.bulk_create(
    [
        # EduToolKit/SEL4C: Emprendimiento social y pensamiento complejo para todos y todas
        # Perfil del Emprendedor Social
        DiagnosisQuestion(
            question="Cuando algo me apasiona hago lo posible para lograr mis metas."
        ),
        DiagnosisQuestion(
            question="Cuando mi trabajo me apasiona hago lo posible por concluirlo, aunque enfrente circunstancias adversas, falta de tiempo o distractores."
        ),
        DiagnosisQuestion(
            question="A pesar del rechazo o problemas, siempre busco conseguir mis objetivos."
        ),
        DiagnosisQuestion(
            question="Soy tolerante ante situaciones ambiguas o que me generen incertidumbre."
        ),
        DiagnosisQuestion(
            question="Tengo la capacidad de establecer una meta clara y los pasos para lograrla."
        ),
        DiagnosisQuestion(
            question="Es común que logre convencer a otros sobre mis ideas y acciones."
        ),
        DiagnosisQuestion(
            question="Domino diferentes formas de comunicar mis ideas: por escrito, en un video o en charlas cara a cara."
        ),
        DiagnosisQuestion(
            question="Se me facilita delegar actividades a los miembros de mi equipo de acuerdo con sus perfiles."
        ),
        DiagnosisQuestion(
            question="Tengo la habilidad de identificar las fortalezas y debilidades de las personas con las que trabajo."
        ),
        DiagnosisQuestion(
            question="Se me facilita colaborar de manera activa en un equipo para lograr objetivos comunes."
        ),
        DiagnosisQuestion(question="Me apasiona trabajar en favor de causas sociales."),
        DiagnosisQuestion(
            question="Creo que la misión de mi vida es trabajar para el cambio social y mejorar la vida de las personas."
        ),
        DiagnosisQuestion(
            question="Me interesa dirigir una iniciativa con resultados favorables para la sociedad y/o el medio ambiente."
        ),
        DiagnosisQuestion(
            question="Soy capaz de identificar problemas en el entorno social o ambiental para generar soluciones innovadoras."
        ),
        DiagnosisQuestion(
            question="Manifiesto un compromiso por participar en aspectos sociales de mi entorno."
        ),
        DiagnosisQuestion(
            question="Opino que el crecimiento económico debe ocurrir en igualdad de oportunidades y equidad para todos."
        ),
        DiagnosisQuestion(
            question="Mis acciones y comportamientos se rigen por normas morales basadas en el respeto y cuidado hacia las personas y a la naturaleza."
        ),
        DiagnosisQuestion(
            question="Sé cómo aplicar estrategias para crear nuevas ideas o proyectos."
        ),
        DiagnosisQuestion(
            question="Sé aplicar conocimientos contables y financieros para el desarrollo de un emprendimiento."
        ),
        DiagnosisQuestion(
            question="Tengo nociones sobre la logística para llevar a cabo la gestión de una organización."
        ),
        DiagnosisQuestion(
            question="Sé cómo realizar un presupuesto para lograr un proyecto."
        ),
        DiagnosisQuestion(
            question="Sé cómo establecer criterios de valoración y medir los resultados de impacto social."
        ),
        DiagnosisQuestion(
            question="Creo que el cometer errores nos ofrece nuevas oportunidades de aprendizaje."
        ),
        DiagnosisQuestion(
            question="Conozco estrategias para desarrollar un proyecto, aún con escasez de recursos."
        ),
        # Pensamiento Complejo
        DiagnosisQuestion(
            question="Tengo la capacidad de encontrar asociaciones entre las variables, condiciones y restricciones en un proyecto."
        ),
        DiagnosisQuestion(
            question="Identifico datos de mi disciplina y de otras áreas que contribuyen a resolver problemas."
        ),
        DiagnosisQuestion(
            question="Participo en proyectos que se tienen que resolver utilizando perspectivas Inter/multidisciplinarias."
        ),
        DiagnosisQuestion(question="Organizo información para resolver problemas."),
        DiagnosisQuestion(
            question="Me agrada conocer perspectivas diferentes de un problema."
        ),
        DiagnosisQuestion(
            question="Me inclino por estrategias para comprender las partes y el todo de un problema."
        ),
        DiagnosisQuestion(
            question="Tengo la capacidad de Identificar los componentes esenciales de un problema para formular una pregunta de investigación."
        ),
        DiagnosisQuestion(
            question="Conozco la estructura y los formatos para elaborar reportes de investigación que se utilizan en mi área o disciplina."
        ),
        DiagnosisQuestion(
            question="Identifico la estructura de un artículo de investigación que se maneja en mi área o disciplina."
        ),
        DiagnosisQuestion(
            question="Identifico los elementos para formular una pregunta de investigación."
        ),
        DiagnosisQuestion(
            question="Diseño instrumentos de investigación coherentes con el método de investigación utilizado."
        ),
        DiagnosisQuestion(question="Formulo y pruebo hipótesis de investigación."),
        DiagnosisQuestion(
            question="Me inclino a usar datos científicos para analizar problemas de investigación."
        ),
        DiagnosisQuestion(
            question="Tengo la capacidad para analizar críticamente problemas desde diferentes perspectivas."
        ),
        DiagnosisQuestion(
            question="Identifico la fundamentación de juicios propios y ajenos para reconocer argumentos falsos."
        ),
        DiagnosisQuestion(
            question="Autoevalúo  el nivel de avance y logro de mis metas para hacer los ajustes necesarios."
        ),
        DiagnosisQuestion(
            question="Utilizo razonamientos basados en el conocimiento científico para emitir juicios ante un problema."
        ),
        DiagnosisQuestion(
            question="Me aseguro de revisar los lineamientos éticos de los proyectos en los que participo."
        ),
        DiagnosisQuestion(
            question="Aprecio críticas en el desarrollo de proyectos para mejorarlos."
        ),
        DiagnosisQuestion(
            question="Conozco los criterios para determinar un problema."
        ),
        DiagnosisQuestion(
            question="Tengo la capacidad de identificar las variables, de diversas disciplinas, que pueden ayudar a responder preguntas."
        ),
        DiagnosisQuestion(
            question="Aplico soluciones innovadoras a diversas problemáticas."
        ),
        DiagnosisQuestion(
            question="Soluciono problemas interpretando datos de diferentes disciplinas."
        ),
        DiagnosisQuestion(
            question="Analizo problemas de investigación contemplando el contexto para crear soluciones."
        ),
        DiagnosisQuestion(
            question="Tiendo a evaluar con sentido crítico e innovador las soluciones derivadas de un problema."
        ),
    ]
)

tests = Test.objects.bulk_create(
    [
        Test(denomination="Perfil del Emprendedor Social", description=None),
        Test(denomination="Pensamiento Complejo", description=None),
    ]
)

tests[0].diagnosisQuestions.add(*diagnosisQuestions[0:25])
tests[1].diagnosisQuestions.add(*diagnosisQuestions[25:50])

trainingReagents = TrainingReagent.objects.bulk_create(
    [
        TrainingReagent(
            denomination="Identificación",
            goals=None,
            description=None,
            indications="Haz una lluvia de ideas sobre problemas sociales o ambientales que se dan en tu entorno.\0Ahora, entrevista a una persona respecto a la misma idea.\0Por último, has un recorrido por tu colonia o ciudad y registra lo que ves relacionado con la situación ambiental o social. Busca identificar situaciones que no te agraden o problemas ya identificados.",
            questions="¿Cuáles identificas?\nMínimo deben poder identificar 5 problemáticas.\n¿Cómo te afectan estos problemas? ¿Has escuchado que le afecten a alguien cercano?\n¿Por qué se consideran un problema?\0¿Qué problemas ambientales o sociales identificas en tu casa, colonia o ciudad o país?\n¿Por qué son un problema?\n¿Quiénes intervienen en el problema?\n¿Te has visto afectado por este problema? ¿Cómo?\0¿Que viste?\n¿Dónde lo viste?\n¿Había alguien ocasionándolo o atendiéndolo?",
        ),
        TrainingReagent(
            denomination="Investigación",
            goals=None,
            description="Los Objetivos de Desarrollo Sostenible\n\nRevisa cada uno de los objetivos y sus metas e investiga como es que estos se relacionan con los problemas que identificaste.\nMira el siguiente video.\0Toca aqui para investigar el siguiente sitio web.\0Mira el siguiente video.\0Toca aqui para investigar el siguiente sitio web.\0¿Qué es un Árbol de Causas?\n\nLos problemas suelen ser como árboles, con causas que se enraízan en la sociedad y con ramas y hojas que se dividen en múltiples consecuencias que afectan a muchas personas, realidades y entornos. Tomemos de ejemplo la contaminación, la cual puede tener múltiples causas, y sus consecuencias pueden impactar tanto al medioambiente, como a las personas, el clima, la economía, el desarrollo de las ciudades, la salud, etc. Para poder hacer algo al respecto, es importante poder identificar qué es lo que está detonando los problemas, ya que solo así se podrán atender posibles consecuencias.",
            indications="Reflexiona acerca de los problemas que identificaste en la Actividad 1. Teniéndolos en mente, haz una investigación sobre los Objetivos de Desarrollo Sostenible. Te sugerimos los siguientes recursos.\0Los ODS nos permiten comprender como es que estas problemáticas son consideradas Retos y Desafíos para todo el Mundo, sin embargo, es importante que podamos conocer cuál es la situación actual. Como segunda parte de esta actividad, te pedimos que de las 5 problemáticas identificadas en la actividad 1, elijas 3 y realices una investigación que responda las siguientes preguntas.\0Con esta investigación, reflexiona sobre cuál es la problemática que consideras valioso atender. Debes conseguir elegir una. Para apoyarte en este proceso de elección, te sugerimos considerar lo siguiente.\0Como último punto de esta actividad, y habiendo elegido una problemática, es necesario que hagas un Árbol de Causas y Consecuencias.\0Una vez hecha esta reflexión, haz una investigación que considere por lo menos 3 posibles causas del problema seleccionado, así como 5 posibles consecuencias. Es relevante que se tomes en cuenta sus consecuencias en el entorno, la sociedad, las personas, la economía u cualquier otra área de abordaje.\nAunque se sugiere que la investigación sea documental, también es posible que te apoyes con entrevistas a especialistas, profesores, familiares o conocedores del tema.\0Una vez se haya hecho esta investigación, podrás hacer tu árbol de causas y consecuencias.\nEl tronco del árbol es el problema seleccionado; las raíces son las causas; las ramas y hojas son las consecuencias. Puedes dividir las consecuencias por su impacto internacional, nacional y local.\nSe sugiere que esta representación sea gráfica y con base en las herramientas propias que tengas.\nEn la parte inferior del árbol se sugiere respondas lo siguiente.\nA partir de esta información, ¿por qué es importante atender este problema?",
            questions="¿Cuál es el ODS (Objetivos de Desarrollo Sostenible) que consideras se relaciona mejor con cada problematica?\n¿Cómo se relaciona con estos temas?\n¿Hay alguna meta de dicho ODS que de manera concreta hable de esta relación?\0¿Cuál es la situación de estas problemáticas a nivel internacional, regional, nacional y local?\n¿Hay registro de afectaciones en la vida de las personas?\n¿Qué tanto afecta a tu localidad?\0Que sea un problema que afecte directamente a tu entorno.\nQue tenga un impacto en la calidad de vida de las personas.\nQue sea una problemática cercana a nosotros o a alguien que conozcamos",
        ),
        TrainingReagent(
            denomination="Ideación",
            goals=None,
            description="Recursos\n\nTe compartimos dos páginas que pueden serte de utilidad, de dos organizaciones que detonan proyectos como el tuyo.\0Reflexiona sobre el hecho de que innovar no siempre es la generación de algo único u original, sino que muchas ocasiones, el innovar puede ser una adaptación a un entorno, momento o grupo poblacional concreto. En ocasiones, lo que se hace en otro contexto puede resultar novedoso en nuestra localidad, lo que lo vuelve innovador. O también, puede haber acciones que se apliquen a cierta población, pero que también pueda ser valioso para otros grupos.\0Por ejemplo:\n\nAcciones para reducir la basura en las empresas que puedan adaptarse para las escuelas; o acciones que se lleven a cabo en Colombia que podrían adoptarse para la propia ciudad o colonia.",
            indications="Antes de arrojarnos a proponer posibles soluciones, es importante que veamos que se hace al respecto en otros lugares. Para ello, te sugerimos que hagas una investigación sobre acciones concretas que se hacen internacional, nacional o localmente para atender el problema que elegiste.\0Una vez reflexionado esto, analiza las acciones que identificaste en el punto anterior, cuestionando lo siguiente.\0Como cierre de este proceso de ideación deberías poder identificar una acción concreta que pudieras adaptar, mejorar y proponer para resolver el problema elegido.",
            questions="Si la solución que identificaste no es del lugar donde vives, ¿se podría llevar a cabo en este?\nSi la solución que identificaste es del lugar donde vives, ¿se podría aplicar en otra ciudad o país?\n¿Quiénes más podrían adoptar la solución que identificaste? ¿Podría realizarse por tus profesores, tu familia o tus vecinos?\n¿Cómo podrías sumarte? ¿Qué necesitarías?\n¿Qué harías diferente? ¿Podrías mejorar algo?\n¿Por qué sería una propuesta innovadora?\n¿Qué nombre le pondrías a su propuesta de solución?",
        ),
    ]
)
