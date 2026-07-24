# -*- coding: utf-8 -*-
"""HR — preslika izvornika (osim ondje gdje je HR bio izvorni jezik)."""

SUBJ = {
0:"Zahtjev za pristup dokumentima — predmet M.10815",
1:"Potvrda primitka — broj predmeta 2025/6534",
2:"Odgovor — tražim necenzurirani ugovor",
3:"Vaš zahtjev za pristup dokumentima — ref. EASE br. 2025/6534",
4:"Zahtjev za produljenje roka za podnošenje ponovnog zahtjeva — ref. EASE 2025/6534",
5:"Produljenje roka od 15 radnih dana nije moguće",
6:"Ponovni zahtjev — čl. 7. st. 2. Uredbe (EZ) br. 1049/2001",
7:"Primitak potvrđen — proslijeđeno Glavnom tajništvu",
8:"Interno preispitivanje zahtjeva za pristup dokumentima — Ares(2026)1214166",
9:"Postupovno pojašnjenje — ponovni zahtjev podnesen 26. siječnja 2026. (predmet M.10815)",
10:"Automatska potvrda primitka — Odjel za transparentnost, Glavno tajništvo",
11:"Stranice trećih osoba — koristite službeni portal",
12:"Postupovno stajalište podnositelja — primitak i obrada ponovnog zahtjeva",
13:"Automatska potvrda primitka — Odjel za transparentnost, Glavno tajništvo",
14:"Podnošenje kaznene prijave — šteta financijskim interesima EU-a (čl. 325. UFEU-a)",
15:"Dopunski dokument",
16:"Odgovor na odluku o odbijanju pristupa dokumentima — COMP/M.10815",
}

BADGE = {"Delivered":"Dostavljeno","Registered":"Evidentirano","Refused":"Odbijeno",
         "Rejected as out of time":"Odbačeno kao nepravodobno","Forwarded":"Proslijeđeno",
         "Received":"Zaprimljeno","Rejected":"Odbačeno"}

PHASES = {0:"Faza I. — prvi zahtjev", 3:"Faza II. — prvo odbijanje",
          6:"Faza III. — ponovni zahtjev", 14:"Faza IV. — eskalacija"}

BODY = {}

BODY[0] = """
<p>Poštovana Glavna uprava za tržišno natjecanje,</p>
<p>na temelju prava na pristup dokumentima iz ugovorâ EU-a, razrađenog Uredbom 1049/2001, tražim dokumente koji sadržavaju sljedeće informacije:</p>
<p>na temelju <strong>Uredbe (EZ) br. 1049/2001</strong>, <strong>članka 15. UFEU-a</strong> i <strong>članka 42. Povelje Europske unije o temeljnim pravima</strong> ovime tražim potpun pristup svim dokumentima predmeta <strong>M.10815 – Deutsche Telekom / Orange / Telefónica / Vodafone – Joint Venture</strong>.</p>
<p>Osobito tražim pristup:</p>
<ul>
<li>cjelovitom ugovoru o zajedničkom pothvatu (necenzuriranom),</li>
<li>svim prilozima i izmjenama ugovora o zajedničkom pothvatu,</li>
<li>ugovoru dioničara,</li>
<li>pravilima upravljanja i poslovanja zajedničkog pothvata,</li>
<li>cjelovitoj i necenzuriranoj verziji odluke Komisije,</li>
<li>prijavi Form CO koju su podnijele stranke,</li>
<li>svim tržišnim analizama i internim procjenama Glavne uprave za tržišno natjecanje,</li>
<li>cjelokupnoj prepisci između Glavne uprave za tržišno natjecanje i stranaka koje su podnijele prijavu, a koja se odnosi na taj zajednički pothvat.</li>
</ul>
<p>Budući da taj zajednički pothvat bitno utječe na tržišno natjecanje na telekomunikacijskom tržištu EU-a i pogađa milijune građana Unije, smatram da javni interes za transparentnošću očito prevladava nad mogućim tvrdnjama o poslovnoj tajni, u skladu s načelima koja je utvrdio Sud Europske unije.</p>
<p>S poštovanjem,<br>Peter Ferenc<br>Rammelkam 2, 84036 Kumhausen, Njemačka</p>"""

