# TripLab Europe Pro

Kompletní statická aplikace pro GitHub Pages. Obsahuje 100 destinací, lokální obrazové zálohy, offline datový fallback, dynamický scoring, rozpočet, počasí, filtry, mapu, detail a porovnání.

## Spuštění
- Dvojklikem na `index.html`: katalog funguje přes `destinations-data.js`; mapa a externí zdroje vyžadují internet.
- Lokální server: `python3 -m http.server 8080`

## GitHub Pages
1. Nahrajte obsah této složky do kořene repozitáře.
2. Settings → Pages.
3. Deploy from a branch → `main` → `/ (root)`.

## Editace dat
- Upravte `destinations.json`.
- Pro offline režim je nutné stejná data promítnout i do `destinations-data.js`.
- Pole `contentStatus` odlišuje redakčně ověřené a orientační profily.
- Ceny, lety a klimatické profily jsou orientační.

## Scoring
Preference 30 %, počasí 15 %, cena 15 %, dostupnost 10 %, aktivity 15 %, autenticita 10 %, turismus 5 %.
