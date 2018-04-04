## Gegevens uit een bestand lezen

Het is handig om gegevens in een bestand op te slaan in plaats van het in uw code te moeten opnemen.

+ Voeg een nieuw bestand toe aan uw project en noem het `pets.txt`:
    
    ![screenshot](images/pets-file.png)

+ Voeg nu gegevens toe aan het bestand. U kunt de favoriete huisdiergegevens gebruiken die u hebt verzameld of de voorbeeldgegevens.
    
    ![screenshot](images/pets-data.png)

+ Schakel terug naar `main.py` en geef commentaar op de lijnen die diagrammen en grafieken weergeven (weergeven) (zodat ze niet worden weergegeven):
    
    ![screenshot](images/pets-comment.png)

+ Laten we nu de gegevens uit het bestand lezen.
    
    ![screenshot](images/pets-read.png)
    
    De lus `voor` loopt over de regels in het bestand. `splitlines ()` verwijdert het nieuwelijnteken vanaf het einde van de regel, omdat u dat niet wilt.

+ Elke regel moet worden gescheiden in een label en een waarde:
    
    ![screenshot](images/pets-split.png)
    
    Hiermee wordt de lijn op de spaties gesplitst, dus geen spaties in de labels. (Later kunt u ondersteuning voor spaties in labels toevoegen.)

+ U krijgt mogelijk de volgende foutmelding:
    
    ![screenshot](images/pets-error.png)
    
    Dit gebeurt als u een lege regel aan het einde van uw bestand hebt.
    
    U kunt de fout oplossen door alleen het label en de waarde te krijgen als de regel niet leeg is.
    
    Hiertoe typt u de code in uw `voor` lus en voegt u de code `toe als regel:` erboven:
    
    ![screenshot](images/pets-fix.png)

+ U kunt de `print (label, waarde)` regel verwijderen nu alles werkt.

+ Laten we nu het label en de waarde toevoegen aan een nieuw cirkeldiagram en het renderen:
    
    ![screenshot](images/pets-pie2.png)
    
    Merk op dat `toevoegen` verwacht dat de waarde een getal is, `int (waarde)` verandert de waarde van een string in een geheel getal.
    
    Als u decimalen zoals 3,5 (drijvende-kommagetallen) wilt gebruiken, kunt u `float (waarde)` gebruiken.