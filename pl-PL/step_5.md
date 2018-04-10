## Czytaj dane z pliku

Warto przechowywać dane w pliku, zamiast umieszczać je w kodzie.

+ Dodaj nowy plik do swojego projektu i zadzwoń do niego `pets.txt`:
    
    ![zrzut ekranu](images/pets-file.png)

+ Teraz dodaj dane do pliku. Możesz użyć zebranych danych ulubionych zwierząt lub danych przykładowych.
    
    ![zrzut ekranu](images/pets-data.png)

+ Przejdź z powrotem na `main.py` i skomentuj linie renderujące (wyświetlaj) wykresy (tak, aby nie były wyświetlane):
    
    ![zrzut ekranu](images/pets-comment.png)

+ Teraz odczytajmy dane z pliku.
    
    ![zrzut ekranu](images/pets-read.png)
    
    Cyfra `dla` będzie pętla nad wierszami w pliku. `splitlines ()` usuwa znak nowego wiersza od końca wiersza, ponieważ tego nie chcesz.

+ Każda linia musi być podzielona na etykietę i wartość:
    
    ![zrzut ekranu](images/pets-split.png)
    
    Spowoduje to podzielenie linii na spacje, więc nie umieszczaj spacji na etykietach. (Możesz później dodać obsługę spacji w etykietach.)

+ Może pojawić się błąd podobny do tego:
    
    ![zrzut ekranu](images/pets-error.png)
    
    Dzieje się tak, jeśli masz pusty wiersz na końcu pliku.
    
    Możesz naprawić błąd, pobierając etykietę i wartość tylko wtedy, gdy linia nie jest pusta.
    
    Aby to zrobić, wprowadź wcięcie kodu wewnątrz `dla ciągu` i dodaj kod `, jeśli linia:` znajduje się powyżej:
    
    ![zrzut ekranu](images/pets-fix.png)

+ You can remove the `print(label, value)` line now everything is working.

+ Teraz dodajmy etykietę i wartość do nowego wykresu kołowego i wyrenderujmy go:
    
    ![zrzut ekranu](images/pets-pie2.png)
    
    Zauważ, że `dodaje` oczekuje, że wartość będzie liczbą, `int (wartość)` zamienia wartość z ciągu na liczbę całkowitą.
    
    Jeśli chciałbyś używać liczb dziesiętnych, takich jak 3,5 (liczba zmiennoprzecinkowa), możesz zamiast tego użyć `float (wartość)`.