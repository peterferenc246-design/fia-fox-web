---
name: fia-fox-web
description: |
  Statický verejný web a register káuz FIA FOX na register.foxprof.club (repo peterferenc246-design/fia-fox-web).
  Použi VŽDY, keď Peter rieši čokoľvek okolo statického registra, editora registra, kariet konaní, dlaždíc káuz,
  HTML klonov dokumentov, VLAJKA-VIEWERA, generátorov alebo nasadzovania na register.foxprof.club.
  Spúšťače: "register", "karta konania", "dlaždica", "editor", "formulár", "klon", "viewer", "vlajky",
  "fia-fox-web", "register.foxprof.club", "nasaď", "pregeneruj", "dáta registra", "fia_data.json".
license: MIT
metadata:
  version: "1.0.0"
  updated: "2026-07-24"
---

# FIA FOX — statický web a register

## 0. Čo si prečítať skôr, než sa čohokoľvek dotkneš

1. Tento súbor celý.
2. `PAMATAJ.md` v koreni repa `fia-fox-web` — stav kampane a otvorené úlohy.
3. Ak ide o konkrétnu kauzu, `PAMATAJ.md` v jej priečinku v repe `fia`.

Peter píše po slovensky, terse, jednoslovné príkazy. Odpovedaj po slovensky, plain text, bez markdownu.
„over" = ukáž diagnózu, nezasahuj. „vykonaj" / „choď" = urob to. „pracuj" = pokračuj.

---

## 1. Dva repozitáre — čo kam patrí

| Repo | Úloha | Obsah |
|---|---|---|
| `peterferenc246-design/fia` | **archív a dielňa** | dokumenty káuz (PDF originály + klony), obrázky, `viewer.html`, `kauzy.js`, bannery, jazykové zdroje, `PAMATAJ.md` káuz |
| `peterferenc246-design/fia-fox-web` | **výkladná skriňa** | `index.html`, `register.html`, `editor.html`, `karta-*.html`, `_data/` (dáta + generátory), `kauzy/` (priečinky káuz na zdroje) |

Doména `register.foxprof.club` je nastavená na **fia-fox-web** (CNAME v koreni).
Na `fia` doménu NIKDY nenastavuj — presmerovala by adresy, ktoré používa ostrý register #303.

Token: `gh.dat` (Peter nahráva `gh.rar` každú session), fine-grained, Contents: read+write na **oba** repa.
Čítaj cez `tr -d ' \n\r\t'`, nikdy needituj, nikdy nenavrhuj revokáciu.

Commity cez git trees API (base64 blob pre binárky, `sha: None` na mazanie).

---

## 2. WordPress sa NEDOTÝKA

Ostrý register `#303` (`foxprof.club/kauzy-koncept/`), homepage `#22`, koncept `#114`, GiveWP stránky —
**čítať áno, zapisovať nie**, pokiaľ Peter výslovne nepovie inak.
Statický register je paralelná vetva; WP beží ďalej nezmenený.

Na WordPresse zostávajú: dary (GiveWP), komentáre, Impressum, Ochrana údajov, Galéria.
Statický web na ne len odkazuje.

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

**Pozor na pasce:**
- `subj` je obyčajný text zo snapu, deväťjazyčná verzia je `subj9`. Nezameň.
- Kauza karty sa určuje cez `kauzy_reg[].ids`, NIE cez `polozky[].kauza` ani `kauzaKey`.
  Kľúče typu `k-jv` sú pracovné a nezodpovedajú registru; skutočné kódy sú `TFIA-2026-JV` atď.
- Extrahované HTML súhrnov a sprievodných textov býva **nevyvážené** (prebytočné `</div>`).
  Vždy dovyvažuj pred vygenerovaním, inak sa rozpadne rozloženie celej stránky.

---

## 4. Generátory (`_data/`)

| Súbor | Čo robí | Čas |
|---|---|---|
| `extract.py` | export #303 (`303.html`) → `fia_data.json`, berie VŠETKY polia | ~0,08 s |
| `gen_register_full.py` | `fia_data.json` → `register.html` s rozbaľovacími kartami | ~0,05 s |
| `gen_live.py` | samostatné `karta-*.html` | ~0,04 s |
| `gen_home.py` | `index.html` 1:1 podľa #114 | ~0,03 s |

Export #303 získa Peter otvorením
`https://public-api.wordpress.com/wp/v2/sites/foxprof.club/pages/303?_fields=content`
a nahraním súboru; z kontajnera sa naň nedá dostať.

