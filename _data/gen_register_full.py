#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Register FIA FOX — dlazdice kauz + rozbalovacie karty konani so vsetkymi poliami.
   Rozlozenie kopiruje zabehnuty system z #303."""
import json, os, html, urllib.parse, hashlib

L9 = ["de","en","sk","hr","pl","es","it","fr","sv"]
FLAG = {"de":"de","en":"gb","sk":"sk","hr":"hr","pl":"pl","es":"es","it":"it","fr":"fr","sv":"se"}
VIEWER = "https://peterferenc246-design.github.io/fia/viewer.html"
WP_KOMENT = "https://foxprof.club/kauzy-koncept/"

D = json.load(open('fia_data.json', encoding='utf-8'))
KARTY, POLOZKY, SUHRNY = D["karty"], D["polozky"], D.get("suhrny", {})
KAUZY = D.get("kauzy_reg", [])

def S(*v): return dict(zip(L9, v))
def g(d):
    if not d: return ""
    fb = d.get("sk") or d.get("de") or d.get("en") or next(iter(d.values()), "")
    return "".join(f'<span class="gtl {L}">{d.get(L) or fb}</span>' for L in L9)
def gb(d):
    if not d: return ""
    fb = d.get("sk") or d.get("de") or next(iter(d.values()), "")
    return "".join(f'<div class="gtl-b {L}">{d.get(L) or fb}</div>' for L in L9)

UI = {
 "reg":  S("Fallregister","Case register","Register káuz","Registar predmeta","Rejestr spraw","Registro de casos","Registro dei casi","Registre des affaires","Ärenderegister"),
 "home": S("← Zur Startseite","← Home","← Späť na úvod","← Naslovnica","← Strona główna","← Inicio","← Home","← Accueil","← Startsidan"),
 "all":  S("Alle","All","Všetko","Sve","Wszystko","Todo","Tutti","Tout","Alla"),
 "jde":  S("Deutschland","Germany","Nemecko","Njemačka","Niemcy","Alemania","Germania","Allemagne","Tyskland"),
 "jsk":  S("Slowakei","Slovakia","Slovensko","Slovačka","Słowacja","Eslovaquia","Slovacchia","Slovaquie","Slovakien"),
 "jeu":  S("EU","EU","EÚ","EU","UE","UE","UE","UE","EU"),
 "allv": S("Alle Fälle anzeigen","Show all cases","Zobraziť všetky kauzy","Prikaži sve predmete","Pokaż wszystkie sprawy","Mostrar todos","Mostra tutti","Tout afficher","Visa alla"),
 "verf": S("Verfahren","proceedings","konania","postupci","postępowania","procedimientos","procedimenti","procédures","förfaranden"),
 "docs": S("Dokumente","documents","dokumentov","dokumenata","dokumentów","documentos","documenti","documents","handlingar"),
 "komu": S("AKTENKOMMUNIKATION","CASE CORRESPONDENCE","SPISOVÁ KOMUNIKÁCIA","KORESPONDENCIJA SPISA","KORESPONDENCJA AKT","CORRESPONDENCIA DEL EXPEDIENTE","CORRISPONDENZA DEL FASCICOLO","CORRESPONDANCE DU DOSSIER","AKTKORRESPONDENS"),
 "sent": S("Gesendet","Sent","Odoslané","Poslano","Wysłane","Enviados","Inviati","Envoyés","Skickat"),
 "recv": S("Eingegangen","Received","Prijaté","Primljeno","Otrzymane","Recibidos","Ricevuti","Reçus","Mottaget"),
 "nores":S("Noch keine Antwort — Empfangsbestätigung wird erwartet.","No reply yet — acknowledgement of receipt expected.","Zatiaľ bez odpovede — potvrdenie príjmu sa očakáva.","Zasad bez odgovora — očekuje se potvrda primitka.","Na razie bez odpowiedzi — oczekiwane potwierdzenie odbioru.","Aún sin respuesta — se espera el acuse de recibo.","Ancora nessuna risposta — si attende la ricevuta.","Pas encore de réponse — accusé de réception attendu.","Ännu inget svar — mottagningsbekräftelse väntas."),
 "open": S("Dokument öffnen","Open document","Otvoriť dokument","Otvori dokument","Otwórz dokument","Abrir documento","Apri documento","Ouvrir le document","Öppna handling"),
 "orig": S("Signiertes Original (QES)","Signed original (QES)","Podpísaný originál (QES)","Potpisani izvornik (QES)","Podpisany oryginał (QES)","Original firmado (QES)","Originale firmato (QES)","Original signé (QES)","Signerat original (QES)"),
 "sum":  S("Zusammenfassung","Summary","Súhrn","Sažetak","Streszczenie","Resumen","Riepilogo","Résumé","Sammanfattning"),
 "kom":  S("Kommentieren","Comment","Komentovať","Komentiraj","Skomentuj","Comentar","Commenta","Commenter","Kommentera"),
 "beg":  S("Begleittext","Cover note","Sprievodný text","Popratni tekst","Tekst przewodni","Nota adjunta","Nota di accompagnamento","Note d'accompagnement","Följebrev"),
 "share":S("Teilen","Share","Zdieľať","Podijeli","Udostępnij","Compartir","Condividi","Partager","Dela"),
 "pin":  S("Angeheftet","Pinned","Pripnuté","Prikvačeno","Przypięte","Fijado","In evidenza","Épinglé","Fäst"),
 "org":  S("Behörde","Authority","Orgán","Tijelo","Organ","Autoridad","Autorità","Autorité","Myndighet"),
 "obl":  S("Bereich","Area","Oblasť","Područje","Obszar","Ámbito","Ambito","Domaine","Område"),
 "our":  S("Unser Az.","Our ref.","Naša spis. zn.","Naš broj","Nasza sygn.","Ntra. ref.","Ns. rif.","Notre réf.","Vårt nr"),
 "pub":  S("Öffentlich","Public","Verejné","Javno","Publiczne","Público","Pubblico","Public","Offentlig"),
 "obl_k":S("Kartellrecht","Competition law","Kartelové právo","Pravo tržišnog natjecanja","Prawo kartelowe","Derecho de la competencia","Diritto della concorrenza","Droit de la concurrence","Konkurrensrätt"),
 "obl_g":S("DSGVO","GDPR","GDPR","GDPR","RODO","RGPD","GDPR","RGPD","Dataskydd"),
 "obl_s":S("Strafanzeige","Criminal complaint","Trestné oznámenie","Kaznena prijava","Zawiadomienie o przestępstwie","Denuncia penal","Denuncia penale","Plainte pénale","Brottsanmälan"),
 "obl_m":S("Eingriff in Eigentumsrechte","Interference with property rights","Zasahovanie do majetkových práv občana","Zadiranje u imovinska prava","Ingerencja w prawa majątkowe","Injerencia en derechos patrimoniales","Lesione dei diritti patrimoniali","Atteinte aux droits patrimoniaux","Ingrepp i egendomsrätt"),
 "sort": S("SORTIEREN","SORT","ZORADIŤ","SORTIRAJ","SORTUJ","ORDENAR","ORDINA","TRIER","SORTERA"),
 "s_dat":S("📅 Älteste","📅 Oldest","📅 Najstaršie","📅 Najstarije","📅 Najstarsze","📅 Más antiguos","📅 Più vecchi","📅 Plus anciens","📅 Äldsta"),
 "s_az": S("🏛 Az.","🏛 File ref.","🏛 Sp. zn.","🏛 Broj","🏛 Sygn.","🏛 Ref.","🏛 Rif.","🏛 Réf.","🏛 Nr"),
 "s_our":S("🦊 Unser Az.","🦊 Our ref.","🦊 Naša spis. zn.","🦊 Naš broj","🦊 Nasza sygn.","🦊 Ntra. ref.","🦊 Ns. rif.","🦊 Notre réf.","🦊 Vårt nr"),
 "s_obl":S("🗂 Bereich","🗂 Area","🗂 Oblasť","🗂 Područje","🗂 Obszar","🗂 Ámbito","🗂 Ambito","🗂 Domaine","🗂 Område"),
 "s_new":S("↓ Neueste","↓ Newest","↓ Najnovšie","↓ Najnovije","↓ Najnowsze","↓ Más recientes","↓ Più recenti","↓ Plus récents","↓ Nyaste"),
 "in_new":S("Neueste","Newest","Najnovšie","Najnovije","Najnowsze","Recientes","Recenti","Récents","Nyaste"),
 "in_old":S("Älteste","Oldest","Najstaršie","Najstarije","Najstarsze","Antiguos","Vecchi","Anciens","Äldsta"),
 "pw":   S("Passwort","Password","Heslo","Lozinka","Hasło","Contraseña","Password","Mot de passe","Lösenord"),
}
STAV = {"laeuft":S("Läuft","Pending","Prebieha","U tijeku","W toku","En curso","In corso","En cours","Pågår"),
 "eingereicht":S("Eingereicht","Filed","Podané","Podneseno","Złożone","Presentado","Depositata","Déposée","Inlämnad"),
 "erledigt":S("Erledigt","Closed","Vybavené","Riješeno","Załatwione","Resuelto","Evaso","Traité","Avslutat"),
 "abgelehnt":S("Abgelehnt","Refused","Zamietnuté","Odbijeno","Odmowa","Denegado","Respinto","Refusé","Avslag")}
