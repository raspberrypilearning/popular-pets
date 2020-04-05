---
title: Beliebte Haustiere
description: Erstelle Kreis- und Balkendiagramme von den Daten, die du gesammelt hast.
notes: "Beliebte Haustiere - notes.md"
layout: project
new: true
---

# Einleitung {.intro}

In diesem Projekt wirst du Tortendiagramme und Balkendiagramme aus Daten erstellen, welche du von Mitgliedern deines Code Clubs gesammelt hast.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/70d24d92b8?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/pets-finished.png">
</div>

# Schritt 1: Erstelle ein Kreisdiagramm {.activity}

Kreisdiagramme sind eine nützliche Methode zum Anzeigen von Daten. Lass uns eine Umfrage über die Lieblingstiere in deinem Code Club durchführen und die Daten als Tortendiagramm darstellen.

## Aufgaben-Checkliste {.check}

+ Bitte einen Freiwilligen, eine Umfrage zu organisieren. Du kannst die Ergebnisse auf einem Computer aufzeichnen, der an einen Projektor oder ein Whiteboard angeschlossen ist und von jedem gesehen werden kann.
    
    Schreibe eine Liste mit Haustieren und vergewissern dich, dass jeder Liebling dabei ist.
    
    Bringe dann alle dazu, für ihren Favoriten zu stimmen, indem du die Hand nach dem Aufruf heben. Nur jeweils eine Stimme!
    
    Zum Beispiel:
    
    ![screenshot](images/pets-favourite.png)

+ Öffne das leere Python-Vorlage-Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Lass uns ein Kreisdiagramm erstellen, um die Ergebnisse deiner Umfrage anzuzeigen. Du wirst die PyGal-Bibliothek verwenden, um einen Teil der harten Arbeit zu erledigen.
    
    Importiere zuerst die Pygal-Bibliothek:
    
    ![screenshot](images/pets-pygal.png)

+ Jetzt erstellen wir ein Kreisdiagramm und rendern es (zeigen es an):
    
    ![screenshot](images/pets-pie.png)
    
    Keine Sorge, es wird interessanter, wenn du Daten hinzufügst!

+ Lass uns die Daten für eines der Haustiere hinzufügen. Verwende die von Dir gesammelten Daten.
    
    ![screenshot](images/pets-add.png)
    
    Es gibt nur ein Datenelement, sodass es das gesamte Kreisdiagramm einnimmt.

+ Füge nun den Rest der Daten auf die gleiche Weise hinzu.
    
    Zum Beispiel:
    
    ![screenshot](images/pets-add-all.png)

+ Und um dein Diagramm zu vervollständigen, füge einen Titel hinzu:
    
    ![screenshot](images/pets-title.png)

## Speichere dein Projekt {.save}

## Daten von einer Datei ablesen {.challenge}

Du kannst Balkendiagramme auf ähnliche Weise erstellen. Verwende einfach `barchart = pygal.Bar ()`, um ein neues Balkendiagramm zu erstellen, füge Daten hinzu und rendern es wie für ein Kreisdiagramm.

Sammle Daten von deinen Code Club-Mitgliedern, um dein eigenes Balkendiagramm zu erstellen.

Stelle sicher, dass du ein Thema auswählst, über das jeder Bescheid weiß!

Hier sind ein paar Vorschläge:

+ Was ist dein Lieblingssport?

+ Was ist dein Lieblingseisgeschmack?

+ Wie kommst du zur Schule?

+ In welchem Monat hast du Geburtstag?

+ Spielst du Minecraft? (ja Nein)

Stelle keine Fragen, die personenbezogene Daten enthalten, z. B. wo Menschen leben. Frage deinen Clubleiter, wenn du dir nicht sicher bist.

Beispiele:

![screenshot](images/pets-bar-examples.png)

## Speichere dein Projekt {.save}

# Schritt 2: Daten aus einer Datei lesen {.activity}

Es ist nützlich, Daten in einer Datei speichern zu können, anstatt sie in den Code aufnehmen zu müssen.

## Aktivitäts-Checkliste {.check}

+ Füge zu deinem Projekt eine neue Datei hinzu und nenne sie `pets.txt`:
    
    ![screenshot](images/pets-file.png)

+ Füge nun der Datei Daten hinzu. Du kannst die von dir gesammelten Lieblingshaustierdaten oder die Beispieldaten verwenden.
    
    ![screenshot](images/pets-data.png)

+ Switch back to `main.py` and comment out the lines that render (display) charts and graphs (so that they aren't displayed):
    
    ![screenshot](images/pets-comment.png)

+ Now let's read the data from the file.
    
    ![screenshot](images/pets-read.png)
    
    The `for` loop will loop over the lines in the file. `splitlines()` removes the newline character from the end of the line as you don't want that.

+ Each line needs to be separated into a label and a value:
    
    ![screenshot](images/pets-split.png)
    
    This will split the line at the spaces so don't include spaces in the labels. (You can add support for spaces in labels later.)

+ You might get an error like this:
    
    ![screenshot](images/pets-error.png)
    
    This happens if you have an empty line at the end of your file.
    
    You can fix the error by only getting the label and value if the line isn't empty.
    
    To do this, indent the code inside your `for` loop and add the code `if line:` above it:
    
    ![screenshot](images/pets-fix.png)

+ You can remove the `print(label, value)` line now everything is working.

+ Now let's add the label and value to a new Pie Chart and render it:
    
    ![screenshot](images/pets-pie2.png)
    
    Note that `add` expects the value to be a number, `int(value)` turns the value from a string into an integer.
    
    If you wanted to use decimals such as 3.5 (floating point numbers) you could use `float(value)` instead.

## Save Your Project {.save}

## Challenge: Create a new chart from a file {.challenge}

Can you create a new bar graph or pie chart from data in a file? You'll need to create a new .txt file.

Tip: If you want to have spaces in the labels then use `line.split(': ')` and add colons to your data file, e.g. 'Red Admiral: 6'

![screenshot](images/pets-butterflies.png)

## Save Your Project {.save}

## Challenge: More charts and graphs! {.challenge}

Can you create a pie chart and a bar chart from the same file? You can either use the data you collected earlier or collect some new data.

![screenshot](images/pets-pn-bar.png)

![screenshot](images/pets-pn.png)

## Save Your Project {.save}