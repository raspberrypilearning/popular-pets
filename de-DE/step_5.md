## Aufgabe: Erstelle ein neues Diagramm aus einer Datei

Es ist nützlich, Daten in einer Datei speichern zu können, anstatt sie in den Code aufnehmen zu müssen.

+ Fügen Sie Ihrem Projekt eine neue Datei hinzu und nennen Sie sie `pets.txt`:
    
    ![Screenshot](images/pets-file.png)

+ Fügen Sie nun der Datei Daten hinzu. Sie können die von Ihnen gesammelten Lieblingshaustierdaten oder die Beispieldaten verwenden.
    
    ![screenshot](images/pets-data.png)

+ Wechseln Sie zurück zu `main.py` und kommentieren Sie die Linien aus, die Diagramme und Grafiken rendern (anzeigen) (damit sie nicht angezeigt werden):
    
    ![Screenshot](images/pets-comment.png)

+ Lesen wir nun die Daten aus der Datei.
    
    ![screenshot](images/pets-read.png)
    
    Die `für` Schleife durchläuft die Zeilen in der Datei. `splitlines ()` entfernt das Zeilenumbruchzeichen vom Zeilenende, da Sie das nicht wollen.

+ Jede Zeile muss in eine Bezeichnung und einen Wert getrennt werden:
    
    ![screenshot](images/pets-split.png)
    
    Dadurch wird die Linie an den Leerzeichen geteilt. Fügen Sie also keine Leerzeichen in die Beschriftungen ein. (Sie können später die Unterstützung für Leerzeichen in Beschriftungen hinzufügen.)

+ Möglicherweise erhalten Sie folgende Fehlermeldung:
    
    ![Screenshot](images/pets-error.png)
    
    Dies passiert, wenn Sie am Ende Ihrer Datei eine leere Zeile haben.
    
    Sie können den Fehler beheben, indem Sie nur die Bezeichnung und den Wert abrufen, wenn die Zeile nicht leer ist.
    
    Um dies zu tun, rücken Sie den Code in Ihre `für` Schleife ein und fügen Sie den Code `wenn Zeile:` darüber:
    
    ![Screenshot](images/pets-fix.png)

+ Sie können die Zeile `print (label, value)` entfernen, jetzt funktioniert alles.

+ Fügen wir nun die Bezeichnung und den Wert zu einem neuen Kreisdiagramm hinzu und rendern Sie es:
    
    ![Screenshot](images/pets-pie2.png)
    
    Beachten Sie, dass `add` ausgeht, dass der Wert eine Zahl ist. `int (value)` wandelt den Wert einer Zeichenfolge in eine Ganzzahl um.
    
    Wenn Sie Dezimalzahlen wie 3,5 (Gleitkommazahlen) verwenden möchten, können Sie stattdessen `float (Wert)` verwenden.