PILL = {"laeuft":"p-blue","eingereicht":"p-amber","erledigt":"p-green","abgelehnt":"p-red"}

def dkey(v):
    v = (v or "").strip()
    import re
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', v)
    if m: return m.group(1)+m.group(2)+m.group(3)
    m = re.match(r'^(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})$', v)
    if m: return m.group(3)+m.group(2).zfill(2)+m.group(1).zfill(2)
    return "00000000"

def jflag(j):
    return '<span class="jf">🇪🇺</span>' if j=="eu" else f'<img class="jf" src="https://flagcdn.com/{FLAG.get(j,"de")}.svg" alt="{j}">'

pol_karty = {}
for p in POLOZKY: pol_karty.setdefault(p.get("karta",""), []).append(p)
karta_by_id = {k["id"]: k for k in KARTY}
def kauza_karty(cid):
    for z in KAUZY:
        if cid in (z.get("ids") or []): return z
    return None

# ───────────── POLOŽKA ─────────────
def polozka(p, n):
    st = p.get("stav") or "laeuft"
    doc = "".join(
        f'<span class="gtl {L}"><a class="ib" href="{html.escape((p.get("urls") or {}).get(L,""))}" '
        f'target="_blank" rel="noopener">📄 {UI["open"][L]}</a></span>'
        for L in L9 if (p.get("urls") or {}).get(L))
    og = ""
    if p.get("orig"):
        u = VIEWER + "?doc=" + urllib.parse.quote(p["orig"], safe="")
        og = f'<a class="ib og" href="{html.escape(u)}" target="_blank" rel="noopener">✍ {g(UI["orig"])}</a>'
    sm = ""
    sid = p.get("summodId","")
    if sid and sid in SUHRNY:
        sm = (f'<button class="ib" onclick="document.getElementById(\'s{n}\').classList.toggle(\'on\')">'
              f'📄 {g(UI["sum"])}</button>')
    kom = f'<button class="ib kom" onclick="toggleCmt(this)">💬 {g(UI["kom"])}</button>'
    subox = f'<div class="sumbox" id="s{n}">{gb(SUHRNY.get(sid, {}))}</div>' if sm else ""
    fn = ""  # nazov suboru sa na verejnom registri nezobrazuje (admin ho vidi v editore)
    acc = ("pw" if p.get("access")=="pw" else "pub")
    subj_sk = (p.get("subj9") or {}).get("sk") or next((v for v in (p.get("subj9") or {}).values() if v), "")
    cid = "fia-" + hashlib.sha1((str(p.get("karta",""))+"|"+str(p.get("date",""))+"|"+subj_sk).encode("utf-8")).hexdigest()[:12]
    ctitle = (subj_sk + " · " + p.get("date","")).strip(" ·")
    thr = f' data-d="{dkey(p.get("date",""))}" data-cid="{cid}" data-ctitle="{html.escape(ctitle)}"'
    if p.get("thread"): thr += f' data-thread="{html.escape(p["thread"])}"'
    return (f'<div class="it{" imp" if p.get("dolezite") else ""}"{thr}>'
            f'<div class="ih"><span class="idt">{html.escape(p.get("date",""))}</span>'
            f'<span class="acc acc-{acc}">{"🔒" if acc=="pw" else "🌐"} {g(UI["pw"] if acc=="pw" else UI["pub"])}</span></div>'
            f'<div class="isj">{"❗ " if p.get("dolezite") else ""}{g(p.get("subj9") or {})}</div>'
            + (f'<div class="iorg">⚖ <b>{g(UI["org"])}:</b> {html.escape(p.get("court",""))}</div>' if p.get("court") else "")
            + fn +
            f'<div class="ibt">{doc}{sm}{kom}</div>{subox}<div class="cmt-wrap"></div></div>')