BODY[1] = """
<p>Poštovani,</p>
<p>ovime potvrđujemo primitak Vašeg zahtjeva za pristup dokumentima poslanog 10. 12. 2025. i evidentiranog 10. 12. 2025. pod brojem predmeta <strong>2025/6534</strong>.</p>
<p>Vaš zahtjev obradit ćemo u roku od <strong>15 radnih dana</strong> od dana evidentiranja. Rok istječe <strong>12. 1. 2026.</strong> Obavijestit ćemo Vas ako bude potrebno produljiti ga za dodatnih 15 radnih dana.</p>
<p>Više o obradi Vaših osobnih podataka nalazi se u izjavi o zaštiti podataka.</p>
<p>S poštovanjem,<br>Glavna uprava za tržišno natjecanje – Pristup dokumentima<br>Europska komisija</p>"""

BODY[2] = """
<p>Poštovana Glavna uprava za tržišno natjecanje,</p>
<p>hvala, čekam Vaš odgovor! Tražim necenzurirani, transparentni ugovor!</p>
<p>S poštovanjem,<br>Peter Ferenc</p>"""

BODY[3] = """
<p>Poštovani gospodine Ferenc,</p>
<p><strong>Predmet:</strong> Vaš zahtjev za pristup dokumentima – ref. EASE br. 2025/6534</p>
<p>Pozivamo se na Vašu poruku od 10. 12. 2025. kojom podnosite zahtjev za pristup dokumentima, evidentiran 10. 12. 2025. pod navedenim referentnim brojem.</p>
<p>U prilogu se nalazi skenirani odgovor na Vaš zahtjev za pristup dokumentima, <strong>koji je potpisao glavni direktor</strong>.</p>
<p>Molimo Vas da odgovorom na ovu poruku potvrdite njezin primitak.</p>
<p>S poštovanjem,</p>
<p>Europska komisija<br>Glavna uprava za tržišno natjecanje<br>Odjel C.5 Koncentracije<br>Uprava C – Tržišta i predmeti: informacijska tehnologija, komunikacije i mediji</p>"""

BODY[4] = """
<p>Poštovani,</p>
<p>ovime formalno tražim produljenje roka za podnošenje ponovnog zahtjeva u vezi s mojim zahtjevom za pristup dokumentima evidentiranim pod referencom EASE 2025/6534.</p>
<p><strong>Razlozi zahtjeva</strong></p>
<p>Iz objektivnih tehničkih razloga trenutačno nemam pouzdan pristup svim tehničkim sredstvima i vjerodajnicama za autentifikaciju potrebnima za pripremu i podnošenje pravno obrazloženog ponovnog zahtjeva.</p>
<p>Opseg i složenost razloga odbijanja zahtijevaju temeljitu pravnu i činjeničnu analizu, osobito u pogledu:</p>
<ul>
<li>primjene iznimaka od prava na pristup dokumentima,</li>
<li>proporcionalnosti provedenih zacrnjenja,</li>
<li>i ocjene usklađenosti s pravom Unije.</li>
</ul>
<p>Podnošenje ponovnog zahtjeva bez takve analize bilo bi čisto formalno i obesmislilo bi samu svrhu pravnog sredstva predviđenog pravom Unije.</p>
<p><strong>Pravna osnova</strong></p>
<p>Ovaj se zahtjev temelji, među ostalim, na:</p>
<ul>
<li>članku 41. Povelje Europske unije o temeljnim pravima (pravo na dobru upravu),</li>
<li>članku 47. Povelje Europske unije o temeljnim pravima (pravo na djelotvoran pravni lijek),</li>
<li>načelu jednakosti oružja i djelotvornog ostvarivanja postupovnih prava,</li>
<li>te ustaljenoj sudskoj praksi prema kojoj se postupovni rokovi ne smiju primjenjivati tako da ostvarivanje prava dodijeljenih pravom Unije učine praktično nemogućim ili pretjerano otežanim.</li>
</ul>
<p><strong>Zahtjev</strong></p>
<p>S obzirom na navedeno, tražim produljenje od <strong>30 dana</strong>, računajući od isteka izvornog roka za podnošenje ponovnog zahtjeva.</p>
<p>Ovaj se zahtjev podnosi bez ikakvog odricanja od prava ili priznanja zakašnjenja, i isključivo radi osiguranja pravilnog, informiranog i pravno djelotvornog ostvarivanja mojeg prava na pravni lijek.</p>
<p>Ljubazno molim pisanu potvrdu je li produljenje odobreno.</p>
<p>S poštovanjem,<br>Peter Ferenc</p>"""

