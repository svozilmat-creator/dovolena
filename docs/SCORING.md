# Scoring 0–100

Výchozí váhy: preference 30 %, počasí 15 %, cena 15 %, dostupnost 10 %, aktivity 15 %, autenticita 10 %, turistická zátěž 5 %.

- Preference = průměr hodnocení zvolených kategorií.
- Počasí = měsíční vhodnost + blízkost preferovanému teplotnímu pásmu.
- Cena = poměr odhadované ceny k rozpočtu; destinace nad limitem zůstává viditelná, ale je penalizována.
- Dostupnost = kompatibilita zvoleného způsobu dopravy a délka cesty.
- Aktivity = aktivní dovolená + rozmanitost zvolených aktivit.
- Autenticita = vlastní skóre autenticity a hidden-gem skóre.
- Turistická zátěž = porovnání měsíční turističnosti s preferencí uživatele.

Každá složka je v `app.js` samostatná a vrací 0–100. Výsledek se skládá ve `scoreDestination()`.