# ───────────── KARTA ─────────────
def karta(cid, ps, otvorena=False):
    k = karta_by_id.get(cid, {})
    z = kauza_karty(cid)
    st = (ps[0].get("stav") if ps else "") or "laeuft"
    sent = sorted([p for p in ps if p.get("dir")=="sent"], key=lambda x: dkey(x.get("date")), reverse=True)
    recv = sorted([p for p in ps if p.get("dir")!="sent"], key=lambda x: dkey(x.get("date")), reverse=True)
    pin = (f'<span class="pill p-gold">📌 {g(UI["pin"])} <b>{k.get("pin")}</b></span>' if k.get("pin") else "")
    meta = k.get("meta") or {}
    if not any(meta.values()):
        meta = {L: f'⚖️ <b>{UI["org"][L]}:</b> {html.escape(k.get("organ_txt",""))}' for L in L9}
    global CIT
    hs = ""
    for p in sent: CIT += 1; hs += polozka(p, CIT)
    hr = ""
    for p in recv: CIT += 1; hr += polozka(p, CIT)
    if not hr: hr = f'<p class="prazdne">{g(UI["nores"])}</p>'
    beg = (f'<button class="cb" onclick="document.getElementById(\'b-{cid}\').classList.toggle(\'on\')">'
           f'📝 {g(UI["beg"])}</button>' if any((k.get("sprievodny") or {}).values()) else "")
    begbox = (f'<div class="begbox" id="b-{cid}">{gb(k.get("sprievodny") or {})}</div>'
              if any((k.get("sprievodny") or {}).values()) else "")
    return (f'<details class="case" id="{cid}"{" open" if otvorena else ""} data-kz="{z["spis"] if z else ""}" '
            f'data-jur="{" ".join(k.get("jur") or [])}" data-d="{dkey(k.get("date",""))}" data-az="{html.escape(k.get("az","") or "zzz")}" data-our="{html.escape(k.get("ourref","") or "zzz")}" data-obl="{" ".join(k.get("area") or [])}" data-pin="{k.get("pin") or ""}">'
            f'<summary class="chead"><div class="cl">'
            f'<div class="ct"><span class="cdate">📅 {html.escape(k.get("datum_txt") or k.get("date",""))}</span>{g(k.get("nazov") or {})}</div>'
            + (f'<div class="csub">{g(k.get("podtitul") or {})}</div>' if any((k.get("podtitul") or {}).values()) else "")
            + f'<div class="cmeta">{g(meta)}'
            + ("" if ("Oblas" in (meta.get("sk") or "") or "Bereich" in (meta.get("de") or ""))
                 else (f' · <b>{g(UI["obl"])}:</b> {" ".join(k.get("area") or [])}' if k.get("area") else ""))
            + ("" if ("spis. zn" in (meta.get("sk") or "") or "Az." in (meta.get("de") or ""))
                 else (f' · <b>{g(UI["our"])}:</b> {html.escape(k.get("ourref",""))}' if k.get("ourref") else ""))
            + f'</div></div><div class="cr">{pin}'
            f'<span class="pill {PILL.get(st,"p-blue")}">{g(k.get("stav") or STAV.get(st, STAV["laeuft"]))}</span>'
            f'<span class="chev">▾</span></div></summary>'
            f'<div class="cbody"><div class="komu"><span class="komu-t">{g(UI["komu"])}</span>'
            f'<button class="isb"><span class="lb-new">↓ {g(UI["in_new"])}</span>'
            f'<span class="lb-old">↑ {g(UI["in_old"])}</span></button></div>'
            f'<div class="cols"><div class="col"><h4>↗ {g(UI["sent"])} <span class="cnt">{len(sent)}</span></h4>{hs}</div>'
            f'<div class="col"><h4>↙ {g(UI["recv"])} <span class="cnt">{len(recv)}</span></h4>{hr}</div></div>'
            f'<div class="cbtns">{beg}<a class="cb" href="{WP_KOMENT}" target="_blank" rel="noopener">↗ {g(UI["share"])}</a></div>'
            f'{begbox}</div></details>')