BODY[5] = """
<p>Poštovani gospodine Ferenc,</p>
<p>zahvaljujemo na Vašoj poruci od 19. siječnja 2026., u kojoj pitate je li moguće produljiti zakonski rok od 15 radnih dana propisan člankom 7. stavkom 2. Uredbe 1049/2001 za podnošenje ponovnog zahtjeva nakon djelomičnog ili potpunog odbijanja zahtjeva za pristup dokumentima.</p>
<p>Obavještavamo Vas da <strong>taj rok od 15 radnih dana nije moguće produljiti</strong>, jer rokovi utvrđeni Uredbom 1049/2001 nisu na raspolaganju strankama i odlučujući su za postupak pristupa dokumentima institucija.</p>
<p>U tom kontekstu ističemo da <strong>faza ponovnog zahtjeva predstavlja potpuno upravno preispitivanje prvotne odluke i mora ispraviti svaki propust prvotne odluke, čak i kada ga podnositelj u ponovnom zahtjevu izričito ne osporava</strong>.</p>
<p>Budući da rok za podnošenje ponovnog zahtjeva protiv prvotnog negativnog odgovora Glavne uprave za tržišno natjecanje od 7. siječnja 2026. na Vaš zahtjev za pristup dokumentima od 10. prosinca 2025., evidentiran pod referencom EASE 2025/6534, <strong>još nije istekao</strong>, obavještavamo Vas da Vaš upit stoga ne tretiramo kao takav ponovni zahtjev u smislu Uredbe 1049/2001.</p>
<p>U tom pogledu ponovno Vas upućujemo na odjeljak 5. našeg prvotnog negativnog odgovora od 7. siječnja 2026., u kojem smo objasnili dostupna pravna sredstva, primjenjivi zakonski rok te način i službu Europske komisije kojoj se takav ponovni zahtjev eventualno podnosi.</p>
<p>Srdačan pozdrav,</p>
<p>Europska komisija<br>Glavna uprava za tržišno natjecanje<br>Odjel C.5 Koncentracije<br>Uprava C – Tržišta i predmeti: informacijska tehnologija, komunikacije i mediji</p>"""

