## Čitaj podatke iz datoteke

Umjesto da upisuješ podatke u svoj kôd, korisnije je da ih smjestiš u datoteku.

+ Dodaj novu datoteku u svoj projekat i nazovi je `ljubimci.txt`:
    
    ![screenshot](images/pets-file.png)

+ Sada upiši podatke u datoteku. Možeš da koristiš podatke o omiljenim ljubimcima koje si prikupio/prikupila ili podatke iz primjera.
    
    ![screenshot](images/pets-data.png)

+ Pređi na `main.py` i komentariši redove koji vizuelizuju (prikazuju) grafikone (tako da ne budu prikazani):
    
    ![screenshot](images/pets-comment.png)

+ Sada učitajmo podatke iz datoteke.
    
    ![screenshot](images/pets-read.png)
    
    Petlja `for` će prolaziti kroz sve redove u datoteci. Funkcija `splitlines()` uklanja znak za novi red sa kraja reda, pošto to ne želimo.

+ Svaki red mora biti podijeljen na naziv i vrijednost:
    
    ![screenshot](images/pets-split.png)
    
    Ovo će podijeliti red tamo gdje su razmaci, pa nemoj unositi razmake u nazive. (Kasnije možeš da dodaš opciju za razmake u nazivima.)

+ Možda ćeš dobiti poruku o grešci kao što je ova:
    
    ![screenshot](images/pets-error.png)
    
    To se dešava ako na kraju svoje datoteke imaš prazan red.
    
    Grešku možeš ispraviti tako da se naziv i vrijednost ispisuju samo ako red nije prazan.
    
    Da to napraviš, uvuci kôd unutar svoje `for` petlje i dodaj kôd `if red:` iznad njega:
    
    ![screenshot](images/pets-fix.png)

+ Sada kada sve funkcioniše, možeš da ukloniš red `print(naziv, vrijednost)`.

+ Sada dodajmo naziv i vrijednost novom stubičastom grafikonu i prikažimo ga:
    
    ![screenshot](images/pets-pie2.png)
    
    Imaj u vidu da `add` očekuje da vrijednost bude broj, a `int(vrijednost)` pretvara vrijednost iz znakovnog niza u integer.
    
    Ako želiš da koristiš decimalne brojeve kao što je 3.5 (broj sa pokretnom tačkom), možeš da koristiš `float(vrijednost)`.