CSS = """
:root{--navy:#1F3864;--red:#C00000;--gold:#f0c040;--bd:#c9d8e8;--muted:#6B7C91}
*{box-sizing:border-box}
body{margin:0;color:#34435A;font:15px/1.55 "Segoe UI",Calibri,Arial,sans-serif;
 background:linear-gradient(#8ec5ea 0,#b9dcf3 30%,#dcecf8 58%,#f3e9d6 100%);background-attachment:fixed;min-height:100vh}
.top{text-align:center;padding:18px 16px 2px}
.top h1{margin:0;font-size:21px;color:var(--navy);font-weight:800}
.wrap{max-width:1020px;margin:0 auto;padding:0 16px 50px}
.navbar{background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(31,56,100,.10);padding:9px 14px;
 display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.hm{border:1px solid var(--bd);border-radius:6px;padding:5px 14px;text-decoration:none;color:var(--navy);font-size:13px}
.lang{display:flex;align-items:center;gap:5px;flex-wrap:wrap}
.lang .lb{font-size:10px;color:#8a97a6;letter-spacing:.12em;margin-right:3px}
.f{background:none;border:1px solid rgba(31,56,100,.3);border-radius:3px;padding:0;cursor:pointer;width:30px;height:20px;opacity:.5;overflow:hidden}
.f img{width:30px;height:20px;object-fit:cover;display:block}
.f.on{opacity:1;border-color:var(--navy);box-shadow:0 0 0 2px rgba(31,56,100,.25)}
.panel{background:rgba(242,246,252,.97);border:1px solid rgba(31,56,100,.12);border-radius:14px;
 padding:12px 16px 14px;margin-bottom:18px;box-shadow:0 6px 18px rgba(31,56,100,.10)}
.panel h2{font-size:19px;color:var(--navy);font-weight:800;margin:0 0 11px}
.cnt2{font-size:12px;font-weight:600;color:var(--muted);margin-left:8px}
.tabs{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:12px}
.tab{cursor:pointer;border:2px solid transparent;border-radius:8px;background:#fff;padding:4px 10px;
 display:inline-flex;align-items:center;gap:6px;font:inherit;font-size:12.5px;font-weight:700;color:var(--navy);box-shadow:0 1px 3px rgba(0,0,0,.12)}
.tab.on{border-color:#FFCB3E;box-shadow:0 0 0 3px rgba(255,203,62,.45)}
.tab img{width:24px;height:auto;border-radius:2px}
.rall{grid-column:1/-1;border-left-color:#FFCB3E!important;background:linear-gradient(135deg,#fff,#FFF8E6)!important}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(218px,1fr));gap:9px}
.tile{display:flex;flex-direction:column;align-items:flex-start;gap:3px;text-align:left;cursor:pointer;
 border:1px solid rgba(31,56,100,.12);border-left:4px solid var(--navy);background:#fff;border-radius:10px;
 padding:9px 12px;font:inherit;line-height:1.2}
.tile:hover{transform:translateY(-2px);box-shadow:0 6px 15px rgba(31,56,100,.13)}
.tile.on{border-color:#FFCB3E;border-left-color:#FFCB3E;background:linear-gradient(135deg,#fff,#FFF8E6);
 box-shadow:0 0 0 3px rgba(255,203,62,.45),0 2px 6px rgba(0,0,0,.16)}
.tile.on .tn{color:#8a5a00}
.tile .tf{display:flex;gap:4px;margin-bottom:2px}
.jf{width:17px;height:12px;object-fit:cover;border-radius:2px;font-size:12px;line-height:1}
.tile .tn{font-size:13.5px;font-weight:700;color:var(--navy)}
.tile .ts{font-size:10.5px;font-weight:600;color:var(--muted);font-family:Consolas,"Courier New",monospace}
.tile .tw{font-size:11px;color:var(--red);font-style:italic;font-weight:700;margin-top:3px}
.tile .tc{font-size:11px;color:#54637a;background:#eef2f7;border-radius:999px;padding:1px 9px;margin-top:5px}
.case{background:#fff;border:1px solid var(--bd);border-radius:10px;margin-bottom:11px;overflow:hidden;
 box-shadow:0 2px 8px rgba(31,56,100,.08)}
.case[open]{box-shadow:0 4px 16px rgba(31,56,100,.14)}
.case[data-pin]:not([data-pin=""]){border-left:4px solid #f5b722}
.chead{cursor:pointer;list-style:none;display:flex;gap:14px;align-items:flex-start;padding:13px 16px;background:#f7fafd}
.chead::-webkit-details-marker{display:none}
.cl{flex:1}
.ct{font-size:16px;font-weight:700;color:var(--navy);line-height:1.35}
.cdate{font-size:12.5px;color:var(--muted);font-weight:600;margin-right:8px;white-space:nowrap}
.csub{font-size:13.5px;font-weight:600;color:var(--navy);margin:3px 0}
.cmeta{font-size:12.5px;color:var(--muted);margin-top:3px}
.cr{display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.pill{font-size:11.5px;border-radius:999px;padding:2px 11px;font-weight:700;white-space:nowrap}
.p-blue{background:#e7effa;color:#1F3864;border:1px solid #bcd0ea}
.p-amber{background:#fff3d6;color:#8a5a00;border:1px solid var(--gold)}
.p-green{background:#e9f7ef;color:#0B7A3B;border:1px solid #b7e2c8}
.p-red{background:#fdeaea;color:#8a1c1c;border:1px solid #f0b8b8}
.p-gold{background:linear-gradient(#ffd34d,#f5b722);color:#3a2c00;border:1px solid #e8b93a}
.chev{color:var(--muted)}
.case[open] .chev{transform:rotate(180deg);display:inline-block}
.cbody{padding:14px 16px 16px;border-top:1px solid var(--bd)}
.komu{font-size:11.5px;letter-spacing:.09em;color:var(--muted);font-weight:700;margin-bottom:9px;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.komu-t{letter-spacing:.09em}
.isb{font-size:11px;border:1px solid var(--bd);background:#fff;color:var(--navy);border-radius:5px;padding:2px 10px;cursor:pointer;font-weight:600;font-family:inherit;white-space:nowrap;letter-spacing:0}
.isb:hover{background:#f2f7fc}
.isb .lb-old{display:none}
details.case[data-iasc="1"] .isb .lb-new{display:none}
details.case[data-iasc="1"] .isb .lb-old{display:inline}
.cmt-wrap{width:100%;flex-basis:100%;margin-top:10px}
.cmt-wrap:empty{margin-top:0}
.kom.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:12px;align-items:start}
.col{min-width:0}
.it{min-width:0;overflow-wrap:anywhere}
@media(max-width:820px){.cols{grid-template-columns:1fr}}
.col{background:#fbfcfe;border:1px solid var(--bd);border-radius:8px;padding:10px 12px}
.col h4{margin:0 0 9px;font-size:13px;color:var(--navy);display:flex;justify-content:space-between}
.col h4 .cnt{background:#eef2f7;color:#54637a;border-radius:999px;padding:0 8px;font-weight:600}
.it{border-left:3px solid var(--bd);padding:8px 0 8px 11px;margin-bottom:10px}
.it.imp{border-left-color:var(--red)}
.ih{display:flex;justify-content:space-between;gap:8px;align-items:center}
.thr{display:inline-flex;align-items:center;justify-content:center;min-width:20px;height:20px;padding:0 6px;border-radius:11px;background:var(--navy);color:#fff;font-size:12px;font-weight:800;cursor:pointer;flex:0 0 auto}
.thr:hover{background:#2a4a80}
.it.thr-hl{background:#fffbe8;border-left-color:var(--gold);box-shadow:0 0 0 2px var(--gold) inset;border-radius:6px}
.idt{font-size:12.5px;color:var(--red);font-weight:700}
.acc{font-size:11px;border-radius:999px;padding:1px 9px;white-space:nowrap}
.acc-pub{background:#e9f7ef;color:#0B7A3B;border:1px solid #b7e2c8}
.acc-pw{background:#fff3d6;color:#8a5a00;border:1px solid var(--gold)}
.isj{font-size:14px;font-weight:600;color:var(--navy);margin:4px 0 3px;line-height:1.35}
.iorg{font-size:12.5px;color:var(--muted)}
.fn{font-size:11.5px;color:var(--muted);font-style:italic;background:#fffdf3;border:1px dashed var(--gold);
 border-radius:4px;padding:3px 8px;margin:5px 0}
.ibt{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px;align-items:center}
.ib{font-size:12px;text-decoration:none;border:1px solid var(--bd);background:#fff;border-radius:4px;
 padding:3px 10px;color:#3d4d5e;cursor:pointer;font-family:inherit}
.ib:hover{border-color:var(--navy);color:var(--navy)}
.ib.og{background:#fff8e6;border-color:var(--gold);color:#8a5a00}
.ib.kom{background:#eef4ff;border-color:#c3d5f5;color:#1F3864;margin-left:auto}
.sumbox,.begbox{display:none;overflow:hidden;margin-top:9px;padding:11px 13px;background:#f7fafd;border:1px solid var(--bd);
 border-radius:6px;font-size:13.5px;line-height:1.6}
.sumbox.on,.begbox.on{display:block}
.sumbox p,.begbox p{margin:0 0 9px}
.prazdne{font-size:13px;color:var(--muted);font-style:italic;margin:4px 0}
.cbtns{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.cb{font-size:13px;border:1px solid var(--bd);background:#fff;border-radius:6px;padding:6px 14px;
 cursor:pointer;text-decoration:none;color:#3d4d5e;font-family:inherit}
.cb:hover{border-color:var(--navy);color:var(--navy)}
.chips{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:0 0 10px}
.chip{font-size:12.5px;border:1px solid var(--bd);background:#fff;border-radius:999px;padding:5px 15px;
 cursor:pointer;color:#3d4d5e;font-family:inherit}
.chip:hover{border-color:var(--navy);color:var(--navy)}
.chip.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.sortbar{display:flex;gap:7px;flex-wrap:wrap;justify-content:center;align-items:center;margin:0 0 16px}
.sl{font-size:10.5px;letter-spacing:.12em;color:var(--muted);margin-right:4px}
.sb{font-size:12.5px;border:1px solid var(--bd);background:#fff;border-radius:6px;padding:5px 13px;
 cursor:pointer;color:#3d4d5e;font-family:inherit}
.sb.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.gtl,.gtl-b{display:none}
"""
SHOW = "".join(f'body[data-l="{L}"] .gtl.{L}{{display:inline}}body[data-l="{L}"] .gtl-b.{L}{{display:block}}' for L in L9)
FLAGS = "".join(f'<button class="f{" on" if L=="sk" else ""}" data-l="{L}"><img src="https://flagcdn.com/{FLAG[L]}.svg" alt="{L.upper()}"></button>' for L in L9)

