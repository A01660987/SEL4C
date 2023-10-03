from SEL4C.models import (
    Gender,
    Country,
    User,
    Administrator,
    Group,
    Institution,
    AcademicDegree,
    AcademicDegreeOffer,
    AcademicDiscipline,
    DiagnosisQuestion,
    Test,
    TrainingReagent,
)

genders = Gender.objects.bulk_create(
    [
        Gender(denomination="Masculino"),
        Gender(denomination="Femenino"),
        Gender(denomination="Prefiero no decir"),
        Gender(denomination="No binario"),
    ]
)

genders.save()

countries = Country.objects.bulk_create(
    [
        Country(denomination="Afganistán", code="AFG"),
        Country(denomination="Albania", code="ALB"),
        Country(denomination="Alemania", code="DEU"),
        Country(denomination="Andorra", code="AND"),
        Country(denomination="Angola", code="AGO"),
        Country(denomination="Anguila", code="AIA"),
        Country(denomination="Antártida", code="ATA"),
        Country(denomination="Antigua y Barbuda", code="ATG"),
        Country(denomination="Arabia Saudita", code="SAU"),
        Country(denomination="Argelia", code="DZA"),
        Country(denomination="Argentina", code="ARG"),
        Country(denomination="Armenia", code="ARM"),
        Country(denomination="Aruba", code="ABW"),
        Country(denomination="Australia", code="AUS"),
        Country(denomination="Austria", code="AUT"),
        Country(denomination="Azerbaiyán", code="AZE"),
        Country(denomination="Bahamas", code="BHS"),
        Country(denomination="Bahrein", code="BHR"),
        Country(denomination="Bailía de Guernsey", code="GGY"),
        Country(denomination="Bangladesh", code="BGD"),
        Country(denomination="Barbados", code="BRB"),
        Country(denomination="Belarús", code="BLR"),
        Country(denomination="Bélgica", code="BEL"),
        Country(denomination="Belice", code="BLZ"),
        Country(denomination="Benín", code="BEN"),
        Country(denomination="Bermudas", code="BMU"),
        Country(denomination="Bolivia", code="BOL"),
        Country(denomination="Bosnia y Hercegovina", code="BIH"),
        Country(denomination="Botsuana", code="BWA"),
        Country(denomination="Brasil", code="BRA"),
        Country(denomination="Brunéi", code="BRN"),
        Country(denomination="Bulgaria", code="BGR"),
        Country(denomination="Burkina Faso", code="BFA"),
        Country(denomination="Burundi", code="BDI"),
        Country(denomination="Bután", code="BTN"),
        Country(denomination="Cabo Verde", code="CPV"),
        Country(denomination="Camboya", code="KHM"),
        Country(denomination="Camerún", code="CMR"),
        Country(denomination="Canadá", code="CAN"),
        Country(denomination="Caribe Neerlandés", code="BES"),
        Country(denomination="Catar", code="QAT"),
        Country(denomination="Chad", code="TCD"),
        Country(denomination="Chequia", code="CZE"),
        Country(denomination="Chile", code="CHL"),
        Country(denomination="China", code="CHN"),
        Country(denomination="Chipre", code="CYP"),
        Country(denomination="Ciudad del Vaticano", code="VAT"),
        Country(denomination="Colombia", code="COL"),
        Country(denomination="Comores", code="COM"),
        Country(denomination="Corea del Norte", code="PRK"),
        Country(denomination="Corea del Sur", code="KOR"),
        Country(denomination="Costa de Marfil", code="CIV"),
        Country(denomination="Costa Rica", code="CRI"),
        Country(denomination="Croacia", code="HRV"),
        Country(denomination="Cuba", code="CUB"),
        Country(denomination="Curaçao", code="CUW"),
        Country(denomination="Dinamarca", code="DNK"),
        Country(denomination="Dominica", code="DMA"),
        Country(denomination="Ecuador", code="ECU"),
        Country(denomination="Egipto", code="EGY"),
        Country(denomination="El Salvador", code="SLV"),
        Country(denomination="Emiratos Árabes Unidos", code="ARE"),
        Country(denomination="Eritrea", code="ERI"),
        Country(denomination="Eslovaquia", code="SVK"),
        Country(denomination="Eslovenia", code="SVN"),
        Country(denomination="España", code="ESP"),
        Country(denomination="Estados Federados de Micronesia", code="FSM"),
        Country(denomination="Estados Unidos de América", code="USA"),
        Country(denomination="Estonia", code="EST"),
        Country(denomination="Esuatini", code="SWZ"),
        Country(denomination="Etiopía", code="ETH"),
        Country(denomination="Filipinas", code="PHL"),
        Country(denomination="Finlandia", code="FIN"),
        Country(denomination="Fiyi", code="FJI"),
        Country(denomination="Francia", code="FRA"),
        Country(denomination="Gabón", code="GAB"),
        Country(denomination="Gambia", code="GMB"),
        Country(denomination="Georgia", code="GEO"),
        Country(
            denomination="Georgia del Sur y las Islas Sandwich del Sur", code="SGS"
        ),
        Country(denomination="Ghana", code="GHA"),
        Country(denomination="Gibraltar", code="GIB"),
        Country(denomination="Granada", code="GRD"),
        Country(denomination="Grecia", code="GRC"),
        Country(denomination="Groenlandia", code="GRL"),
        Country(denomination="Guadalupe", code="GLP"),
        Country(denomination="Guam", code="GUM"),
        Country(denomination="Guatemala", code="GTM"),
        Country(denomination="Guayana", code="GUY"),
        Country(denomination="Guayana Francesa", code="GUF"),
        Country(denomination="Guinea", code="GIN"),
        Country(denomination="Guinea Ecuatorial", code="GNQ"),
        Country(denomination="Guinea-Bissau", code="GNB"),
        Country(denomination="Haití", code="HTI"),
        Country(denomination="Honduras", code="HND"),
        Country(denomination="Hong Kong", code="HKG"),
        Country(denomination="Hungría", code="HUN"),
        Country(denomination="India", code="IND"),
        Country(denomination="Indonesia", code="IDN"),
        Country(denomination="Irán", code="IRN"),
        Country(denomination="Iraq", code="IRQ"),
        Country(denomination="Irlanda", code="IRL"),
        Country(denomination="Isla Bouvet", code="BVT"),
        Country(denomination="Isla de Man", code="IMN"),
        Country(denomination="Isla de Navidad", code="CXR"),
        Country(denomination="Isla de San Martín", code="MAF"),
        Country(denomination="Isla Mauricio", code="MUS"),
        Country(denomination="Isla Norfolk", code="NFK"),
        Country(denomination="Islandia", code="ISL"),
        Country(denomination="Islas Åland", code="ALA"),
        Country(denomination="Islas Caimán", code="CYM"),
        Country(denomination="Islas Cocos", code="CCK"),
        Country(denomination="Islas Cook", code="COK"),
        Country(denomination="Islas Feroe", code="FRO"),
        Country(denomination="Islas Heard y McDonald", code="HMD"),
        Country(denomination="Islas Malvinas", code="FLK"),
        Country(denomination="Islas Marianas del Norte", code="MNP"),
        Country(denomination="Islas Marshall", code="MHL"),
        Country(denomination="Islas Pitcairn", code="PCN"),
        Country(denomination="Islas Salomón", code="SLB"),
        Country(denomination="Islas Turcas y Caicos", code="TCA"),
        Country(
            denomination="Islas ultramarinas menores de los Estados Unidos", code="UMI"
        ),
        Country(denomination="Islas Vírgenes (UK)", code="VGB"),
        Country(denomination="Islas Vírgenes Americanas", code="VIR"),
        Country(denomination="Israel", code="ISR"),
        Country(denomination="Italia", code="ITA"),
        Country(denomination="Jamaica", code="JAM"),
        Country(denomination="Japón", code="JPN"),
        Country(denomination="Jersey", code="JEY"),
        Country(denomination="Jordania", code="JOR"),
        Country(denomination="Kazajistán​​​", code="KAZ"),
        Country(denomination="Kenia", code="KEN"),
        Country(denomination="Kirguistán", code="KGZ"),
        Country(denomination="Kiribati", code="KIR"),
        Country(denomination="Kosovo", code="XXK"),
        Country(denomination="Kuwait", code="KWT"),
        Country(denomination="Laos", code="LAO"),
        Country(denomination="Lesotho", code="LSO"),
        Country(denomination="Letonia", code="LVA"),
        Country(denomination="Líbano", code="LBN"),
        Country(denomination="Liberia", code="LBR"),
        Country(denomination="Libia", code="LBY"),
        Country(denomination="Liechtenstein", code="LIE"),
        Country(denomination="Lituania", code="LTU"),
        Country(denomination="Luxemburgo", code="LUX"),
        Country(denomination="Macao", code="MAC"),
        Country(denomination="Macedonia del Norte", code="MKD"),
        Country(denomination="Madagascar", code="MDG"),
        Country(denomination="Malasia", code="MYS"),
        Country(denomination="Malaui", code="MWI"),
        Country(denomination="Maldivas", code="MDV"),
        Country(denomination="Malí", code="MLI"),
        Country(denomination="Malta", code="MLT"),
        Country(denomination="Marruecos", code="MAR"),
        Country(denomination="Martinica", code="MTQ"),
        Country(denomination="Mauritania", code="MRT"),
        Country(denomination="Mayotte", code="MYT"),
        Country(denomination="México", code="MEX"),
        Country(denomination="Moldavia", code="MDA"),
        Country(denomination="Mongolia", code="MNG"),
        Country(denomination="Montenegro", code="MNE"),
        Country(denomination="Montserrat", code="MSR"),
        Country(denomination="Mozambique", code="MOZ"),
        Country(denomination="Myanmar", code="MMR"),
        Country(denomination="Namibia", code="NAM"),
        Country(denomination="Nauru", code="NRU"),
        Country(denomination="Nepal", code="NPL"),
        Country(denomination="Nicaragua", code="NIC"),
        Country(denomination="Níger", code="NER"),
        Country(denomination="Nigeria", code="NGA"),
        Country(denomination="Niue", code="NIU"),
        Country(denomination="Noruega", code="NOR"),
        Country(denomination="Nueva Caledonia", code="NCL"),
        Country(denomination="Nueva Zelandia", code="NZL"),
        Country(denomination="Omán", code="OMN"),
        Country(denomination="Países Bajos", code="NLD"),
        Country(denomination="Pakistán", code="PAK"),
        Country(denomination="Palaos", code="PLW"),
        Country(denomination="Palestina", code="PSE"),
        Country(denomination="Panamá", code="PAN"),
        Country(denomination="Papúa Nueva Guinea", code="PNG"),
        Country(denomination="Paraguay", code="PRY"),
        Country(denomination="Perú", code="PER"),
        Country(denomination="Polinesia Francesa", code="PYF"),
        Country(denomination="Polonia", code="POL"),
        Country(denomination="Portugal", code="PRT"),
        Country(denomination="Principado de Mónaco", code="MCO"),
        Country(denomination="Puerto Rico", code="PRI"),
        Country(denomination="Reino Unido", code="GBR"),
        Country(denomination="República Centroafricana", code="CAF"),
        Country(denomination="República del Congo", code="COG"),
        Country(denomination="República Democrática del Congo", code="COD"),
        Country(denomination="República Dominicana", code="DOM"),
        Country(denomination="Reunión", code="REU"),
        Country(denomination="Ruanda", code="RWA"),
        Country(denomination="Rumania", code="ROU"),
        Country(denomination="Rusia", code="RUS"),
        Country(denomination="Sáhara Occidental", code="ESH"),
        Country(denomination="Samoa", code="WSM"),
        Country(denomination="Samoa Americana", code="ASM"),
        Country(denomination="San Bartolomé", code="BLM"),
        Country(denomination="San Cristóbal y Nieves", code="KNA"),
        Country(denomination="San Marino", code="SMR"),
        Country(denomination="San Pedro y Miquelón", code="SPM"),
        Country(denomination="San Vicente y las Granadinas", code="VCT"),
        Country(denomination="Santa Elena, Ascensión y Tristán de Acuña", code="SHN"),
        Country(denomination="Santa Lucía", code="LCA"),
        Country(denomination="Santo Tomé y Príncipe", code="STP"),
        Country(denomination="Senegal", code="SEN"),
        Country(denomination="Serbia", code="SRB"),
        Country(denomination="Seychelles", code="SYC"),
        Country(denomination="Sierra Leona", code="SLE"),
        Country(denomination="Singapur", code="SGP"),
        Country(denomination="Sint Maarten", code="SXM"),
        Country(denomination="Siria", code="SYR"),
        Country(denomination="Somalia", code="SOM"),
        Country(denomination="Sri Lanka", code="LKA"),
        Country(denomination="Sudáfrica", code="ZAF"),
        Country(denomination="Sudán", code="SDN"),
        Country(denomination="Sudán del Sur", code="SSD"),
        Country(denomination="Suecia", code="SWE"),
        Country(denomination="Suiza", code="CHE"),
        Country(denomination="Surinam", code="SUR"),
        Country(denomination="Svalbard y Jan Mayen", code="SJM"),
        Country(denomination="Tailandia", code="THA"),
        Country(denomination="Taiwán", code="TWN"),
        Country(denomination="Tanzania", code="TZA"),
        Country(denomination="Tayikistán", code="TJK"),
        Country(denomination="Territorio Británico del Océano Índico", code="IOT"),
        Country(
            denomination="Territorios Australes y Antárticos Franceses", code="ATF"
        ),
        Country(denomination="Timor Oriental", code="TLS"),
        Country(denomination="Togo", code="TGO"),
        Country(denomination="Tokelau", code="TKL"),
        Country(denomination="Tonga", code="TON"),
        Country(denomination="Trinidad y Tobago", code="TTO"),
        Country(denomination="Túnez", code="TUN"),
        Country(denomination="Turkmenistán", code="TKM"),
        Country(denomination="Turquía", code="TUR"),
        Country(denomination="Tuvalu", code="TUV"),
        Country(denomination="Ucrania", code="UKR"),
        Country(denomination="Uganda", code="UGA"),
        Country(denomination="Uruguay", code="URY"),
        Country(denomination="Uzbekistán", code="UZB"),
        Country(denomination="Vanuatu", code="VUT"),
        Country(denomination="Venezuela", code="VEN"),
        Country(denomination="Vietnam", code="VNM"),
        Country(denomination="Wallis y Futuna", code="WLF"),
        Country(denomination="Yemen", code="YEM"),
        Country(denomination="Yibuti", code="DJI"),
        Country(denomination="Zambia", code="ZMB"),
        Country(denomination="Zimbabue", code="ZWE"),
    ]
)

