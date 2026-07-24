# -*- coding: utf-8 -*-
"""FR — copie de l'original (sauf là où FR était langue originale)."""

SUBJ = {
0:"Demande d'accès aux documents — affaire M.10815",
1:"Accusé de réception — numéro de dossier 2025/6534",
2:"Réponse — je demande le contrat non caviardé",
3:"Votre demande d'accès aux documents — réf. EASE n° 2025/6534",
4:"Demande de prorogation du délai pour la demande confirmative — réf. EASE 2025/6534",
5:"La prorogation du délai de 15 jours ouvrables n'est pas possible",
6:"Demande confirmative — art. 7, par. 2, du règlement (CE) n° 1049/2001",
7:"Réception confirmée — transmis au Secrétariat général",
8:"Réexamen interne de la demande d'accès aux documents — Ares(2026)1214166",
9:"Clarification procédurale — demande confirmative déposée le 26 janvier 2026 (affaire M.10815)",
10:"Accusé de réception automatique — unité Transparence, Secrétariat général",
11:"Sites de tiers — veuillez utiliser le portail officiel",
12:"Position procédurale du demandeur — réception et traitement de la demande confirmative",
13:"Accusé de réception automatique — unité Transparence, Secrétariat général",
14:"Dépôt d'une plainte pénale — atteinte aux intérêts financiers de l'UE (art. 325 TFUE)",
15:"Document complémentaire",
16:"Réponse à la décision de refus d'accès aux documents — COMP/M.10815",
}

BADGE = {"Delivered":"Remis","Registered":"Enregistré","Refused":"Refusé",
         "Rejected as out of time":"Rejeté comme tardif","Forwarded":"Transmis",
         "Received":"Reçu","Rejected":"Rejeté"}

PHASES = {0:"Phase I — demande initiale", 3:"Phase II — refus initial",
          6:"Phase III — demande confirmative", 14:"Phase IV — escalade"}

BODY = {}

BODY[0] = """
<p>Madame, Monsieur (Direction générale de la concurrence),</p>
<p>en vertu du droit d'accès aux documents consacré par les traités de l'UE et développé par le règlement 1049/2001, je demande les documents contenant les informations suivantes :</p>
<p>en application du <strong>règlement (CE) n° 1049/2001</strong>, de l'<strong>article 15 TFUE</strong> et de l'<strong>article 42 de la charte des droits fondamentaux de l'Union européenne</strong>, je demande par la présente un accès complet à tous les documents de l'affaire <strong>M.10815 – Deutsche Telekom / Orange / Telefónica / Vodafone – Joint Venture</strong>.</p>
<p>Je demande en particulier l'accès :</p>
<ul>
<li>à l'accord d'entreprise commune complet (non caviardé),</li>
<li>à toutes les annexes et modifications de l'accord d'entreprise commune,</li>
<li>au pacte d'actionnaires,</li>
<li>aux règles de gouvernance et de fonctionnement de l'entreprise commune,</li>
<li>à la version complète et non caviardée de la décision de la Commission,</li>
<li>à la notification Form CO déposée par les parties,</li>
<li>à l'ensemble des analyses de marché et évaluations internes réalisées par la DG Concurrence,</li>
<li>à toute la correspondance échangée entre la DG Concurrence et les parties notifiantes au sujet de cette entreprise commune.</li>
</ul>
<p>Cette entreprise commune influençant fondamentalement le paysage concurrentiel du marché des télécommunications de l'UE et concernant des millions de citoyens de l'Union, j'estime que l'intérêt public à la transparence l'emporte clairement sur d'éventuelles allégations de confidentialité commerciale, conformément aux principes dégagés par la Cour de justice de l'Union européenne.</p>
<p>Veuillez agréer mes salutations distinguées,<br>Peter Ferenc<br>Rammelkam 2, 84036 Kumhausen, Allemagne</p>"""

BODY[1] = """
<p>Madame, Monsieur,</p>
<p>nous accusons par la présente réception de votre demande d'accès aux documents, envoyée le 10/12/2025 et enregistrée le 10/12/2025 sous le numéro de dossier <strong>2025/6534</strong>.</p>
<p>Nous traiterons votre demande dans un délai de <strong>15 jours ouvrables</strong> à compter de la date d'enregistrement. Le délai expire le <strong>12/01/2026</strong>. Nous vous informerons s'il devait être prorogé de 15 jours ouvrables supplémentaires.</p>
<p>Pour en savoir plus sur le traitement de vos données à caractère personnel, veuillez consulter la déclaration de confidentialité.</p>
<p>Veuillez agréer nos salutations distinguées,<br>Direction générale de la concurrence – Accès aux documents<br>Commission européenne</p>"""