CIT = 0
tiles = ""
for z in KAUZY:
    cids = [c for c in (z.get("ids") or []) if c in pol_karty or c in karta_by_id]
    nd = sum(len(pol_karty.get(c, [])) for c in cids)
    js = z.get("jur") or ["de"]
    tiles += (f'<button class="tile" data-k="{z["spis"]}" data-jur="{" ".join(js)}">'
              f'<div class="tf">{"".join(jflag(j) for j in js)}</div>'
              f'<div class="tn">{g(z.get("nazov") or {})}</div><div class="ts">{z["spis"]}</div>'
              + (f'<div class="tw">{g(z.get("warn"))}</div>' if any((z.get("warn") or {}).values()) else "")
              + f'<div class="tc">{len(cids)} {g(UI["verf"])} · {nd} {g(UI["docs"])}</div></button>')

def poradie(x):
    k = karta_by_id.get(x[0], {})
    pin = k.get("pin")
    try: pin = int(pin)
    except (TypeError, ValueError): pin = 9999
    return (pin, "9999" if pin == 9999 else "", 10**9 - int(dkey(k.get("date","")) or 0))
karty_html = "".join(karta(cid, ps) for cid, ps in
    sorted(((c, p) for c, p in pol_karty.items() if c), key=poradie))

import json as _j
kj_json = _j.dumps({z["spis"]: (z.get("jur") or []) for z in KAUZY}, ensure_ascii=False)

