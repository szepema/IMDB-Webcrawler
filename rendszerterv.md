Rendszerterv
---

1. A rendszer célja

    Az interneten népszerűek az adatvizualizációs grafikonok, aminek a megvalósítására nem nagyon van eszköz. Célunk ennek a hiánynak a pótlása egy egyszerűen használható programmal.

2. Projektterv
  
  - Projektvezető: Szepesi Máté
  
  - Résztvevők: Csóka Péter, Gődény Szabolcs, Szepesi Máté
  
  - Feladatok:

    - Grafikus felhasználói felület létrehozása (Szepesi Máté)

    - Google-s keresés megvalósítása (Csóka Péter)

    - Adatok grafikus megjelenítése (Gődény Szabolcs)
        

  - Mérföldkövek:
    
    1. GUI létrehozása
    2. Kereső program létrehozása
    3. Adatok grafikonon való megjelenítése
  
4. Követelmények

    - Sorozat nevének bekérése a felhasználótól
    - Keresés lefuttatása a bekért névre
    - Adatok vizualizálása egy grafikonon

5. Funkcionális terv

    Az program az alábbi funkciókat tölti be:
        - Megjelenít egy asztali alkalmazást ami bekéri az adatokat a felhasználótól
        - Az input box alatt megjelenít egy Search gombot ami elindítja a program többi részét
        - A gomb megnyomása után lefutattja a keresést
        - A bekért adatokat megjeleníti a matplotlib nevű python könyvtár segítségével
      


6. Fizikai környezet

    - Az IMDB_Webcrawler egy asztali alkalmazásként futtatható program
    - Elkészítésére a következő szoftvereket használtuk
        - Fejlesztői környezetek:
            - Visual Studio Code
            - NotePad++
        - Felhasznált python könyvtárak:
            - tkinter
            - matloptlib
            - bs4
            - google


7. Telepítés

    A program futattásához szükségünk van a tkinter, matplotlib, bs4 és google python könyvtárakra amiket parancsorban linuxos környezetben a -pip3 install [könyvtár neve], windowson pedig a -pip install [könyvtár neve] parancsokkal tudunk telepíteni