BODY[6] = """
<p>Poštovani,</p>
<p>ovaj je ponovni zahtjev već podnesen <strong>26. siječnja 2026.</strong> putem platforme AskTheEU. Zbog tehničke pogreške poslan je preko pogrešnog sučelja i nije stigao do institucije.</p>
<p>Tim AskTheEU / Access Info Europe pisano je potvrdio da je poruka podnesena pravodobno i to može posvjedočiti bude li potrebno. U nastavku je poveznica na dokument koji potvrđuje da je moj ponovni zahtjev podnesen pravodobno alternativnim kanalom, zbog tehničke pogreške platforme.</p>
<p>Ovime podnosim ponovni zahtjev na temelju <strong>članka 7. stavka 2. Uredbe (EZ) br. 1049/2001</strong> i tražim potpuno upravno preispitivanje prvotnog negativnog odgovora od 7. siječnja 2026. koji je izdala Glavna uprava za tržišno natjecanje na moj zahtjev za pristup dokumentima od 10. prosinca 2025., evidentiran pod referencom EASE 2025/6534.</p>
<p>S poštovanjem ostajem pri tome da prvotna odluka nezakonito ograničava moje pravo na pristup dokumentima i ne poštuje načela transparentnosti, proporcionalnosti i dobre uprave utvrđena Uredbom 1049/2001 i člankom 15. UFEU-a.</p>
<p>Osobito:</p>
<p><strong>1. Netočna ili preširoka primjena iznimaka</strong><br>
Prvotni se odgovor oslanja na iznimke za koje nije dokazano da se konkretno i pojedinačno primjenjuju na tražene dokumente. Dano obrazloženje ostaje apstraktno i ne pokazuje kako bi otkrivanje konkretno i stvarno ugrozilo zaštićeni interes, kako to zahtijeva ustaljena sudska praksa Suda.</p>
<p><strong>2. Izostanak pravilne ocjene prevladavajućeg javnog interesa</strong><br>
Traženi se dokumenti odnose na pitanja od znatnog javnog interesa, uključujući funkcioniranje provedbe prava tržišnog natjecanja, poštovanje prava Unije i zaštitu temeljnih prava. Prvotna odluka ne sadržava stvarnu i obrazloženu ocjenu postoji li prevladavajući javni interes za otkrivanjem.</p>
<p><strong>3. Nedostatno obrazloženje i izostanak pojedinačnog ispitivanja</strong><br>
Odbijanje ne pokazuje da je svaki dokument ispitan pojedinačno, niti objašnjava zašto se nije mogao odobriti djelomičan pristup u skladu s člankom 4. stavkom 6. Uredbe 1049/2001.</p>
<p><strong>4. Značaj zaštite podataka i usklađenosti s GDPR-om</strong><br>
U mjeri u kojoj su istaknuta razmatranja o zaštiti podataka, napominjem da Uredba (EU) 2018/1725 i Uredba (EU) 2016/679 (GDPR) ne opravdavaju paušalno odbijanje. Sva pitanja osobnih podataka mogu se i moraju riješiti primjerenim zacrnjenjem, a ne uskratom pristupa.</p>
<p>Kako podsjećate u svojem dopisu od 20. siječnja 2026., faza ponovnog zahtjeva predstavlja potpuno upravno preispitivanje prvotne odluke. Stoga pozivam Komisiju da zahtjev preispita u cijelosti i ispravi sve propuste ili pogreške sadržane u prvotnom odgovoru, uključujući one koje gore nisam izričito osporio.</p>
<p>S poštovanjem tražim da Komisija odobri pristup traženim dokumentima, u cijelosti ili barem djelomično, u skladu s Uredbom 1049/2001.</p>
<p>S poštovanjem,<br>Peter Ferenc</p>"""

BODY[7] = """
<p>Poštovani gospodine Ferenc,</p>
<p>ovime potvrđujemo primitak Vaše poruke od 30. siječnja 2026., kojom podnosite zahtjev za ponovnu odluku.</p>
<p>Obavještavamo Vas da smo <strong>Vašu poruku proslijedili nadležnom Glavnom tajništvu Europske komisije</strong>.</p>
<p>Srdačan pozdrav<br>COMP C-5</p>"""

BODY[8] = """
<p>Poštovani podnositelju,</p>
<p>pozivam se na Vašu poruku od 30. siječnja 2026., kojom podnosite ponovni zahtjev u skladu s člankom 7. stavkom 2. Uredbe 1049/2001 o javnom pristupu dokumentima Europskog parlamenta, Vijeća i Komisije (dalje: Uredba 1049/2001).</p>
<p>Sa žaljenjem Vas obavještavam da je <strong>Vaš ponovni zahtjev podnesen izvan primjenjivog roka</strong> utvrđenog člankom 7. stavkom 2. Uredbe 1049/2001. Taj članak propisuje da u slučaju potpunog ili djelomičnog odbijanja podnositelj može u roku od 15 radnih dana od primitka odgovora institucije podnijeti ponovni zahtjev kojim traži od institucije da preispita svoje stajalište.</p>
<p><strong>Komisija stoga nije u mogućnosti postupati po Vašem zahtjevu.</strong></p>
<p>S poštovanjem,<br>Europska komisija<br>Tim za pristup dokumentima</p>"""

