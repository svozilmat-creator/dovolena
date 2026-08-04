# TripLab Europe

Statický prototyp inteligentního katalogu 100 evropských destinací. Aplikace kombinuje termín, délku pobytu, rozpočet, počet cestujících, dopravu, zájmy, počasí, turistickou zátěž a autenticitu. Nevyžaduje backend ani placené API.

> **Datové omezení:** ceny, dostupnost letů, doby jízdy a klimatické profily jsou orientační modelová data. Nejde o jízdní řád, nabídku zájezdu ani cenovou nabídku.

## Architektura a datový model

- [Architektura](docs/ARCHITECTURE.md)
- [Datový model](docs/DATA_MODEL.md)
- [Scoring](docs/SCORING.md)
- Komentovaný příklad: `destination.schema.example.jsonc`

## Struktura

```text
/
├── index.html
├── styles.css
├── app.js
├── destinations.json
├── destination.schema.example.jsonc
├── README.md
├── .nojekyll
├── assets/images/
└── docs/
```

## Lokální spuštění

Kvůli načítání `destinations.json` nestačí otevřít `index.html` dvojklikem. V kořeni projektu spusťte:

```bash
python3 -m http.server 8080
```

Poté otevřete `http://localhost:8080`.

## Nahrání na GitHub

```bash
git init
git add .
git commit -m "Initial TripLab prototype"
git branch -M main
git remote add origin https://github.com/UZIVATEL/REPOZITAR.git
git push -u origin main
```

## GitHub Pages

1. Otevřete repozitář na GitHubu.
2. `Settings` → `Pages`.
3. U `Source` zvolte `Deploy from a branch`.
4. Vyberte `main` a složku `/ (root)`.
5. Uložte.

GitHub Pages podporuje publikování ze zvolené větve a z kořene nebo složky `/docs`. Tento projekt je připraven pro kořen repozitáře. Soubor `.nojekyll` vypíná zbytečné Jekyll zpracování.

## Přidání destinace

1. Zkopírujte objekt v `destination.schema.example.jsonc`.
2. Odstraňte komentáře, doplňte všechna pole a vložte objekt do pole v `destinations.json`.
3. Použijte jedinečné `id`.
4. Hodnocení držte na stupnici 0–10.
5. U `tourism` znamená vyšší hodnota více turistů.
6. Doplňte všech 12 měsíců v `seasonality`.
7. Ceny zadávejte jako intervaly.
8. Letecké spojení popisujte kategorií, ne neověřeným letovým řádem.

## Změna scoringu

V `app.js` upravte `scoreDestination()`. Výchozí váhy:

```text
Preference 30 %
Počasí 15 %
Cena 15 %
Dostupnost 10 %
Aktivity 15 %
Autenticita 10 %
Turistická zátěž 5 %
```

Jednotlivé dílčí funkce (`preferenceScore`, `weatherScore`, `priceScore`, `accessScore`, `tourismScore`) vracejí 0–100.

## Změna vzhledu

Barevné tokeny jsou na začátku `styles.css` v `:root`. Obrázky jsou v `assets/images/`. Cesta k obrázku se nastavuje v poli `image` destinace.

## Aktualizace databáze

Frontend není nutné měnit. Stačí aktualizovat `destinations.json`, zachovat názvy polí a validní JSON. Doporučená kontrola:

```bash
python3 -m json.tool destinations.json > /dev/null
```

## Budoucí API

Datový model je připraven pro nahrazení statických částí adaptéry:

- Open-Meteo: počasí podle `coordinates` a termínu;
- OSM/Google Maps: trasy a doby jízdy;
- letenky: aktualizace `transport.flight`;
- ubytování: aktualizace `costs.accommodationPerNight`.

Doporučený postup: vytvořit samostatnou vrstvu `services/`, která vrátí stejný tvar dat jako JSON. Scoring pak není nutné přepisovat.

## Mapa

Mapa je přes Leaflet CDN a OpenStreetMap. Při nedostupném CDN zůstává plánovač, scoring, porovnání a detail funkční; pouze se nezobrazí interaktivní mapa.

## Licence a obrázky

V prototypu jsou lokální generované editorial vizuály. Pokud je nahradíte veřejnými fotografiemi, ověřte licenci a doplňte autora, zdroj a licenci podle podmínek konkrétního souboru.
