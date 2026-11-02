#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Générateur du site statique Clé en Main Genève.

Usage :  python3 src/build.py
Sortie : dossier public/ (prêt à déployer sur Netlify ou Vercel).
Aucune dépendance : Python 3.8+ standard uniquement.
"""
import html
import json
import os
import re
from datetime import date

import content as C

# ==========================================================================
# CONFIGURATION — à compléter avant la mise en ligne
# ==========================================================================
SITE_URL = os.environ.get("SITE_URL", "https://www.cle-en-main-geneve.ch").rstrip("/")
NAME = "Clé en Main Genève"
PHONE_DISPLAY = "+41 79 942 95 44"
PHONE_TEL = "+41799429544"

# --- Titulaire (obligatoire pour une entreprise individuelle) ---------------
OWNER_NAME = "[NOM DU TITULAIRE]"   # prénom et nom du titulaire, ex. "Jean Dupont"

# --- Adresse ----------------------------------------------------------------
STREET = ""                    # rue et numéro (facultatif), ex. "Chemin de l'Exemple 12"
POSTAL_CODE = "1224"
LOCALITY = "Chêne-Bougeries"
ADDRESS = ", ".join(x for x in [STREET, f"{POSTAL_CODE} {LOCALITY}"] if x)
IDE = ""                       # numéro IDE si l'entreprise en obtient un, ex. "CHE-123.456.789" (vide = non affiché)
HOSTING = "Netlify, Inc., San Francisco, Californie, États-Unis – www.netlify.com"

# --- Horaires ---------------------------------------------------------------
# True  = le site annonce « 7j/7, 24h/24 ». À n'activer QUE si quelqu'un répond
#         réellement au téléphone la nuit, le week-end et les jours fériés.
# False = le site annonce les horaires de HOURS ci-dessous.
HOURS_24_7 = False
# Horaires normaux (utilisés si HOURS_24_7 = False). None = fermé ce jour-là.
HOURS = {
    "lundi":    ("07:00", "20:00"),
    "mardi":    ("07:00", "20:00"),
    "mercredi": ("07:00", "20:00"),
    "jeudi":    ("07:00", "20:00"),
    "vendredi": ("07:00", "20:00"),
    "samedi":   ("08:00", "18:00"),
    "dimanche": None,
}
LASTMOD = date.today().isoformat()

# ==========================================================================
# Textes d'horaires dérivés de la configuration (ne pas modifier)
# ==========================================================================
DAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
DAYS_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ABBR = {"lundi": "lun", "mardi": "mar", "mercredi": "mer", "jeudi": "jeu", "vendredi": "ven", "samedi": "sam", "dimanche": "dim"}


def _h(t):
    hh, mm = t.split(":")
    return f"{int(hh)}h" + ("" if mm == "00" else mm)


def _groups():
    """Regroupe les jours consécutifs ayant les mêmes horaires."""
    out = []
    for d in DAYS:
        v = HOURS.get(d)
        if v is None:
            continue
        if out and out[-1][2] == v and DAYS.index(out[-1][1]) == DAYS.index(d) - 1:
            out[-1][1] = d
        else:
            out.append([d, d, v])
    return out


if HOURS_24_7:
    J7, J7L = "7j/7", "7 jours sur 7"
    DISPO = "7j/7, 24h/24"
    DISPO_LONG = "7 jours sur 7, 24 heures sur 24, jours fériés compris"
else:
    _n = sum(1 for d in DAYS if HOURS.get(d))
    J7 = f"{_n}j/7"
    J7L = f"{_n} jours sur 7"
    DISPO = ", ".join(
        (ABBR[a] if a == b else f"{ABBR[a]}–{ABBR[b]}") + f" {_h(o)}–{_h(c)}" for a, b, (o, c) in _groups())
    DISPO_LONG = ", ".join(
        (f"le {a}" if a == b else f"du {a} au {b}") + f" de {_h(o).replace('h', ' h ').strip()} à {_h(c).replace('h', ' h ').strip()}"
        for a, b, (o, c) in _groups())

TOKENS = {"{DISPO_LONG}": DISPO_LONG, "{DISPO}": DISPO, "{J7L}": J7L, "{J7}": J7}
_COND = re.compile(r"\[\[(.*?)\|\|(.*?)\]\]", re.S)


def resolve(x):
    """Applique les horaires aux textes : {DISPO}, {J7}… et [[si 24/7||sinon]]."""
    if isinstance(x, str):
        x = _COND.sub(lambda m: m.group(1) if HOURS_24_7 else m.group(2), x)
        for k, v in TOKENS.items():
            x = x.replace(k, v)
        return x
    if isinstance(x, dict):
        return {k: resolve(v) for k, v in x.items()}
    if isinstance(x, list):
        return [resolve(v) for v in x]
    if isinstance(x, tuple):
        return tuple(resolve(v) for v in x)
    return x


SERVICES, COMMUNES, HOME_FAQ, STEPS, LOCAL = (resolve(C.SERVICES), resolve(C.COMMUNES), resolve(C.HOME_FAQ),
                                       resolve(C.STEPS), resolve(C.LOCAL))

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
SVC = {s["slug"]: s for s in SERVICES}
COM = {c["slug"]: c for c in COMMUNES}
e = html.escape

# ==========================================================================
# CSS (inline dans chaque page : zéro requête bloquante)
# ==========================================================================
CSS = """
:root{--red:#B3121F;--red-d:#8f0e18;--yel:#F2B705;--cream:#FBF8F1;--dark:#1F1A17;--muted:#5b524b;--line:#e7dfcf;--white:#fff;
--fh:Archivo,"Arial Black","Helvetica Neue",Arial,sans-serif;--fb:Inter,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--cream);color:var(--dark);font:400 1rem/1.65 var(--fb);padding-bottom:84px}
@media(min-width:900px){body{padding-bottom:0}}
h1,h2,h3{font-family:var(--fh);font-weight:900;line-height:1.08;letter-spacing:-.015em;margin:0 0 .55em}
h1{font-size:clamp(2rem,7vw,3.5rem)}h2{font-size:clamp(1.55rem,4.6vw,2.35rem)}h3{font-size:1.2rem;line-height:1.2}
p{margin:0 0 1em}a{color:var(--red);text-underline-offset:2px}
img{max-width:100%;height:auto;display:block}
ul,ol{padding-left:1.2rem;margin:0 0 1em}li{margin:.25em 0}
.wrap{max-width:1140px;margin:0 auto;padding:0 16px}
.skip{position:absolute;left:-9999px;top:8px;background:#fff;padding:8px 12px;z-index:100}.skip:focus{left:16px}
.ico{width:1.15em;height:1.15em;flex:none;fill:currentColor}
/* bandeau urgence */
.urgent{background:var(--red);color:#fff;font-size:.86rem;font-weight:600}
.urgent .wrap{display:flex;flex-wrap:wrap;gap:.15rem 1rem;justify-content:center;align-items:center;padding-top:.45rem;padding-bottom:.45rem;text-align:center}
.urgent a{color:#fff;font-weight:700;white-space:nowrap}
.pulse{display:inline-block;width:.55rem;height:.55rem;border-radius:50%;background:var(--yel);margin-right:.45rem;vertical-align:.05em}
/* en-tête */
.site-h{background:var(--cream);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50}
.hbar{display:flex;align-items:center;justify-content:space-between;gap:10px;min-height:66px}
.brand{display:flex;align-items:center;gap:.6rem;color:var(--dark);text-decoration:none;font:900 1.02rem/1.05 var(--fh)}
.brand svg{width:40px;height:40px;flex:none;border-radius:6px}
.brand small{display:block;font:700 .66rem/1.4 var(--fb);color:var(--red);letter-spacing:.09em;text-transform:uppercase}
.nav{display:none}
.nav a{color:var(--dark);text-decoration:none;font-weight:600;font-size:.92rem;padding:.4rem .55rem;border-radius:6px}
.nav a:hover,.nav a[aria-current]{background:#f1e9d8}
.hright{display:flex;align-items:center;gap:8px}
.menu{position:relative}
.menu summary{list-style:none;cursor:pointer;font-weight:700;font-size:.9rem;padding:.6rem .7rem;border:2px solid var(--dark);border-radius:10px;min-height:44px;display:flex;align-items:center}
.menu summary::-webkit-details-marker{display:none}
.menu[open] summary{background:var(--dark);color:#fff}
.menu-p{position:absolute;right:0;top:calc(100% + 8px);background:#fff;border:1px solid var(--line);border-radius:12px;box-shadow:0 12px 30px rgba(31,26,23,.15);padding:8px;width:min(86vw,300px)}
.menu-p a{display:block;padding:.7rem .8rem;color:var(--dark);text-decoration:none;font-weight:600;border-radius:8px}
.menu-p a:hover{background:var(--cream)}
@media(min-width:1000px){.nav{display:flex;gap:2px}.menu{display:none}}
/* boutons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.55rem;font-weight:700;text-decoration:none;border-radius:12px;padding:.85rem 1.25rem;min-height:50px;line-height:1.2;border:2px solid transparent;transition:transform .15s,background .15s}
.btn:hover{transform:translateY(-1px)}
.b-red{background:var(--red);color:#fff}.b-red:hover{background:var(--red-d)}
.b-yel{background:var(--yel);color:var(--dark)}
.b-dark{background:var(--dark);color:#fff}
.b-ghost{border-color:currentColor;color:inherit}
.b-sm{padding:.5rem .8rem;min-height:44px;font-size:.92rem;border-radius:10px}
.hphone .lbl{display:none}@media(min-width:420px){.hphone .lbl{display:inline}}
/* hero */
.hero{background:var(--dark);color:var(--cream);padding:36px 0 44px;overflow:hidden}
.hero-g{display:grid;gap:28px;align-items:center}
@media(min-width:900px){.hero{padding:64px 0 72px}.hero-g{grid-template-columns:1.3fr .7fr}}
.kick{display:inline-block;font:800 .78rem/1.3 var(--fb);letter-spacing:.09em;text-transform:uppercase;background:var(--yel);color:var(--dark);padding:.35rem .6rem;border-radius:6px;margin-bottom:.9rem}
h1 .kick{display:table}
.hl{color:var(--yel)}
.lead{font-size:1.1rem;color:#ece4d4;max-width:40rem}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin:1.4rem 0 1.1rem}
.checks{list-style:none;padding:0;margin:0;display:grid;gap:.45rem;font-size:.97rem}
.checks li{display:flex;gap:.55rem;align-items:flex-start;margin:0}
.checks li::before{content:"";flex:none;width:1.15rem;height:1.15rem;margin-top:.22rem;border-radius:50%;background:var(--yel) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9.5 16.2 5.3 12l-1.4 1.4 5.6 5.6L21 7.5l-1.4-1.4z' fill='%231F1A17'/%3E%3C/svg%3E") center/80% no-repeat}
.hero-img{max-width:340px;margin:0 auto;width:100%;aspect-ratio:640/560;border-radius:18px}
@media(min-width:900px){.hero-img{max-width:440px}}
/* page intérieure */
.phero{background:var(--dark);color:var(--cream);padding:24px 0 36px}
@media(min-width:900px){.phero{padding:40px 0 52px}}
.phero h1{font-size:clamp(1.8rem,5.6vw,3rem);max-width:52rem}
.crumbs{font-size:.84rem;margin-bottom:1rem;color:#cfc6b6}
.crumbs ol{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.3rem}
.crumbs li{margin:0}.crumbs li+li::before{content:"›";margin-right:.3rem;color:var(--yel)}
.crumbs a{color:#efe8da}
/* sections */
.sec{padding:52px 0}@media(min-width:900px){.sec{padding:76px 0}}
.sec-w{background:#fff}
.sec-h{max-width:46rem;margin-bottom:28px}
.sec-h p{color:var(--muted);font-size:1.05rem}
.eyebrow{font:800 .78rem/1.3 var(--fb);letter-spacing:.1em;text-transform:uppercase;color:var(--red);margin-bottom:.6rem}
.cards{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;border-top:5px solid var(--red)}
.sec-w .card{background:var(--cream)}
.card img{width:100%;aspect-ratio:4/3;object-fit:cover;background:var(--cream)}
.card-b{padding:18px 18px 20px;display:flex;flex-direction:column;flex:1}
.card-b p{color:var(--muted);flex:1}
.card-b a.more{font-weight:700;text-decoration:none}
.card-b a.more::after{content:" →"}
/* bandeau jaune */
.band{background:var(--yel);color:var(--dark);padding:40px 0}
.band-g{display:grid;gap:18px;align-items:center}
@media(min-width:900px){.band-g{grid-template-columns:1fr auto}}
.band h2{margin:0 0 .35em}.band p{margin:0;font-weight:600}
.band .btn{font-size:1.15rem;padding:1rem 1.5rem}
/* zones */
.zg{display:grid;gap:26px}@media(min-width:800px){.zg{grid-template-columns:2fr 1fr}}
.zg h3{font-size:1rem;font-family:var(--fb);font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:0}
.chips li{margin:0}
.chips a{display:inline-flex;align-items:center;min-height:44px;padding:.45rem .95rem;border-radius:999px;background:#fff;border:1.5px solid var(--line);color:var(--dark);text-decoration:none;font-weight:600}
.sec-w .chips a{background:var(--cream)}
.chips a:hover{border-color:var(--red);color:var(--red)}
/* faq */
.faq{max-width:50rem}
.faq details{background:#fff;border:1px solid var(--line);border-radius:12px;margin-bottom:10px}
.sec-w .faq details{background:var(--cream)}
.faq summary{cursor:pointer;list-style:none;padding:16px 48px 16px 18px;font-weight:700;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:18px;top:50%;transform:translateY(-50%);font:900 1.4rem/1 var(--fh);color:var(--red)}
.faq details[open] summary::after{content:"–"}
.faq details>div{padding:0 18px 16px;color:var(--muted)}
.faq details>div p{margin:0}
/* contenu + aside */
.cols{display:grid;gap:32px}@media(min-width:960px){.cols{grid-template-columns:minmax(0,1fr) 330px;gap:48px}}
.prose{max-width:46rem}
.prose h2{margin-top:1.6em}.prose h2:first-child{margin-top:0}
.prose h3{margin-top:1.2em}
.aside-box{background:var(--dark);color:var(--cream);border-radius:18px;padding:22px}
@media(min-width:960px){.aside-box{position:sticky;top:90px}}
.aside-box .btn{width:100%;margin:.6rem 0}
.aside-box p{color:#e2dacb;font-size:.95rem}
.aside-box .big{font:900 1.35rem/1.15 var(--fh);color:#fff}
.tip{background:#fff;border-left:6px solid var(--yel);border-radius:0 12px 12px 0;padding:16px 18px;margin:1.4em 0}
.tip strong{display:block;font-family:var(--fh);font-weight:900;margin-bottom:.3em}
.sit{display:grid;gap:12px;margin:1em 0 1.4em}
.sit div{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.sit h3{margin-top:0;font-size:1.08rem}.sit p{margin:0;color:var(--muted)}
.steps{counter-reset:s;list-style:none;padding:0;display:grid;gap:14px;margin:0}
@media(min-width:800px){.steps{grid-template-columns:repeat(3,1fr)}}
.steps li{counter-increment:s;background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:18px;margin:0}
.steps li::before{content:counter(s);display:grid;place-items:center;width:2.2rem;height:2.2rem;border-radius:50%;background:var(--red);color:#fff;font:900 1.1rem/1 var(--fh);margin-bottom:.6rem}
.steps strong{display:block;font-family:var(--fh);font-weight:900;font-size:1.1rem;margin-bottom:.25rem}
.svc-img{border-radius:16px;margin:1.2em 0;max-width:420px;width:100%;aspect-ratio:4/3}
.alert{background:#fff3f3;border:2px solid var(--red);border-radius:12px;padding:14px 16px}
.info{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));margin:1.2em 0}
.info div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px}
.info strong{display:block;font-family:var(--fh);font-weight:900;margin-bottom:.2em}
/* pied de page */
.foot{background:var(--dark);color:#d9d0c0;padding:48px 0 28px;font-size:.93rem}
.foot a{color:#fff;text-decoration:none}.foot a:hover{text-decoration:underline}
.fg{display:grid;gap:28px}@media(min-width:800px){.fg{grid-template-columns:1.3fr 1fr 1.4fr}}
.foot .brand{color:#fff}.foot .brand small{color:var(--yel)}
.fh{font:900 1rem/1.2 var(--fh);color:var(--yel);margin:0 0 .7em}
.flist{list-style:none;padding:0;margin:0;columns:2;column-gap:16px}.flist li{margin:0 0 .4em;break-inside:avoid}
.flist.one{columns:1}
.legal{border-top:1px solid #3a332e;margin-top:32px;padding-top:18px;display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between;font-size:.84rem;color:#a99f90}
/* barre d'appel mobile */
.callbar{position:fixed;left:0;right:0;bottom:0;z-index:60;padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:rgba(31,26,23,.97)}
.callbar a{width:100%;font-size:1.08rem;min-height:56px}
@media(min-width:900px){.callbar{display:none}}
:focus-visible{outline:3px solid var(--yel);outline-offset:2px}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

# ==========================================================================
# Fragments
# ==========================================================================
ICO_PHONE = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>'
LOGO = ('<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="32" height="64" fill="#F2B705"/>'
        '<rect x="32" width="32" height="64" fill="#B3121F"/><circle cx="22" cy="32" r="9" fill="none" stroke="#fff" stroke-width="5"/>'
        '<rect x="29" y="29.5" width="24" height="5" rx="1.5" fill="#fff"/><rect x="43" y="33" width="4.5" height="8" rx="1" fill="#fff"/>'
        '<rect x="49" y="33" width="4.5" height="6" rx="1" fill="#fff"/></svg>')

DEVIS = "Devis gratuit par téléphone avant intervention"
LANGS = "On vous répond en FR, EN, ES"


def tel_link(cls="btn b-red", label=None, extra=""):
    label = label or f'Appeler le {PHONE_DISPLAY}'
    return f'<a class="{cls}" href="tel:{PHONE_TEL}"{extra}>{ICO_PHONE}<span>{label}</span></a>'


def url(path):
    return SITE_URL + path


GE = [c for c in COMMUNES if c["canton"] == "GE"]
VD = [c for c in COMMUNES if c["canton"] == "VD"]


def chips(coms, current=None):
    items = "".join(
        f'<li><a href="/{c["slug"]}/"{" aria-current=\"page\"" if c["slug"] == current else ""}>{e(c["label"])}</a></li>'
        for c in coms)
    return f'<ul class="chips">{items}</ul>'


def faq_html(items):
    return '<div class="faq">' + "".join(
        f'<details><summary>{e(q)}</summary><div><p>{a}</p></div></details>' for q, a in items) + "</div>"


def service_cards(exclude=None, heading_level=3):
    out = []
    for s in SERVICES:
        if s["slug"] == exclude:
            continue
        out.append(
            f'<article class="card"><img src="/img/{s["img"]}.webp" alt="{e(s["img_alt"])}" width="480" height="360" loading="lazy" decoding="async">'
            f'<div class="card-b"><h{heading_level}>{e(s["name"])}</h{heading_level}><p>{e(s["short"])}</p>'
            f'<a class="more" href="/{s["slug"]}/">{e(s["name"])} à Genève</a></div></article>')
    return '<div class="cards">' + "".join(out) + "</div>"


def call_band(title="Bloqué devant votre porte ? Appelez maintenant."):
    return (f'<section class="band" aria-label="Appeler un serrurier"><div class="wrap band-g"><div><h2>{e(title)}</h2>'
            f'<p>{DEVIS} · {DISPO} · {LANGS}.</p></div>{tel_link("btn b-dark")}</div></section>')


def aside(context=""):
    return (f'<aside><div class="aside-box"><p class="big">Besoin d\'un serrurier{e(context)} maintenant ?</p>'
            f'<p>Un serrurier décroche {"7j/7, 24h/24" if HOURS_24_7 else DISPO}. {DEVIS} : rien n\'est fait sans votre accord.</p>'
            f'{tel_link("btn b-yel", PHONE_DISPLAY)}<p>{LANGS}.</p></div></aside>')


def crumbs(items):
    lis = []
    for i, (label, path) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{e(label)}</li>')
        else:
            lis.append(f'<li><a href="{path}">{e(label)}</a></li>')
    return f'<nav class="crumbs" aria-label="Fil d\'Ariane"><ol>{"".join(lis)}</ol></nav>'


# ==========================================================================
# Données structurées
# ==========================================================================
def opening_hours_ld():
    if HOURS_24_7:
        return [{"@type": "OpeningHoursSpecification", "dayOfWeek": DAYS_EN, "opens": "00:00", "closes": "23:59"}]
    return [{"@type": "OpeningHoursSpecification", "dayOfWeek": DAYS_EN[DAYS.index(d)], "opens": HOURS[d][0], "closes": HOURS[d][1]}
            for d in DAYS if HOURS.get(d)]


def business_ld():
    area = [{"@type": "City", "name": c["name"] if c["slug"] != "serrurier-grand-saconnex" else "Le Grand-Saconnex"} for c in COMMUNES]
    return {
        "@context": "https://schema.org",
        "@type": "Locksmith",
        "@id": url("/#entreprise"),
        "name": NAME,
        "url": url("/"),
        "telephone": PHONE_TEL,
        "image": url("/img/og-image.jpg"),
        "logo": url("/img/logo-512.png"),
        "description": "Serrurier à Genève et sur La Côte : ouverture de porte, changement de serrure, sécurisation et blindage, mise en sécurité après effraction. " + DISPO_LONG[0].upper() + DISPO_LONG[1:] + ". Devis gratuit par téléphone avant intervention.",
        "address": {"@type": "PostalAddress", **({"streetAddress": STREET} if STREET else {}), "postalCode": POSTAL_CODE, "addressLocality": LOCALITY,
                    "addressRegion": "GE", "addressCountry": "CH"},
        "areaServed": area,
        "openingHoursSpecification": opening_hours_ld(),
        "knowsLanguage": ["fr", "en", "es"],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": url(f'/{s["slug"]}/')}} for s in SERVICES],
    }


def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": label, "item": url(path)} for i, (label, path) in enumerate(items)]}


def faq_ld(items):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in items]}


def ld_script(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


# ==========================================================================
# Gabarit de page
# ==========================================================================
NAV = [("Ouverture de porte", "/ouverture-de-porte-geneve/"), ("Serrures", "/changement-de-serrure-geneve/"),
       ("Blindage", "/securisation-blindage-geneve/"), ("Après effraction", "/apres-effraction-geneve/"),
       ("Zones", "/#zones"), ("Contact", "/contact/")]


def header(path):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{l}</a>' for l, h in NAV)
    menu = "".join(f'<a href="{h}">{l}</a>' for l, h in [("Accueil", "/")] + NAV)
    return f"""<a class="skip" href="#contenu">Aller au contenu</a>
<div class="urgent"><div class="wrap"><span><span class="pulse" aria-hidden="true"></span>{'Urgence serrurerie 7j/7 – 24h/24' if HOURS_24_7 else 'Serrurerie · ' + DISPO}</span><span>{DEVIS} : <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span></div></div>
<header class="site-h"><div class="wrap hbar">
<a class="brand" href="/">{LOGO}<span>Clé en Main<small>Serrurier Genève</small></span></a>
<nav class="nav" aria-label="Navigation principale">{nav}</nav>
<div class="hright">{tel_link("btn b-red b-sm hphone", f'<span class="lbl">{PHONE_DISPLAY}</span>', f' aria-label="Appeler le {PHONE_DISPLAY}"')}
<details class="menu"><summary>Menu</summary><nav class="menu-p" aria-label="Menu mobile">{menu}</nav></details></div>
</div></header>"""


def footer():
    svc = "".join(f'<li><a href="/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    com = "".join(f'<li><a href="/{c["slug"]}/">Serrurier {e(c["label"])}</a></li>' for c in COMMUNES)
    return f"""<footer class="foot"><div class="wrap"><div class="fg">
<div><a class="brand" href="/">{LOGO}<span>{NAME}<small>Serrurier {J7}</small></span></a>
<p style="margin-top:1rem">Serrurerie à Genève et sur La Côte vaudoise : ouverture de porte, changement de serrure, sécurisation et mise en sécurité après effraction.</p>
<p><a href="tel:{PHONE_TEL}"><strong>{PHONE_DISPLAY}</strong></a><br>{DISPO} · {LANGS}<br>{DEVIS}</p>
<p>{e(ADDRESS)}{"<br>IDE : " + e(IDE) if IDE else ""}</p></div>
<div><p class="fh">Services</p><ul class="flist one">{svc}<li><a href="/contact/">Contact</a></li></ul></div>
<div><p class="fh">Communes desservies</p><ul class="flist">{com}</ul></div>
</div>
<div class="legal"><span>© {date.today().year} {NAME}</span><span><a href="/mentions-legales/">Mentions légales et confidentialité</a> · <a href="/contact/">Contact</a> · <a href="/sitemap.xml">Plan du site</a></span></div>
</div></footer>
<div class="callbar">{tel_link("btn b-red", f"Appeler · {PHONE_DISPLAY}")}</div>"""


def page(path, title, desc, body, ld=(), robots="index,follow", og_type="website"):
    canonical = url(path)
    fonts = "https://fonts.googleapis.com/css2?family=Archivo:wght@900&family=Inter:wght@400;600;700;800&display=swap"
    lds = "\n".join(ld_script(x) for x in ld)
    return f"""<!doctype html>
<html lang="fr-CH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{"" if robots.startswith("noindex") else f'<link rel="canonical" href="{canonical}">'}
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#1F1A17">
<meta name="format-detection" content="telephone=yes">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="fr_CH">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{url('/img/og-image.jpg')}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="{fonts}"></noscript>
<style>{" ".join(l.strip() for l in CSS.strip().splitlines())}</style>
{lds}
</head>
<body>
{header(path)}
<main id="contenu">
{body}
</main>
{footer()}
</body>
</html>
"""


def write(path, content):
    rel = path.strip("/")
    target = os.path.join(ROOT, rel, "index.html") if rel and not rel.endswith(".html") else os.path.join(ROOT, rel or "index.html")
    if rel == "":
        target = os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)


# ==========================================================================
# Pages
# ==========================================================================
def build_home():
    body = f"""
<section class="hero"><div class="wrap hero-g"><div>
<h1><span class="kick">Serrurier Genève · {'7j/7 · 24h/24' if HOURS_24_7 else J7}</span> Porte claquée, clé perdue, serrure bloquée ? <span class="hl">On s'en occupe.</span></h1>
<p class="lead">Clé en Main Genève, c'est un serrurier qui décroche, vous écoute et vous explique avant de venir ce qu'il va faire. {DEVIS}, à Genève et sur La Côte.</p>
<div class="ctas">{tel_link("btn b-yel")}<a class="btn b-ghost" href="#services">Nos interventions</a></div>
<ul class="checks"><li>{DEVIS}</li><li>Rien n'est fait sans votre accord</li><li>{LANGS}</li></ul>
</div>
<img class="hero-img" src="/img/hero-porte.webp" alt="Illustration d'une porte rouge et d'une clé, symbole de Clé en Main Genève" width="640" height="560" fetchpriority="high" decoding="async">
</div></section>

<section class="sec" id="services"><div class="wrap">
<div class="sec-h"><p class="eyebrow">Nos interventions</p><h2>Quatre métiers, un seul numéro</h2>
<p>Dépannage urgent ou projet réfléchi : on vous dit au téléphone ce qui est nécessaire, et seulement ce qui est nécessaire.</p></div>
{service_cards()}
</div></section>

{call_band()}

<section class="sec sec-w" id="zones"><div class="wrap">
<div class="sec-h"><p class="eyebrow">Zones d'intervention</p><h2>Serrurier à Genève et sur La Côte</h2>
<p>Nous intervenons dans tout le canton de Genève et jusqu'à Gland. Que vous ayez tapé « serrurier Genève » ou « serrurier geneve », choisissez votre commune pour voir comment on y travaille.</p></div>
<div class="zg"><div><h3>Canton de Genève</h3>{chips(GE)}</div><div><h3>Canton de Vaud – La Côte</h3>{chips(VD)}</div></div>
<p style="margin-top:1.4rem;color:var(--muted)">Votre commune n'est pas dans la liste ? Appelez le <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> : on vous dit franchement si on peut venir, et dans quel délai.</p>
</div></section>

<section class="sec" id="faq"><div class="wrap">
<div class="sec-h"><p class="eyebrow">FAQ</p><h2>Questions fréquentes</h2></div>
{faq_html(HOME_FAQ)}
</div></section>
"""
    write("/", page("/", f"Serrurier Genève – Dépannage {J7} | Clé en Main Genève",
                    f"Serrurier Genève {DISPO} : porte claquée, clé perdue, serrure bloquée. Devis gratuit par téléphone avant intervention. On répond en FR, EN, ES.",
                    body, ld=[business_ld(), faq_ld(HOME_FAQ)]))


def build_service(s):
    path = f'/{s["slug"]}/'
    bc = [("Accueil", "/"), ("Services", "/#services"), (s["name"], path)]
    secs = "".join(f'<h2>{e(t)}</h2>' + "".join(p if p.startswith("<") else f"<p>{p}</p>" for p in ps)
                   for t, ps in s["sections"])
    steps = "".join(f"<li><strong>{e(t)}</strong>{e(d)}</li>" for t, d in STEPS)
    body = f"""
<section class="phero"><div class="wrap">{crumbs(bc)}
<h1>{e(s["h1"])}</h1><p class="lead">{e(s["lead"])}</p>
<div class="ctas">{tel_link("btn b-yel")}</div>
<ul class="checks"><li>{DEVIS}</li><li>{DISPO}</li><li>{LANGS}</li></ul>
</div></section>
<section class="sec"><div class="wrap cols"><div class="prose">
{secs}
<img class="svc-img" src="/img/{s["img"]}.webp" alt="{e(s["img_alt"])}" width="480" height="360" loading="lazy" decoding="async">
<h2>Questions fréquentes : {e(s["name"].lower())}</h2>
{faq_html(s["faq"])}
</div>{aside()}</div></section>
<section class="sec sec-w"><div class="wrap"><div class="sec-h"><h2>Comment se passe l'intervention</h2></div><ol class="steps">{steps}</ol></div></section>
{call_band()}
<section class="sec"><div class="wrap"><div class="sec-h"><h2>Nos autres services</h2></div>{service_cards(exclude=s["slug"])}</div></section>
<section class="sec sec-w"><div class="wrap"><div class="sec-h"><h2>{e(s["name"])} : où intervenons-nous ?</h2>
<p>Dans tout le canton de Genève et sur La Côte vaudoise. Choisissez votre commune :</p></div>
<div class="zg"><div><h3>Canton de Genève</h3>{chips(GE)}</div><div><h3>Canton de Vaud – La Côte</h3>{chips(VD)}</div></div></div></section>
"""
    write(path, page(path, s["title"], s["desc"], body, ld=[business_ld(), breadcrumb_ld(bc)]))


def build_commune(c):
    path = f'/{c["slug"]}/'
    bc = [("Accueil", "/"), ("Zones", "/#zones"), (c["label"], path)]
    canton = "Canton de Genève" if c["canton"] == "GE" else "Canton de Vaud · La Côte"
    sits = "".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d in c["situations"])
    svc_links = "".join(
        f'<li><a href="/{s["slug"]}/"><strong>{e(s["name"])}</strong></a> – {e(s["short"])}</li>' for s in SERVICES)
    near = [COM[n] for n in c["near"]]
    body = f"""
<section class="phero"><div class="wrap">{crumbs(bc)}
<span class="kick">{canton}</span>
<h1>{e(c["h1"])}</h1><p class="lead">{e(c["lead"])}</p>
<div class="ctas">{tel_link("btn b-yel")}</div>
<ul class="checks"><li>{DEVIS}</li><li>{DISPO}</li><li>{LANGS}</li></ul>
</div></section>
<section class="sec"><div class="wrap cols"><div class="prose">
{"".join(f"<p>{p}</p>" for p in c["intro"])}
<h2>{e(c["label"])} : quartiers, bâtiments et repères</h2>
{"".join(f"<p>{e(p)}</p>" for p in LOCAL[c["slug"]])}
<h2>Ce qu'on rencontre souvent à {e(c["label"])}</h2>
<div class="sit">{sits}</div>
<div class="tip"><strong>Le conseil du serrurier</strong>{e(c["tip"])}</div>
<h2>Nos services à {e(c["label"])}</h2>
<ul>{svc_links}</ul>
<h2>Questions fréquentes à {e(c["label"])}</h2>
{faq_html(c["faq"])}
<h2>Nous intervenons aussi à proximité</h2>
{chips(near)}
<p style="margin-top:1rem"><a href="/#zones">Voir toutes nos zones d'intervention</a></p>
</div>{aside(" à " + c["label"])}</div></section>
{call_band(f"Serrurier à {c['label']} : appelez maintenant.")}
"""
    write(path, page(path, c["title"], c["desc"], body, ld=[business_ld(), breadcrumb_ld(bc)]))


def build_contact():
    path = "/contact/"
    bc = [("Accueil", "/"), ("Contact", path)]
    body = f"""
<section class="phero"><div class="wrap">{crumbs(bc)}
<h1>Contact – Serrurier Genève {J7}</h1>
<p class="lead">Le plus rapide, c'est le téléphone : un serrurier décroche, comprend votre situation et vous donne un devis gratuit avant d'intervenir.</p>
<div class="ctas">{tel_link("btn b-yel")}<a class="btn b-ghost" href="sms:{PHONE_TEL}">Envoyer un SMS</a></div>
</div></section>
<section class="sec"><div class="wrap cols"><div class="prose">
<div class="info">
<div><strong>Téléphone</strong><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
<div><strong>Horaires</strong>{DISPO_LONG[0].upper() + DISPO_LONG[1:]}</div>
<div><strong>Langues</strong>{LANGS}</div>
<div><strong>Adresse</strong>{e(ADDRESS)}</div>
</div>
<h2>Avant d'appeler</h2>
<p>Pour qu'on puisse vous donner un devis précis par téléphone, préparez si possible :</p>
<ul><li>l'adresse exacte, l'étage et le code d'accès de l'immeuble ;</li><li>le type de problème : porte claquée, fermée à clé, clé cassée, serrure forcée… ;</li><li>le type de porte : appartement, maison, commerce, porte blindée.</li></ul>
<p>Après une ouverture de porte, nous vous demanderons un justificatif de domicile (pièce d'identité avec adresse, bail ou courrier à votre nom).</p>
<div class="alert"><p style="margin:0"><strong>Urgence vitale ?</strong> Personne en danger, enfant seul enfermé, plaque de cuisson allumée : appelez d'abord le <strong>118</strong> (pompiers) ou le <strong>144</strong> (urgences sanitaires). Cambriolage en cours : <strong>117</strong> (police).</p></div>
<h2>Zones d'intervention</h2>
<div class="zg"><div><h3>Canton de Genève</h3>{chips(GE)}</div><div><h3>Canton de Vaud – La Côte</h3>{chips(VD)}</div></div>
</div>{aside()}</div></section>
"""
    write(path, page(path, f"Contact – Serrurier Genève {J7} | Clé en Main Genève",
                     f"Contactez Clé en Main Genève, serrurier ({DISPO}) au +41 79 942 95 44. Devis gratuit par téléphone avant intervention. On répond en FR, EN, ES.",
                     body, ld=[business_ld(), breadcrumb_ld(bc)]))


def build_legal():
    path = "/mentions-legales/"
    bc = [("Accueil", "/"), ("Mentions légales", path)]
    body = f"""
<section class="phero"><div class="wrap">{crumbs(bc)}
<h1>Mentions légales – Clé en Main Genève, serrurier Genève</h1></div></section>
<section class="sec"><div class="wrap"><div class="prose">
<h2>Éditeur du site</h2>
<p><strong>{NAME}</strong><br>Entreprise individuelle – titulaire : {e(OWNER_NAME)}<br>Adresse : {e(ADDRESS)}<br>{"Numéro IDE : " + e(IDE) + "<br>" if IDE else ""}Téléphone : <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
<h2>Hébergement</h2>
<p>{e(HOSTING)}</p>
<h2>Tarifs et devis</h2>
<p>Aucun prix n'est publié sur ce site. Chaque intervention fait l'objet d'un devis gratuit communiqué par téléphone avant intervention. Aucune prestation n'est réalisée sans l'accord du client.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes, illustrations, logo et éléments graphiques de ce site sont la propriété de {e(OWNER_NAME)}, exploitant {NAME}. Toute reproduction sans autorisation écrite est interdite.</p>
<h2>Protection des données</h2>
<p>Ce site est une vitrine : il ne comporte ni formulaire, ni compte client, ni outil de mesure d'audience, ni cookie publicitaire. Aucune donnée personnelle n'est collectée par le site lui-même.</p>
<p>Lorsque vous nous appelez ou nous envoyez un SMS, nous traitons votre numéro, votre adresse et les informations nécessaires à l'intervention, uniquement pour réaliser la prestation et établir la facture, conformément à la loi fédérale sur la protection des données (LPD). Vous pouvez demander l'accès à vos données ou leur suppression, sous réserve des obligations légales de conservation, en nous contactant au {PHONE_DISPLAY}.</p>
<p>Les polices de caractères sont chargées depuis Google Fonts (Google LLC). Lors de ce chargement, votre adresse IP est transmise à Google. L'hébergeur du site peut également enregistrer des journaux techniques (adresse IP, date, page demandée) à des fins de sécurité.</p>
<h2>Responsabilité</h2>
<p>Les informations de ce site sont fournies à titre indicatif et peuvent être modifiées sans préavis. Les conseils donnés ne remplacent pas un diagnostic sur place. {NAME} ne peut être tenu responsable des contenus des sites vers lesquels pointent d'éventuels liens externes.</p>
<h2>Droit applicable</h2>
<p>Le présent site est soumis au droit suisse. For : Genève.</p>
</div></div></section>
"""
    write(path, page(path, "Mentions légales – Serrurier Genève | Clé en Main Genève",
                     "Mentions légales et protection des données de Clé en Main Genève, serrurier à Genève : éditeur, hébergement, données personnelles.",
                     body, ld=[business_ld(), breadcrumb_ld(bc)]))


def build_404():
    body = f"""
<section class="phero"><div class="wrap"><h1>Page introuvable – serrurier Genève</h1>
<p class="lead">Cette page n'existe pas ou a été déplacée. Si vous êtes bloqué devant votre porte, n'attendez pas : appelez-nous.</p>
<div class="ctas">{tel_link("btn b-yel")}<a class="btn b-ghost" href="/">Retour à l'accueil</a></div></div></section>
"""
    html_ = page("/404.html", "Page introuvable | Clé en Main Genève", "Page introuvable.", body, robots="noindex,follow")
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(html_)


def build_meta_files():
    paths = ["/"] + [f'/{s["slug"]}/' for s in SERVICES] + [f'/{c["slug"]}/' for c in COMMUNES] + ["/contact/", "/mentions-legales/"]
    rows = "\n".join(
        f"  <url><loc>{url(p)}</loc><lastmod>{LASTMOD}</lastmod></url>" for p in paths)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {url('/sitemap.xml')}\n")
    with open(os.path.join(ROOT, "site.webmanifest"), "w", encoding="utf-8") as f:
        json.dump({"name": NAME, "short_name": "Clé en Main", "start_url": "/", "display": "browser",
                   "background_color": "#FBF8F1", "theme_color": "#1F1A17",
                   "icons": [{"src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                             {"src": "/img/logo-512.png", "sizes": "512x512", "type": "image/png"}]},
                  f, ensure_ascii=False)
    return paths


def build_google_business():
    """Génère GOOGLE-BUSINESS.md (horaires et adresse issus de la configuration)."""
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base, "google-business.template.md"), encoding="utf-8") as f:
        t = resolve(f.read())
    if HOURS_24_7:
        hours = ("**Ouvert 24 heures sur 24**, du lundi au dimanche.\n"
                 "(Pour chaque jour : cocher « Ouvert », puis choisir « 24 heures sur 24 ».)")
    else:
        rows = "\n".join(f"| {d.capitalize()} | " + (f"{HOURS[d][0]} – {HOURS[d][1]}" if HOURS.get(d) else "Fermé") + " |" for d in DAYS)
        hours = ("| Jour | Horaires |\n|---|---|\n" + rows +
                 "\n\nN'indiquez pas « 24 heures sur 24 » : la fiche doit correspondre aux horaires réels et à ceux du site.")
    t = t.replace("{HOURS_GBP}", hours).replace("{ADDRESS}", ADDRESS)
    desc = t.split("## 4. Description")[1].split("```")[1].strip()
    t = t.replace("{DESC_LEN}", str(len(desc)))
    assert len(desc) <= 750, f"Description Google trop longue : {len(desc)} caractères"
    with open(os.path.join(base, "..", "GOOGLE-BUSINESS.md"), "w", encoding="utf-8") as f:
        f.write(t)


def main():
    os.makedirs(ROOT, exist_ok=True)
    build_home()
    for s in SERVICES:
        build_service(s)
    for c in COMMUNES:
        build_commune(c)
    build_contact()
    build_legal()
    build_404()
    paths = build_meta_files()
    build_google_business()
    print(f"{len(paths)} pages générées dans {os.path.abspath(ROOT)} (SITE_URL={SITE_URL})")


if __name__ == "__main__":
    main()
