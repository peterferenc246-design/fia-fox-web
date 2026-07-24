# -*- coding: utf-8 -*-
"""SV — kopia av originalet."""

SUBJ = {
0:"Ansökan om tillgång till handlingar — ärende M.10815",
1:"Mottagningsbekräftelse — ärendenummer 2025/6534",
2:"Svar — jag begär det omaskerade avtalet",
3:"Er ansökan om tillgång till handlingar — ref. EASE nr 2025/6534",
4:"Begäran om förlängning av fristen för den bekräftande ansökan — ref. EASE 2025/6534",
5:"Fristen på 15 arbetsdagar kan inte förlängas",
6:"Bekräftande ansökan — art. 7.2 i förordning (EG) nr 1049/2001",
7:"Mottagande bekräftat — vidarebefordrat till generalsekretariatet",
8:"Intern omprövning av ansökan om tillgång till handlingar — Ares(2026)1214166",
9:"Processuellt klargörande — bekräftande ansökan inlämnad den 26 januari 2026 (ärende M.10815)",
10:"Automatisk mottagningsbekräftelse — enheten för öppenhet, generalsekretariatet",
11:"Tredje parters webbplatser — använd den officiella portalen",
12:"Sökandens processuella ståndpunkt — mottagande och handläggning av den bekräftande ansökan",
13:"Automatisk mottagningsbekräftelse — enheten för öppenhet, generalsekretariatet",
14:"Inlämnande av brottsanmälan — skada på EU:s ekonomiska intressen (art. 325 FEUF)",
15:"Kompletterande handling",
16:"Svar på beslutet att neka tillgång till handlingar — COMP/M.10815",
}

BADGE = {"Delivered":"Levererat","Registered":"Registrerat","Refused":"Avslag",
         "Rejected as out of time":"Avvisad som för sent inkommen","Forwarded":"Vidarebefordrat",
         "Received":"Mottaget","Rejected":"Avvisad"}

PHASES = {0:"Fas I — ursprunglig ansökan", 3:"Fas II — ursprungligt avslag",
          6:"Fas III — bekräftande ansökan", 14:"Fas IV — eskalering"}

BODY = {}

BODY[0] = """
<p>Till generaldirektoratet för konkurrens,</p>
<p>med stöd av rätten till tillgång till handlingar enligt EU:s fördrag, utvecklad genom förordning 1049/2001, begär jag handlingar som innehåller följande uppgifter:</p>
<p>enligt <strong>förordning (EG) nr 1049/2001</strong>, <strong>artikel 15 FEUF</strong> och <strong>artikel 42 i Europeiska unionens stadga om de grundläggande rättigheterna</strong> begär jag härmed fullständig tillgång till samtliga handlingar i ärendet <strong>M.10815 – Deutsche Telekom / Orange / Telefónica / Vodafone – Joint Venture</strong>.</p>
<p>Jag begär särskilt tillgång till:</p>
<ul>
<li>det fullständiga avtalet om det gemensamma företaget (omaskerat),</li>
<li>samtliga bilagor och ändringar till avtalet om det gemensamma företaget,</li>
<li>aktieägaravtalet,</li>
<li>reglerna för styrning och drift av det gemensamma företaget,</li>
<li>den fullständiga och omaskerade versionen av kommissionens beslut,</li>
<li>den anmälan (Form CO) som parterna lämnat in,</li>
<li>samtliga marknadsanalyser och interna bedömningar som utförts av GD Konkurrens,</li>
<li>all korrespondens mellan GD Konkurrens och de anmälande parterna avseende detta gemensamma företag.</li>
</ul>
<p>Eftersom detta gemensamma företag i grunden påverkar konkurrensförhållandena på EU:s telekommarknad och berör miljontals unionsmedborgare anser jag att allmänintresset av öppenhet klart väger tyngre än eventuella påståenden om affärshemligheter, i linje med de principer som Europeiska unionens domstol har fastställt.</p>
<p>Med vänlig hälsning,<br>Peter Ferenc<br>Rammelkam 2, 84036 Kumhausen, Tyskland</p>"""

