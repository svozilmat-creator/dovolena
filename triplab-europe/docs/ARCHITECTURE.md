# Architektura

- **index.html**: sémantická kostra, formulář, výsledky, mapa, modaly.
- **styles.css**: responzivní editorial design, mobilní filtry a přístupnost.
- **app.js**: načtení JSON, stav, kalkulátor, scoring, filtry, porovnání, detail a mapa.
- **destinations.json**: jediný editovatelný zdroj dat.
- **assets/images/**: lokální obrázky bez závislosti na externím hostingu.

Aplikace nemá build krok ani backend. Stav formuláře se drží v paměti a oblíbené položky v localStorage. Leaflet je progresivní doplněk: když CDN není dostupná, aplikace dál funguje bez mapy.