BODY[9] = """
<p>Poštovani,</p>
<p>moram se formalno usprotiviti stajalištu koje se sada zastupa u ovoj stvari i tražim da se činjenično i postupovno stanje točno prikaže.</p>
<p><strong>1. Pravodobno podnošenje ponovnog zahtjeva</strong><br>
Moj ponovni zahtjev na temelju članka 7. stavka 2. Uredbe (EZ) br. 1049/2001 bio je <strong>u cijelosti sastavljen i podnesen 26. siječnja 2026.</strong>, dakle <strong>posljednjeg dana zakonskog roka</strong>, putem platforme AskTheEU. Ta činjenica <strong>nije sporna</strong> i <strong>izričito je pisano potvrđena od strane Access Info Europe</strong>, uključujući dokaznu dokumentaciju (potvrda primitka moje poruke s vremenskim žigom od 26. siječnja 2026.).</p>
<p><strong>2. Tehnički izostanak prosljeđivanja ne može se pripisati podnositelju</strong><br>
Svaki izostanak prosljeđivanja ponovnog zahtjeva Komisiji proizašao je isključivo iz tehničkog i organizacijskog problema na strani posredničke platforme. Prema ustaljenoj sudskoj praksi i općim načelima prava Unije:</p>
<ul>
<li>podnositelj se <strong>ne smije sankcionirati</strong> zbog tehničkih kvarova posredničke platforme korištene u dobroj vjeri;</li>
<li>postupovna prava dodijeljena Uredbom 1049/2001 <strong>ne mogu se ugasiti pretjeranim formalizmom</strong>.</li>
</ul>
<p><strong>3. Legitimna očekivanja i postupovni primitak</strong><br>
Bitno je da je ponovni zahtjev zaprimljen, interno obrađen i proslijeđen nadležnim službama Komisije. Ti akti predstavljaju <strong>formalne postupovne korake</strong> kojima je <strong>prešutno priznata postupovna valjanost</strong> ponovnog zahtjeva. Nakon što je do takvog postupovnog primitka došlo, <strong>pravno je nedopušteno</strong> retroaktivno ga negirati, jer bi se time povrijedilo:</p>
<ul>
<li>načelo dobre uprave (članak 41. Povelje),</li>
<li>zaštita legitimnih očekivanja,</li>
<li>i djelotvornost prava Unije.</li>
</ul>
<p><strong>4. Posljedice</strong><br>
Svaki pokušaj da se uredno podnesen ponovni zahtjev sada prekvalificira u „nepravodoban" predstavljao bi proizvoljno upravno postupanje, očito neproporcionalan formalizam i povredu članaka 41. i 47. Povelje o temeljnim pravima. Takvo bi postupanje bilo <strong>samostalno preispitivo</strong> pred Europskim ombudsmanom i, ako bude potrebno, pred sudovima Unije.</p>
<p><strong>5. Zahtjev</strong><br>
Stoga tražim da se:</p>
<ul>
<li>spis ispravi tako da odražava pravodobno podnošenje 26. siječnja 2026.,</li>
<li>ponovni zahtjev tretira kao valjano podnesen,</li>
<li>i da Komisija provede potpuno upravno preispitivanje propisano člankom 7. stavkom 2. Uredbe 1049/2001.</li>
</ul>
<p>Ova se poruka podnosi <strong>radi izbjegavanja dvojbi i bez utjecaja</strong> na sva daljnja pravna sredstva koja mi pripadaju prema pravu Unije.</p>
<p><strong>Dodatno postupovno pojašnjenje</strong><br>
Radi izbjegavanja svake dvojbe potvrđujem da je isti ponovni zahtjev <strong>7. veljače 2026.</strong> dostavljen i izravno Europskoj komisiji službenim kanalima elektroničke pošte, kao i kabinetu člana Komisije. Sadržaj ponovnog zahtjeva time je Komisiji nedvojbeno stavljen na raspolaganje putem više službenih kanala, što dodatno pokazuje moju dobru vjeru, postupovnu suradnju i istinsku namjeru da svoja prava iz Uredbe (EZ) br. 1049/2001 ostvarujem uredno i s dužnom pažnjom.</p>
<p>S poštovanjem,<br>Peter Ferenc<br>Predmet br.: TFIA-2026-JV-002</p>"""

