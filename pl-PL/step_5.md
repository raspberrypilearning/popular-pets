## Wczytaj dane z pliku

Warto przechowywać dane w pliku, zamiast umieszczać je w kodzie.

+ Dodaj nowy plik do projektu i nazwij go `pets.txt`:
    
    ![zrzut ekranu](images/pets-file.png)

+ Teraz dodaj dane do pliku. Możesz użyć zebranych danych ulubionych zwierząt lub danych przykładowych.
    
    ![zrzut ekranu](images/pets-data.png)

+ Przejdź z powrotem na `main.py` i zakomentuj linie renderujące (wyświetlające) wykresy (tak, aby nie były wyświetlane):
    
    ![zrzut ekranu](images/pets-comment.png)

+ Teraz odczytajmy dane z pliku.
    
    ![zrzut ekranu](images/pets-read.png)
    
    Pętla `for` będzie powtarzać linie w pliku. `splitlines()` usuwa znak nowego wiersza z końca wiersza, ponieważ tego nie chcesz.

+ Każda linia musi być podzielona na etykietę(label) i wartość(value):
    
    ![zrzut ekranu](images/pets-split.png)
    
    Spowoduje to podzielenie linii spacjami, więc nie umieszczaj spacji na etykietach. (Możesz później dodać obsługę spacji w etykietach.)

+ Może pojawić się błąd podobny do tego:
    
    ![zrzut ekranu](images/pets-error.png)
    
    Dzieje się tak, jeśli masz pusty wiersz na końcu pliku.
    
    Możesz naprawić błąd, pobierając etykietę i wartość tylko wtedy, gdy linia nie jest pusta.
    
    Aby to zrobić, wprowadź wcięcie kodu wewnątrz pętli `for` i dodaj kod, `if line:` powyżej niego:
    
    ![zrzut ekranu](images/pets-fix.png)

+ Możesz usunąć linię `print(label, value)`, teraz wszystko działa.

+ Teraz dodajmy etykietę i wartość do nowego wykresu kołowego i wyrenderujmy go:
    
    ![zrzut ekranu](images/pets-pie2.png)
    
    Zauważ, że `add` oczekuje, że wartość będzie liczbą, `int (wartość)` zamienia wartość z ciągu znaków na liczbę całkowitą- integer.
    
    Jeśli chciałbyś używać liczb dziesiętnych, takich jak 3.5 (liczba zmiennoprzecinkowa), możesz zamiast tego użyć `float (wartość)`.