---

## 5. Register — ako sa má správať (kopíruje #303)

- **Dlaždice káuz** hore, pod nimi **rozbaľovacie karty konaní** (`<details class="case">`).
  Karta sa rozbalí priamo v registri, neodklikáva sa na inú stránku.
- **Vybraná dlaždica ZOŽLTNE** — zlatý rám `#FFCB3E`, podklad `linear-gradient(135deg,#fff,#FFF8E6)`,
  nadpis `#8a5a00`. Sivý obrys je nepoužiteľný, na modrom podklade ho nevidno.
- **Filter jurisdikcie (DE/SK/EÚ) filtruje KAUZY, nie konania.** Kauza `TFIA-2026-JV` má `de eu`,
  takže pri Nemecku ostáva viditeľná aj s konaniami označenými EÚ. Filtrovanie konaní podľa
  ich vlastnej jurisdikcie je CHYBA — stratia sa konania pred súdmi EÚ.
- **Pripnuté konania idú navrch pri KAŽDOM radení**, zoradené podľa čísla pinu. Pin má prednosť
  pred dátumom aj pred ostatnými kľúčmi. Pripnutá karta má zlatý ľavý pruh.
- **Radenie:** Najstaršie (vzostupne) a Najnovšie (zostupne) musia byť DVE RÔZNE poradia.
  Ak obe padnú do rovnakej vetvy, tlačidlá vyzerajú nefunkčne.
  Ďalej Sp. zn., Naša spis. zn., Oblasť. Prázdne hodnoty padajú na koniec (`'zzz'`).
- **Tematické štítky:** kartell / gdpr / strafrecht / majetok, filtrujú konania, druhý klik vypína.
- **Karta obsahuje:** dátum, názov, podtitul, riadok Orgán · Oblasť · Naša spis. zn.,
  pilulku pripnutia, farebnú pilulku stavu, SPISOVÁ KOMUNIKÁCIA v dvoch stĺpcoch
  (Odoslané / Prijaté s počtami), dole Sprievodný text a Zdieľať.
- **Položka obsahuje:** dátum červeno, štítok prístupu 🌐 Verejné / 🔒 Heslo, ❗ a červený pruh
  pri dôležitých, orgán, názov súboru v prerušovanom rámčeku, tlačidlá
  Otvoriť dokument (9 jazykov) · ✍ Podpísaný originál (QES) · 📄 Súhrn · 💬 Komentovať.

---

## 6. Editor registra `editor.html`

Verejná adresa `https://register.foxprof.club/editor.html`, `noindex`, **bez tokenu** — nič nezapisuje.
Kolobeh: načíta dáta → Peter upraví → Stiahnuť JSON → nahrá Claudovi → Claude commitne a pregeneruje.

Musí obsahovať:
- jazykový prepínač nad kauzami; prepína **kauzy aj konania aj dokumenty**
- počítadlo chýbajúcich položiek v zvolenom jazyku
- dlaždice kauz → karty konaní → dokumenty v dvoch stĺpcoch (rovnaké rozloženie ako register)
- pri každom dokumente tlačidlá **Otvoriť** (v zvolenom jazyku) a **Originál (QES)**
- ⟳ Aktualizovať formulár — **zachová rozpracované dáta, výber, jazyk aj pozíciu**
  (`sessionStorage`), bez rozrobených zmien stiahne čerstvé dáta z webu
- automatické načítanie dát pri otvorení; pri zlyhaní červená hláška, nie prázdna stránka
- polia podľa x5: pripnutie + odopnutie, bez dátumu, prístup, dôležité, komentáre,
  tlačidlá vo VLAJKA-VIEWERI (QES/Súhrn/Predpis), Predpis URL~CELEX~popis, strana podpisu `qes=`,
  názov súboru, cesta, fallback, thread, replyTo, sprievodný text, súhrn v 9 jazykoch
- kontrolu úplnosti a export JSON

---

## 7. Klony dokumentov

**Pravidlo:** klon = HTML alebo nepodpísané PDF, originál = podpísané PDF s QES, ktoré sa NIKDY needituje.
Čokoľvek sa ODOSIELA orgánu, musí byť PDF s QES.

### HTML klon
- zdroj formátovania je **Word / Markdown od Petra**, nie text vytiahnutý z PDF
  (z PDF sa stratí dvojstĺpcová hlavička, tabuľky aj podpisový blok)