BODY[2] = """
<p>Madame, Monsieur (Direction générale de la concurrence),</p>
<p>merci, j'attendrai votre réponse ! Je demande un contrat transparent et non caviardé !</p>
<p>Veuillez agréer mes salutations distinguées,<br>Peter Ferenc</p>"""

BODY[3] = """
<p>Monsieur Ferenc,</p>
<p><strong>Objet :</strong> Votre demande d'accès aux documents – réf. EASE n° 2025/6534</p>
<p>Nous nous référons à votre message du 10/12/2025 par lequel vous formulez une demande d'accès aux documents, enregistrée le 10/12/2025 sous la référence susmentionnée.</p>
<p>Vous trouverez ci-joint la copie numérisée de la réponse à votre demande d'accès aux documents, <strong>signée par la directrice générale</strong>.</p>
<p>Nous vous prions de bien vouloir répondre au présent courriel pour en accuser réception.</p>
<p>Veuillez agréer nos salutations distinguées,</p>
<p>Commission européenne<br>Direction générale de la concurrence<br>Unité C.5 Concentrations<br>Direction C – Marchés et affaires : technologies de l'information, communication et médias</p>"""

BODY[4] = """
<p>Madame, Monsieur,</p>
<p>je sollicite formellement par la présente une prorogation du délai pour déposer une demande confirmative relative à ma demande d'accès aux documents enregistrée sous la référence EASE 2025/6534.</p>
<p><strong>Motifs de la demande</strong></p>
<p>Pour des raisons techniques objectives, je ne dispose pas actuellement d'un accès fiable à l'ensemble des moyens techniques et des identifiants d'authentification nécessaires pour préparer et déposer une demande confirmative juridiquement motivée.</p>
<p>L'étendue et la complexité des motifs de refus exigent une analyse juridique et factuelle approfondie, notamment quant :</p>
<ul>
<li>à l'application des exceptions au droit d'accès aux documents,</li>
<li>à la proportionnalité des occultations opérées,</li>
<li>et à l'appréciation de la conformité au droit de l'Union.</li>
</ul>
<p>Déposer une demande confirmative sans une telle analyse serait purement formel et priverait de son sens même la voie de recours prévue par le droit de l'Union.</p>
<p><strong>Base juridique</strong></p>
<p>La présente demande se fonde notamment sur :</p>
<ul>
<li>l'article 41 de la charte des droits fondamentaux de l'Union européenne (droit à une bonne administration),</li>
<li>l'article 47 de la charte des droits fondamentaux de l'Union européenne (droit à un recours effectif),</li>
<li>le principe de l'égalité des armes et de l'exercice effectif des droits procéduraux,</li>
<li>et la jurisprudence constante selon laquelle les délais de procédure ne sauraient être appliqués d'une manière rendant pratiquement impossible ou excessivement difficile l'exercice des droits conférés par le droit de l'Union.</li>
</ul>
<p><strong>Demande</strong></p>
<p>Au vu de ce qui précède, je sollicite une prorogation de <strong>30 jours</strong>, calculée à compter de l'expiration du délai initial pour le dépôt de la demande confirmative.</p>
<p>La présente demande est présentée sans renonciation à aucun droit ni reconnaissance d'un quelconque retard, et aux seules fins d'assurer un exercice correct, éclairé et juridiquement effectif de mon droit de recours.</p>
<p>Je vous prie de bien vouloir me confirmer par écrit si la prorogation est accordée.</p>
<p>Veuillez agréer mes salutations distinguées,<br>Peter Ferenc</p>"""