countries.save()


administrator = User.objects.create(
    email="admin@tec.mx",
    name="José Carlos",
    firstLastname="Vázquez",
    age=47,
    password="1230",
    gender=genders[0],
    country=countries[0],
)
administrator = Administrator.objects.create(identificator=administrator, code="")

administrator.save()

groups = Group.objects.bulk_create(
    [
        Group(denomination="Cátedra UNESCO-Invierno 2023"),
        Group(denomination="Grupo Prueba"),
        Group(denomination="Prueba Novus"),
    ]
)

groups.save()

institutions = Institution.objects.bulk_create(
    [
        Institution(denomination="Tecnológico de Monterrey"),
    ]
)

institutions.save()

academicDegrees = AcademicDegree.objects.bulk_create(
    [
        AcademicDegree(denomination="University"),
    ]
)

academicDegrees.save()

academicDegreeOffers = AcademicDegreeOffer.objects.bulk_create(
    [
        AcademicDegreeOffer(
            institution=institutions[0],
            academicDegree=academicDegrees[0],
            denomination="Pregrado",
        ),
        AcademicDegreeOffer(
            institution=institutions[0],
            academicDegree=academicDegrees[0],
            denomination="Posgrado",
        ),
        AcademicDegreeOffer(
            institution=institutions[0],
            academicDegree=academicDegrees[0],
            denomination="Educación continua",
        ),
    ]
)

