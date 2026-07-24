# -*- coding: utf-8 -*-
"""ES — copia del original (salvo donde ES fue lengua original)."""

SUBJ = {
0:"Solicitud de acceso a documentos — asunto M.10815",
1:"Acuse de recibo — número de asunto 2025/6534",
2:"Respuesta — exijo el contrato sin censurar",
3:"Su solicitud de acceso a documentos — ref. EASE n.º 2025/6534",
4:"Solicitud de prórroga del plazo para presentar la solicitud confirmatoria — ref. EASE 2025/6534",
5:"No es posible prorrogar el plazo de 15 días hábiles",
6:"Solicitud confirmatoria — art. 7, apdo. 2, del Reglamento (CE) n.º 1049/2001",
7:"Recepción confirmada — remitido a la Secretaría General",
8:"Revisión interna de la solicitud de acceso a documentos — Ares(2026)1214166",
9:"Aclaración procedimental — solicitud confirmatoria presentada el 26 de enero de 2026 (asunto M.10815)",
10:"Acuse de recibo automático — Unidad de Transparencia, Secretaría General",
11:"Sitios web de terceros — utilice el portal oficial",
12:"Posición procedimental del solicitante — recepción y tramitación de la solicitud confirmatoria",
13:"Acuse de recibo automático — Unidad de Transparencia, Secretaría General",
14:"Presentación de denuncia penal — perjuicio a los intereses financieros de la UE (art. 325 TFUE)",
15:"Documento complementario",
16:"Respuesta a la decisión de denegación de acceso a documentos — COMP/M.10815",
}

BADGE = {"Delivered":"Entregado","Registered":"Registrado","Refused":"Denegado",
         "Rejected as out of time":"Rechazado por extemporáneo","Forwarded":"Remitido",
         "Received":"Recibido","Rejected":"Rechazado"}

PHASES = {0:"Fase I — solicitud inicial", 3:"Fase II — denegación inicial",
          6:"Fase III — solicitud confirmatoria", 14:"Fase IV — escalada"}

BODY = {}

BODY[0] = """
<p>Estimada Dirección General de Competencia,</p>
<p>en virtud del derecho de acceso a los documentos reconocido en los Tratados de la UE y desarrollado por el Reglamento 1049/2001, solicito los documentos que contienen la siguiente información:</p>
<p>con arreglo al <strong>Reglamento (CE) n.º 1049/2001</strong>, al <strong>artículo 15 TFUE</strong> y al <strong>artículo 42 de la Carta de los Derechos Fundamentales de la Unión Europea</strong>, solicito por la presente el acceso íntegro a todos los documentos del asunto <strong>M.10815 – Deutsche Telekom / Orange / Telefónica / Vodafone – Joint Venture</strong>.</p>
<p>En particular, solicito el acceso a:</p>
<ul>
<li>el acuerdo completo de empresa en participación (sin censurar),</li>
<li>todos los anexos y modificaciones del acuerdo de empresa en participación,</li>
<li>el acuerdo de accionistas,</li>
<li>las normas de gobernanza y funcionamiento de la empresa en participación,</li>
<li>la versión completa y no censurada de la decisión de la Comisión,</li>
<li>la notificación Form CO presentada por las partes,</li>
<li>todos los análisis de mercado y evaluaciones internas realizados por la DG Competencia,</li>
<li>toda la correspondencia intercambiada entre la DG Competencia y las partes notificantes relativa a esta empresa en participación.</li>
</ul>
<p>Dado que esta empresa en participación influye de manera fundamental en el panorama competitivo del mercado de telecomunicaciones de la UE y afecta a millones de ciudadanos de la Unión, considero que el interés público en la transparencia prevalece claramente sobre cualquier eventual alegación de confidencialidad comercial, conforme a los principios establecidos por el Tribunal de Justicia de la Unión Europea.</p>
<p>Atentamente,<br>Peter Ferenc<br>Rammelkam 2, 84036 Kumhausen, Alemania</p>"""