BODY[10] = """
<p>Vaša je poruka zaprimljena u Odjelu za transparentnost Glavnog tajništva Europske komisije.</p>
<p>Zahtjevi za javni pristup dokumentima obrađuju se na temelju Uredbe (EZ) br. 1049/2001 od 30. svibnja 2001. o javnom pristupu dokumentima Europskog parlamenta, Vijeća i Komisije.</p>
<p>Glavno tajništvo odgovorit će na Vaš zahtjev u roku od <strong>15 radnih dana</strong> od njegova evidentiranja i uredno će Vas obavijestiti o evidentiranju zahtjeva (ili o dodatnim informacijama koje treba dostaviti radi evidentiranja i/ili obrade).</p>
<p><em>Isti je tekst uslijedio na engleskom, francuskom i njemačkom.</em></p>"""

BODY[11] = """
<p>Poštovani podnositelju,</p>
<p><strong>Europska komisija ne može se smatrati odgovornom za probleme sa stranicama trećih osoba.</strong> Pozivamo Vas da koristite službeni portal za traženje dokumenata Europske komisije.</p>
<p>Srdačan pozdrav,<br>Europska komisija<br>Tim za pristup dokumentima</p>"""

BODY[12] = """
<p>Poštovani,</p>
<p>primam na znanje Vašu izjavu prema kojoj se Europska komisija ne može smatrati odgovornom za tehničko funkcioniranje stranica trećih osoba kao što je platforma AskTheEU. <strong>S tom se tvrdnjom ne mogu složiti.</strong></p>
<p>Platformu AskTheEU Europska komisija dugo prihvaća, koristi i stvarno se na nju oslanja kao na standardni alat za ostvarivanje javnog prava na pristup dokumentima; preko nje Komisija:</p>
<ul>
<li>redovito zaprima i obrađuje zahtjeve za pristup dokumentima,</li>
<li>komunicira s podnositeljima, i</li>
<li>sustavno obrađuje podneske na temelju Uredbe (EZ) br. 1049/2001.</li>
</ul>
<p>U tim se okolnostima AskTheEU ne može smatrati nasumičnom ili neovlaštenom trećom osobom čije bi korištenje išlo na vlastiti rizik podnositelja.</p>
<p>Neovisno o navedenom, naglašavam da to pitanje nije odlučujuće za ocjenu postupovne dopuštenosti mojeg podneska. <strong>Odlučujuća je činjenica da je Europska komisija moj ponovni zahtjev zaprimila, potvrdila njegov primitak i započela njegovu obradu</strong>, kako je izričito potvrdila poruka Odjela za transparentnost Glavnog tajništva.</p>
<p>Od trenutka u kojem je Komisija podnesak zaprimila, smjestila ga u okvir Uredbe (EZ) br. 1049/2001 i obavijestila me da će biti obrađen u zakonskom roku od evidentiranja, <strong>nastao je formalni postupovni odnos između podnositelja i institucije</strong>, za koji punu odgovornost snosi isključivo Europska komisija.</p>
<p>Pitanje kanala kojim je podnesak prvotno dostavljen ne može retroaktivno utjecati na njegovu postupovnu dopuštenost, tim više što je sama Komisija potvrdila primitak i početak obrade.</p>
<p>U tim je okolnostima pravno nedopušteno naknadno osporavati pravodobnost ili dopuštenost ponovnog zahtjeva, niti prenositi posljedice tehničkih ili ugovornih aranžmana između Komisije i treće osobe na podnositelja.</p>
<p>Stoga tražim da Komisija provede potpuno upravno preispitivanje ponovnog zahtjeva u skladu s člankom 7. stavkom 2. Uredbe (EZ) br. 1049/2001.</p>
<p>S poštovanjem,<br>Peter Ferenc</p>"""