BODY[1] = """
<p>Bästa mottagare,</p>
<p>vi bekräftar härmed mottagandet av er ansökan om tillgång till handlingar, skickad den 10.12.2025 och registrerad den 10.12.2025 under ärendenummer <strong>2025/6534</strong>.</p>
<p>Vi handlägger er ansökan inom <strong>15 arbetsdagar</strong> från registreringsdagen. Fristen löper ut den <strong>12.01.2026</strong>. Vi meddelar er om den behöver förlängas med ytterligare 15 arbetsdagar.</p>
<p>Mer information om hur vi behandlar era personuppgifter finns i integritetsmeddelandet.</p>
<p>Med vänlig hälsning,<br>Generaldirektoratet för konkurrens – Tillgång till handlingar<br>Europeiska kommissionen</p>"""

BODY[2] = """
<p>Till generaldirektoratet för konkurrens,</p>
<p>tack, jag inväntar ert svar! Jag begär ett omaskerat och transparent avtal!</p>
<p>Med vänlig hälsning,<br>Peter Ferenc</p>"""

BODY[3] = """
<p>Bäste herr Ferenc,</p>
<p><strong>Ärende:</strong> Er ansökan om tillgång till handlingar – ref. EASE nr 2025/6534</p>
<p>Vi hänvisar till ert meddelande av den 10.12.2025 med en ansökan om tillgång till handlingar, registrerad den 10.12.2025 under ovan angivna referensnummer.</p>
<p>Bifogat finner ni en inskannad kopia av svaret på er ansökan om tillgång till handlingar, <strong>undertecknat av generaldirektören</strong>.</p>
<p>Vi ber er svara på detta e-postmeddelande och bekräfta mottagandet.</p>
<p>Med vänlig hälsning,</p>
<p>Europeiska kommissionen<br>Generaldirektoratet för konkurrens<br>Enhet C.5 Koncentrationer<br>Direktorat C – Marknader och ärenden: informationsteknik, kommunikation och medier</p>"""

BODY[4] = """
<p>Bästa mottagare,</p>
<p>jag begär härmed formellt en förlängning av fristen för att lämna in en bekräftande ansökan i fråga om min ansökan om tillgång till handlingar, registrerad under referensen EASE 2025/6534.</p>
<p><strong>Skäl för begäran</strong></p>
<p>Av objektiva tekniska skäl har jag för närvarande inte tillförlitlig tillgång till alla tekniska hjälpmedel och autentiseringsuppgifter som krävs för att förbereda och lämna in en rättsligt underbyggd bekräftande ansökan.</p>
<p>Avslagsskälens omfattning och komplexitet kräver en grundlig rättslig och faktisk analys, särskilt i fråga om:</p>
<ul>
<li>tillämpningen av undantagen från rätten till tillgång till handlingar,</li>
<li>proportionaliteten i de maskeringar som gjorts,</li>
<li>och bedömningen av förenligheten med unionsrätten.</li>
</ul>
<p>Att lämna in en bekräftande ansökan utan en sådan analys vore rent formellt och skulle undergräva själva syftet med det rättsmedel som unionsrätten föreskriver.</p>
<p><strong>Rättslig grund</strong></p>
<p>Denna begäran grundar sig bland annat på:</p>
<ul>
<li>artikel 41 i Europeiska unionens stadga om de grundläggande rättigheterna (rätten till god förvaltning),</li>
<li>artikel 47 i Europeiska unionens stadga om de grundläggande rättigheterna (rätten till ett effektivt rättsmedel),</li>
<li>principen om parternas likställdhet och om ett effektivt utövande av processuella rättigheter,</li>
<li>samt fast rättspraxis enligt vilken processuella frister inte får tillämpas på ett sätt som gör utövandet av de rättigheter som unionsrätten ger praktiskt taget omöjligt eller orimligt svårt.</li>
</ul>
<p><strong>Yrkande</strong></p>
<p>Mot bakgrund av det ovanstående begär jag en förlängning med <strong>30 dagar</strong>, räknat från utgången av den ursprungliga fristen för att lämna in den bekräftande ansökan.</p>
<p>Denna begäran framställs utan avstående från några rättigheter och utan erkännande av dröjsmål, och uteslutande för att säkerställa ett korrekt, informerat och rättsligt verksamt utövande av min rätt till rättsmedel.</p>
<p>Jag ber vänligen om skriftlig bekräftelse på om förlängningen har beviljats.</p>
<p>Med vänlig hälsning,<br>Peter Ferenc</p>"""