# Cusdis lokalizácia komentárového okna — oficiálne de/en/es/fr + vlastné sk/hr/pl/it/sv
CUS_LOCALES = {
 "de":{"powered_by":"Kommentare powered by Cusdis","post_comment":"Kommentieren","loading":"Lädt","email":"Email (optional)","nickname":"Spitzname","reply_placeholder":"Antworten...","reply_btn":"Antworten","sending":"senden...","mod_badge":"MOD","content_is_required":"Inhalt ist erforderlich","nickname_is_required":"Spitzname ist erforderlich","comment_has_been_sent":"Ihr Kommentar wurde abgeschickt. Bitte warten Sie auf die Bestätigung."},
 "en":{"powered_by":"Comments powered by Cusdis","post_comment":"Comment","loading":"Loading","email":"Email (optional)","nickname":"Nickname","reply_placeholder":"Reply...","reply_btn":"Reply","sending":"sending...","mod_badge":"MOD","content_is_required":"Content is required","nickname_is_required":"Nickname is required","comment_has_been_sent":"Your comment has been sent. Please wait for approval."},
 "sk":{"powered_by":"Komentáre poháňa Cusdis","post_comment":"Komentovať","loading":"Načítava sa","email":"E-mail (nepovinné)","nickname":"Prezývka","reply_placeholder":"Odpovedať...","reply_btn":"Odpovedať","sending":"odosiela sa...","mod_badge":"MOD","content_is_required":"Obsah je povinný","nickname_is_required":"Prezývka je povinná","comment_has_been_sent":"Váš komentár bol odoslaný. Počkajte, prosím, na schválenie."},
 "hr":{"powered_by":"Komentare pokreće Cusdis","post_comment":"Komentiraj","loading":"Učitavanje","email":"E-mail (neobavezno)","nickname":"Nadimak","reply_placeholder":"Odgovori...","reply_btn":"Odgovori","sending":"slanje...","mod_badge":"MOD","content_is_required":"Sadržaj je obavezan","nickname_is_required":"Nadimak je obavezan","comment_has_been_sent":"Vaš komentar je poslan. Pričekajte odobrenje."},
 "pl":{"powered_by":"Komentarze obsługiwane przez Cusdis","post_comment":"Skomentuj","loading":"Ładowanie","email":"E-mail (opcjonalnie)","nickname":"Pseudonim","reply_placeholder":"Odpowiedz...","reply_btn":"Odpowiedz","sending":"wysyłanie...","mod_badge":"MOD","content_is_required":"Treść jest wymagana","nickname_is_required":"Pseudonim jest wymagany","comment_has_been_sent":"Twój komentarz został wysłany. Poczekaj na zatwierdzenie."},
 "es":{"powered_by":"Desarrollado por Cusdis","post_comment":"Comentar","loading":"Cargando","email":"Correo electrónico (opcional)","nickname":"Nombre","reply_placeholder":"Responder...","reply_btn":"Responder","sending":"Enviando...","mod_badge":"MOD","content_is_required":"El contenido es obligatorio","nickname_is_required":"El nombre es obligatorio","comment_has_been_sent":"Tu comentario ha sido enviado. Por favor, espera su aprobación."},
 "it":{"powered_by":"Commenti offerti da Cusdis","post_comment":"Commenta","loading":"Caricamento","email":"Email (facoltativa)","nickname":"Nickname","reply_placeholder":"Rispondi...","reply_btn":"Rispondi","sending":"invio...","mod_badge":"MOD","content_is_required":"Il contenuto è obbligatorio","nickname_is_required":"Il nickname è obbligatorio","comment_has_been_sent":"Il tuo commento è stato inviato. Attendi l'approvazione."},
 "fr":{"powered_by":"Commentaires propulsés par Cusdis","post_comment":"Publier un commentaire","loading":"Chargement","email":"Email (optionnel)","nickname":"Pseudonyme","reply_placeholder":"Commentaire...","reply_btn":"Répondre","sending":"Publication...","mod_badge":"MOD","content_is_required":"Commentaire requis","nickname_is_required":"Pseudonyme requis","comment_has_been_sent":"Votre commentaire a été publié. Attendez son approbation."},
 "sv":{"powered_by":"Kommentarer drivs av Cusdis","post_comment":"Kommentera","loading":"Laddar","email":"E-post (valfritt)","nickname":"Smeknamn","reply_placeholder":"Svara...","reply_btn":"Svara","sending":"skickar...","mod_badge":"MOD","content_is_required":"Innehåll krävs","nickname_is_required":"Smeknamn krävs","comment_has_been_sent":"Din kommentar har skickats. Vänta på godkännande."},
}
cus_locales_json = _j.dumps(CUS_LOCALES, ensure_ascii=False)