BODY[5] = """
<p>Monsieur Ferenc,</p>
<p>nous vous remercions de votre courriel du 19 janvier 2026, dans lequel vous demandez s'il est possible de proroger le délai légal de 15 jours ouvrables prévu à l'article 7, paragraphe 2, du règlement 1049/2001 pour déposer une demande confirmative à la suite d'un refus partiel ou total d'une demande d'accès aux documents.</p>
<p>Nous vous informons qu'<strong>il n'est pas possible de proroger ce délai de 15 jours ouvrables</strong>, les délais fixés par le règlement 1049/2001 n'étant pas à la disposition des parties et étant déterminants pour la procédure d'accès aux documents détenus par les institutions.</p>
<p>Dans ce contexte, nous soulignons que <strong>le stade confirmatif constitue un réexamen administratif complet de la décision initiale et doit corriger toute omission de celle-ci, même lorsqu'elle n'est pas expressément contestée par le demandeur dans la demande confirmative</strong>.</p>
<p>Le délai pour déposer une demande confirmative contre la réponse négative initiale de la direction générale de la concurrence du 7 janvier 2026 à votre demande d'accès aux documents du 10 décembre 2025, enregistrée sous la référence EASE 2025/6534, <strong>n'ayant pas encore expiré</strong>, nous vous informons que nous ne traitons dès lors pas votre demande comme une telle demande confirmative au sens du règlement 1049/2001.</p>
<p>À cet égard, nous attirons à nouveau votre attention sur la section 5 de notre réponse négative initiale du 7 janvier 2026, dans laquelle nous avons exposé les voies de recours disponibles, le délai légal applicable ainsi que les modalités et le service de la Commission européenne auquel une telle demande confirmative doit, le cas échéant, être adressée.</p>
<p>Cordialement,</p>
<p>Commission européenne<br>Direction générale de la concurrence<br>Unité C.5 Concentrations<br>Direction C – Marchés et affaires : technologies de l'information, communication et médias</p>"""

BODY[6] = """
<p>Madame, Monsieur,</p>
<p>cette demande confirmative a déjà été déposée le <strong>26 janvier 2026</strong> via la plateforme AskTheEU. En raison d'une erreur technique, elle a été envoyée par la mauvaise interface et n'est pas parvenue à l'institution.</p>
<p>L'équipe AskTheEU / Access Info Europe a confirmé par écrit que le message avait été déposé dans les délais et peut en attester si nécessaire. Vous trouverez ci-dessous le lien vers le document confirmant que ma demande confirmative a été déposée en temps utile par un canal alternatif, en raison d'une erreur technique de la plateforme.</p>
<p>Je dépose par la présente une demande confirmative au titre de l'<strong>article 7, paragraphe 2, du règlement (CE) n° 1049/2001</strong> et sollicite un réexamen administratif complet de la réponse négative initiale du 7 janvier 2026 rendue par la direction générale de la concurrence sur ma demande d'accès aux documents du 10 décembre 2025, enregistrée sous la référence EASE 2025/6534.</p>
<p>Je maintiens respectueusement que la décision initiale restreint illégalement mon droit d'accès aux documents et méconnaît les principes de transparence, de proportionnalité et de bonne administration consacrés par le règlement 1049/2001 et l'article 15 TFUE.</p>
<p>En particulier :</p>
<p><strong>1. Application erronée ou excessivement large des exceptions</strong><br>
La réponse initiale s'appuie sur des exceptions dont il n'a pas été démontré qu'elles s'appliquent concrètement et individuellement aux documents demandés. La motivation fournie demeure abstraite et ne montre pas en quoi la divulgation porterait concrètement et effectivement atteinte à un intérêt protégé, comme l'exige la jurisprudence constante de la Cour de justice.</p>
<p><strong>2. Absence d'appréciation correcte de l'intérêt public supérieur</strong><br>
Les documents demandés concernent des questions d'intérêt public important, dont le fonctionnement de la mise en œuvre du droit de la concurrence, le respect du droit de l'Union et la protection des droits fondamentaux. La décision initiale ne procède à aucune appréciation réelle et motivée de l'existence d'un intérêt public supérieur à la divulgation.</p>
<p><strong>3. Motivation insuffisante et absence d'examen individuel</strong><br>
Le refus ne démontre pas que chaque document a été examiné individuellement et n'explique pas pourquoi un accès partiel n'a pu être accordé conformément à l'article 4, paragraphe 6, du règlement 1049/2001.</p>
<p><strong>4. Pertinence de la protection des données et de la conformité au RGPD</strong><br>
Dans la mesure où des considérations de protection des données ont été invoquées, je relève que le règlement (UE) 2018/1725 et le règlement (UE) 2016/679 (RGPD) ne justifient pas un refus global. Toute question relative aux données à caractère personnel peut et doit être réglée par une occultation appropriée plutôt que par un refus d'accès.</p>
<p>Comme vous le rappelez dans votre courrier du 20 janvier 2026, le stade confirmatif constitue un réexamen administratif complet de la décision initiale. J'invite dès lors la Commission à réexaminer la demande dans son intégralité et à remédier à toute omission ou erreur contenue dans la réponse initiale, y compris celles non expressément contestées ci-dessus.</p>
<p>Je demande respectueusement que la Commission accorde l'accès aux documents demandés, en totalité ou à tout le moins en partie, conformément au règlement 1049/2001.</p>
<p>Veuillez agréer mes salutations distinguées,<br>Peter Ferenc</p>"""

