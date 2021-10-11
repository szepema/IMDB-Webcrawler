1. Jelenlegi helyzet

A IMDB_Webcrawler alkalmazásunkkal kapcsolatos feladatokat felosztottuk a csapat tagjai között: a GUI létrehozása, a sorozatrészek értékeléseinek lekérdezése és az értékelések vizualizálása

2. Kész program

A program kérjen be egy user inputot, aminek megkeresi az IMDB oldalát egy Google keresés segítségével, majd a sorozat részeihez hozzátartozó IMDB étékeléseket jelenítse meg egy oszlopdiagrammon.

3. Üzleti folyamatok modellje
	
	Az interneten manapság népszerűek az adatvizualizációs grafikonok, azonban a sorozatok értékeléseinek vizualizálására még nincs eszköz. Célunk ennek az űrnek a betöltése ezzel az egyszerű programmal.

4. Követelménylista 

	* A diagramnak egy oszlopdiagramként kell megjelennie.

	* A diagram oszlopai különböző színűek a sorozat évadai szerint. 

	* A diagram függőleges ágán az értékelések egy 1-10ig terjedő skálán jelenjenek meg. 

	* A diagram vízszintes oldalán a számok az adott évadonként jelenjenek meg.

	* A programnak meg kell jeleníteni egy felhasználói felületet amin meg kell jelennie egy szövegdoboznak és egy gombnak.

	* A gombnak el kell indítania egy webes lekérdezést a szövegdobozban feltüntetett szövegre.
	
	* A szövegdoboz lesz a program bemenete amire a keresés fog elindulni a gomb megnyomása esetén.

5. Használati esetek

	A felhasználó az alábbi tevékenységeket végezheti: 
	
	- Gépelhet a kereső szövegdobozába.
	- Elindíthatja a keresést.
	- Bezárhatja bármelyik ablakot az X gombbal.

6. Képernyő tervek
	
	A program egy asztali alkalmazás, aminek felhasználói felülete egy ablakból álljon, amiben egy szövegdoboz és egy keresőgomb található. A lekérdezés után jelenjen meg a grafikon.

7. Funkció

	A program egy sorozat részeinek IMDB értékeléseit jeleníti meg grafikusan, annak címe alapján. A programot Python 3.9.7-ben valósítjuk meg.
A programot három modulra szedjük szét: felhasználói felület, értékelések lekérdezése, ábrázolás.

Felhasználói felület:
- a Tkinter csomag segítségével egy szövegdobozt és egy gombot tartalmazó felhasználói felületet hozunk létre
- a szövegdobozba írt sorozatcímet eltároljuk

Értékelések lekérdezése:
- az eltárolt címre a googlesearch és requests csomagok segítségével rákeresünk, eltároljuk az első linket amit visszaad
- a bs4 könyvtárból importált BeautifulSoup csomag segítségével a linken keresztül megkeressük és eltároljuk az évadok számát
- az évadok száma segítéségével legeneráljuk az egyes évadok IMDB oldalának URL-jét
- a requests és a BeautifulSoup csomagok segítésével az évadokon belül az egyes részek értékeléseit is eltároljuk

Ábrázolás:
- matplotlib csomag segítéségével az összes értékelést ábrázoljuk
- a random modul segítségével az egyes részek értékeléseinek eltérő színezést adunk, hogy elkülönüljenek

8. Fogalomszótár
	
	- GUI: Graphical User Interface, grafikus felhasználói felület, hely ahol a felhasználó interakcióba léphet a programmal.
	- User input: a felhasználó által megadott adat.
	- IMDB: egy népszerű online filmes és sorozatos adatbázis.
	- googlesearch, bs4, tkinter, matplotlib: Python3 könyvtárak.