BODY[5] = """
<p>Bäste herr Ferenc,</p>
<p>tack för ert e-postmeddelande av den 19 januari 2026, i vilket ni frågar om det är möjligt att förlänga den lagstadgade fristen på 15 arbetsdagar enligt artikel 7.2 i förordning 1049/2001 för att lämna in en bekräftande ansökan efter ett helt eller delvis avslag på en ansökan om tillgång till handlingar.</p>
<p>Vi meddelar att <strong>det inte är möjligt att förlänga denna frist på 15 arbetsdagar</strong>, eftersom de frister som fastställs i förordning 1049/2001 inte står till parternas förfogande och är avgörande för förfarandet för tillgång till institutionernas handlingar.</p>
<p>I detta sammanhang vill vi påpeka att <strong>det bekräftande skedet utgör en fullständig administrativ omprövning av det ursprungliga beslutet och måste rätta varje brist i detta, även när sökanden inte uttryckligen har bestritt den i den bekräftande ansökan</strong>.</p>
<p>Eftersom fristen för att lämna in en bekräftande ansökan mot generaldirektoratet för konkurrens ursprungliga avslag av den 7 januari 2026 på er ansökan om tillgång till handlingar av den 10 december 2025, registrerad under referensen EASE 2025/6534, <strong>ännu inte har löpt ut</strong>, meddelar vi att vi följaktligen inte behandlar er förfrågan som en sådan bekräftande ansökan i den mening som avses i förordning 1049/2001.</p>
<p>Vi hänvisar i detta avseende på nytt till avsnitt 5 i vårt ursprungliga avslag av den 7 januari 2026, där vi redogjorde för tillgängliga rättsmedel, den tillämpliga lagstadgade fristen samt hur och till vilken enhet vid Europeiska kommissionen en sådan bekräftande ansökan i förekommande fall ska lämnas in.</p>
<p>Vänliga hälsningar,</p>
<p>Europeiska kommissionen<br>Generaldirektoratet för konkurrens<br>Enhet C.5 Koncentrationer<br>Direktorat C – Marknader och ärenden: informationsteknik, kommunikation och medier</p>"""

BODY[6] = """
<p>Bästa mottagare,</p>
<p>denna bekräftande ansökan lämnades redan in den <strong>26 januari 2026</strong> via plattformen AskTheEU. På grund av ett tekniskt fel skickades den via fel gränssnitt och nådde inte institutionen.</p>
<p>Teamet vid AskTheEU / Access Info Europe har skriftligen bekräftat att meddelandet lämnades in i tid och kan intyga detta vid behov. Nedan finns länken till den handling som bekräftar att min bekräftande ansökan lämnades in i tid via en alternativ kanal, till följd av ett tekniskt fel i plattformen.</p>
<p>Jag lämnar härmed in en bekräftande ansökan enligt <strong>artikel 7.2 i förordning (EG) nr 1049/2001</strong> och begär en fullständig administrativ omprövning av det ursprungliga avslaget av den 7 januari 2026 från generaldirektoratet för konkurrens på min ansökan om tillgång till handlingar av den 10 december 2025, registrerad under referensen EASE 2025/6534.</p>
<p>Jag vidhåller att det ursprungliga beslutet olagligen inskränker min rätt till tillgång till handlingar och inte uppfyller principerna om öppenhet, proportionalitet och god förvaltning i förordning 1049/2001 och artikel 15 FEUF.</p>
<p>Särskilt:</p>
<p><strong>1. Felaktig eller alltför vid tillämpning av undantagen</strong><br>
Det ursprungliga svaret stöder sig på undantag som inte har visats vara tillämpliga konkret och individuellt på de begärda handlingarna. Den lämnade motiveringen förblir abstrakt och visar inte hur ett utlämnande konkret och faktiskt skulle skada ett skyddat intresse, såsom domstolens fasta rättspraxis kräver.</p>
<p><strong>2. Utebliven prövning av ett övervägande allmänintresse</strong><br>
De begärda handlingarna rör frågor av betydande allmänintresse, bland annat konkurrensrättens genomförande, efterlevnaden av unionsrätten och skyddet av de grundläggande rättigheterna. Det ursprungliga beslutet innehåller ingen verklig och motiverad bedömning av om det finns ett övervägande allmänintresse av utlämnande.</p>
<p><strong>3. Otillräcklig motivering och avsaknad av individuell prövning</strong><br>
Avslaget visar inte att varje handling har prövats individuellt och förklarar inte varför delvis tillgång inte kunde beviljas enligt artikel 4.6 i förordning 1049/2001.</p>
<p><strong>4. Betydelsen av dataskydd och efterlevnad av dataskyddsförordningen</strong><br>
I den mån dataskyddsöverväganden åberopats noterar jag att förordning (EU) 2018/1725 och förordning (EU) 2016/679 (dataskyddsförordningen) inte motiverar ett generellt avslag. Frågor om personuppgifter kan och ska lösas genom lämplig maskering i stället för genom nekad tillgång.</p>
<p>Som ni erinrar om i er skrivelse av den 20 januari 2026 utgör det bekräftande skedet en fullständig administrativ omprövning av det ursprungliga beslutet. Jag uppmanar därför kommissionen att ompröva ansökan i sin helhet och att avhjälpa alla brister eller fel i det ursprungliga svaret, inbegripet sådana som inte uttryckligen bestritts ovan.</p>
<p>Jag begär att kommissionen beviljar tillgång till de begärda handlingarna, helt eller åtminstone delvis, enligt förordning 1049/2001.</p>
<p>Med vänlig hälsning,<br>Peter Ferenc</p>"""