BODY[7] = """
<p>Monsieur Ferenc,</p>
<p>nous accusons réception de votre courriel du 30 janvier 2026, par lequel vous introduisez une demande de décision confirmative.</p>
<p>Nous vous informons que <strong>nous avons transmis votre courriel au Secrétariat général compétent de la Commission européenne</strong>.</p>
<p>Cordialement<br>COMP C-5</p>"""

BODY[8] = """
<p>Madame, Monsieur le demandeur,</p>
<p>je me réfère à votre courriel du 30 janvier 2026, par lequel vous introduisez une demande confirmative conformément à l'article 7, paragraphe 2, du règlement 1049/2001 relatif à l'accès du public aux documents du Parlement européen, du Conseil et de la Commission (ci-après « règlement 1049/2001 »).</p>
<p>J'ai le regret de vous informer que <strong>votre demande confirmative a été introduite en dehors du délai applicable</strong> défini à l'article 7, paragraphe 2, du règlement 1049/2001. Cet article prévoit qu'en cas de refus total ou partiel, le demandeur peut, dans un délai de 15 jours ouvrables à compter de la réception de la réponse de l'institution, présenter une demande confirmative tendant à ce que l'institution revoie sa position.</p>
<p><strong>Par conséquent, la Commission n'est pas en mesure de traiter votre demande.</strong></p>
<p>Veuillez agréer mes salutations distinguées,<br>Commission européenne<br>Équipe Accès aux documents</p>"""