BODY[1] = """
<p>Estimados señores:</p>
<p>por la presente acusamos recibo de su solicitud de acceso a documentos, enviada el 10/12/2025 y registrada el 10/12/2025 con el número de asunto <strong>2025/6534</strong>.</p>
<p>Tramitaremos su solicitud en un plazo de <strong>15 días hábiles</strong> a partir de la fecha de registro. El plazo expira el <strong>12/01/2026</strong>. Le informaremos si fuera necesario prorrogarlo otros 15 días hábiles.</p>
<p>Para más información sobre el tratamiento de sus datos personales, consulte la declaración de privacidad.</p>
<p>Atentamente,<br>Dirección General de Competencia – Acceso a documentos<br>Comisión Europea</p>"""

BODY[2] = """
<p>Estimada Dirección General de Competencia,</p>
<p>gracias, esperaré su respuesta. Exijo un contrato transparente y sin censurar.</p>
<p>Atentamente,<br>Peter Ferenc</p>"""

BODY[3] = """
<p>Estimado Sr. Ferenc:</p>
<p><strong>Asunto:</strong> Su solicitud de acceso a documentos – ref. EASE n.º 2025/6534</p>
<p>Nos remitimos a su mensaje de 10/12/2025 por el que formula una solicitud de acceso a documentos, registrada el 10/12/2025 con la referencia arriba indicada.</p>
<p>Adjunto encontrará copia escaneada de la respuesta a su solicitud de acceso a documentos, <strong>firmada por la Directora General</strong>.</p>
<p>Le rogamos que responda al presente correo acusando recibo del mismo.</p>
<p>Atentamente,</p>
<p>Comisión Europea<br>Dirección General de Competencia<br>Unidad C.5 Concentraciones<br>Dirección C – Mercados y asuntos: tecnologías de la información, comunicación y medios</p>"""

BODY[4] = """
<p>Estimados señores:</p>
<p>por la presente solicito formalmente una prórroga del plazo para presentar una solicitud confirmatoria en relación con mi solicitud de acceso a documentos registrada con la referencia EASE 2025/6534.</p>
<p><strong>Motivos de la solicitud</strong></p>
<p>Por razones técnicas objetivas, actualmente no dispongo de acceso fiable a todos los medios técnicos y credenciales de autenticación necesarios para preparar y presentar una solicitud confirmatoria jurídicamente fundamentada.</p>
<p>El alcance y la complejidad de los motivos de denegación exigen un análisis jurídico y fáctico exhaustivo, en particular en cuanto a:</p>
<ul>
<li>la aplicación de las excepciones al derecho de acceso a los documentos,</li>
<li>la proporcionalidad de las supresiones practicadas,</li>
<li>y la evaluación de la conformidad con el Derecho de la Unión.</li>
</ul>
<p>Presentar una solicitud confirmatoria sin ese análisis sería meramente formal y desvirtuaría la finalidad misma del recurso previsto por el Derecho de la Unión.</p>
<p><strong>Fundamento jurídico</strong></p>
<p>Esta solicitud se basa, entre otros, en:</p>
<ul>
<li>el artículo 41 de la Carta de los Derechos Fundamentales de la Unión Europea (derecho a una buena administración),</li>
<li>el artículo 47 de la Carta de los Derechos Fundamentales de la Unión Europea (derecho a la tutela judicial efectiva),</li>
<li>el principio de igualdad de armas y de ejercicio efectivo de los derechos procesales,</li>
<li>y la jurisprudencia reiterada según la cual los plazos procesales no pueden aplicarse de modo que hagan prácticamente imposible o excesivamente difícil el ejercicio de los derechos conferidos por el Derecho de la Unión.</li>
</ul>
<p><strong>Petición</strong></p>
<p>Por lo expuesto, solicito una prórroga de <strong>30 días</strong>, contados desde el vencimiento del plazo original para presentar la solicitud confirmatoria.</p>
<p>Esta solicitud se presenta sin renuncia alguna de derechos ni reconocimiento de retraso, y con la única finalidad de garantizar un ejercicio adecuado, informado y jurídicamente efectivo de mi derecho al recurso.</p>
<p>Ruego confirmación por escrito de si se ha concedido la prórroga.</p>
<p>Atentamente,<br>Peter Ferenc</p>"""

