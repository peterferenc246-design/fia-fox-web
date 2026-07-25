---
name: fia-fox-web
description: |
  Statický verejný web a register káuz FIA FOX na register.foxprof.club (repo peterferenc246-design/fia-fox-web).
  Použi VŽDY, keď Peter rieši čokoľvek okolo statického registra, editora registra, kariet konaní, dlaždíc káuz,
  položiek (odoslané/došlé), 9-jazyčného .gtl textu, súhrnov, sprievodných textov, HTML aj PDF/DOCX klonov
  dokumentov, VLAJKA-VIEWERA, tlačidiel QES/Súhrn/predpis, vlákien odpovedí, generátorov alebo nasadzovania.
  Spúšťače: "register", "karta konania", "dlaždica", "položka", "odoslané/došlé", "editor", "formulár",
  "gtl", "súhrn", "sprievodný text", "klon", "HTML klon", "viewer", "VLAJKA-VIEWER", "qes", "predpis/law",
  "vlákno/odpoveď na", "vlajky", "fia-fox-web", "register.foxprof.club", "nasaď", "pregeneruj",
  "dáta registra", "fia_data.json", "prelož podanie na kartu", "napoj vlajky".
license: MIT
metadata:
  version: "1.2.2"
  updated: "2026-07-25"
---

# FIA FOX — statický web a register (`fia-fox-web`)