BODY[9] = """
<p>Madame, Monsieur,</p>
<p>je dois m'opposer formellement à la position désormais soutenue dans cette affaire et demande que la réalité factuelle et procédurale soit fidèlement retranscrite.</p>
<p><strong>1. Dépôt en temps utile de la demande confirmative</strong><br>
Ma demande confirmative au titre de l'article 7, paragraphe 2, du règlement (CE) n° 1049/2001 a été <strong>intégralement rédigée et déposée le 26 janvier 2026</strong>, soit <strong>le dernier jour du délai légal</strong>, via la plateforme AskTheEU. Ce fait <strong>n'est pas contesté</strong> et a été <strong>expressément confirmé par écrit par Access Info Europe</strong>, preuve documentaire à l'appui (accusé de réception horodaté de mon message du 26 janvier 2026).</p>
<p><strong>2. Le défaut de transmission technique ne saurait être imputé au demandeur</strong><br>
Tout défaut de transmission de la demande confirmative à la Commission résulte exclusivement d'un problème technique et organisationnel du côté de la plateforme intermédiaire. Selon la jurisprudence constante et les principes généraux du droit de l'Union :</p>
<ul>
<li>un demandeur <strong>ne saurait être pénalisé</strong> pour les dysfonctionnements techniques d'une plateforme intermédiaire utilisée de bonne foi ;</li>
<li>les droits procéduraux conférés par le règlement 1049/2001 <strong>ne sauraient s'éteindre par un formalisme excessif</strong>.</li>
</ul>
<p><strong>3. Confiance légitime et acceptation procédurale</strong><br>
Il est déterminant que la demande confirmative ait été reçue, traitée en interne et transmise aux services compétents de la Commission. Ces actes constituent des <strong>étapes procédurales formelles</strong> qui ont <strong>implicitement reconnu la validité procédurale</strong> de la demande confirmative. Une telle acceptation procédurale étant intervenue, il est <strong>juridiquement inadmissible</strong> de la nier rétroactivement, ce qui violerait :</p>
<ul>
<li>le principe de bonne administration (article 41 de la charte),</li>
<li>la protection de la confiance légitime,</li>
<li>et l'effectivité du droit de l'Union.</li>
</ul>
<p><strong>4. Conséquences</strong><br>
Toute tentative de requalifier aujourd'hui en « tardive » une demande confirmative dûment déposée équivaudrait à un comportement administratif arbitraire, à un formalisme manifestement disproportionné et à une violation des articles 41 et 47 de la charte des droits fondamentaux. Un tel comportement serait <strong>contrôlable de manière autonome</strong> par le Médiateur européen et, si nécessaire, par les juridictions de l'Union.</p>
<p><strong>5. Demande</strong><br>
Je demande dès lors que :</p>
<ul>
<li>le dossier soit rectifié afin de refléter le dépôt en temps utile du 26 janvier 2026,</li>
<li>la demande confirmative soit traitée comme valablement introduite,</li>
<li>et que la Commission procède au réexamen administratif complet exigé par l'article 7, paragraphe 2, du règlement 1049/2001.</li>
</ul>
<p>Le présent message est présenté <strong>à toutes fins utiles et sans préjudice</strong> de tout autre recours dont je dispose en vertu du droit de l'Union.</p>
<p><strong>Clarification procédurale complémentaire</strong><br>
Pour lever tout doute, je confirme que la même demande confirmative a été transmise le <strong>7 février 2026</strong> également directement à la Commission européenne par des canaux officiels de courrier électronique, ainsi qu'au cabinet d'un membre de la Commission. Le contenu de la demande confirmative a donc été mis sans équivoque à la disposition de la Commission par plusieurs canaux officiels, ce qui démontre en outre ma bonne foi, ma coopération procédurale et ma volonté réelle d'exercer mes droits au titre du règlement (CE) n° 1049/2001 de manière correcte et diligente.</p>
<p>Veuillez agréer mes salutations distinguées,<br>Peter Ferenc<br>Réf. : TFIA-2026-JV-002</p>"""

BODY[10] = """
<p>L'unité « Transparence » du secrétariat général de la Commission européenne a bien reçu votre message.</p>
<p>Les demandes d'accès du public aux documents sont traitées sur la base du règlement (CE) n° 1049/2001 du 30 mai 2001 relatif à l'accès du public aux documents du Parlement européen, du Conseil et de la Commission.</p>
<p>Le secrétariat général répondra à votre demande dans un délai de <strong>15 jours ouvrables</strong> à compter de la date d'enregistrement de votre demande, et vous informera de cet enregistrement (ou vous indiquera toute information supplémentaire à fournir en vue de l'enregistrement et/ou du traitement de votre demande).</p>
<p><em>Le même texte figurait en anglais et en allemand.</em></p>"""

BODY[11] = """
<p>Madame, Monsieur le demandeur,</p>
<p><strong>La Commission européenne ne saurait être tenue pour responsable des problèmes liés aux sites internet de tiers.</strong> Nous vous invitons à utiliser le portail officiel pour demander des documents de la Commission européenne.</p>
<p>Cordialement,<br>Commission européenne<br>Équipe Accès aux documents</p>"""