HTML = f"""<!DOCTYPE html>
<html lang="sk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Register káuz — FIA FOX</title>
<style>{CSS}{SHOW}</style></head><body data-l="sk">
<div class="top"><h1>FIA FOX — Fair Internet Initiative</h1></div>
<div class="wrap">
 <div class="navbar"><a class="hm" href="index.html">{g(UI["home"])}</a>
  <div class="lang"><span class="lb">LANG</span>{FLAGS}</div></div>

 <div class="panel"><h2>{g(UI["reg"])} <span class="cnt2"><span id="pocet">0</span> {g(UI["verf"])}</span></h2>
  <div class="tabs"><button class="tab on" data-j="all">{g(UI["all"])}</button>
   <button class="tab" data-j="de"><img src="https://flagcdn.com/de.svg" alt="DE">{g(UI["jde"])}</button>
   <button class="tab" data-j="sk"><img src="https://flagcdn.com/sk.svg" alt="SK">{g(UI["jsk"])}</button>
   <button class="tab" data-j="eu">🇪🇺 {g(UI["jeu"])}</button></div>
  <div class="grid"><button class="tile rall" data-k="all" data-jur="de sk eu">
    <div class="tn">🌐 {g(UI["allv"])}</div><div class="tc">{len(KAUZY)} {g(UI["verf"])}</div></button>{tiles}</div>
 </div>

 <div class="chips">
  <button class="chip" data-o="kartell">{g(UI["obl_k"])}</button>
  <button class="chip" data-o="gdpr">{g(UI["obl_g"])}</button>
  <button class="chip" data-o="strafrecht">{g(UI["obl_s"])}</button>
  <button class="chip" data-o="majetok">{g(UI["obl_m"])}</button>
 </div>
 <div class="sortbar"><span class="sl">{g(UI["sort"])}</span>
  <button class="sb" data-s="d">{g(UI["s_dat"])}</button>
  <button class="sb" data-s="az">{g(UI["s_az"])}</button>
  <button class="sb" data-s="our">{g(UI["s_our"])}</button>
  <button class="sb" data-s="obl">{g(UI["s_obl"])}</button>
  <button class="sb on" data-s="new">{g(UI["s_new"])}</button>
 </div>

 <div id="zoznam">{karty_html}</div>
</div>
<script>
var KJ = {kj_json};
var CUS_L = {cus_locales_json};
var SEL='all', JUR='all', OBL='', SORT='new', IASC=false;
function kauzaOk(kz){{
 if(JUR==='all') return true;
 var j = KJ[kz] || [];
 return j.indexOf(JUR) >= 0;
}}
function apply(){{
 document.querySelectorAll('.tile').forEach(function(t){{
  var ok = t.dataset.k==='all' || kauzaOk(t.dataset.k);
  t.style.display = ok?'':'none';
  t.classList.toggle('on', SEL===t.dataset.k || (SEL==='all' && t.dataset.k==='all'));}});
 document.querySelectorAll('.case').forEach(function(c){{
  var okk = (SEL==='all') ? kauzaOk(c.dataset.kz) : (c.dataset.kz===SEL);
  var oko = !OBL || (c.dataset.obl||'').split(' ').indexOf(OBL)>=0;
  c.style.display = (okk&&oko)?'':'none';}});
 var z=document.getElementById('zoznam');
 function pinR(c){{ var v=parseInt(c.dataset.pin,10); return isNaN(v)?9999:v; }}
 [].slice.call(z.querySelectorAll('.case')).sort(function(a,b){{
  var pa=pinR(a), pb=pinR(b);
  if(pa!==pb) return pa-pb;                       // pripnute vzdy hore, podla cisla
  if(SORT==='az')  return (a.dataset.az||'zzz').localeCompare(b.dataset.az||'zzz');
  if(SORT==='our') return (a.dataset.our||'zzz').localeCompare(b.dataset.our||'zzz');
  if(SORT==='obl') return (a.dataset.obl||'zzz').localeCompare(b.dataset.obl||'zzz');
  if(SORT==='d')   return (a.dataset.d||'').localeCompare(b.dataset.d||'');   // od najstarších
  return (b.dataset.d||'').localeCompare(a.dataset.d||'');                    // najnovšie

 }}).forEach(function(c){{ z.appendChild(c); }});
 orderItems();
 var n=[].slice.call(z.querySelectorAll('.case')).filter(function(c){{return c.style.display!=='none';}}).length;
 var pv=document.getElementById('pocet'); if(pv) pv.textContent=n;
}}
document.querySelectorAll('.tile').forEach(function(t){{
 t.addEventListener('click',function(){{ SEL=(SEL===t.dataset.k?'all':t.dataset.k); apply(); }});}});
document.querySelectorAll('.chip').forEach(function(b){{
 b.addEventListener('click',function(){{ OBL=(OBL===b.dataset.o?'':b.dataset.o);
  document.querySelectorAll('.chip').forEach(function(x){{x.classList.remove('on');}});
  if(OBL) b.classList.add('on'); apply(); }});}});
document.querySelectorAll('.sb').forEach(function(b){{
 b.addEventListener('click',function(){{ SORT=b.dataset.s;
  if(SORT==='d'||SORT==='new'){{ IASC=(SORT==='d');
    document.querySelectorAll('details.case').forEach(function(c){{c.setAttribute('data-iasc', IASC?'1':'0');}}); }}
  document.querySelectorAll('.sb').forEach(function(x){{x.classList.remove('on');}}); b.classList.add('on'); apply(); }});}});
document.querySelectorAll('.tab').forEach(function(b){{
 b.addEventListener('click',function(){{ JUR=b.dataset.j; SEL='all';
  document.querySelectorAll('.tab').forEach(function(x){{x.classList.remove('on');}}); b.classList.add('on'); apply(); }});}});
document.querySelectorAll('.f').forEach(function(b){{
 b.addEventListener('click',function(){{ document.body.dataset.l=b.dataset.l; document.documentElement.lang=b.dataset.l;
  document.querySelectorAll('.f').forEach(function(x){{x.classList.remove('on');}}); b.classList.add('on'); }});}});
if(location.hash){{ var c=document.querySelector(location.hash); if(c&&c.tagName==='DETAILS'){{ c.open=true; c.scrollIntoView(); }} }}
apply();
/* vlákna: číslovanie krúžkov (1=pôvodné, 2=reakcia) + zvýraznenie a scroll na partnera */
(function(){{
  document.querySelectorAll('details.case').forEach(function(c){{
    var g={{}};
    c.querySelectorAll('.it[data-thread]').forEach(function(el){{
      var t=el.getAttribute('data-thread'); if(!t)return;
      (g[t]=g[t]||[]).push(el);
    }});
    Object.keys(g).forEach(function(t){{
      g[t].sort(function(a,b){{return (a.getAttribute('data-d')||'').localeCompare(b.getAttribute('data-d')||'');}});
      g[t].forEach(function(el,i){{
        var ih=el.querySelector('.ih'); if(!ih)return;
        var b=ih.querySelector('.thr');
        if(!b){{b=document.createElement('span');b.className='thr';ih.appendChild(b);}}
        b.textContent=String(i+1); b.title='Vlákno · '+(i+1)+'. dokument';
      }});
    }});
  }});
  function items(t){{return document.querySelectorAll('.it[data-thread="'+t+'"]');}}  function tOf(el){{var it=el.closest('.it[data-thread]');return it?it.getAttribute('data-thread'):null;}}
  document.addEventListener('mouseover',function(ev){{var h=ev.target.closest&&ev.target.closest('.thr');if(!h)return;var t=tOf(h);if(t)items(t).forEach(function(e){{e.classList.add('thr-hl');}});}});
  document.addEventListener('mouseout',function(ev){{var h=ev.target.closest&&ev.target.closest('.thr');if(!h)return;var t=tOf(h);if(t)items(t).forEach(function(e){{e.classList.remove('thr-hl');}});}});
  document.addEventListener('click',function(ev){{var h=ev.target.closest&&ev.target.closest('.thr');if(!h)return;var t=tOf(h);if(!t)return;var all=items(t);if(!all.length)return;all.forEach(function(e){{e.classList.add('thr-hl');}});var self=h.closest('.it'),partner=null;all.forEach(function(e){{if(e!==self)partner=e;}});if(partner)partner.scrollIntoView({{behavior:'smooth',block:'center'}});setTimeout(function(){{all.forEach(function(e){{e.classList.remove('thr-hl');}});}},2600);}});
}})();
/* poradie položiek v stĺpcoch podľa dátumu — per-kartu prepínač v hlavičke SPISOVÁ KOMUNIKÁCIA (data-iasc na .case; sortbar Najstaršie/Najnovšie preusporiada všetky karty) */
function sortCardItems(c){{
  var asc = c.getAttribute('data-iasc')==='1';
  c.querySelectorAll('.col').forEach(function(col){{
    var its=[].slice.call(col.querySelectorAll('.it'));
    its.sort(function(a,b){{var x=a.getAttribute('data-d')||'',y=b.getAttribute('data-d')||'';
      return asc?(x<y?-1:x>y?1:0):(x<y?1:x>y?-1:0);}});
    its.forEach(function(it){{col.appendChild(it);}});
  }});
}}
function orderItems(){{ document.querySelectorAll('details.case').forEach(sortCardItems); }}
document.addEventListener('click',function(ev){{
  var b=ev.target.closest&&ev.target.closest('.isb'); if(!b) return;
  var c=b.closest('details.case'); if(!c) return;
  c.setAttribute('data-iasc', c.getAttribute('data-iasc')==='1'?'0':'1'); sortCardItems(c);
}});
/* Cusdis komentáre — per dokument, načíta sa až po kliknutí na Komentovať (jedno vlákno naraz) */
var CUS_APP='6fdea40e-6f8a-4877-b2e0-7b83dee8ee45';
function toggleCmt(btn){{
  var it=btn.closest('.it'), box=it&&it.querySelector('.cmt-wrap'); if(!box) return;
  if(box.getAttribute('data-open')==='1'){{ box.innerHTML=''; box.removeAttribute('data-open'); btn.classList.remove('on'); return; }}
  document.querySelectorAll('.cmt-wrap[data-open="1"]').forEach(function(o){{o.innerHTML=''; o.removeAttribute('data-open');}});
  document.querySelectorAll('.kom.on').forEach(function(b){{b.classList.remove('on');}});
  var t=document.createElement('div');
  t.setAttribute('data-host','https://cusdis.com');
  t.setAttribute('data-app-id',CUS_APP);
  t.setAttribute('data-page-id', it.getAttribute('data-cid'));
  t.setAttribute('data-page-url', location.origin+location.pathname);
  t.setAttribute('data-page-title', it.getAttribute('data-ctitle')||document.title);
  t.setAttribute('data-theme','light');
  box.appendChild(t); box.setAttribute('data-open','1'); btn.classList.add('on');
  (function go(){{ if(window.CUSDIS&&window.CUSDIS.renderTo){{ try{{window.CUSDIS_LOCALE=CUS_L[document.body.dataset.l]||CUS_L.en;}}catch(e){{}} window.CUSDIS.renderTo(t); }} else {{ setTimeout(go,150); }} }})();
}}
</script><script>window.CUSDIS_PREVENT_INITIAL_RENDER=true;</script><script async defer src="https://cusdis.com/js/cusdis.es.js"></script></body></html>"""

open('register.html','w',encoding='utf-8').write(HTML)
print(f"register.html: {len(HTML)//1024} kB")
print(f"  kauzy {len(KAUZY)} · karty {len([c for c in pol_karty if c])} · dokumenty {len(POLOZKY)} · súhrny {len(SUHRNY)}")