BODY[13] = """
<p>Vaša je poruka zaprimljena u Odjelu za transparentnost Glavnog tajništva Europske komisije.</p>
<p>Zahtjevi za javni pristup dokumentima obrađuju se na temelju Uredbe (EZ) br. 1049/2001 od 30. svibnja 2001. o javnom pristupu dokumentima Europskog parlamenta, Vijeća i Komisije.</p>
<p>Glavno tajništvo odgovorit će na Vaš zahtjev u roku od 15 radnih dana od njegova evidentiranja i uredno će Vas o tome obavijestiti.</p>
<p><em>Isti je tekst uslijedio na engleskom, francuskom i njemačkom.</em></p>"""

BODY[14] = """
<p>Poštovane dame i gospodo,</p>
<p>ovime Vam kaznenu prijavu dostavljam u obliku poveznice.</p>
<p>Riječ je o kaznenoj prijavi zbog sumnje na kaznena djela koja štete financijskim interesima Europske unije u smislu <strong>članka 325. UFEU-a</strong> i <strong>Direktive (EU) 2017/1371 (PIF)</strong>.</p>
<p>Kaznena je prijava sastavljena kao PDF dokument potpisan <strong>kvalificiranim elektroničkim potpisom (QES)</strong>, koji prema članku 25. stavku 2. Uredbe (EU) br. 910/2014 (eIDAS) ima iste pravne učinke kao vlastoručni potpis.</p>
<p>Podnesak se podnosi na slovačkom jeziku, koji je službeni jezik Europske unije. <strong>Slovačka se jezična verzija smatra izvornom i pravno obvezujućom verzijom.</strong> Verzije EN → DE → FR → ES → PL → IT priložene su isključivo kao vjerni zrcalni prijevodi radi lakše obrade.</p>
<p>Izričito ističem da <strong>nijedan propis prava Unije ne propisuje obvezu podnošenja kaznene prijave putem određenog internetskog obrasca</strong>. Prema članku 24. Uredbe Vijeća (EU) 2017/1939 Ured europskog javnog tužitelja može primati informacije o kaznenim djelima koja štete financijskim interesima Unije iz bilo kojeg izvora, uključujući od fizičkih osoba.</p>
<p>Svako tehničko ili postupovno ograničenje koje bi:</p>
<ul>
<li>onemogućilo dostavu cjelovitog sadržaja,</li>
<li>iznudilo njegovo skraćivanje ili dovelo do gubitka činjeničnih navoda ili dokaza,</li>
<li>ili uvjetovalo njegovo prihvaćanje dodatnom „prethodnom procjenom",</li>
</ul>
<p>smatram nezakonitom preprekom pristupu pravosuđu i povredom članka 47. Povelje Europske unije o temeljnim pravima i članka 13. Europske konvencije za zaštitu ljudskih prava.</p>
<p>Stoga očekujem da će kaznena prijava biti uredno evidentirana, ispitana i riješena prema svojem sadržaju, u skladu s pravom Europske unije, neovisno o tehničkom načinu njezine dostave.</p>
<p>S poštovanjem,<br>Kumhausen, 09. 02. 2026.<br>Peter Ferenc</p>
<p><em>Istovjetan je tekst u istoj poruci dostavljen i na EN, DE, FR, ES, PL i IT.</em></p>"""