academicDegreeOffers.save()

academicDisciplines = AcademicDiscipline.objects.bulk_create(
    [
        AcademicDiscipline(
            denomination="Ingeniería y Ciencias",
            academicDegreeOffer=academicDegreeOffers[0],
        ),
        AcademicDiscipline(
            denomination="Humanidades y Educación",
            academicDegreeOffer=academicDegreeOffers[0],
        ),
        AcademicDiscipline(
            denomination="Ciencias Sociales",
            academicDegreeOffer=academicDegreeOffers[0],
        ),
        AcademicDiscipline(
            denomination="Ciencias de la Salud",
            academicDegreeOffer=academicDegreeOffers[0],
        ),
        AcademicDiscipline(
            denomination="Arquitectura, Arte y Diseño",
            academicDegreeOffer=academicDegreeOffers[0],
        ),
        AcademicDiscipline(
            denomination="Negocios", academicDegreeOffer=academicDegreeOffers[0]
        ),
        AcademicDiscipline(
            denomination="Ingeniería y Ciencias",
            academicDegreeOffer=academicDegreeOffers[1],
        ),
        AcademicDiscipline(
            denomination="Humanidades y Educación",
            academicDegreeOffer=academicDegreeOffers[1],
        ),
        AcademicDiscipline(
            denomination="Ciencias Sociales",
            academicDegreeOffer=academicDegreeOffers[1],
        ),
        AcademicDiscipline(
            denomination="Ciencias de la Salud",
            academicDegreeOffer=academicDegreeOffers[1],
        ),
        AcademicDiscipline(
            denomination="Arquitectura, Arte y Diseño",
            academicDegreeOffer=academicDegreeOffers[1],
        ),
        AcademicDiscipline(
            denomination="Negocios", academicDegreeOffer=academicDegreeOffers[1]
        ),
        AcademicDiscipline(
            denomination="Ingeniería y Ciencias",
            academicDegreeOffer=academicDegreeOffers[2],
        ),
        AcademicDiscipline(
            denomination="Humanidades y Educación",
            academicDegreeOffer=academicDegreeOffers[2],
        ),
        AcademicDiscipline(
            denomination="Ciencias Sociales",
            academicDegreeOffer=academicDegreeOffers[2],
        ),
        AcademicDiscipline(
            denomination="Ciencias de la Salud",
            academicDegreeOffer=academicDegreeOffers[2],
        ),
        AcademicDiscipline(
            denomination="Arquitectura, Arte y Diseño",
            academicDegreeOffer=academicDegreeOffers[2],
        ),
        AcademicDiscipline(
            denomination="Negocios", academicDegreeOffer=academicDegreeOffers[2]
        ),
    ]
)

academicDisciplines.save()

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

diagnosisQuestions.save()

tests = Test.objects.bulk_create(
    [
        Test(denomination="Perfil del Emprendedor Social", description=None),
        Test(denomination="Pensamiento Complejo", description=None),
    ]
)

tests.save()

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
trainingReagents.save()