BODY[5] = """
<p>Estimado Sr. Ferenc:</p>
<p>gracias por su correo de 19 de enero de 2026, en el que pregunta si es posible prorrogar el plazo legal de 15 días hábiles establecido en el artículo 7, apartado 2, del Reglamento 1049/2001 para presentar una solicitud confirmatoria frente a una denegación total o parcial de una solicitud de acceso a documentos.</p>
<p>Le informamos de que <strong>no es posible prorrogar este plazo de 15 días hábiles</strong>, ya que los plazos fijados en el Reglamento 1049/2001 no están a disposición de las partes y son determinantes para el procedimiento de acceso a los documentos en poder de las instituciones.</p>
<p>En este contexto, señalamos que <strong>la fase confirmatoria constituye una revisión administrativa completa de la decisión inicial y debe corregir cualquier omisión de esta, aun cuando el solicitante no la haya impugnado expresamente en la solicitud confirmatoria</strong>.</p>
<p>Dado que el plazo para presentar una solicitud confirmatoria frente a la respuesta negativa inicial de la Dirección General de Competencia de 7 de enero de 2026 a su solicitud de acceso a documentos de 10 de diciembre de 2025, registrada con la referencia EASE 2025/6534, <strong>aún no ha expirado</strong>, le comunicamos que, en consecuencia, no tratamos su consulta como tal solicitud confirmatoria en el sentido del Reglamento 1049/2001.</p>
<p>A este respecto, le remitimos de nuevo a la sección 5 de nuestra respuesta negativa inicial de 7 de enero de 2026, en la que explicamos las vías de recurso disponibles, el plazo legal aplicable y cómo y a qué servicio de la Comisión Europea debe presentarse, en su caso, dicha solicitud confirmatoria.</p>
<p>Un cordial saludo,</p>
<p>Comisión Europea<br>Dirección General de Competencia<br>Unidad C.5 Concentraciones<br>Dirección C – Mercados y asuntos: tecnologías de la información, comunicación y medios</p>"""

BODY[6] = """
<p>Estimados señores:</p>
<p>esta solicitud confirmatoria ya se presentó el <strong>26 de enero de 2026</strong> a través de la plataforma AskTheEU. Debido a un error técnico, se envió por la interfaz equivocada y no llegó a la institución.</p>
<p>El equipo de AskTheEU / Access Info Europe ha confirmado por escrito que el mensaje se presentó en plazo y puede acreditarlo si es necesario. A continuación figura el enlace al documento que confirma que mi solicitud confirmatoria se presentó en plazo por un canal alternativo, debido a un error técnico de la plataforma.</p>
<p>Por la presente presento una solicitud confirmatoria con arreglo al <strong>artículo 7, apartado 2, del Reglamento (CE) n.º 1049/2001</strong>, y solicito una revisión administrativa completa de la respuesta negativa inicial de 7 de enero de 2026 emitida por la Dirección General de Competencia respecto de mi solicitud de acceso a documentos de 10 de diciembre de 2025, registrada con la referencia EASE 2025/6534.</p>
<p>Mantengo respetuosamente que la decisión inicial restringe ilegalmente mi derecho de acceso a los documentos y no respeta los principios de transparencia, proporcionalidad y buena administración establecidos en el Reglamento 1049/2001 y en el artículo 15 TFUE.</p>
<p>En particular:</p>
<p><strong>1. Aplicación incorrecta o excesivamente amplia de las excepciones</strong><br>
La respuesta inicial se apoya en excepciones respecto de las cuales no se ha demostrado que se apliquen concreta e individualmente a los documentos solicitados. La motivación ofrecida sigue siendo abstracta y no muestra cómo la divulgación perjudicaría concreta y efectivamente un interés protegido, como exige la jurisprudencia reiterada del Tribunal de Justicia.</p>
<p><strong>2. Falta de evaluación adecuada del interés público superior</strong><br>
Los documentos solicitados se refieren a cuestiones de considerable interés público, incluido el funcionamiento de la aplicación del Derecho de la competencia, el cumplimiento del Derecho de la Unión y la protección de los derechos fundamentales. La decisión inicial no realiza una evaluación real y motivada de si existe un interés público superior en la divulgación.</p>
<p><strong>3. Motivación insuficiente y ausencia de examen individual</strong><br>
La denegación no demuestra que cada documento haya sido examinado individualmente, ni explica por qué no pudo concederse el acceso parcial conforme al artículo 4, apartado 6, del Reglamento 1049/2001.</p>
<p><strong>4. Relevancia de la protección de datos y del cumplimiento del RGPD</strong><br>
En la medida en que se invocaron consideraciones de protección de datos, señalo que el Reglamento (UE) 2018/1725 y el Reglamento (UE) 2016/679 (RGPD) no justifican una denegación global. Cualquier cuestión de datos personales puede y debe resolverse mediante la supresión adecuada y no mediante la denegación del acceso.</p>
<p>Como recuerdan en su comunicación de 20 de enero de 2026, la fase confirmatoria constituye una revisión administrativa completa de la decisión inicial. Invito, por tanto, a la Comisión a reexaminar la solicitud en su totalidad y a subsanar cualquier omisión o error contenido en la respuesta inicial, incluidos los no impugnados expresamente más arriba.</p>
<p>Solicito respetuosamente que la Comisión conceda el acceso a los documentos solicitados, íntegramente o al menos en parte, conforme al Reglamento 1049/2001.</p>
<p>Atentamente,<br>Peter Ferenc</p>"""