BODY[7] = """
<p>Bäste herr Ferenc,</p>
<p>vi bekräftar härmed mottagandet av ert e-postmeddelande av den 30 januari 2026, genom vilket ni lämnar in en begäran om bekräftande beslut.</p>
<p>Vi meddelar att <strong>vi har vidarebefordrat ert meddelande till det behöriga generalsekretariatet vid Europeiska kommissionen</strong>.</p>
<p>Vänliga hälsningar<br>COMP C-5</p>"""

BODY[8] = """
<p>Bäste sökande,</p>
<p>jag hänvisar till ert e-postmeddelande av den 30 januari 2026, genom vilket ni lämnar in en bekräftande ansökan enligt artikel 7.2 i förordning 1049/2001 om allmänhetens tillgång till Europaparlamentets, rådets och kommissionens handlingar (nedan kallad förordning 1049/2001).</p>
<p>Jag beklagar att behöva meddela att <strong>er bekräftande ansökan lämnades in efter utgången av den tillämpliga fristen</strong> i artikel 7.2 i förordning 1049/2001. Enligt den artikeln får sökanden vid helt eller delvis avslag inom 15 arbetsdagar från mottagandet av institutionens svar lämna in en bekräftande ansökan om att institutionen ska ompröva sin ståndpunkt.</p>
<p><strong>Kommissionen har följaktligen inte möjlighet att handlägga er ansökan.</strong></p>
<p>Med vänlig hälsning,<br>Europeiska kommissionen<br>Teamet för tillgång till handlingar</p>"""