- hlavička dvojstĺpcová: vľavo oznamovateľ, vpravo adresát; **ikony 📍📧📞📠 patria PRED text
  na jeden riadok**, nie na samostatný riadok pod ním
- na konci podpisový blok s obrázkom podpisu (Peter s tým súhlasí) a poznámkou o QES
- obrázky cez **relatívnu cestu `img/…`**, NIE cez jsDelivr — ten cachuje `@main` až 12 hodín
  a servíruje starú verziu

### VLAJKA-VIEWER, metóda 6
`viewer.html?doc=<KLON>&doc2=<ORIGINÁL>&langs=DE:1,EN:19,…&page=N&qes=STRANA:DOK:ZAROVNANIE&sum=<summodId>&orig=<ORIGINÁL>`
- klon sa smie spájať a dopĺňať, originál nikdy — podpis by sa zneplatnil
- `qes=9:2:0.58` → strana 9 v doc2, zarovnanie zisti z podpisového widgetu:
  `1 − ((rect.y0+rect.y1)/2)/výška_strany`
- **po vložení strán do klonu prepočítaj mapu vlajok**, inak vlajky skáču mimo
- `orig=` MUSÍ byť vyplnené, inak tlačidlo „Podpísaný originál" stiahne klon

---

## 8. Odkazy na dokumenty — železné pravidlo

Dokument sa **vždy** otvára cez náš viewer:
`https://peterferenc246-design.github.io/fia/viewer.html?doc=<URL>`

Nikdy holým odkazom na PDF — ten prehliadač odovzdá Acrobatu.
Nikdy cez `github.com/.../blob/...` — GitHub PDF prevádza na obrázkový náhľad a odkazy zomrú.
Nikdy s atribútom `download` tam, kde má dokument zobraziť.

---

## 9. Obrázky

- z PDF **nevyťahuj objekt cez xref** — stratí sa priehľadnostná maska a obrázok vybledne
- render strany pri 300 dpi a výrez podľa bbox dá správnu kompozíciu
- ak Peter pošle čistý obrázok, použi ten a needituj ho okrem orezania a zväčšenia
- vodoznaky AI sa neodstraňujú

---

## 10. Nasadenie — poradie krokov

1. uprav dáta alebo generátor
2. pregeneruj (`gen_register_full.py`, prípadne `gen_live.py`, `gen_home.py`)
3. skontroluj vyváženosť značiek: `<div>` vs `</div>`, `<details>` vs `</details>`
4. commitni do `fia-fox-web` (stránky + `_data/`)
5. daj Petrovi odkaz a napíš, že treba Ctrl+F5

Po commite môže GitHub Pages prestavovať 1–2 minúty. Ak Peter hlási, že nič nevidí,
najprv over súbor v repe cez `raw.githubusercontent.com` a až potom hľadaj chybu v kóde.

---

## 11. Čo som už raz pokazil — nerob znova

- Kauzy som bral z pracovných kľúčov položiek namiesto dlaždíc registra → nesprávne názvy aj kódy.
- Extrakcia brala len časť polí → chýbal podtitul, oblasť, prístup, orgán, pripnutie, sprievodné texty.
- Nevyvážené HTML v súhrnoch rozbilo rozloženie celej stránky.
- Jurisdikcia filtrovala konania namiesto káuz → z piatich konaní sa zobrazili tri.
- „Dátum" a „Najnovšie" viedli do rovnakej vetvy → tlačidlá vyzerali nefunkčne.
- Pripnuté konania neboli navrchu.
- Vybraná dlaždica nezožltla.
- Obrázky cez jsDelivr → Peter videl starú verziu a myslel si, že som ju pokazil.
- Odkaz na originál bez `orig=` → tlačidlo sťahovalo klon.
- Klon som staval z PDF namiesto Wordu → stratená hlavička, tabuľky aj podpisový blok.
- Poslal som Petra na kartu, keď hovoril o formulári → dve kolá zbytočnej práce.

---

## 12. Otvorené (k 24.07.2026)

- doplniť `orig=` ostatným položkám
- prepojiť polia `law`, `qes`, `btnQes/btnSum/btnLaw` z editora do generovaných URL
- dorobiť zvyšných 8 jazykov HTML klonu trestného oznámenia
- text kampane vložiť do GiveWP, anonymné darovanie, obrázok 1200×630
- **M.10815 — lehota na žalobu podľa čl. 263 ZFEÚ proti rozhodnutiu Generálneho sekretariátu
  z 03.02.2026; časovo citlivé, register počká, lehota nie**