BODY[7] = """
<p>Estimado Sr. Ferenc:</p>
<p>acusamos recibo de su correo de 30 de enero de 2026, por el que presenta una solicitud de decisión confirmatoria.</p>
<p>Le informamos de que <strong>hemos remitido su correo a la Secretaría General competente de la Comisión Europea</strong>.</p>
<p>Un cordial saludo<br>COMP C-5</p>"""

BODY[8] = """
<p>Estimado solicitante:</p>
<p>me remito a su correo de 30 de enero de 2026, por el que presenta una solicitud confirmatoria con arreglo al artículo 7, apartado 2, del Reglamento 1049/2001 relativo al acceso del público a los documentos del Parlamento Europeo, del Consejo y de la Comisión (en lo sucesivo, «Reglamento 1049/2001»).</p>
<p>Lamento comunicarle que <strong>su solicitud confirmatoria se presentó fuera del plazo aplicable</strong> definido en el artículo 7, apartado 2, del Reglamento 1049/2001. Dicho artículo establece que, en caso de denegación total o parcial, el solicitante podrá presentar, en el plazo de 15 días hábiles a partir de la recepción de la respuesta de la institución, una solicitud confirmatoria instando a la institución a reconsiderar su posición.</p>
<p><strong>En consecuencia, la Comisión no está en condiciones de tramitar su solicitud.</strong></p>
<p>Atentamente,<br>Comisión Europea<br>Equipo de Acceso a Documentos</p>"""