BODY[12] = """
<p>Madame, Monsieur,</p>
<p>je prends acte de votre affirmation selon laquelle la Commission européenne ne saurait être tenue pour responsable du fonctionnement technique de sites de tiers tels que la plateforme AskTheEU. <strong>Je ne puis souscrire à cette affirmation.</strong></p>
<p>La plateforme AskTheEU est de longue date acceptée, utilisée et effectivement mise à profit par la Commission européenne comme outil standard d'exercice du droit public d'accès aux documents ; par son intermédiaire, la Commission :</p>
<ul>
<li>reçoit et traite régulièrement des demandes d'accès aux documents,</li>
<li>communique avec les demandeurs, et</li>
<li>traite systématiquement des écrits au titre du règlement (CE) n° 1049/2001.</li>
</ul>
<p>Dans ces conditions, AskTheEU ne saurait être regardée comme un tiers quelconque ou non autorisé dont l'usage se ferait aux risques et périls du demandeur.</p>
<p>Indépendamment de ce qui précède, je souligne que cette question n'est pas déterminante pour l'appréciation de la recevabilité procédurale de mon écrit. <strong>Ce qui est déterminant, c'est que la Commission européenne a reçu ma demande confirmative, en a accusé réception et en a entamé le traitement</strong>, ainsi que l'a expressément confirmé le message de l'unité Transparence du secrétariat général.</p>
<p>À compter du moment où la Commission a reçu l'écrit, l'a inscrit dans le cadre du règlement (CE) n° 1049/2001 et m'a informé qu'il serait traité dans le délai légal courant à compter de l'enregistrement, <strong>une relation procédurale formelle est née entre le demandeur et l'institution</strong>, dont la pleine responsabilité incombe exclusivement à la Commission européenne.</p>
<p>La question du canal par lequel l'écrit a été initialement transmis ne saurait affecter rétroactivement sa recevabilité procédurale, d'autant que la Commission elle-même a confirmé la réception et le début du traitement.</p>
<p>Dans ces conditions, il est juridiquement inadmissible de contester a posteriori le caractère tardif ou la recevabilité de la demande confirmative, ou de reporter sur le demandeur les conséquences d'arrangements techniques ou contractuels entre la Commission et un tiers.</p>
<p>Je demande dès lors que la Commission procède au réexamen administratif complet de la demande confirmative conformément à l'article 7, paragraphe 2, du règlement (CE) n° 1049/2001.</p>
<p>Veuillez agréer mes salutations distinguées,<br>Peter Ferenc</p>"""

BODY[13] = """
<p>L'unité « Transparence » du secrétariat général de la Commission européenne a bien reçu votre message.</p>
<p>Les demandes d'accès du public aux documents sont traitées sur la base du règlement (CE) n° 1049/2001 du 30 mai 2001 relatif à l'accès du public aux documents du Parlement européen, du Conseil et de la Commission.</p>
<p>Le secrétariat général répondra à votre demande dans un délai de 15 jours ouvrables à compter de l'enregistrement et vous informera de cet enregistrement.</p>
<p><em>Le même texte figurait en anglais et en allemand.</em></p>"""

BODY[14] = """
<p>Madame, Monsieur,</p>
<p>je vous transmets par la présente une plainte pénale sous forme de lien.</p>
<p>La plainte concerne des soupçons d'infractions pénales portant atteinte aux intérêts financiers de l'Union européenne, au sens de l'<strong>article 325 TFUE</strong> et de la <strong>directive (UE) 2017/1371 (PIF)</strong>.</p>
<p>La plainte pénale a été établie sous la forme d'un document PDF signé par une <strong>signature électronique qualifiée (QES)</strong>, laquelle, conformément à l'article 25, paragraphe 2, du règlement (UE) n° 910/2014 (eIDAS), produit les mêmes effets juridiques qu'une signature manuscrite.</p>
<p>La soumission est effectuée en langue slovaque, qui est une langue officielle de l'Union européenne. <strong>La version linguistique slovaque est considérée comme la version originale et juridiquement contraignante.</strong> Les versions EN → DE → FR → ES → PL → IT sont jointes exclusivement en tant que traductions miroir fidèles, afin de faciliter le traitement.</p>
<p>Je souligne expressément qu'<strong>aucune disposition du droit de l'Union n'impose le dépôt d'une plainte pénale via un formulaire en ligne spécifique</strong>. Conformément à l'article 24 du règlement (UE) 2017/1939, le Parquet européen peut recevoir des informations relatives à des infractions portant atteinte aux intérêts financiers de l'Union de toute source, y compris de personnes physiques.</p>
<p>Toute restriction technique ou procédurale qui :</p>
<ul>
<li>empêcherait la transmission de l'intégralité du contenu,</li>
<li>imposerait un raccourcissement ou entraînerait la perte d'allégations factuelles ou de preuves,</li>
<li>ou subordonnerait l'acceptation à une « évaluation préalable »,</li>
</ul>
<p>constituerait une entrave illégale à l'accès à la justice et une violation de l'article 47 de la charte des droits fondamentaux de l'UE et de l'article 13 de la CEDH.</p>
<p>J'attends en conséquence que la plainte pénale soit dûment enregistrée, examinée et traitée sur le fond, conformément au droit de l'Union, indépendamment du mode technique de transmission.</p>
<p>Veuillez agréer l'expression de ma considération distinguée,<br>Peter Ferenc<br>Kumhausen, le 11.02.2026</p>
<p><em>Le même texte a été transmis dans le même message également en EN, DE, ES, PL, IT et SK.</em></p>"""

