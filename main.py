from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


PREGUNTAS_Y_RESPUESTAS = {
    "Hola": "Soy un bot creado para responder tus preguntas sobre tus Prácticas PreProfesionales. Si quieres ver las preguntas disponibles ingresa el comando /listar_preguntas",
    "¿Cuántas horas prácticas debo completar durante el curso?": "Debes completar un total de 192 horas prácticas, equivalentes a los 4 créditos asignados a la asignatura. Estas horas están distribuidas a lo largo del semestre según el cronograma establecido.",
    "¿Cómo se elige la organización donde se realizarán las prácticas?": "La elección de la organización debe realizarse en coordinación con tu tutor académico. Debes buscar una empresa que permita aplicar los conocimientos adquiridos en el ámbito de las Tecnologías de la Información. Y registrarlo en la siguiente plataforma: https://practicaspreprofesionales.utpl.edu.ec, aquí puedes proponer una plaza, buscar alguna plaza interna o externa que ofrece la UTPL mediante convenios.",
    "¿Cuáles son los pasos para registrar las actividades realizadas en la organización?": "1.	Realiza un registro diario o semanal de las actividades ejecutadas en la organización. 2.	Usa el formato proporcionado en el Entorno Virtual de Aprendizaje (EVA) para documentar tus actividades. 3.	Adjunta evidencias como fotografías, reportes, o documentación que respalde las tareas realizadas. 4. Envía el registro a través del EVA dentro de las fechas establecidas por el cronograma.",
    "¿Qué actividades técnicas puedo realizar como complemento académico en mi organización?": (
        "Las actividades complementarias deben estar acorde a sus actividades y el entorno de la organización. "
        "Posibles actividades que pueden realizarse como complemento académico:\n\n"
        "• Levantamiento de infraestructura tecnológica de la entidad.\n"
        "• Análisis de datos de las actividades realizadas hasta el momento.\n"
        "• Análisis de un proceso que se puede mejorar.\n"
        "• Diseño de una mejora de un proceso.\n"
        "• Análisis de una automatización requerida.\n"
        "• Diseño de una automatización requerida.\n"
        "• Validación de un diseño (proceso/automatización).\n"
        "• Preparación de propuesta requerida.\n"
        "• Diseño de página web.\n"
        "• Realizar la propuesta del desarrollo de la página web.\n"
        "• Levantamiento de necesidades de TI de la entidad (Nueva actividad sugerida)."),
        "¿Puedo realizar las prácticas en modalidad remota si la organización lo permite?": "Sí, es posible realizar las prácticas en modalidad remota, siempre y cuando la organización esté de acuerdo y puedas cumplir con los objetivos y actividades planificadas. Además, deberás asegurarte de registrar todas tus actividades y mantener comunicación constante con tu tutor académico y de la empresa.",
        "¿Debo firmar algún acuerdo o llevar alguna carta de solicitud en la organización para realizar las prácticas?": "Depende la empresa, en la mayoría de los casos deberás presentar una carta de solicitud de prácticas proporcionada por el tutor académico enviada por el correo electrónico para la empresa. El registro de convenio se lo hace mediante la plataforma de registro de prácticas.",
        "¿A quién acudir para manejar problemas éticos o conflictos en la organización durante las prácticas?": "Debes informar de inmediato a tu tutor académico sobre cualquier conflicto o problema ético que enfrentes en la organización. Él o ella te guiará sobre cómo proceder y, de ser necesario, se comunicará con los responsables de la organización para resolver la situación.",
        "¿Es posible reprogramar una actividad si no logro completarla a tiempo por razones justificadas?": "Sí, puedes reprogramar actividades si presentas una justificación válida, como problemas de salud o imprevistos laborales. Comunica la situación a tu tutor académico lo antes posible para que puedas coordinar una nueva fecha de entrega o ajustar tu cronograma.",
        "¿Cuánto tiempo tengo para conseguir una organización para realizar mis prácticas?": "Debes formalizar la selección de la organización durante lo más adecuado sería en las primeras tres semanas del curso, o lo más pronto posible porque se pueden generar atraso, problemas con el convenio, pero se debe solucionar lo más pronto posible para empezar las practicas y poder completar todas las horas requeridas. Esto incluye coordinar con tu tutor académico y realizar el registro de postulación de prácticas en la plataforma.",
        "¿Qué tipos de organizaciones son aptas para realizar las prácticas?": (
        "Son aptas las organizaciones que permitan aplicar los conocimientos de Tecnologías de la Información, como:\n\n"
        "•	Empresas públicas o privadas.\n"
        "•	Empresas Internacionales.\n"
        "•	Observatorios de Sociedad de la Información y Telecomunicaciones.\n"
        "•	Startups o emprendimientos tecnológicos.\n"
        "La organización debe ofrecer oportunidades para identificar problemas tecnológicos, aplicar métodos de análisis y proponer soluciones relacionadas con las TI."),

}


async def listar_preguntas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    lista_preguntas = "\n".join(f"- {pregunta}" for pregunta in PREGUNTAS_Y_RESPUESTAS.keys())
   
    await update.message.reply_text(f"Estas son las preguntas disponibles:\n\n{lista_preguntas}")


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text  
    respuesta = PREGUNTAS_Y_RESPUESTAS.get(mensaje, "Lo siento, no sé cómo responder esa pregunta.")
    await update.message.reply_text(respuesta)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot para estas Prácticas PreProfesionales. ¿Cómo puedo ayudarte?. Si quieres ver las preguntas disponibles ingresa el comando /listar_preguntas")


application = ApplicationBuilder().token("8124477977:AAF6ba2u9GjpJpT8U4GSjKdufvtxPKeA6D4").build()


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("listar_preguntas", listar_preguntas))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))


application.run_polling()