BODY[9] = """
<p>Estimados señores:</p>
<p>debo oponerme formalmente a la posición que ahora se sostiene en este asunto y solicito que se refleje con exactitud la realidad fáctica y procedimental.</p>
<p><strong>1. Presentación en plazo de la solicitud confirmatoria</strong><br>
Mi solicitud confirmatoria conforme al artículo 7, apartado 2, del Reglamento (CE) n.º 1049/2001 fue <strong>redactada íntegramente y presentada el 26 de enero de 2026</strong>, esto es, <strong>el último día del plazo legal</strong>, a través de la plataforma AskTheEU. Este hecho <strong>no es controvertido</strong> y ha sido <strong>expresamente confirmado por escrito por Access Info Europe</strong>, incluida prueba documental (acuse de recibo con sello de tiempo de mi mensaje de 26 de enero de 2026).</p>
<p><strong>2. La falta de reenvío técnico no puede imputarse al solicitante</strong><br>
Cualquier fallo en el reenvío de la solicitud confirmatoria a la Comisión se debió exclusivamente a un problema técnico y organizativo del lado de la plataforma intermediaria. Conforme a la jurisprudencia reiterada y a los principios generales del Derecho de la Unión:</p>
<ul>
<li>el solicitante <strong>no puede ser penalizado</strong> por fallos técnicos de una plataforma intermediaria utilizada de buena fe;</li>
<li>los derechos procesales conferidos por el Reglamento 1049/2001 <strong>no pueden extinguirse por un formalismo excesivo</strong>.</li>
</ul>
<p><strong>3. Confianza legítima y aceptación procedimental</strong><br>
Es esencial que la solicitud confirmatoria fue recibida, tramitada internamente y remitida a los servicios competentes de la Comisión. Estos actos constituyen <strong>trámites formales</strong> que <strong>reconocieron implícitamente la validez procedimental</strong> de la solicitud confirmatoria. Producida tal aceptación procedimental, resulta <strong>jurídicamente inadmisible</strong> negarla retroactivamente, pues ello vulneraría:</p>
<ul>
<li>el principio de buena administración (artículo 41 de la Carta),</li>
<li>la protección de la confianza legítima,</li>
<li>y la efectividad del Derecho de la Unión.</li>
</ul>
<p><strong>4. Consecuencias</strong><br>
Todo intento de recalificar ahora como «extemporánea» una solicitud confirmatoria debidamente presentada equivaldría a una actuación administrativa arbitraria, a un formalismo manifiestamente desproporcionado y a una vulneración de los artículos 41 y 47 de la Carta de los Derechos Fundamentales. Tal conducta sería <strong>controlable de forma autónoma</strong> por el Defensor del Pueblo Europeo y, en su caso, por los órganos jurisdiccionales de la Unión.</p>
<p><strong>5. Petición</strong><br>
Solicito, por tanto, que:</p>
<ul>
<li>se rectifique el expediente para reflejar la presentación en plazo el 26 de enero de 2026,</li>
<li>se considere válidamente presentada la solicitud confirmatoria,</li>
<li>y la Comisión lleve a cabo la revisión administrativa completa exigida por el artículo 7, apartado 2, del Reglamento 1049/2001.</li>
</ul>
<p>El presente escrito se presenta <strong>a efectos de evitar dudas y sin perjuicio</strong> de cualesquiera otros recursos que me asistan conforme al Derecho de la Unión.</p>
<p><strong>Aclaración procedimental adicional</strong><br>
Para evitar cualquier duda, confirmo que la misma solicitud confirmatoria fue transmitida el <strong>7 de febrero de 2026</strong> también directamente a la Comisión Europea por canales oficiales de correo electrónico, así como al Gabinete de un miembro de la Comisión. El contenido de la solicitud confirmatoria quedó así puesto inequívocamente a disposición de la Comisión por múltiples canales oficiales, lo que acredita además mi buena fe, mi cooperación procedimental y mi voluntad real de ejercer mis derechos conforme al Reglamento (CE) n.º 1049/2001 de manera adecuada y diligente.</p>
<p>Atentamente,<br>Peter Ferenc<br>Ref.: TFIA-2026-JV-002</p>"""

BODY[10] = """
<p>Su mensaje ha sido recibido por la Unidad de Transparencia de la Secretaría General de la Comisión Europea.</p>
<p>Las solicitudes de acceso público a documentos se tramitan sobre la base del Reglamento (CE) n.º 1049/2001, de 30 de mayo de 2001, relativo al acceso del público a los documentos del Parlamento Europeo, del Consejo y de la Comisión.</p>
<p>La Secretaría General responderá a su solicitud en un plazo de <strong>15 días hábiles</strong> desde su registro y le informará debidamente del registro de la solicitud (o de la información adicional que deba aportarse para su registro o tramitación).</p>
<p><em>El mismo texto seguía en inglés, francés y alemán.</em></p>"""

BODY[11] = """
<p>Estimado solicitante:</p>
<p><strong>La Comisión Europea no puede ser considerada responsable de los problemas de sitios web de terceros.</strong> Le invitamos a utilizar el portal oficial para solicitar documentos de la Comisión Europea.</p>
<p>Un cordial saludo,<br>Comisión Europea<br>Equipo de Acceso a Documentos</p>"""

