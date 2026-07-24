#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FIA FOX — DG COMP M.10815, uplne znenie korespondencie, viacjazycne.
   Jazyk, v ktorom sprava skutocne odisla/prisla = ORIGINAL, ostatne = KOPIA ORIGINALU (preklad)."""
import re, html, importlib
import analyza

ns = {}
exec(open('gen_full.py', encoding='utf-8').read().split("open('dgcomp")[0], ns)
M, EXT, CSS, SRC = ns["M"], ns["EXT"], ns["CSS"], ns["SRC"]
PH_EN, linkify_en = ns["PHASES"], ns["linkify"]

LANGS = ["en", "sk", "de", "hr", "pl", "es", "it", "fr", "sv"]
FLAG = {"en":"gb","sk":"sk","de":"de","hr":"hr","pl":"pl","es":"es","it":"it","fr":"fr","sv":"se"}
MOD = {}
for L in LANGS:
    if L == "en": continue
    try: MOD[L] = importlib.import_module(L)
    except ModuleNotFoundError: pass
ACTIVE = ["en"] + [L for L in LANGS if L in MOD]

ORIG = {i: {"en"} for i in range(len(M))}
ORIG[10] = {"en", "fr", "de"}
ORIG[13] = {"en", "fr", "de"}
ORIG[14] = {"en", "de", "fr", "es", "pl", "it", "sk"}
ORIG[16] = {"de", "en", "sk"}

MARK = {
 "en":("<b>ORIGINAL</b> — wording as sent/received","<b>COPY OF THE ORIGINAL</b> — translation"),
 "sk":("<b>ORIGINÁL</b> — znenie tak, ako bolo odoslané/doručené","<b>KÓPIA ORIGINÁLU</b> — preklad"),
 "de":("<b>ORIGINAL</b> — Wortlaut wie gesendet/empfangen","<b>KOPIE DES ORIGINALS</b> — Übersetzung"),
 "hr":("<b>IZVORNIK</b> — tekst kako je poslan/primljen","<b>PRESLIKA IZVORNIKA</b> — prijevod"),
 "pl":("<b>ORYGINAŁ</b> — brzmienie jak wysłano/otrzymano","<b>KOPIA ORYGINAŁU</b> — tłumaczenie"),
 "es":("<b>ORIGINAL</b> — texto tal como se envió/recibió","<b>COPIA DEL ORIGINAL</b> — traducción"),
 "it":("<b>ORIGINALE</b> — testo come inviato/ricevuto","<b>COPIA DELL'ORIGINALE</b> — traduzione"),
 "fr":("<b>ORIGINAL</b> — texte tel qu'envoyé/reçu","<b>COPIE DE L'ORIGINAL</b> — traduction"),
 "sv":("<b>ORIGINAL</b> — lydelse som skickad/mottagen","<b>KOPIA AV ORIGINALET</b> — översättning"),
}
UI = {  # (Attachments, Links in the message, Back to case, Summary, truncated-note, Applicant, Institution, Legal basis, Channel, messages, Source)
 "en":("Attachments","Links in the message","← Back to case","Summary version →",
       "— link truncated in the AskTheEU export; open the original via “source”",
       "Applicant","Institution","Legal basis","Channel","messages","Source of the record"),
 "sk":("Prílohy","Odkazy v správe","← Späť na kartu","Skrátený prehľad →",
       "— odkaz je useknutý v exporte AskTheEU; originál otvor cez „source“",
       "Žiadateľ","Inštitúcia","Právny základ","Kanál","správ","Zdroj záznamu"),
 "de":("Anlagen","Links in der Nachricht","← Zurück zur Akte","Kurzfassung →",
       "— Link im AskTheEU-Export abgeschnitten; Original über „source“ öffnen",
       "Antragsteller","Organ","Rechtsgrundlage","Kanal","Nachrichten","Quelle des Vorgangs"),
  "hr":("Prilozi","Poveznice u poruci","← Natrag na predmet","Skraćeni pregled →",
       "— poveznica je skraćena u izvozu s AskTheEU; izvornik otvorite preko „source“",
       "Podnositelj","Institucija","Pravna osnova","Kanal","poruka","Izvor zapisa"),
  "pl":("Załączniki","Linki w wiadomości","← Powrót do sprawy","",
       "— link skrócony w eksporcie AskTheEU; oryginał otwórz przez „source“",
       "Wnioskodawca","Instytucja","Podstawa prawna","Kanał","wiadomości","Źródło zapisu"),
  "es":("Anexos","Enlaces del mensaje","← Volver al asunto","",
       "— enlace truncado en la exportación de AskTheEU; abra el original mediante «source»",
       "Solicitante","Institución","Fundamento jurídico","Canal","mensajes","Fuente del expediente"),
  "it":("Allegati","Link nel messaggio","← Torna al caso","",
       "— link troncato nell'esportazione da AskTheEU; apri l'originale tramite «source»",
       "Richiedente","Istituzione","Base giuridica","Canale","messaggi","Fonte del fascicolo"),
  "fr":("Pièces jointes","Liens dans le message","← Retour au dossier","",
       "— lien tronqué dans l'export AskTheEU ; ouvrez l'original via « source »",
       "Demandeur","Institution","Base juridique","Canal","messages","Source du dossier"),
  "sv":("Bilagor","Länkar i meddelandet","← Tillbaka till ärendet","",
       "— länken är avkortad i AskTheEU-exporten; öppna originalet via ”source”",
       "Sökande","Institution","Rättslig grund","Kanal","meddelanden","Källa för akten"),
}
CELEX = {"R1049":"32001R1049","TFEU15":"12016E015","CHARTER":"12012P/TXT","GDPR":"32016R0679",
         "R1725":"32018R1725","PIF":"32017L1371","EPPO":"32017R1939","EIDAS":"32014R0910",
         "TFEU325":"12016E325","TFEU263":"12016E263"}
PATS = {  # jazyk -> [(regex, kluc)]
 "sk":[(r"nariadenia \(ES\) č\. 1049/2001","R1049"),(r"nariadenie \(ES\) č\. 1049/2001","R1049"),
       (r"nariadením 1049/2001","R1049"),(r"nariadenia 1049/2001","R1049"),(r"nariadení 1049/2001","R1049"),
       (r"článku 7 ods\. 2","R1049"),(r"článok 7 ods\. 2","R1049"),(r"čl\. 7 ods\. 2","R1049"),
       (r"článku 4 ods\. 6","R1049"),(r"čl\. 4 ods\. 6","R1049"),
       (r"článku 15 ZFEÚ","TFEU15"),(r"čl\. 15 ods\. 3 ZFEÚ","TFEU15"),
       (r"článku 42 Charty základných práv Európskej únie","CHARTER"),
       (r"čl\. 42 Charty základných práv EÚ","CHARTER"),
       (r"článok 41 Charty základných práv Európskej únie","CHARTER"),
       (r"článok 47 Charty základných práv Európskej únie","CHARTER"),
       (r"článkov 41 a 47 Charty základných práv","CHARTER"),
       (r"článku 47 Charty základných práv EÚ","CHARTER"),(r"článku 41 Charty","CHARTER"),
       (r"nariadenie \(EÚ\) 2016/679 \(GDPR\)","GDPR"),(r"nariadenie \(EÚ\) 2018/1725","R1725"),
       (r"smernice \(EÚ\) 2017/1371 \(PIF\)","PIF"),(r"nariadenia Rady \(EÚ\) 2017/1939","EPPO"),
       (r"nariadenia \(EÚ\) č\. 910/2014 \(eIDAS\)","EIDAS"),(r"nariadenia eIDAS \(č\. 910/2014\)","EIDAS"),
       (r"článku 325 ZFEÚ","TFEU325"),(r"čl\. 263 ZFEÚ","TFEU263")],
 "hr":[(r"Uredbe \(EZ\) br\. 1049/2001","R1049"),(r"Uredba \(EZ\) br\. 1049/2001","R1049"),
       (r"Uredbom 1049/2001","R1049"),(r"Uredbe 1049/2001","R1049"),(r"Uredbom \(EZ\) br\. 1049/2001","R1049"),
       (r"članka 7\. stavka 2\.","R1049"),(r"člankom 7\. stavkom 2\.","R1049"),(r"čl\. 7\. st\. 2\.","R1049"),
       (r"članka 4\. stavka 6\.","R1049"),(r"čl\. 4\. st\. 6\.","R1049"),
       (r"čl\. 2\. st\. 1\. Uredbe \(EZ\) br\. 1049/2001","R1049"),
       (r"članka 15\. UFEU-a","TFEU15"),(r"čl\. 15\. st\. 3\. UFEU-a","TFEU15"),
       (r"članka 42\. Povelje Europske unije o temeljnim pravima","CHARTER"),
       (r"čl\. 42\. Povelje Europske unije o temeljnim pravima","CHARTER"),
       (r"članku 41\. Povelje Europske unije o temeljnim pravima","CHARTER"),
       (r"članku 47\. Povelje Europske unije o temeljnim pravima","CHARTER"),
       (r"članaka 41\. i 47\. Povelje o temeljnim pravima","CHARTER"),
       (r"članka 47\. Povelje Europske unije o temeljnim pravima","CHARTER"),
       (r"članak 41\. Povelje","CHARTER"),
       (r"Uredba \(EU\) 2016/679 \(GDPR\)","GDPR"),(r"Uredba \(EU\) 2018/1725","R1725"),
       (r"Direktive \(EU\) 2017/1371 \(PIF\)","PIF"),(r"Uredbe Vijeća \(EU\) 2017/1939","EPPO"),
       (r"Uredbe \(EU\) br\. 910/2014 \(eIDAS\)","EIDAS"),(r"Uredbe eIDAS \(br\. 910/2014\)","EIDAS"),
       (r"članka 325\. UFEU-a","TFEU325"),(r"čl\. 263\. UFEU-a","TFEU263")],
 "pl":[(r"rozporządzenia \(WE\) nr 1049/2001","R1049"),(r"rozporządzenie \(WE\) nr 1049/2001","R1049"),
       (r"rozporządzeniu 1049/2001","R1049"),(r"rozporządzenia 1049/2001","R1049"),(r"rozporządzeniem 1049/2001","R1049"),
       (r"art\. 7 ust\. 2","R1049"),(r"art\. 4 ust\. 6","R1049"),
       (r"art\. 2 ust\. 1 rozporządzenia \(WE\) nr 1049/2001","R1049"),
       (r"art\. 15 TFUE","TFEU15"),(r"art\. 15 ust\. 3 TFUE","TFEU15"),
       (r"art\. 42 Karty praw podstawowych Unii Europejskiej","CHARTER"),
       (r"art\. 42 Karty praw podstawowych UE","CHARTER"),
       (r"art\. 41 Karty praw podstawowych Unii Europejskiej","CHARTER"),
       (r"art\. 47 Karty praw podstawowych Unii Europejskiej","CHARTER"),
       (r"art\. 41 i 47 Karty praw podstawowych","CHARTER"),
       (r"art\. 47 Karty praw podstawowych UE","CHARTER"),(r"art\. 41 Karty","CHARTER"),
       (r"rozporządzenie \(UE\) 2016/679 \(RODO\)","GDPR"),(r"rozporządzenie \(UE\) 2018/1725","R1725"),
       (r"dyrektywy \(UE\) 2017/1371 \(PIF\)","PIF"),(r"rozporządzenia Rady \(UE\) 2017/1939","EPPO"),
       (r"rozporządzenia \(UE\) nr 910/2014 \(eIDAS\)","EIDAS"),(r"rozporządzenia eIDAS \(nr 910/2014\)","EIDAS"),
       (r"art\. 325 TFUE","TFEU325"),(r"art\. 263 TFUE","TFEU263")],
 "es":[(r"Reglamento \(CE\) n\.º 1049/2001","R1049"),(r"Reglamento 1049/2001","R1049"),
       (r"artículo 7, apartado 2","R1049"),(r"art\. 7, apdo\. 2","R1049"),
       (r"artículo 4, apartado 6","R1049"),(r"art\. 4, apdo\. 6","R1049"),
       (r"art\. 2, apdo\. 1, del Reglamento \(CE\) n\.º 1049/2001","R1049"),
       (r"artículo 15 TFUE","TFEU15"),(r"art\. 15, apdo\. 3, TFUE","TFEU15"),
       (r"artículo 42 de la Carta de los Derechos Fundamentales de la Unión Europea","CHARTER"),
       (r"art\. 42 de la Carta de los Derechos Fundamentales de la UE","CHARTER"),
       (r"artículo 41 de la Carta de los Derechos Fundamentales de la Unión Europea","CHARTER"),
       (r"artículo 47 de la Carta de los Derechos Fundamentales de la Unión Europea","CHARTER"),
       (r"artículos 41 y 47 de la Carta de los Derechos Fundamentales","CHARTER"),
       (r"artículo 47 de la Carta de los Derechos Fundamentales de la UE","CHARTER"),
       (r"artículo 41 de la Carta","CHARTER"),
       (r"Reglamento \(UE\) 2016/679 \(RGPD\)","GDPR"),(r"Reglamento \(UE\) 2018/1725","R1725"),
       (r"Directiva \(UE\) 2017/1371 \(PIF\)","PIF"),(r"Reglamento \(UE\) 2017/1939","EPPO"),
       (r"Reglamento \(UE\) n\.º 910/2014 \(eIDAS\)","EIDAS"),(r"Reglamento eIDAS \(n\.º 910/2014\)","EIDAS"),
       (r"artículo 325 TFUE","TFEU325"),(r"art\. 263 TFUE","TFEU263")],
 "it":[(r"regolamento \(CE\) n\. 1049/2001","R1049"),(r"regolamento 1049/2001","R1049"),
       (r"articolo 7, paragrafo 2","R1049"),(r"art\. 7, par\. 2","R1049"),
       (r"articolo 4, paragrafo 6","R1049"),(r"art\. 4, par\. 6","R1049"),
       (r"art\. 2, par\. 1, del regolamento \(CE\) n\. 1049/2001","R1049"),
       (r"articolo 15 TFUE","TFEU15"),(r"art\. 15, par\. 3, TFUE","TFEU15"),
       (r"articolo 42 della Carta dei diritti fondamentali dell'Unione europea","CHARTER"),
       (r"art\. 42 della Carta dei diritti fondamentali dell'UE","CHARTER"),
       (r"articolo 41 della Carta dei diritti fondamentali dell'Unione europea","CHARTER"),
       (r"articolo 47 della Carta dei diritti fondamentali dell'Unione europea","CHARTER"),
       (r"articoli 41 e 47 della Carta dei diritti fondamentali","CHARTER"),
       (r"articolo 47 della Carta dei diritti fondamentali dell'UE","CHARTER"),
       (r"articolo 41 della Carta","CHARTER"),
       (r"regolamento \(UE\) 2016/679 \(GDPR\)","GDPR"),(r"regolamento \(UE\) 2018/1725","R1725"),
       (r"direttiva \(UE\) 2017/1371 \(PIF\)","PIF"),(r"regolamento \(UE\) 2017/1939","EPPO"),
       (r"regolamento \(UE\) n\. 910/2014 \(eIDAS\)","EIDAS"),(r"regolamento eIDAS \(n\. 910/2014\)","EIDAS"),
       (r"articolo 325 TFUE","TFEU325"),(r"art\. 263 TFUE","TFEU263")],
 "fr":[(r"règlement \(CE\) n° 1049/2001","R1049"),(r"règlement 1049/2001","R1049"),
       (r"article 7, paragraphe 2","R1049"),(r"art\. 7, par\. 2","R1049"),
       (r"article 4, paragraphe 6","R1049"),(r"art\. 4, par\. 6","R1049"),
       (r"art\. 2, par\. 1, du règlement \(CE\) n° 1049/2001","R1049"),
       (r"article 15 TFUE","TFEU15"),(r"art\. 15, par\. 3, TFUE","TFEU15"),
       (r"article 42 de la charte des droits fondamentaux de l'Union européenne","CHARTER"),
       (r"art\. 42 de la charte des droits fondamentaux de l'UE","CHARTER"),
       (r"article 41 de la charte des droits fondamentaux de l'Union européenne","CHARTER"),
       (r"article 47 de la charte des droits fondamentaux de l'Union européenne","CHARTER"),
       (r"articles 41 et 47 de la charte des droits fondamentaux","CHARTER"),
       (r"article 47 de la charte des droits fondamentaux de l'UE","CHARTER"),
       (r"article 41 de la charte","CHARTER"),
       (r"règlement \(UE\) 2016/679 \(RGPD\)","GDPR"),(r"règlement \(UE\) 2018/1725","R1725"),
       (r"directive \(UE\) 2017/1371 \(PIF\)","PIF"),(r"règlement \(UE\) 2017/1939","EPPO"),
       (r"règlement \(UE\) n° 910/2014 \(eIDAS\)","EIDAS"),(r"règlement eIDAS \(n° 910/2014\)","EIDAS"),
       (r"article 325 TFUE","TFEU325"),(r"art\. 263 TFUE","TFEU263")],
 "sv":[(r"förordning \(EG\) nr 1049/2001","R1049"),(r"förordning 1049/2001","R1049"),
       (r"artikel 7\.2","R1049"),(r"art\. 7\.2","R1049"),(r"artikel 4\.6","R1049"),(r"art\. 4\.6","R1049"),
       (r"art\. 2\.1 i förordning \(EG\) nr 1049/2001","R1049"),
       (r"artikel 15 FEUF","TFEU15"),(r"art\. 15\.3 FEUF","TFEU15"),
       (r"artikel 42 i Europeiska unionens stadga om de grundläggande rättigheterna","CHARTER"),
       (r"art\. 42 i EU:s stadga om de grundläggande rättigheterna","CHARTER"),
       (r"artikel 41 i Europeiska unionens stadga om de grundläggande rättigheterna","CHARTER"),
       (r"artikel 47 i Europeiska unionens stadga om de grundläggande rättigheterna","CHARTER"),
       (r"artiklarna 41 och 47 i stadgan om de grundläggande rättigheterna","CHARTER"),
       (r"artikel 47 i EU:s stadga om de grundläggande rättigheterna","CHARTER"),
       (r"artikel 41 i stadgan","CHARTER"),
       (r"förordning \(EU\) 2016/679 \(dataskyddsförordningen\)","GDPR"),(r"förordning \(EU\) 2018/1725","R1725"),
       (r"direktiv \(EU\) 2017/1371 \(PIF\)","PIF"),(r"rådets förordning \(EU\) 2017/1939","EPPO"),
       (r"förordning \(EU\) nr 910/2014 \(eIDAS\)","EIDAS"),(r"eIDAS-förordningen \(nr 910/2014\)","EIDAS"),
       (r"artikel 325 FEUF","TFEU325"),(r"art\. 263 FEUF","TFEU263")],
 "de":[(r"Verordnung \(EG\) Nr\. 1049/2001","R1049"),(r"Verordnung 1049/2001","R1049"),
       (r"Artikel 7 Absatz 2","R1049"),(r"Art\. 7 Abs\. 2","R1049"),
       (r"Artikel 4 Absatz 6","R1049"),(r"Art\. 4 Abs\. 6","R1049"),
       (r"Art\. 2 Abs\. 1 der Verordnung \(EG\) Nr\. 1049/2001","R1049"),
       (r"Artikel 15 AEUV","TFEU15"),(r"Art\. 15 Abs\. 3 AEUV","TFEU15"),
       (r"Artikel 42 der Charta der Grundrechte der Europäischen Union","CHARTER"),
       (r"Art\. 42 der Charta der Grundrechte der EU","CHARTER"),
       (r"Artikel 41 der Charta der Grundrechte der Europäischen Union","CHARTER"),
       (r"Artikel 47 der Charta der Grundrechte der Europäischen Union","CHARTER"),
       (r"Artikel 41 und 47 der Charta der Grundrechte","CHARTER"),
       (r"Artikel 47 der Charta der Grundrechte der EU","CHARTER"),(r"Artikel 41 der Charta","CHARTER"),
       (r"Verordnung \(EU\) 2016/679 \(DSGVO\)","GDPR"),(r"Verordnung \(EU\) 2018/1725","R1725"),
       (r"Richtlinie \(EU\) 2017/1371 \(PIF\)","PIF"),(r"Verordnung \(EU\) 2017/1939","EPPO"),
       (r"Verordnung \(EU\) Nr\. 910/2014 \(eIDAS\)","EIDAS"),(r"eIDAS-Verordnung \(Nr\. 910/2014\)","EIDAS"),
       (r"Artikel 325 AEUV","TFEU325"),(r"Art\. 263 AEUV","TFEU263")],
}
OMB = {"sv":(r"Europeiska ombudsmannen",), "fr":(r"Médiateur européen",), "it":(r"Mediatore europeo",), "es":(r"Defensor del Pueblo Europeo",), "pl":(r"Europejskiego Rzecznika Praw Obywatelskich",), "hr":(r"Europskom ombudsmanu|Europskim ombudsmanom",), "sk":(r"európskemu ombudsmanovi|európskym ombudsmanom",),
       "de":(r"Europäischen Bürgerbeauftragten",)}
_T = "\x00%d\x00"
def linkify(h, L):
    if L == "en": return linkify_en(h)
    keep=[]
    def stash(m):
        keep.append(m.group(0)); return _T % (len(keep)-1)
    h = re.sub(r'<a\b.*?</a>', stash, h, flags=re.S); h = re.sub(r'<[^>]+>', stash, h)
    UL = L.upper()
    tbl = list(PATS.get(L, []))
    for pat, key in tbl:
        url = f"https://eur-lex.europa.eu/legal-content/{UL}/TXT/?uri=CELEX:{CELEX[key]}"
        h = re.sub(r'(?<![\w/])(' + pat + r')(?![\w/])',
                   lambda m,u=url: f'<a href="{u}" target="_blank" rel="noopener">{m.group(1)}</a>', h)
    for pat in OMB.get(L, ()):
        h = re.sub(r'(' + pat + r')',
                   lambda m: f'<a href="https://www.ombudsman.europa.eu/" target="_blank" rel="noopener">{m.group(1)}</a>', h)
    for pat in (r"C-404/10 P", r"C-477/10 P"):
        num = pat.replace(" P","")
        h = re.sub(r'(' + pat + r')',
                   lambda m,n=num: f'<a href="https://curia.europa.eu/juris/liste.jsf?num={n}" target="_blank" rel="noopener">{m.group(1)}</a>', h)
    h = re.sub(r'(M\.10815)(?! –)',
               lambda m: f'<a href="https://competition-cases.ec.europa.eu/cases/M.10815" target="_blank" rel="noopener">{m.group(1)}</a>', h, count=1)
    for i,v in enumerate(keep): h = h.replace(_T % i, v)
    return h

def gt(d):   # d: lang -> text  -> inline .gtl
    return "".join(f'<span class="gtl {L}">{d.get(L, d["en"])}</span>' for L in ACTIVE)
def ui(idx):
    return gt({L: html.escape(UI.get(L, UI["en"])[idx]) if idx != 4 else UI.get(L, UI["en"])[idx] for L in ACTIVE})

def subj(i, m):
    return gt({L: html.escape(m["subject"] if L=="en" else MOD[L].SUBJ[i]) for L in ACTIVE})
def badge(i, m):
    lab = m["badge"][1]
    return ('<span class="badge badge-%s">%s</span>' % (m["badge"][0],
            gt({L: html.escape(lab if L=="en" else MOD[L].BADGE[lab]) for L in ACTIVE})))
def omark(i):
    o = ORIG[i]
    return '<span class="omark">' + gt({L: MARK[L][0] if L in o else MARK[L][1] for L in ACTIVE}) + '</span>'
def body(i, m):
    out = []
    for L in ACTIVE:
        raw = m["body"].strip() if L=="en" else MOD[L].BODY[i].strip()
        out.append(f'<div class="gtl-b {L}">{linkify(raw, L)}</div>')
    return "".join(out)

def bubble(i, m):
    att = ""
    if m.get("att"):
        att = ('<div class="att"><span class="attl">' + ui(0) + '</span>'
               + "".join(f'<span class="attf">{html.escape(a)}</span>' for a in m["att"]) + '</div>')
    ext = ""
    if i in EXT:
        rows = []
        for label, url, st in EXT[i]:
            if st == "ok":
                rows.append(f'<span class="extf"><a href="{url}" target="_blank" rel="noopener">{html.escape(label)}</a></span>')
            else:
                rows.append('<span class="extf trunc">' + html.escape(label) + ' <em>'
                            + gt({L: html.escape(UI.get(L, UI["en"])[4]) for L in ACTIVE}) + '</em></span>')
        ext = '<div class="att"><span class="attl">' + ui(1) + '</span>' + "".join(rows) + '</div>'
    note = f'<div class="ref-box">{html.escape(m["note"])}</div>' if m.get("note") else ""
    src = (f'<a class="src" href="{SRC}#{m["anchor"]}" target="_blank" rel="noopener">source</a>'
           if m.get("anchor") else "")
    return f"""<div class="msg {m['who']}" id="msg-{i+1}">