BODY[15] = """
<p>Chère équipe AskTheEU,</p>
<p>[lien vers le document signé]</p>
<p>Veuillez agréer mes salutations distinguées,<br>Peter Ferenc</p>"""

BODY[16] = """
<p>Madame la Directrice générale, Monsieur Whelan,</p>
<p>je vous transmets ci-joint ma réponse à votre décision du 7 janvier 2026 par laquelle vous m'avez refusé l'accès aux documents du dossier dans l'affaire COMP/M.10815. Le document est revêtu d'une <strong>signature électronique qualifiée (QES)</strong> au titre de l'art. 25, par. 2, du règlement eIDAS (n° 910/2014) et équivaut juridiquement à une signature manuscrite.</p>
<p>L'accès aux documents des institutions ne relève pas du pouvoir discrétionnaire de la Commission. En vertu de l'<strong>art. 15, par. 3, TFUE</strong>, de l'<strong>art. 42 de la charte des droits fondamentaux de l'UE</strong> et de l'<strong>art. 2, par. 1, du règlement (CE) n° 1049/2001</strong>, tout citoyen de l'Union a un droit d'accès aux documents des institutions sans avoir à justifier d'un intérêt ni d'un motif. Le refus est l'exception ; selon la jurisprudence constante de la Cour, il est d'interprétation stricte et <strong>la charge de la preuve pèse sur l'institution, non sur le demandeur</strong>.</p>
<p>Dans ma réponse j'expose cinq motifs pour lesquels la décision ne saurait prospérer :</p>
<p><strong>1.</strong> Vous avez calculé le délai à compter de la date de la réponse, alors que l'art. 7, par. 2, du règlement le rattache à la réception. En outre : le 20 janvier 2026 vous m'avez indiqué par écrit que le délai n'avait pas encore expiré ; le 30 janvier l'unité COMP C-5 a accusé réception et transmis l'écrit au Secrétariat général ; le 3 février il a été rejeté comme tardif. <strong>Ces trois actes se contredisent.</strong></p>
<p><strong>2.</strong> Vous qualifiez vous-même de réfragable la présomption générale de non-divulgation, tout en me reprochant de ne pas avoir démontré le contraire — alors que vous me refusez jusqu'à l'inventaire du dossier. <strong>Une présomption qui ne peut être renversée n'est pas une présomption réfragable</strong> (Odile Jacob, C-404/10 P ; Agrofert, C-477/10 P).</p>
<p><strong>3.</strong> La présomption ne couvre ni les analyses de marché internes de la DG Concurrence ni la version non caviardée de la décision elle-même : ce sont des actes de l'institution, non des écrits des parties. Votre décision ne comporte aucun examen individuel de ces catégories.</p>
<p><strong>4.</strong> Vous n'avez pas apprécié l'accès partiel au titre de l'art. 4, par. 6 ; vous me renvoyez à des documents qui sont publics même sans votre décision.</p>
<p><strong>5.</strong> Vous avez écarté l'intérêt public supérieur comme relevant de considérations d'ordre général, alors que j'ai renvoyé aux <strong>points 138 à 142 de votre propre décision M.10815</strong>, dans lesquels la Commission indique elle-même qu'elle n'a pas examiné le respect du RGPD par les parties.</p>
<p>Je vous invite à traiter la demande au fond, à me communiquer l'inventaire du dossier et à examiner chaque document demandé de manière concrète et individuelle. Si la Commission ne répond pas au fond à la présente, je me réserve :</p>
<ul>
<li>une plainte auprès du <strong>Médiateur européen</strong> pour mauvaise administration ;</li>
<li>l'introduction d'un <strong>recours au titre de l'art. 263 TFUE</strong>.</li>
</ul>
<p>Cette réserve produit ses effets juridiques dès la réception de la présente lettre.</p>
<p>Veuillez agréer l'expression de ma haute considération,<br>Peter Ferenc</p>
<p><em>Le même texte a été transmis dans le même message également en allemand et en anglais.</em></p>"""