BODY[12] = """
<p>Estimados señores:</p>
<p>tomo nota de su afirmación según la cual la Comisión Europea no puede ser considerada responsable del funcionamiento técnico de sitios web de terceros como la plataforma AskTheEU. <strong>No puedo compartir esa afirmación.</strong></p>
<p>La plataforma AskTheEU ha sido durante mucho tiempo aceptada, utilizada y efectivamente empleada por la Comisión Europea como herramienta estándar para el ejercicio del derecho público de acceso a los documentos; a través de ella la Comisión:</p>
<ul>
<li>recibe y tramita periódicamente solicitudes de acceso a documentos,</li>
<li>se comunica con los solicitantes, y</li>
<li>procesa sistemáticamente escritos con arreglo al Reglamento (CE) n.º 1049/2001.</li>
</ul>
<p>En estas circunstancias, AskTheEU no puede considerarse un tercero aleatorio o no autorizado cuyo uso corriera por cuenta y riesgo del solicitante.</p>
<p>Con independencia de lo anterior, subrayo que esta cuestión no es determinante para apreciar la admisibilidad procedimental de mi escrito. <strong>Lo determinante es que la Comisión Europea recibió mi solicitud confirmatoria, acusó su recibo e inició su tramitación</strong>, como confirmó expresamente el mensaje de la Unidad de Transparencia de la Secretaría General.</p>
<p>Desde el momento en que la Comisión recibió el escrito, lo encuadró en el marco del Reglamento (CE) n.º 1049/2001 y me informó de que sería tramitado en el plazo legal desde su registro, <strong>surgió una relación procedimental formal entre el solicitante y la institución</strong>, cuya plena responsabilidad recae exclusivamente en la Comisión Europea.</p>
<p>La cuestión del canal por el que se transmitió inicialmente el escrito no puede afectar retroactivamente a su admisibilidad procedimental, máxime cuando la propia Comisión confirmó la recepción y el inicio de la tramitación.</p>
<p>En estas circunstancias, resulta jurídicamente inadmisible cuestionar a posteriori la temporaneidad o la admisibilidad de la solicitud confirmatoria, o trasladar al solicitante las consecuencias de acuerdos técnicos o contractuales entre la Comisión y un tercero.</p>
<p>Solicito, por tanto, que la Comisión lleve a cabo la revisión administrativa completa de la solicitud confirmatoria conforme al artículo 7, apartado 2, del Reglamento (CE) n.º 1049/2001.</p>
<p>Atentamente,<br>Peter Ferenc</p>"""

BODY[13] = """
<p>Su mensaje ha sido recibido por la Unidad de Transparencia de la Secretaría General de la Comisión Europea.</p>
<p>Las solicitudes de acceso público a documentos se tramitan sobre la base del Reglamento (CE) n.º 1049/2001, de 30 de mayo de 2001, relativo al acceso del público a los documentos del Parlamento Europeo, del Consejo y de la Comisión.</p>
<p>La Secretaría General responderá a su solicitud en un plazo de 15 días hábiles desde su registro y le informará debidamente del registro.</p>
<p><em>El mismo texto seguía en inglés, francés y alemán.</em></p>"""

BODY[14] = """
<p>Estimados señores:</p>
<p>por la presente les remito una denuncia penal mediante un enlace.</p>
<p>La denuncia se refiere a la sospecha de delitos que afectan a los intereses financieros de la Unión Europea, en el sentido del <strong>artículo 325 TFUE</strong> y de la <strong>Directiva (UE) 2017/1371 (PIF)</strong>.</p>
<p>La denuncia penal fue elaborada como documento PDF firmado con una <strong>firma electrónica cualificada (QES)</strong>, que, conforme al artículo 25, apartado 2, del Reglamento (UE) n.º 910/2014 (eIDAS), tiene los mismos efectos jurídicos que una firma manuscrita.</p>
<p>La presentación se realiza en lengua eslovaca, que es lengua oficial de la Unión Europea. <strong>La versión en lengua eslovaca se considera la versión original y jurídicamente vinculante.</strong> Las versiones EN → DE → FR → ES → PL → IT se adjuntan exclusivamente como traducciones espejo fieles, para facilitar su tramitación.</p>
<p>Señalo expresamente que <strong>ninguna norma del Derecho de la Unión exige que una denuncia penal se presente mediante un formulario en línea específico</strong>. De conformidad con el artículo 24 del Reglamento (UE) 2017/1939, la Fiscalía Europea puede recibir información sobre delitos que afecten a los intereses financieros de la Unión de cualquier fuente, incluidas personas físicas.</p>
<p>Cualquier restricción técnica o procedimental que:</p>
<ul>
<li>impida la presentación del contenido íntegro,</li>
<li>obligue a su reducción o provoque la pérdida de hechos o pruebas,</li>
<li>o condicione su aceptación a una «evaluación previa»,</li>
</ul>
<p>constituiría una barrera ilegal al acceso a la justicia y una vulneración del artículo 47 de la Carta de los Derechos Fundamentales de la UE y del artículo 13 del CEDH.</p>
<p>Por ello, espero que la denuncia penal sea debidamente registrada, examinada y tramitada en cuanto al fondo, con arreglo al Derecho de la Unión, con independencia del medio técnico utilizado para su transmisión.</p>
<p>Atentamente,<br>Kumhausen, 11.02.2026<br>Peter Ferenc</p>
<p><em>El mismo texto se transmitió en el mismo mensaje también en EN, DE, FR, PL, IT y SK.</em></p>"""

