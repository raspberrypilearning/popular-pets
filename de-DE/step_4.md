## Daten von einer Datei ablesen

Es ist hilfreich, Daten in einer Datei zu speichern, anstatt sie in deinen Code mit einzubeziehen. 

+ Füge deinem Projekt eine neue Datei hinzu und nenne sie `pets.txt` (Haustiere):

  ![screenshot](images/pets-file.png)

+ Füge dieser Datei jetzt deine Daten hinzu. Du kannst die Daten aus der Umfrage über die Lieblingshaustiere oder die Musterdaten benutzen.

  ![screenshot](images/pets-data.png)
  
+ Geh zurück zu `main.py` und kommentiere die Zeilen weg, die die Kreis- und Balkendiagramme rendern (anzeigen), damit diese nicht mehr angezeigt werden:

  ![screenshot](images/pets-comment.png)

+ Lass uns jetzt die Daten aus der Datei ablesen. 

  ![screenshot](images/pets-read.png)
  
  Die `for` (für)Schleife wird eine Schleife über die Zeilen in der Datei ziehen. Mit `splitlines()` (geteilte Zeilen) wird das „neue Zeile“ Zeichen vom Ende der Zeile entfernt, weil du dies nicht brauchst. 
  
+ Jede Zeile muss in ein Etikett (label) und in einen Wert (value) getrennt werden:
  
  ![screenshot](images/pets-split.png)
  
  Dies teilt die Zeile an den Leerplätzen, du solltest daher kein Leerzeichen in dein Etikett einfügen. (Du kannst später die entprechende Hilfe für die Leerzeichen in den Etiketten einfügen.)
  
+ Du wirst vielleicht eine der folgenden Fehlermeldungen erhalten:

  ![screenshot](images/pets-error.png)
  
  Das passiert, wenn du eine Leerzeile am Ende deiner Datei hast. 
  
  Du kannst den Fehler beheben, indem du nur das Etikett und den Wert holst, wenn die Zeile nicht leer ist.

  Um dies zu tun musst du den Code in deiner `for` (für) Schleife einrücken und den Code `if line:` (wenn Linie) darüber hinzufügen:
  
  ![screenshot](images/pets-fix.png)
  
+ Du kannst jetzt die Zeile `print(label, value)` (Etikett, Wert drucken) entfernen, weil alles funktioniert. 
  
+ Lass uns jetzt das Etikett und den Wert in ein neues Kreisdiagramm hinzufügen und dies dann rendern:

  ![screenshot](images/pets-pie2.png)
  
  Denke daran, dass `add` (hinzufügen/addieren) davon ausgeht, dass der Wert eine Ziffer ist, `int(value)`  (Integer (Wert)) wandelt den Wert von einer Zeichenkette in ein Integer um.
  
  Wenn du Dezimalzahlen, wie z. B. 3.0 benutzen willst, (Gleitkommazahlen), dann kannst du statt dessen einen `float(value)` (Gleitkomma (Wert)) benutzen (Achtung: aber immer einen Punkt und kein Komma setzen!). 
