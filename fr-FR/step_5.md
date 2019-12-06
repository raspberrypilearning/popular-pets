## Lire les données d'un fichier

Il est utile de pouvoir stocker des données dans un fichier plutôt que de les inclure dans votre code.

+ Ajoutez un nouveau fichier à votre projet et appelez-le `pets.txt`:
    
    ![capture d'écran](images/pets-file.png)

+ Ajoutez maintenant des données au fichier. Vous pouvez utiliser les données des animaux de compagnie que vous avez collectées ou les exemples de données.
    
    ![captures d'écran](images/pets-data.png)

+ Revenez à `main.py` et commentez les lignes qui affichent les camemberts et les histogrammes (de sorte qu'ils ne sont pas affichés):
    
    ![capture d'écran](images/pets-comment.png)

+ Lisons maintenant les données du fichier.
    
    ![capture d'écran](images/pets-read.png)
    
    La boucle `for` passera en boucle sur toutes les lignes du fichier. `splitlines()` supprime le caractère de retour à la ligne de la fin de la ligne car vous ne souhaitez pas le conserver.

+ Chaque ligne doit être séparée entre un libellé et une valeur:
    
    ![capture d'écran](images/pets-split.png)
    
    Cela divisera la ligne au niveau des espaces, alors n'incluez pas d'espaces dans les libellés. (Vous pourrez ajouter ultérieurement une prise en charge des espaces dans les libellés.)

+ Vous pourriez obtenir une erreur comme ceci:
    
    ![capture d'écran](images/pets-error.png)
    
    Cela se produit si vous avez une ligne vide à la fin de votre fichier.
    
    Vous pouvez corriger l'erreur en récupérant uniquement le libellé et la valeur si la ligne n'est pas vide.
    
    Pour ce faire, indentez le code dans votre boucle `for` et ajoutez le code `if line:` juste avant:
    
    ![capture d'écran](images/pets-fix.png)

+ Vous pouvez supprimer la ligne `print(label, value)` maintenant que tout fonctionne.

+ Ajoutons maintenant le libellé et la valeur à un nouveau camembert et affichons-le:
    
    ![capture d'écran](images/pets-pie2.png)
    
    Notez que `add` suppose que la valeur est un nombre, `int (value)` transforme la valeur d'une chaîne de caractères en un entier.
    
    Si vous souhaitez utiliser des nombres décimaux tels que 3.5 (nombres à virgule flottante), vous pouvez utiliser `float (value)` à la place.