BODY[9] = """
<p>Bästa mottagare,</p>
<p>jag måste formellt invända mot den ståndpunkt som nu framförs i ärendet och begär att de faktiska och processuella omständigheterna återges korrekt.</p>
<p><strong>1. Bekräftande ansökan inlämnad i tid</strong><br>
Min bekräftande ansökan enligt artikel 7.2 i förordning (EG) nr 1049/2001 var <strong>fullständigt utformad och inlämnad den 26 januari 2026</strong>, det vill säga <strong>den sista dagen av den lagstadgade fristen</strong>, via plattformen AskTheEU. Detta förhållande <strong>är inte bestritt</strong> och har <strong>uttryckligen bekräftats skriftligen av Access Info Europe</strong>, inklusive skriftlig bevisning (tidsstämplad kvittens på mitt meddelande av den 26 januari 2026).</p>
<p><strong>2. Utebliven teknisk vidarebefordran kan inte tillskrivas sökanden</strong><br>
Varje utebliven vidarebefordran av den bekräftande ansökan till kommissionen berodde uteslutande på ett tekniskt och organisatoriskt problem hos den förmedlande plattformen. Enligt fast rättspraxis och unionsrättens allmänna principer gäller att:</p>
<ul>
<li>en sökande <strong>inte får bestraffas</strong> för tekniska fel hos en förmedlande plattform som använts i god tro,</li>
<li>processuella rättigheter enligt förordning 1049/2001 <strong>inte får utsläckas genom överdriven formalism</strong>.</li>
</ul>
<p><strong>3. Berättigade förväntningar och processuellt godtagande</strong><br>
Avgörande är att den bekräftande ansökan mottogs, handlades internt och vidarebefordrades till kommissionens behöriga enheter. Dessa åtgärder utgör <strong>formella processuella steg</strong> som <strong>underförstått erkände den bekräftande ansökans processuella giltighet</strong>. När ett sådant processuellt godtagande väl har skett är det <strong>rättsligt otillåtet</strong> att retroaktivt förneka det, eftersom det skulle strida mot:</p>
<ul>
<li>principen om god förvaltning (artikel 41 i stadgan),</li>
<li>skyddet för berättigade förväntningar,</li>
<li>och unionsrättens effektivitet.</li>
</ul>
<p><strong>4. Följder</strong><br>
Varje försök att nu omkvalificera en korrekt inlämnad bekräftande ansökan till "för sent inkommen" skulle utgöra godtyckligt förvaltningshandlande, uppenbart oproportionerlig formalism och en kränkning av artiklarna 41 och 47 i stadgan om de grundläggande rättigheterna. Ett sådant agerande skulle vara <strong>självständigt prövbart</strong> av Europeiska ombudsmannen och vid behov av unionsdomstolarna.</p>
<p><strong>5. Yrkande</strong><br>
Jag yrkar därför att:</p>
<ul>
<li>akten rättas så att den återspeglar den inlämning i tid som skedde den 26 januari 2026,</li>
<li>den bekräftande ansökan behandlas som giltigt inlämnad,</li>
<li>och att kommissionen genomför den fullständiga administrativa omprövning som krävs enligt artikel 7.2 i förordning 1049/2001.</li>
</ul>
<p>Detta meddelande lämnas <strong>för undvikande av tvivel och utan att det påverkar</strong> övriga rättsmedel som står mig till buds enligt unionsrätten.</p>
<p><strong>Ytterligare processuellt klargörande</strong><br>
För undvikande av varje tvivel bekräftar jag att samma bekräftande ansökan den <strong>7 februari 2026</strong> även översändes direkt till Europeiska kommissionen via officiella e-postkanaler samt till kabinettet för en kommissionsledamot. Innehållet i den bekräftande ansökan gjordes därmed otvetydigt tillgängligt för kommissionen genom flera officiella kanaler, vilket ytterligare visar min goda tro, mitt processuella samarbete och min verkliga avsikt att utöva mina rättigheter enligt förordning (EG) nr 1049/2001 på ett korrekt och omsorgsfullt sätt.</p>
<p>Med vänlig hälsning,<br>Peter Ferenc<br>Ref.: TFIA-2026-JV-002</p>"""

BODY[10] = """
<p>Ert meddelande har mottagits av enheten för öppenhet vid Europeiska kommissionens generalsekretariat.</p>
<p>Ansökningar om allmänhetens tillgång till handlingar behandlas på grundval av förordning (EG) nr 1049/2001 av den 30 maj 2001 om allmänhetens tillgång till Europaparlamentets, rådets och kommissionens handlingar.</p>
<p>Generalsekretariatet besvarar er ansökan inom <strong>15 arbetsdagar</strong> från registreringen och underrättar er vederbörligen om registreringen av ansökan (eller om ytterligare uppgifter som ska lämnas för registrering och/eller handläggning).</p>
<p><em>Samma text följde på engelska, franska och tyska.</em></p>"""

BODY[11] = """
<p>Bäste sökande,</p>
<p><strong>Europeiska kommissionen kan inte hållas ansvarig för problem med tredje parters webbplatser.</strong> Vi uppmanar er att använda den officiella portalen för att begära handlingar från Europeiska kommissionen.</p>
<p>Vänliga hälsningar,<br>Europeiska kommissionen<br>Teamet för tillgång till handlingar</p>"""

