# fia-fox-web

Verejný web **FIA FOX** — statické stránky pre GitHub Pages.

- `index.html` — Home (1:1 podľa pracovného konceptu #114)
- `register.html` — Verejný register: dlaždice káuz, filtre DE/SK/EU, radenie
- `karta-case-*.html` — karty konaní, každá s odoslanými a došlými dokumentmi a súhrnmi v 9 jazykoch

Stránky sa **generujú z dát** v repozitári `peterferenc246-design/fia`
(`prototypy/_data/fia_data.json`, generátory `extract.py` a `gen_live.py`).
Tu ležia len hotové výstupy — zdroj pravdy je `fia`.

**Čo ostáva na WordPresse (foxprof.club):** dary (GiveWP), komentáre, Impressum,
Ochrana osobných údajov, Galéria. Tieto stránky na ne len odkazujú.

Podpísané originály (PAdES/QES) sú v repozitári `fia` a servírujú sa cez jsDelivr so SHA-pinom.