<div class="bubble">
 <div class="subject">{subj(i,m)}</div>
 <div class="sender"><span class="sender-name">{html.escape(m['name'])}</span>
  <span class="sender-date">{m['date']}</span>{badge(i,m)}{src}</div>
 {omark(i)}
 {body(i,m)}
 {note}{att}{ext}
</div></div>"""

parts = []
for i, m in enumerate(M):
    if i in PH_EN:
        parts.append('<div class="phase-label"><span>%s</span></div>'
                     % gt({L: (PH_EN[i] if L=="en" else MOD[L].PHASES[i]) for L in ACTIVE}))
    parts.append(bubble(i, m))

show_in = "".join(f'body[data-lang="{L}"] .gtl.{L}' + ("," if L!=ACTIVE[-1] else "") for L in ACTIVE)
show_bl = "".join(f'body[data-lang="{L}"] .gtl-b.{L}' + ("," if L!=ACTIVE[-1] else "") for L in ACTIVE)
EXTRA = f"""
.src{{font-size:11px;color:#7a8899;text-decoration:none;border-bottom:1px dotted #b9c4d1}}
.src:hover{{color:var(--navy)}}
.att{{margin-top:12px;padding-top:10px;border-top:1px dashed var(--border);font-size:12px;color:#555}}
.attl{{display:block;font-weight:700;text-transform:uppercase;letter-spacing:.5px;font-size:11px;color:#7a8899;margin-bottom:4px}}
.attf{{display:block;padding-left:16px;position:relative}}
.attf::before{{content:'\\1F4CE';position:absolute;left:0}}
.extf{{display:block;padding-left:16px;position:relative;margin-bottom:3px}}
.extf::before{{content:'\\1F517';position:absolute;left:0}}
.extf.trunc{{color:#8a8a8a}}.extf.trunc em{{font-size:11px}}
.omark{{display:block;font-size:11px;margin:0 0 10px;padding:4px 9px;border-radius:3px;
 background:#eef2f7;color:#54637a;border-left:3px solid #b9c4d1}}
.omark b{{color:var(--navy)}}
.anal{{scroll-margin-top:74px;margin:34px 0 0;padding:26px 30px;background:#fff;border:1px solid var(--border);
 border-top:4px solid var(--red);border-radius:4px}}
.lbanal{{border-bottom:1px solid rgba(255,255,255,.45)}}
.lbanal:hover{{border-bottom-color:#fff}}
.anal h3{{margin:0 0 14px;font-size:21px;color:var(--navy);letter-spacing:-.01em}}
.anal h4{{margin:20px 0 6px;font-size:15px;color:var(--navy)}}
.anal p{{margin:0 0 10px;line-height:1.62}}
.anal .lead{{font-size:15px;color:#333;padding-bottom:6px;border-bottom:1px solid var(--border)}}
.anal .closing{{margin-top:18px;padding:12px 16px;background:var(--yellow);border-radius:4px}}
.note-verbatim{{background:var(--yellow);border:1px solid #f0c040;border-radius:4px;padding:12px 16px;margin:0 0 26px;font-size:13px}}
.gtl-b{{display:none}}
{show_in}{{display:inline}}
{show_bl}{{display:block}}
"""
NOTE = {
 "en":"<strong>Full record.</strong> Every message is reproduced in full; nothing has been shortened or paraphrased. Removed are only the platform elements of AskTheEU. Under each flag every message carries a marker: the language in which the message was actually sent or received is labelled <b>ORIGINAL</b>; every other language is labelled <b>COPY OF THE ORIGINAL — translation</b> and serves for comprehension only. In case of discrepancy, the original prevails.",
 "sk":"<strong>Úplný záznam.</strong> Každá správa je uvedená v plnom znení; nič nie je skrátené ani preformulované. Odstránené sú výlučne prvky platformy AskTheEU. Pod každou vlajkou má každá správa označenie: jazyk, v ktorom bola správa skutočne odoslaná alebo doručená, je označený ako <b>ORIGINÁL</b>; každý ďalší jazyk je označený ako <b>KÓPIA ORIGINÁLU — preklad</b> a slúži len na porozumenie. V prípade rozporu má prednosť originál.",
 "hr":"<strong>Cjelovit zapis.</strong> Svaka je poruka navedena u punom tekstu; ništa nije skraćeno ni preoblikovano. Uklonjeni su isključivo elementi platforme AskTheEU. Pod svakom zastavom svaka poruka nosi oznaku: jezik na kojem je poruka doista poslana ili primljena označen je kao <b>IZVORNIK</b>; svaki drugi jezik označen je kao <b>PRESLIKA IZVORNIKA — prijevod</b> i služi samo za razumijevanje. U slučaju neslaganja prednost ima izvornik.",
 "pl":"<strong>Pełny zapis.</strong> Każda wiadomość podana jest w pełnym brzmieniu; nic nie zostało skrócone ani przeredagowane. Usunięto wyłącznie elementy platformy AskTheEU. Pod każdą flagą każda wiadomość nosi oznaczenie: język, w którym wiadomość rzeczywiście wysłano lub otrzymano, oznaczono jako <b>ORYGINAŁ</b>; każdy inny język oznaczono jako <b>KOPIA ORYGINAŁU — tłumaczenie</b> i służy on wyłącznie do zrozumienia treści. W razie rozbieżności pierwszeństwo ma oryginał.",
 "es":"<strong>Expediente completo.</strong> Cada mensaje se reproduce íntegramente; nada se ha abreviado ni reformulado. Solo se han eliminado los elementos de la plataforma AskTheEU. Bajo cada bandera, cada mensaje lleva una marca: la lengua en la que el mensaje fue realmente enviado o recibido se señala como <b>ORIGINAL</b>; cualquier otra lengua se señala como <b>COPIA DEL ORIGINAL — traducción</b> y sirve únicamente para la comprensión. En caso de discrepancia prevalece el original.",
 "it":"<strong>Fascicolo completo.</strong> Ogni messaggio è riportato integralmente; nulla è stato abbreviato o riformulato. Sono stati rimossi soltanto gli elementi della piattaforma AskTheEU. Sotto ogni bandiera ciascun messaggio reca un contrassegno: la lingua in cui il messaggio è stato effettivamente inviato o ricevuto è indicata come <b>ORIGINALE</b>; ogni altra lingua è indicata come <b>COPIA DELL'ORIGINALE — traduzione</b> e serve unicamente alla comprensione. In caso di discordanza prevale l'originale.",
 "fr":"<strong>Dossier complet.</strong> Chaque message est reproduit intégralement ; rien n'a été abrégé ni reformulé. Seuls les éléments de la plateforme AskTheEU ont été retirés. Sous chaque drapeau, chaque message porte une mention : la langue dans laquelle le message a effectivement été envoyé ou reçu est signalée comme <b>ORIGINAL</b> ; toute autre langue est signalée comme <b>COPIE DE L'ORIGINAL — traduction</b> et ne sert qu'à la compréhension. En cas de divergence, l'original prévaut.",
 "sv":"<strong>Fullständig akt.</strong> Varje meddelande återges i sin helhet; ingenting har förkortats eller omformulerats. Endast plattformselementen från AskTheEU har tagits bort. Under varje flagga bär varje meddelande en märkning: det språk på vilket meddelandet faktiskt skickades eller mottogs anges som <b>ORIGINAL</b>; varje annat språk anges som <b>KOPIA AV ORIGINALET — översättning</b> och tjänar endast förståelsen. Vid avvikelse har originalet företräde.",
 "de":"<strong>Vollständiger Vorgang.</strong> Jede Nachricht ist im vollen Wortlaut wiedergegeben; nichts wurde gekürzt oder umformuliert. Entfernt wurden ausschließlich die Plattformelemente von AskTheEU. Unter jeder Flagge trägt jede Nachricht eine Kennzeichnung: die Sprache, in der die Nachricht tatsächlich gesendet oder empfangen wurde, ist als <b>ORIGINAL</b> gekennzeichnet; jede weitere Sprache als <b>KOPIE DES ORIGINALS — Übersetzung</b> und dient allein dem Verständnis. Im Widerspruchsfall geht das Original vor.",
}
flags = "".join(
 f'<button class="lbf{" active" if L=="en" else ""}" data-lang="{L}" title="{L.upper()}">'
 f'<img src="https://flagcdn.com/{FLAG[L]}.svg" alt="{L.upper()}"></button>' for L in ACTIVE)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DG COMP · M.10815 — full correspondence (EASE 2025/6534)</title>
<style>
{CSS}
{EXTRA}
</style></head>
<body data-lang="en">

<div id="langbar"><div class="lbinner">
<a class="lbhome" href="https://foxprof.club/kauzy-koncept/">{ui(2)}</a>
<div class="lbflags"><span class="lbl">Lang</span>{flags}</div>
<a class="lbhome lbanal" href="#anal">⚖ {gt({L: html.escape(analyza.TITLE[L]) for L in ACTIVE})}</a>
</div></div>

<div class="case-header">
<h1>Request for access to documents — Case M.10815<br>
Deutsche Telekom / Orange / Telefónica / Vodafone — Joint Venture</h1>
<div class="meta">{ui(5)}: Peter Ferenc · {ui(6)}: European Commission, DG Competition, Unit C.5 Mergers ·
Secretariat-General, Transparency Unit<br>
{ui(7)}: Regulation (EC) No 1049/2001 · Art. 15(3) TFEU · Art. 42 Charter<br>
{ui(8)}: AskTheEU.org — 10.12.2025 → 20.07.2026 · {len(M)} {ui(9)}</div>
<div class="ref">EASE 2025/6534 · COMP/C5/LC/(2025)/6534 · TFIA-2026-JV-009</div>
</div>

<div class="note-verbatim">{"".join(f'<span class="gtl-b {L}">{NOTE.get(L, NOTE["en"])}</span>' for L in ACTIVE)}</div>

<div class="timeline">
{chr(10).join(parts)}
</div>

<div class="anal" id="anal">
{"".join('<div class="gtl-b %s"><h3>%s</h3>%s</div>' % (L, html.escape(analyza.TITLE[L]), linkify(analyza.ANALYSIS[L].strip(), L)) for L in ACTIVE)}
</div>

<div class="case-footer">
FIA FOX — Fair Internet Alliance · <a href="https://foxprof.club/">foxprof.club</a><br>
{ui(10)}: <a href="{SRC}" target="_blank" rel="noopener">asktheeu.org</a> · M.10815 · EASE 2025/6534
</div>

<script>
document.querySelectorAll('button.lbf').forEach(function(b){{
  b.addEventListener('click',function(){{
    document.body.dataset.lang=b.dataset.lang;
    document.documentElement.lang=b.dataset.lang;
    document.querySelectorAll('button.lbf').forEach(function(x){{x.classList.remove('active');}});
    b.classList.add('active');
  }});
}});
</script>
</body></html>"""
open('dgcomp-correspondence-full.html','w',encoding='utf-8').write(HTML)
print("jazyky:", ", ".join(x.upper() for x in ACTIVE), "|", len(HTML), "znakov |", len(M), "sprav")