BODY[12] = """
<p>Bästa mottagare,</p>
<p>jag noterar ert påstående om att Europeiska kommissionen inte kan hållas ansvarig för den tekniska funktionen hos tredje parters webbplatser såsom plattformen AskTheEU. <strong>Jag kan inte instämma i detta påstående.</strong></p>
<p>Plattformen AskTheEU har sedan lång tid accepterats, använts och faktiskt tillämpats av Europeiska kommissionen som ett standardverktyg för utövandet av allmänhetens rätt till tillgång till handlingar; genom den:</p>
<ul>
<li>tar kommissionen regelbundet emot och handlägger ansökningar om tillgång till handlingar,</li>
<li>kommunicerar den med sökande, och</li>
<li>behandlar den systematiskt inlagor enligt förordning (EG) nr 1049/2001.</li>
</ul>
<p>Under dessa omständigheter kan AskTheEU inte betraktas som en godtycklig eller obehörig tredje part vars användning skulle ske på sökandens egen risk.</p>
<p>Oberoende av detta framhåller jag att frågan inte är avgörande för bedömningen av min inlagas processuella tillåtlighet. <strong>Avgörande är att Europeiska kommissionen har mottagit min bekräftande ansökan, bekräftat mottagandet och inlett handläggningen</strong>, vilket uttryckligen bekräftades av meddelandet från enheten för öppenhet vid generalsekretariatet.</p>
<p>Från den tidpunkt då kommissionen mottog inlagan, placerade den inom ramen för förordning (EG) nr 1049/2001 och underrättade mig om att den skulle handläggas inom den lagstadgade fristen från registreringen, <strong>uppstod ett formellt processuellt förhållande mellan sökanden och institutionen</strong>, för vilket det fulla ansvaret uteslutande vilar på Europeiska kommissionen.</p>
<p>Frågan om vilken kanal inlagan ursprungligen översändes genom kan inte retroaktivt påverka dess processuella tillåtlighet, särskilt som kommissionen själv har bekräftat mottagandet och handläggningens början.</p>
<p>Under dessa omständigheter är det rättsligt otillåtet att i efterhand ifrågasätta den bekräftande ansökans rättidighet eller tillåtlighet, eller att övervältra följderna av tekniska eller avtalsmässiga arrangemang mellan kommissionen och en tredje part på sökanden.</p>
<p>Jag begär därför att kommissionen genomför den fullständiga administrativa omprövningen av den bekräftande ansökan enligt artikel 7.2 i förordning (EG) nr 1049/2001.</p>
<p>Med vänlig hälsning,<br>Peter Ferenc</p>"""

BODY[13] = """
<p>Ert meddelande har mottagits av enheten för öppenhet vid Europeiska kommissionens generalsekretariat.</p>
<p>Ansökningar om allmänhetens tillgång till handlingar behandlas på grundval av förordning (EG) nr 1049/2001 av den 30 maj 2001 om allmänhetens tillgång till Europaparlamentets, rådets och kommissionens handlingar.</p>
<p>Generalsekretariatet besvarar er ansökan inom 15 arbetsdagar från registreringen och underrättar er vederbörligen om registreringen.</p>
<p><em>Samma text följde på engelska, franska och tyska.</em></p>"""

BODY[14] = """
<p>Bästa mottagare,</p>
<p>härmed översänder jag en brottsanmälan i form av en länk.</p>
<p>Anmälan avser misstanke om brott som skadar Europeiska unionens ekonomiska intressen i den mening som avses i <strong>artikel 325 FEUF</strong> och <strong>direktiv (EU) 2017/1371 (PIF)</strong>.</p>
<p>Brottsanmälan har upprättats som en PDF-handling undertecknad med en <strong>kvalificerad elektronisk underskrift (QES)</strong>, som enligt artikel 25.2 i förordning (EU) nr 910/2014 (eIDAS) har samma rättsliga verkan som en egenhändig underskrift.</p>
<p>Inlagan lämnas på slovakiska, som är ett officiellt språk i Europeiska unionen. <strong>Den slovakiska språkversionen anses vara originalet och den rättsligt bindande versionen.</strong> Versionerna EN → DE → FR → ES → PL → IT bifogas uteslutande som troget spegelöversatta texter för att underlätta handläggningen.</p>
<p>Jag framhåller uttryckligen att <strong>ingen bestämmelse i unionsrätten kräver att en brottsanmälan lämnas via ett visst webbformulär</strong>. Enligt artikel 24 i rådets förordning (EU) 2017/1939 får Europeiska åklagarmyndigheten ta emot information om brott som skadar unionens ekonomiska intressen från vilken källa som helst, inbegripet från fysiska personer.</p>
<p>Varje teknisk eller processuell begränsning som skulle:</p>
<ul>
<li>hindra översändandet av det fullständiga innehållet,</li>
<li>framtvinga en förkortning eller leda till förlust av faktiska påståenden eller bevis,</li>
<li>eller göra mottagandet beroende av en ytterligare "förhandsbedömning",</li>
</ul>
<p>utgör enligt min mening ett olagligt hinder för tillgången till rättslig prövning och en kränkning av artikel 47 i EU:s stadga om de grundläggande rättigheterna och artikel 13 i Europakonventionen.</p>
<p>Jag förväntar mig därför att brottsanmälan registreras, prövas och handläggs i sak i enlighet med unionsrätten, oberoende av det tekniska sättet för dess översändande.</p>
<p>Med vänlig hälsning,<br>Kumhausen, 11.02.2026<br>Peter Ferenc</p>
<p><em>Samma text översändes i samma meddelande även på EN, DE, FR, ES, PL, IT och SK.</em></p>"""