Tento skill je pre statický register na `register.foxprof.club`. Vznikol adaptáciou WP-skillu `fia-mk`
(#303, `wp_section_replace`) na svet **HTML formulár → `fia_data.json` → generátory → commit**.
Kde `fia-mk` píše priamo do WordPressu, tu sa mení dátový súbor a stránky sa pregenerujú.

## 0. Čo si prečítať skôr, než sa čohokoľvek dotkneš

1. Tento súbor celý.
2. `PAMATAJ.md` v koreni repa `fia-fox-web` — stav kampane, prototypu a otvorené/časovo citlivé úlohy.
3. Ak ide o konkrétnu kauzu, `PAMATAJ.md` v jej priečinku v repe `fia`.
4. Pri poliach formulára je zdroj pravdy **`editor.html`** (živý formulár na `register.foxprof.club`) a pôvodný
   **`Formular-podania-x5.html`** v repe `fia`. Popisky nevymýšľaj spamäti — vytiahni ich z týchto súborov.

Peter píše po slovensky, terse, jednoslovné príkazy. Odpovedaj po slovensky, plain text, bez markdownu.
„over" = ukáž diagnózu, nezasahuj. „vykonaj" / „choď" = urob to. „pracuj" = pokračuj (napr. po FR breakpointe).

---

## 0b. ŽELEZNÉ PRAVIDLÁ (platia vo všetkých vetvách)

- **Vstup je HTML formulár, nie MK blok.** Ekvivalent `fia-mk` MK bloku (Objekt/Akcia/Smer) je tu dvojica
  **{vybraný objekt vo formulári} × {Akcia: Pridať | Opraviť | Vymazať}**, plus Smer (Odoslané/Došlé) pri položke.
  Kolobeh: Peter vyplní formulár → Stiahnuť JSON → nahrá Claudovi → Claude commitne dáta a pregeneruje.
- **Jediný zdroj pravdy registra = `_data/fia_data.json`.** Text súhrnu aj sprievodného textu žije v `suhrny{}`
  resp. `polozky[].sprievodny{}`. **Nikdy nezakladaj druhú kópiu textu** — ani do URL, ani na samostatnú stránku.
  (Toto je INVERZIA oproti `fia-mk`, kde jediným zdrojom bol WP modál na #303.)
- **WordPress sa nezapisuje.** Statický register je paralelná vetva; #303/#22/#114/GiveWP bežia nezmenené (čítať áno).
- **9 jazykov vždy** v poradí `de, en, sk, hr, pl, es, it, fr, sv`. Vo formulári sa vyplní JEDEN (jazyk aktívnej
  vlajky), zvyšných 8 doplní Claude. **Base jazyk prekladu:** DE pre DE-jurisdikciu, SK pre SK originály.
  ES a SV → z EN, ak nie sú explicitne zapnuté.
- **Chirurgické zmeny dát.** Meň v `fia_data.json` len dotknuté polia; nezmaž `thread`, `summodId`, `oblast`,
  pripnutie, sprievodné texty. Ak MK/formulár pole neobsahuje medzi zmenenými, nechaj ho tak
  (napr. už hotové 9-jazyčné `subj9` neprepisuj jednojazyčným textom z formulára).
- **Doručuj len vyžiadaný typ výstupu.** Žiadne bonusové DOCX/pracovné súbory — míňajú kredity.
- **Pred zverejnením preveriť dôverné dokumenty** (VERTRAULICH v prebiehajúcom konaní = procesné riziko).
- **Token** `gh.dat` (Peter nahráva `gh.rar` každú session), fine-grained, Contents: read+write na **oba** repa.
  Čítaj cez `tr -d ' \n\r\t'`, nikdy needituj, nikdy needituj v texte, nikdy nenavrhuj revokáciu.

---

## 1. Dva repozitáre — čo kam patrí

| Repo | Úloha | Obsah |
|---|---|---|
| `peterferenc246-design/fia` | **archív a dielňa** | dokumenty káuz (PDF originály + klony), obrázky, `viewer.html`, `kauzy.js`, bannery, jazykové zdroje, `tools/`, `PAMATAJ.md` káuz |
| `peterferenc246-design/fia-fox-web` | **výkladná skriňa** | `index.html`, `register.html`, `editor.html`, `karta-*.html`, `_data/` (dáta + generátory), `kauzy/`, `skills/` (verzia tohto skillu + `.zip`) |

Doména `register.foxprof.club` je nastavená na **fia-fox-web** (CNAME v koreni).
Na `fia` doménu NIKDY nenastavuj — presmerovala by adresy, ktoré používa ostrý register #303 a viewer.

Commity cez **Contents API** (jednosúborové) alebo **Git Data API** (blob→tree→commit→ref, viacsúborové).
Detail v §13.

---

## 2. WordPress sa NEDOTÝKA

Ostrý register `#303` (`foxprof.club/kauzy-koncept/`), homepage `#22`, koncept `#114`, GiveWP stránky —
**čítať áno, zapisovať nie**, pokiaľ Peter výslovne nepovie inak. Na WordPresse zostávajú dary (GiveWP),
komentáre, Impressum, Ochrana údajov, Galéria; statický web na ne len odkazuje.

---

## 3. Dátová štruktúra `_data/fia_data.json`

```
kauzy_reg[]   spis, jur[], ids[], nazov{9}, warn{9}          ← dlaždice, zdroj pravdy pre kauzy
karty[]       id, pin, jur[], date, az, ourref, area[], organ_txt, datum_txt,
              nazov{9}, podtitul{9}, meta{9}, stav{9}, stav_trieda, sprievodny{9}
polozky[]     karta, kauza, dir(sent|recv), date, stav, access(pub|pw), az, ourref, court,
              subj9{9}, urls{9}, orig, summodId, fname, fpath, fallback, begleit, cardsubj,
              thread, replyTo, dolezite, komentare, oblast[], law, qes, bezDatumu,
              btnQes, btnSum, btnLaw
suhrny{}      summodId -> {9 jazykov HTML}
```

**Pasce:**
- `subj` je obyčajný text zo snapu, deväťjazyčná verzia je `subj9`. Nezameň.
- Kauza karty sa určuje cez `kauzy_reg[].ids`, NIE cez `polozky[].kauza` ani `kauzaKey`.
  Kľúče typu `k-jv` sú pracovné; skutočné kódy sú `TFIA-2026-JV` atď.
- Extrahované HTML súhrnov a sprievodných textov býva **nevyvážené** (prebytočné `</div>`).
  Vždy dovyvažuj pred vygenerovaním, inak sa rozpadne rozloženie celej stránky.
- `summodId` sa vo formulári nezobrazuje — generuje sa sám: `summod-<karta bez case->-<poradie>`.

**Polia tlačidiel/vlákna (mapovanie na štandard §6b a §7):**
- `qes` = `STRANA[:DOK[:ZAROVNANIE]]` (skok na podpisový blok), `law` = `CELEX|URL~POPIS~TOOLTIP` (predpis),
  `summodId` = zdroj súhrnu, `btnQes/btnSum/btnLaw` = či sa tlačidlo vykreslí.
- `thread`/`replyTo` = vlákno odpovede (§7). `orig` = jsDelivr @SHA link na podpísaný originál (`doc2`).

---

## 4. Generátory (`_data/`)

| Súbor | Čo robí |
|---|---|
| `extract.py` | export #303 (`303.html`) → `fia_data.json`, berie VŠETKY polia |
| `gen_register_full.py` | `fia_data.json` → `register.html` s rozbaľovacími kartami |
| `gen_live.py` | samostatné `karta-*.html` |
| `gen_home.py` | `index.html` 1:1 podľa #114 |

Export #303 získa Peter otvorením
`https://public-api.wordpress.com/wp/v2/sites/foxprof.club/pages/303?_fields=content` a nahraním súboru.

**Viewer URL stavia generátor podľa štandardu §6b.** Dnešný stav: generátory skladajú len
`viewer.html?doc=<orig>` (bez `qes/sum/law/langs`), súhrn ukazujú inline z `suhrny{}`. Cieľ (rozhodnuté
25.07.2026): generátor buduje plný viewer URL pre všetkých 9 vlajok + fallback zo stavebných blokov
(`doc1/doc2/orig/langs/qes/sum/law/d/page/vw`). Kým to nie je dorobené, drž sa §6b ako špecifikácie.

---

## 5. Register — ako sa má správať (kopíruje #303)

- **Dlaždice káuz** hore, pod nimi **rozbaľovacie karty konaní** (`<details class="case">`).
  Karta sa rozbalí priamo v registri, neodklikáva sa inam.
- **Vybraná dlaždica ZOŽLTNE** — zlatý rám `#FFCB3E`, podklad `linear-gradient(135deg,#fff,#FFF8E6)`,
  nadpis `#8a5a00`. Sivý obrys je nepoužiteľný, na modrom podklade ho nevidno.
- **Filter jurisdikcie (DE/SK/EÚ) filtruje KAUZY, nie konania.** Kauza `TFIA-2026-JV` má `de eu`,
  takže pri Nemecku ostáva viditeľná aj s konaniami označenými EÚ. Filtrovať konania podľa ich vlastnej
  jurisdikcie je CHYBA — stratia sa konania pred súdmi EÚ.
- **Pripnuté konania idú navrch pri KAŽDOM radení**, podľa čísla pinu; pin má prednosť pred dátumom.
  Pripnutá karta má zlatý ľavý pruh.
- **Radenie:** Najstaršie (vzostupne) a Najnovšie (zostupne) musia byť DVE RÔZNE poradia.
  Ďalej Sp. zn., Naša spis. zn., Oblasť. Prázdne hodnoty padajú na koniec (`'zzz'`).
- **Tematické štítky:** kartell / gdpr / strafrecht / majetok, filtrujú konania, druhý klik vypína.
- **Karta obsahuje:** dátum, názov, podtitul, riadok Orgán · Oblasť · Naša spis. zn., pilulku pripnutia,
  farebnú pilulku stavu, SPISOVÁ KOMUNIKÁCIA v dvoch stĺpcoch (Odoslané/Prijaté s počtami), dole
  Sprievodný text a Zdieľať.
- **Položka obsahuje:** dátum červeno, štítok prístupu 🌐 Verejné / 🔒 Heslo, ❗ a červený pruh pri dôležitých,
  orgán, názov súboru v prerušovanom rámčeku, tlačidlá **Otvoriť dokument (9 jazykov) · 📄 Súhrn · 💬 Komentovať**.
  **★ ŽELEZNÉ PRAVIDLO (Peter 25.07.2026): „Podpísaný originál" sa NIKDY nekreslí na karte.** Originál je dostupný
  až PO otvorení dokumentu — tlačidlo naň žije v hlavičke otvoreného klonu (§8a), nie na karte. Generátory
  `gen_register_full.py` aj `gen_live.py` preto do karty `og`/orig button NEvkladajú (pole `orig` môže v dátach
  ostať ako kanonický odkaz, karta ho ale nezobrazuje).
  **Popis tlačidla: „(QES)" LEN ak dokument reálne nesie Petrov kvalifikovaný podpis** (jeho odoslané podpísané
  podania). Dokument bez QES (došlá pošta, nepodpísané) → v tlačidle „(PDF)", nikdy „(QES)". Napr. došlá odpoveď
  orgánu = „Signiertes Original (PDF)" / „Podpísaný originál (PDF)".

---

## 6. Editor registra `editor.html`

Verejná adresa `https://register.foxprof.club/editor.html`, `noindex`, **bez tokenu** — nič nezapisuje.
**Layout (od 25.07.2026):** stránka je rozdelená **vodorovne** na dva samostatne scrollovateľné panely
(`#hTop` hore: Kauzy → Konania → Dokumenty; `#hBot` dole: formulár na plnú šírku) s ťahateľným
rozdeľovačom `#hDrag` (ťah hore/dole, dvojklik = 50/50). „⟳ Aktualizovať formulár" ukladá scroll oboch
panelov (nie okna) do `sessionStorage`.

### Objekt × Akcia (ekvivalent MK)
Objekty: **KAUZA (dlaždica) · KARTA (konanie) · POLOŽKA (dokument, Smer Odoslané/Došlé)**.
Akcia vo formulári: **Pridať | Opraviť | Vymazať**. Podľa dvojice objekt×akcia Claude upraví príslušné pole
v `fia_data.json` (§8 vetvenie).

### Základné princípy formulára
- **Jeden jazyk, nie deväť.** Každé viacjazyčné pole má JEDNO textové pole v jazyku aktívnej vlajky. Pod ním
  stav: „ostatné jazyky doplní Claude" / „vyplnených ďalších N z 8" / „✔ ostatných 8 jazykov vyplnených".
- **Bohatý text sa needituje ako HTML.** Súhrn aj sprievodný text sa zobrazujú ako čitateľný text v odsekoch;
  odkaz `[text](adresa)`. Pri ukladaní sa prevedie na HTML a doplní sa jazykový nadpis
  (`Súhrn dokumentu` / `O tomto podaní` a preklady). Surové značky v políčku = chyba.
- **Prepínacie tlačidlá** (nie rozbaľovacie zoznamy) tam, kde ich má x5: Smer, Typ výstupu, Akcia, Oblasť práva.

### Polia položky (poradie ako v x5 / editor.html)
Dátum · Prístup · bez dátumu (—) · Smer (↗/↙) · Stav · Typ výstupu (Celý riadok / Len odkaz) · Konanie ·
⚖️ Orgán tejto položky (len ak iný než na konaní) · Az. súdna · Naša spis. zn. interná · Predmet dokumentu ·
🔒 Pokyn k heslu · **rámček Tlačidlá vo VLAJKA-VIEWERI (✍ QES · 📄 Súhrn · ⚖ predpis + Predpis URL/CELEX~popis
+ Strana podpisu `qes=`)** · ↩ Odpoveď na (vlákno) · Odkaz na dokument · Fallback URL ·
✍ Podpísaný originál (QES) URL · 🛈 Názov súboru · 📁 Cesta k súboru · 🔗 Extra odkaz text + URL ·
📄 Súhrn dokumentu · 📝 Sprievodný text · 🗒️ Príkazy pre Claude ·
🏷 Oblasť práva (prenesie sa na celú kartu) · Akcia (Pridať/Opraviť/Vymazať).

### Polia karty
ID karty (`case-…`, slug z názvu) · Spis · Naša značka · Dátum RRRR-MM-DD · Dátum ako text ·
Jurisdikcia (de sk eu) · Oblasť · Orgán (text) · 📌 Pripnúť (pozícia) · Názov · Podtitul · Riadok Orgán/Oblasť · Stav.

### Polia kauzy
Kód kauzy (`data-spis`) · Jurisdikcia · Názov · Červený podtitul (nepovinné) · Konania v kauze.

### Ďalšie požiadavky editora
- jazykový prepínač nad kauzami prepína kauzy aj konania aj dokumenty; počítadlo chýbajúcich v zvolenom jazyku;
- dlaždice → karty → dokumenty v dvoch stĺpcoch (ako register); pri každom dokumente **Otvoriť** (v zvolenom
  jazyku) a **Originál (QES)** cez viewer; automatické načítanie dát pri otvorení, pri zlyhaní červená hláška;
  kontrola úplnosti a export JSON.

---

## 6b. ★ ŠTANDARD TLAČIDIEL DOKUMENTU — QES · Súhrn · predpis (prevzaté z fia-mk, adaptované)

Rozhodnuté 25.07.2026: statický register **preberá 3-tlačidlový štandard `fia-mk`**. Za 9 vlajkami
(„Otvoriť dokument") idú pri **odoslaných podaniach** default tri tlačidlá v poradí **✍ QES · 📄 Súhrn · ⚖ predpis**.
Došlá pošta spravidla QES ani predpis nemá (§8b). Poradie tlačidiel riadi `viewer.html`, nie poradie parametrov.

Generátor skladá pre KAŽDÚ z 9 vlajok + `fallback` jednu viewer URL zo stavebných blokov:
```
viewer.html?doc=<doc1 @SHA>&doc2=<doc2 @SHA>&orig=<doc2 @SHA>
           &langs=CODE:PAGE[:2],...&qes=STR:DOK:ZAROV&sum=<summodId>&law=<...>&d=<1|2>&page=<N>&vw=<N>
```
- **doc1** = klon prekladov (`..._ALL.pdf` alebo HTML klon), **doc2** = podpísaný originál INTACT,
  **orig=** = jsDelivr @SHA link na `doc2` (tlačidlo „⬇ Podpísaný originál (QES)"). `orig=` je POVINNÉ,
  inak tlačidlo stiahne klon.
- **langs=** `CODE:PAGE[:2]` — `:2` = jazyk žije v `doc2` (podpísanom); preferuj `doc2`, ak je jazyk v oboch.
- **Escaping:** v `data-snap`/dátach `&amp;`, vo viditeľnom `href` obyčajné `&`.
- **Cache:** po úprave `viewer.html` bumpni `&vw=N` vo všetkých URL, inak prehliadač drží starú verziu.

**✍ QES — `qes=STRANA[:DOK[:ZAROVNANIE]]`.** Skáče na vizuálny podpisový blok (fotka + pečiatka).
`DOK=2` (podpísaný originál). `ZAROVNANIE`: `b` = spodok strany; pomer `0..1` = stred bloku ako podiel výšky
strany (preferuj pomer — trafí presne bez ohľadu na zoom). **Zadáva sa vždy — nikdy sa neodvodzuje**; hodnotu
vytiahni PROGRAMOVO z podpísaného PDF:
```python
acro = PdfReader(SIGNED).trailer['/Root']['/AcroForm']
# pole s /FT=='/Sig' -> jeho /Rect [x0,y0,x1,y1]; stranu nájdi porovnaním /Rect s /Annots strán
# ALIGN = ((H-y1)+(H-y0))/2 / H     (H = mediabox.height)
```
Bez `qes=` sa tlačidlo NEVYKRESLÍ (zámer, nie chyba).

**📄 Súhrn — `sum=<summodId>`.** Jediný zdroj textu = `suhrny{}` vo `fia_data.json` (INVERZIA oproti fia-mk,
kde zdrojom bol WP modál na #303). **Implementačná pozn.:** dnešný `viewer.html` číta súhrn z verejného WP API
#303 — pre statický register ho treba naučiť čítať súhrn z registra (napr. malý JSON na `register.foxprof.club`),
alebo súhrn ponechať **inline** z `suhrny{}` (súčasný generátor). Kým viewer nevie čítať z registra, drž súhrn
inline a `sum=` do URL nedávaj. Text sa nikdy nekopíruje do druhého zdroja.

**⚖ predpis — `law=CELEX|URL~POPIS[~TOOLTIP]`.** Môže sa opakovať. Pri tvare `CELEX:` viewer poskladá EUR-Lex
odkaz v jazyku aktívnej vlajky (klik na SK vlajku → slovenské znenie), zadáva sa len CELEX. Nemecký národný →
plná `URL` (`gesetze-im-internet.de/...`). `POPIS`/`TOOLTIP` url-encoduj (medzera `%20`, `§`=`%C2%A7`,
`—`=`%E2%80%94`). **Tooltip musí byť 9-jazyčný** — pri každom NOVOM predpise doplň všetkých 9 jazykov do mapy
`LAW_TITLES` vo `viewer.html`, inak sa vo všetkých jazykoch ukáže ten istý text z URL. Vyber NOSNÝ predpis
podania; ak nie je zjavný, spýtaj sa Petra ktorý.

**Zápis efektívne:** neukladaj 9 takmer rovnakých URL do dát — ulož STAVEBNÉ BLOKY (doc1/doc2/orig/langs/qes/
sum/law/d/page/vw) a nechaj generátor URL poskladať. Reťazce/SHA generuj programovo, nikdy neprepisuj SHA ručne.

---

## 7. Vlákna odpovedí (thread) — párovanie [FUNGUJE v statickom registri od 25.07.2026]

- **Dáta:** obom partnerským položkám nastav rovnaký `thread` (`thr-<slug predmetu pôvodného podania>`);
  odpovedi navyše `replyTo` = predmet pôvodného podania. Partnera dohľadaj podľa `replyTo`. Bez rovnakého
  `thread` na OBOCH položkách vlákno neexistuje.
- **Renderuje sa automaticky — čísla ani krúžky NEPÍŠ do dát ani markupu.** `gen_register_full.py` vypíše na
  položku (`.it`) `data-thread` + `data-d` (dátumový kľúč). Skript registra v rámci každej karty zoskupí položky
  podľa `data-thread`, zoradí podľa dátumu a nakreslí do hlavičky (`.ih`) číslovaný krúžok `.thr`
  (1 = pôvodné podanie, 2 = reakcia …). Klik/hover na krúžok zvýrazní celé vlákno (`.thr-hl`) a odscrolluje
  na partnera.
- Vlákno spája položky NAPRIEČ stĺpcami Odoslané/Došlé v tej istej karte (odoslané podanie ↔ došlá odpoveď).
- Karta-stránky `karta-*.html` z `gen_live.py` — rovnaké číslovanie doplniť analogicky (TODO, ak treba samostatné stránky).

---

## 8. Klony dokumentov — dve vetvy

**Pravidlo:** klon = HTML alebo nepodpísané PDF; originál = podpísané PDF s QES, ktoré sa NIKDY needituje.
Čokoľvek sa ODOSIELA orgánu, musí byť PDF s QES (HTML sa nedá priložiť ani podpísať PAdES).

### 8a. HTML klon — DEFAULT pre verejný register
- zdroj formátovania je **Word / Markdown od Petra**, nie text vytiahnutý z PDF (z PDF sa stratí dvojstĺpcová
  hlavička, tabuľky aj podpisový blok);
- hlavička dvojstĺpcová: vľavo oznamovateľ, vpravo adresát; ikony 📍📧📞📠 patria **PRED text na jeden riadok**;
- na konci podpisový blok s obrázkom podpisu a poznámkou o QES;
- obrázky cez **relatívnu cestu `img/…`**, NIE cez jsDelivr (`@main` cachuje až 12 h);
- vzor hotového riešenia: `dg-comp-kartel-pristup-k-dokumentom/dgcomp-correspondence-full.html` (repo `fia`);
- **tlačidlo originálu žije v hlavičke klonu (langbar), NIE na karte** (§5). Popis „(QES)" LEN pri Petrovom
  kvalifikovanom podpise; inak „(PDF)" (napr. došlá pošta = „Signiertes Original (PDF)" / „Podpísaný originál (PDF)").
- podpísaný originál (PDF/QES) ostáva samostatné tlačidlo na stiahnutie ako dôkaz.

### 8b. PDF/DOCX klon — pre ODOSIELANÉ/podpisované dokumenty (prevzaté z fia-mk §4.1)
Keď treba viacjazyčný PDF klon do jedného súboru (nie HTML) alebo keď sa dokument reálne odosiela:
1. **Klon sa stavia z Petrovho WORDU, nie z vlastného layoutu.** `tools/build_docx_clone.py` (repo `fia`):
   naklonuje DOCX, vymení LEN text (zachová Calibri/okraje/štýly/zarovnania/tučné úseky/hypertextové e-maily/
   zalomenie sekcií), vloží jazykový banner ako **plávajúci ukotvený objekt** a čistý podpis; prevod cez LibreOffice.
   - Pri výmene textu odstraňuj LEN behy s `w:t`; beh s `w:drawing`/`w:pict`/`mc:AlternateContent` nechaj
     (inak zmizne podpisový blok). Prázdne odseky nemajú behy — výšku určuje `w:pPr/w:rPr/w:sz`.
   - **FIT-PASS:** FR/ES/IT sú dlhšie než SK; klon musí mať toľko strán ako originál. Stláčaj LEN prázdne medzery,
     odstupy a riadkovanie — **telo nikdy pod 12 pt**.
2. **DOŠLÁ POŠTA (cudzí dokument) sa nekloní z DOCX** — zdroj je sken s OCR. (a) OCR ručne over proti obrázku
   (typicky `0`↔`O` v spisovej značke, `S`↔`§`, rozbité dátumy), (b) preklad sádzaj nanovo 1 strana/jazyk
   s bannerom vpravo hore, (c) do pätičky KAŽDÉHO jazyka **disclaimer o neoficiálnom preklade** s odkazom, že
   záväzný je originál cez vlajku pôvodného jazyka. Originál = `doc2`, klon = `doc1`; `qes=` sa NEPRIDÁVA.
3. **BREAKPOINT — FR VZORKA NAJPRV.** Vyrenderuj celý **FR** klon, over (banner ~3,6 cm, pomer ~2,8; podpis nad
   STREDOM bodkovanej čiary, odchýlka 0,00 cm; počet strán = ako originál), doruč FR PDF Petrovi a **ZASTAV**.
   Pokračuj až na „pracuj".
4. **TRI SÚBORY:** `doc1` = MERGE klonov jazykov, ktoré NIE sú v podpísanom; `doc2` = podpísaný originál INTACT
   (nikdy nerozdeľuj — rozdelenie zneplatní PAdES); `orig=` = jsDelivr @SHA link na ten istý `doc2`.
   Mapu strán zisti `pypdf` pre OBA súbory; jazyk v doc2 aj doc1 → preferuj doc2 (`:2`).
5. Commit oboch do `docs/` (§13). Overenie: stiahni späť cez `raw.githubusercontent.com`, skontroluj počet strán
   + prítomnosť `/Sig` v podpísanom.

### 8c. VLAJKA-VIEWER, metóda 6 (spája obe vetvy)
`viewer.html?doc=<KLON>&doc2=<ORIGINÁL>&orig=<ORIGINÁL>&langs=DE:1,EN:19,…&qes=STR:DOK:ZAROV&sum=<summodId>&law=…&d=<1|2>&page=<N>&vw=<N>`
- klon sa smie spájať a dopĺňať, originál nikdy; `qes=6:2:0.58` → strana 6 v doc2, pomer 0.58 výšky;
- **po vložení strán do klonu prepočítaj mapu vlajok**, inak vlajky skáču mimo;
- robustný skok vo viewer.html: `history.scrollRestoration="manual"`, `scrollTo` s offsetom pod sticky hlavičku,
  retry kým `cur==target` (krehký `scrollIntoView({behavior:"instant"})` padá na str. 1).

---

## 9. Odkazy na dokumenty — železné pravidlo

Dokument sa **vždy** otvára cez náš viewer: `https://peterferenc246-design.github.io/fia/viewer.html?doc=<URL>`.
Nikdy holým odkazom na PDF (prehliadač ho odovzdá Acrobatu), nikdy cez `github.com/.../blob/...`
(GitHub PDF prevádza na obrázkový náhľad, odkazy zomrú), nikdy s atribútom `download` tam, kde má zobraziť.

---

## 10. Obrázky

- z PDF **nevyťahuj objekt cez xref** (stratí sa priehľadnostná maska, obrázok vybledne); render strany 300 dpi
  + výrez podľa bbox dá správnu kompozíciu;
- ak Peter pošle čistý obrázok, použi ho a needituj okrem orezania/zväčšenia; vodoznaky AI sa neodstraňujú;
- OG obrázok na zdieľanie 1200×630 (1.91:1); po zmene pretlač FB cache cez Sharing Debugger → Scrape Again.

---

## 11. Čítanie zdrojov — tokenová disciplína (z fia-mk §1a)

- **Text na preklad ber VÝHRADNE z MD** (nesie text aj formátovanie — `**tučné**`, nadpisy, odrážky). Podpísané
  PDF ani Word sa do kontextu NENAČÍTAVAJÚ celé; Word slúži len ako predloha formátovania pre kód (`python-docx`
  číta štýly, LibreOffice renderuje). Súbor na disku nestojí nič.
- **Podpísané PDF nečítaj celé** — vypíš ~300 znakov z pár strán len na zistenie jazykov a strán (`pypdf`), nehádaj.
- Nevypisuj štruktúru Wordu do konverzácie; nechaj kód spárovať MD s odsekmi a vypíš JEDINÝ kontrolný riadok
  `N blokov MD, M odsekov Wordu, K nespárovaných`.

---

## 12. DOCX / podpisový blok / orgán labely (z fia-mk)

- **DOCX štandard:** Calibri, **telo 12 pt** (nikdy nižšie kvôli zmesteniu — najprv fit-pass); okraje ~1,6/1,6/2,2/2,2 cm;
  banner hore VPRAVO ~3,6 cm (`tools/mkbanner.py`); nadpisy navy `#1F3864`; page-break medzi pod-dokumentmi.
- **Podpisový blok:** 2-stĺpcová tabuľka BEZ okrajov, `w:cantSplit` (nikdy cez 2 strany). Vľavo (bottom) záver +
  „Miesto, dátum". Vpravo (bottom) podpis NAD STREDOM bodkovanej čiary (šírka ~3,4 cm), pod ním bold
  „Peter Ferenc ...............". Nikdy plávajúci textbox (dlhší preklad ho vytlačí pod okraj). Podpis =
  `sig_hires_clean.png` (čisté modré ťahy bez mena) z rootu repa `fia`.
- **Orgán label (9 jaz.):** DE Behörde · EN Body · SK Orgán · HR Tijelo · PL Organ · ES Órgano · IT Organo ·
  FR Autorité · SV Myndighet.

---

## 13. Commit disciplína (oba repa)

- Token: `cat /tmp/tok/gh.clean` (z `gh.rar` cez `libarchive-c`: `pip install --break-system-packages libarchive-c`;
  unrar/bsdtar v kontajneri nie sú). **Nikdy neechovať, nikdy nerevokovať.**
- **Contents API** (jednosúborové): `base64 -w0 SRC > /tmp/b64.txt`, payload cez `json.dump({...},open(...))` do
  SÚBORU, `curl -d @payload.json` PUT `/repos/.../contents/{path}` s `{message, content:<base64>, branch:"main"[, sha]}`.
  **NIKDY base64 cez argv** (Argument list too long) a **NIKDY nepresmeruj python stdout do toho istého payload súboru**.
- **Git Data API** (viacsúborové): blob → tree → commit → PATCH ref. Nový HEAD SHA cez `git ls-remote`.
- **Po commite over cez `raw.githubusercontent.com`** (nie `github.io` — Pages prestavuje 1–2 min).
- CDN dokumentov: `https://cdn.jsdelivr.net/gh/peterferenc246-design/fia@{SHA}/docs/{FILE}.pdf` (SHA-pin, hneď čerstvé).

---

## 14. Nasadenie — poradie krokov

1. uprav dáta (`fia_data.json`) alebo generátor;
2. pregeneruj (`gen_register_full.py`, príp. `gen_live.py`, `gen_home.py`);
3. skontroluj vyváženosť značiek: `<div>` vs `</div>`, `<details>` vs `</details>`;
4. commitni do `fia-fox-web` (stránky + `_data/`);
5. daj Petrovi odkaz a napíš, že treba Ctrl+F5. Pages prestavuje 1–2 min — pri „nič nevidím" over najprv
   súbor cez `raw.githubusercontent.com`, až potom hľadaj chybu v kóde.

**Nasadenie zmeny tohto skillu:** uprav `skills/fia-fox-web/SKILL.md`, **pregeneruj `skills/fia-fox-web.zip`**
(rovnaký obsah), commitni oba, a zosúlaď lokálnu kópiu v `/mnt/skills/user/fia-fox-web/SKILL.md`.

---

## 15. Čo som už raz pokazil — nerob znova

- Kauzy som bral z pracovných kľúčov položiek namiesto dlaždíc registra → nesprávne názvy aj kódy.
- Extrakcia brala len časť polí → chýbal podtitul, oblasť, prístup, orgán, pripnutie, sprievodné texty.
- Nevyvážené HTML v súhrnoch rozbilo rozloženie celej stránky.
- Jurisdikcia filtrovala konania namiesto káuz → z piatich konaní sa zobrazili tri.
- „Dátum" a „Najnovšie" viedli do rovnakej vetvy → tlačidlá vyzerali nefunkčne.
- Pripnuté konania neboli navrchu; vybraná dlaždica nezožltla.
- Obrázky cez jsDelivr → Peter videl starú verziu a myslel si, že som ju pokazil.
- Odkaz na originál bez `orig=` → tlačidlo sťahovalo klon.
- Klon som staval z PDF namiesto Wordu → stratená hlavička, tabuľky aj podpisový blok.
- Poslal som Petra na kartu, keď hovoril o formulári → dve kolá zbytočnej práce.
- Popisky polí som písal spamäti namiesto z `editor.html`/`Formular-podania-x5.html`.
- Do políčka som strkal surové HTML namiesto čitateľného textu.
- `qes=` som hádal namiesto vytiahnutia z podpísaného PDF → tlačidlo netrafilo podpis.
- Založil som druhú kópiu textu súhrnu → pri zmene sa rozišli. Jediný zdroj = `suhrny{}` vo `fia_data.json`.
- Patch skript spadol na chybe, ale commit sa aj tak vykonal a nasadil nezmenený súbor.
  **Po každej úprave over, že sa súbor naozaj zmenil, a až potom commituj.**

---

## 16. Povinná kontrola pred commitom

1. `node --check` na skript editora/stránky (vytiahni `<script>` do `/tmp/ed.js`, `node --check`).
2. Vyváženosť značiek vygenerovanej stránky: `<div>` vs `</div>`, `<details>` vs `</details>`.
3. Over, že patch skript naozaj zmenil súbor (veľkosť, verzia, výskyt nového reťazca). Ak spadol → **necommituj**.
4. Po nasadení over súbor cez `raw.githubusercontent.com`, nie cez `github.io`.

---

## 17. Otvorené (k 25.07.2026)

- **Dorobiť v generátore stavbu viewer URL podľa §6b** (qes/sum/law/langs pre 9 vlajok + fallback zo stavebných
  blokov). Vyriešiť zdroj súhrnu pre `sum=` (viewer čítajúci z registra) — dovtedy súhrn inline z `suhrny{}`.
- doplniť `orig=` ostatným položkám;
- dorobiť zvyšných 8 jazykov HTML klonu trestného oznámenia;
- text kampane do GiveWP, anonymné darovanie, obrázok 1200×630 (viď root `PAMATAJ.md`);
- **M.10815 — lehota na žalobu podľa čl. 263 ZFEÚ (rozhodnutie Gen. sekretariátu 03.02.2026); časovo citlivé,
  register počká, lehota nie.**