BODY[15] = """
<p>Poštovani AskTheEU,</p>
<p>[poveznica na potpisani dokument]</p>
<p>S poštovanjem,<br>Peter Ferenc</p>"""

BODY[16] = """
<p>Poštovana glavna direktorice, poštovani gospodine Whelan,</p>
<p>u prilogu Vam dostavljam svoj odgovor na Vašu odluku od 7. siječnja 2026. kojom ste mi odbili pristup dokumentima u spisu predmeta COMP/M.10815. Dokument je opremljen <strong>kvalificiranim elektroničkim potpisom (QES)</strong> u skladu s čl. 25. st. 2. Uredbe eIDAS (br. 910/2014) i pravno je istovjetan vlastoručnom potpisu.</p>
<p>Pristup dokumentima institucija nije stvar diskrecije Komisije. Prema <strong>čl. 15. st. 3. UFEU-a</strong>, <strong>čl. 42. Povelje Europske unije o temeljnim pravima</strong> i <strong>čl. 2. st. 1. Uredbe (EZ) br. 1049/2001</strong> svaki građanin Unije ima pravo na pristup dokumentima institucija bez potrebe dokazivanja interesa ili razloga. Odbijanje je iznimka; prema ustaljenoj sudskoj praksi Suda tumači se restriktivno, a <strong>teret dokazivanja snosi institucija, a ne podnositelj</strong>.</p>
<p>U svojem odgovoru navodim pet razloga zbog kojih odluka ne može opstati:</p>
<p><strong>1.</strong> Rok ste računali od datuma odgovora, iako ga čl. 7. st. 2. Uredbe veže uz primitak. Uz to: 20. siječnja 2026. pisano ste mi priopćili da rok još nije istekao; 30. siječnja odjel COMP C-5 potvrdio je primitak i proslijedio podnesak Glavnom tajništvu; 3. veljače odbačen je kao nepravodoban. <strong>Ta si tri akta međusobno proturječe.</strong></p>
<p><strong>2.</strong> Opću pretpostavku neotkrivanja i sami označavate oborivom, no istodobno mi prigovarate da suprotno nisam dokazao — pritom mi odbijate dati na uvid i sam popis spisa. <strong>Pretpostavka koja se ne može oboriti nije oboriva pretpostavka</strong> (Odile Jacob, C-404/10 P; Agrofert, C-477/10 P).</p>
<p><strong>3.</strong> Pretpostavka ne obuhvaća ni interne tržišne analize Glavne uprave za tržišno natjecanje ni necenzuriranu verziju same odluke — riječ je o aktima institucije, a ne o podnescima stranaka. Pojedinačno ispitivanje tih kategorija Vaša odluka ne sadržava.</p>
<p><strong>4.</strong> Djelomičan pristup prema čl. 4. st. 6. niste ocijenili; upućujete me na dokumente koji su javni i bez Vaše odluke.</p>
<p><strong>5.</strong> Prevladavajući javni interes odbacili ste kao razmatranja opće naravi, iako sam uputio na <strong>točke 138. do 142. Vaše vlastite odluke M.10815</strong>, u kojima Komisija sama navodi da usklađenost stranaka s GDPR-om nije ocjenjivala.</p>
<p>Tražim od Vas da zahtjev riješite meritorno, da mi dostavite popis spisa i da svaki traženi dokument ispitate konkretno i pojedinačno. Ako Komisija na ovaj odgovor meritorno ne reagira, pridržavam pravo na:</p>
<ul>
<li>pritužbu <strong>Europskom ombudsmanu</strong> zbog nepravilnosti u postupanju;</li>
<li>podnošenje <strong>tužbe na temelju čl. 263. UFEU-a</strong>.</li>
</ul>
<p>Ovaj pridržaj proizvodi pravni učinak od primitka ovog dopisa.</p>
<p>S poštovanjem,<br>Peter Ferenc</p>
<p><em>Istovjetan je tekst u istoj poruci dostavljen i na njemačkom i engleskom.</em></p>"""