BODY[15] = """
<p>Till AskTheEU-teamet,</p>
<p>[länk till den undertecknade handlingen]</p>
<p>Med vänlig hälsning,<br>Peter Ferenc</p>"""

BODY[16] = """
<p>Bästa generaldirektör, bäste herr Whelan,</p>
<p>bifogat översänder jag mitt svar på ert beslut av den 7 januari 2026, genom vilket ni nekade mig tillgång till handlingarna i akten i ärendet COMP/M.10815. Handlingen är försedd med en <strong>kvalificerad elektronisk underskrift (QES)</strong> enligt art. 25.2 i eIDAS-förordningen (nr 910/2014) och är rättsligt likvärdig med en egenhändig underskrift.</p>
<p>Tillgången till institutionernas handlingar är inte en fråga för kommissionens skönsmässiga bedömning. Enligt <strong>art. 15.3 FEUF</strong>, <strong>art. 42 i EU:s stadga om de grundläggande rättigheterna</strong> och <strong>art. 2.1 i förordning (EG) nr 1049/2001</strong> har varje unionsmedborgare rätt till tillgång till institutionernas handlingar utan att behöva ange något intresse eller skäl. Avslag är undantaget; enligt domstolens fasta rättspraxis ska det tolkas restriktivt, och <strong>bevisbördan åvilar institutionen, inte sökanden</strong>.</p>
<p>I mitt svar anför jag fem skäl till varför beslutet inte kan bestå:</p>
<p><strong>1.</strong> Ni beräknade fristen från svarets datum, trots att art. 7.2 i förordningen knyter den till mottagandet. Härtill kommer: den 20 januari 2026 meddelade ni mig skriftligen att fristen ännu inte löpt ut; den 30 januari bekräftade enheten COMP C-5 mottagandet och vidarebefordrade inlagan till generalsekretariatet; den 3 februari avvisades den som för sent inkommen. <strong>Dessa tre åtgärder motsäger varandra.</strong></p>
<p><strong>2.</strong> Ni betecknar själva den allmänna presumtionen om att handlingar inte ska lämnas ut som motbevisbar, men invänder samtidigt att jag inte visat motsatsen — samtidigt som ni nekar mig till och med en förteckning över akten. <strong>En presumtion som inte kan motbevisas är inte en motbevisbar presumtion</strong> (Odile Jacob, C-404/10 P; Agrofert, C-477/10 P).</p>
<p><strong>3.</strong> Presumtionen omfattar varken GD Konkurrens interna marknadsanalyser eller den omaskerade versionen av själva beslutet — det är institutionens rättsakter, inte parternas inlagor. Ert beslut innehåller ingen individuell prövning av dessa kategorier.</p>
<p><strong>4.</strong> Ni prövade inte delvis tillgång enligt art. 4.6; ni hänvisar mig till handlingar som är offentliga även utan ert beslut.</p>
<p><strong>5.</strong> Ni avfärdade det övervägande allmänintresset som överväganden av allmän art, trots att jag hänvisade till <strong>punkterna 138–142 i ert eget beslut M.10815</strong>, där kommissionen själv anger att den inte prövade parternas efterlevnad av dataskyddsförordningen.</p>
<p>Jag uppmanar er att handlägga ansökan i sak, att översända förteckningen över akten till mig och att pröva varje begärd handling konkret och individuellt. Om kommissionen inte besvarar detta svar i sak förbehåller jag mig:</p>
<ul>
<li>ett klagomål till <strong>Europeiska ombudsmannen</strong> för administrativt missförhållande,</li>
<li>väckande av <strong>talan enligt art. 263 FEUF</strong>.</li>
</ul>
<p>Detta förbehåll får rättsverkan från mottagandet av denna skrivelse.</p>
<p>Högaktningsfullt,<br>Peter Ferenc</p>
<p><em>Samma text översändes i samma meddelande även på tyska och engelska.</em></p>"""