BODY[15] = """
<p>Estimado equipo de AskTheEU:</p>
<p>[enlace al documento firmado]</p>
<p>Atentamente,<br>Peter Ferenc</p>"""

BODY[16] = """
<p>Estimada Sra. Directora General, estimado Sr. Whelan:</p>
<p>adjunto les remito mi respuesta a su decisión de 7 de enero de 2026, por la que me denegaron el acceso a los documentos del expediente del asunto COMP/M.10815. El documento lleva una <strong>firma electrónica cualificada (QES)</strong> conforme al art. 25, apdo. 2, del Reglamento eIDAS (n.º 910/2014) y equivale jurídicamente a una firma manuscrita.</p>
<p>El acceso a los documentos de las instituciones no es una cuestión de discrecionalidad de la Comisión. Conforme al <strong>art. 15, apdo. 3, TFUE</strong>, al <strong>art. 42 de la Carta de los Derechos Fundamentales de la UE</strong> y al <strong>art. 2, apdo. 1, del Reglamento (CE) n.º 1049/2001</strong>, todo ciudadano de la Unión tiene derecho de acceso a los documentos de las instituciones sin necesidad de alegar interés o motivo. La denegación es la excepción; conforme a la jurisprudencia reiterada del Tribunal de Justicia debe interpretarse restrictivamente, y <strong>la carga de la prueba recae en la institución, no en el solicitante</strong>.</p>
<p>En mi respuesta expongo cinco razones por las que la decisión no puede sostenerse:</p>
<p><strong>1.</strong> Calcularon el plazo desde la fecha de la respuesta, aunque el art. 7, apdo. 2, del Reglamento lo vincula a la recepción. Además: el 20 de enero de 2026 me comunicaron por escrito que el plazo aún no había expirado; el 30 de enero la unidad COMP C-5 acusó recibo y remitió el escrito a la Secretaría General; el 3 de febrero fue rechazado por extemporáneo. <strong>Esos tres actos se contradicen entre sí.</strong></p>
<p><strong>2.</strong> Ustedes mismos califican de iuris tantum la presunción general de no divulgación, pero al mismo tiempo me reprochan no haber demostrado lo contrario, negándome incluso el inventario del expediente. <strong>Una presunción que no puede destruirse no es una presunción iuris tantum</strong> (Odile Jacob, C-404/10 P; Agrofert, C-477/10 P).</p>
<p><strong>3.</strong> La presunción no abarca ni los análisis de mercado internos de la DG Competencia ni la versión no censurada de la propia decisión: son actos de la institución, no escritos de las partes. Su decisión no contiene examen individual de esas categorías.</p>
<p><strong>4.</strong> No evaluaron el acceso parcial conforme al art. 4, apdo. 6; me remiten a documentos que son públicos incluso sin su decisión.</p>
<p><strong>5.</strong> Descartaron el interés público superior como consideraciones de carácter general, pese a que me referí a los <strong>considerandos 138 a 142 de su propia decisión M.10815</strong>, en los que la Comisión afirma que no evaluó el cumplimiento del RGPD por las partes.</p>
<p>Les insto a tramitar la solicitud sobre el fondo, a facilitarme el inventario del expediente y a examinar cada documento solicitado de manera concreta e individual. Si la Comisión no responde sobre el fondo a esta respuesta, me reservo:</p>
<ul>
<li>una reclamación ante el <strong>Defensor del Pueblo Europeo</strong> por mala administración;</li>
<li>la interposición de un <strong>recurso conforme al art. 263 TFUE</strong>.</li>
</ul>
<p>Esta reserva produce efectos jurídicos desde la recepción del presente escrito.</p>
<p>Respetuosamente,<br>Peter Ferenc</p>
<p><em>El mismo texto se transmitió en el mismo mensaje también en alemán e inglés.</em></p>"""
