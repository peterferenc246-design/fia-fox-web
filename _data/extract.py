#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uplna extrakcia z exportu #303 -> fia_data.json.
   Berie VSETKO, co karty a polozky nesu: atributy, 9-jazycne texty, snapy, suhrny,
   sprievodne texty kariet a dlazdice kauz z bloku #fia-reg."""
import json, re, html as H, os

L9 = ["de","en","sk","hr","pl","es","it","fr","sv"]
h = open('303.html', encoding='utf-8').read()

def gtl(seg, cls="gtl"):
    """z useku vytiahne prvu sadu 9 jazykovych spanov/divov"""
    out = {}
    for L, t in re.findall(r'<(?:span|div) class="'+cls+r' (\w\w)">(.*?)</(?:span|div)>', seg, re.S):
        if L in L9 and L not in out:
            out[L] = re.sub(r'<[^>]+>', '', t).strip()
    return out

def gtl_html(seg, cls="gtl-b"):
    """to iste, ale zachova HTML (pre suhrny a sprievodne texty)"""
    out = {}
    for L, t in re.findall(r'<div class="'+cls+r' (\w\w)">(.*?)(?=<div class="'+cls+r' \w\w">|</div></div>)', seg, re.S):
        if L in L9 and L not in out:
            out[L] = t.strip()
    return out

# ─────────── KAUZY (dlaždice #fia-reg) ───────────
reg = h[h.find('id="fia-reg"'):][:60000]
kauzy = []
for at, inner in re.findall(r'<button class="rbtn"([^>]*)>(.*?)</button>', reg, re.S):
    def a(n, d=""):
        m = re.search(n+r'="([^"]*)"', at); return m.group(1) if m else d
    rt = re.search(r'<span class="rt">(.*?)</span>\s*<span class="rs"', inner, re.S)
    rw = re.search(r'<span class="rw">(.*?)</span>', inner, re.S)
    kauzy.append(dict(spis=a("data-spis"), jur=a("data-jur").split(), ids=a("data-ids").split(),
                      nazov=gtl(rt.group(1) if rt else inner), warn=gtl(rw.group(1)) if rw else {}))

# ─────────── KARTY ───────────
karty = []
hran = []
for m in re.finditer(r'<details class="case"([^>]*)>(.*?)</summary>', h, re.S):
    at, head = m.group(1), m.group(2)
    def a(n, d=""):
        r = re.search(n+r'="([^"]*)"', at); return r.group(1) if r else d
    cid = a("id")
    hran.append((m.start(), cid))
    tit  = re.search(r'<div class="case-title">(.*?)</div>', head, re.S)
    sub  = re.search(r'<div class="court-subj"[^>]*>(.*?)</div>', head, re.S)
    meta = re.search(r'<div class="case-meta">(.*?)</div>', head, re.S)
    pill = re.search(r'<span class="pill ([^"]*)">(.*?)</span>\s*<span class="chev"', head, re.S)
    dat  = re.search(r'<span class="case-date">([^<]*)</span>', head)
    # sprievodny text karty = modal <div id="<cid>-modal" class="kmodal">
    mod = re.search(r'<div id="'+re.escape(cid)+r'-modal" class="kmodal">(.*?)</div></div>', h, re.S)
    karty.append(dict(
        id=cid, pin=a("data-pin"), jur=a("data-cat").split(), date=a("data-date"),
        az=a("data-az"), ourref=a("data-ourref"), area=a("data-area").split(),
        organ_txt=a("data-court"), datum_txt=(dat.group(1).replace("📅","").strip() if dat else ""),
        nazov=gtl(tit.group(1)) if tit else {},
        podtitul=gtl(sub.group(1)) if sub else {},
        meta=gtl(meta.group(1)) if meta else {},
        stav=gtl(pill.group(2)) if pill else {},
        stav_trieda=(pill.group(1) if pill else ""),
        sprievodny=gtl_html(mod.group(1)) if mod else {},
    ))

def karta_pre(pos):
    cur = ""
    for st, cid in hran:
        if st <= pos: cur = cid
        else: break
    return cur

# ─────────── POLOŽKY ───────────
poz = [m.start() for m in re.finditer(r'<div class="item[^"]*"[^>]{0,60}?data-snap=', h)]
bloky = re.split(r'(?=<div class="item[^"]*"[^>]{0,60}?data-snap=)', h)
polozky = []
for idx, b in enumerate(bloky[1:]):
    ms = re.match(r"<div class=\"item[^\"]*\"[^>]{0,60}?data-snap='(.*?)'>", b, re.S)
    if not ms: continue
    try: snap = json.loads(H.unescape(ms.group(1)))
    except Exception: continue
    telo = b[:60000]
    subj = re.search(r'<div class="subj">(.*?)</div>', telo, re.S)
    sm   = re.search(r'href="#(summod-[^"]+)"', telo)
    links = {}
    for L, u in re.findall(r'<span class="gtl (\w\w)"><a class="open" href="([^"]+)"', telo):
        links.setdefault(L, H.unescape(u))
    p = dict(snap)                       # VSETKY polia zo snapu
    p["karta"]     = karta_pre(poz[idx]) if idx < len(poz) else ""
    p["subj9"]     = gtl(subj.group(1)) if subj else {}
    p["urls"]      = snap.get("urls") or links
    p["summodId"]  = snap.get("summodId") or (sm.group(1) if sm else "")
    p["dolezite"]  = bool(snap.get("important"))
    p["komentare"] = bool(snap.get("comments"))
    p["oblast"]    = (snap.get("cats") or {}).get("area", [])
    p["jur"]       = (snap.get("cats") or {}).get("jur", [])
    polozky.append(p)

# ─────────── SÚHRNY ───────────
suhrny = {}
for m in re.finditer(r'<div id="(summod-[^"]+)" class="kmodal summod">(.*?)(?=<div id="|<div class="item"|</details>)', h, re.S):
    d = gtl_html(m.group(2))
    if d: suhrny[m.group(1)] = d

# ─────────── priradenie karta -> kauza ───────────
k2k = {cid: z["spis"] for z in kauzy for cid in z["ids"]}
for p in polozky:
    if k2k.get(p.get("karta")): p["kauza"] = k2k[p["karta"]]

D = dict(kauzy_reg=kauzy, karty=karty, polozky=polozky, suhrny=suhrny,
         kauzy=[dict(spis=z["spis"], jur=z["jur"], ids=z["ids"],
                     n=sum(1 for p in polozky if p.get("karta") in z["ids"])) for z in kauzy])
json.dump(D, open('fia_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)

print(f"KAUZY   {len(kauzy)}")
print(f"KARTY   {len(karty)}")
print(f"POLOZKY {len(polozky)}")
print(f"SUHRNY  {len(suhrny)}  ({sum(len(v) for v in suhrny.values())} jazykovych verzii)")
print("\nvyplnenost poli KARTY:")
for f in ["pin","jur","date","az","ourref","area","organ_txt","nazov","podtitul","meta","stav","sprievodny"]:
    n = sum(1 for k in karty if k.get(f))
    print(f"  {f:<12} {n:>2}/{len(karty)}")
print("\nvyplnenost poli POLOZKY:")
for f in ["access","az","ourref","court","begleit","cardsubj","summary","summodId","fname","fpath",
          "fallback","thread","replyTo","extra","dolezite","komentare","oblast","subj9","urls"]:
    n = sum(1 for p in polozky if p.get(f))
    print(f"  {f:<12} {n:>2}/{len(polozky)}")
print("\nsubor:", os.path.getsize('fia_data.json'), "B")
