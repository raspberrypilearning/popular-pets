## Ler dados de um arquivo

É útil poder armazenar dados em um arquivo em vez de ter que incluí-los em seu código.

+ Adicione um novo arquivo ao seu projeto e chame-o de `pets.txt`:
    
    ![captura de tela](images/pets-file.png)

+ Agora adicione dados ao arquivo. You can use the favourite pets data that you collected or the example data.
    
    ![captura de tela](images/pets-data.png)

+ Volte para `main.py` e comente as linhas que renderizam (exibem) tabelas e gráficos (para que não sejam exibidos):
    
    ![captura de tela](images/pets-comment.png)

+ Agora vamos ler os dados do arquivo.
    
    ![captura de tela](images/pets-read.png)
    
    The `for` loop will loop over the lines in the file. `splitlines ()` remove o caractere de nova linha do final da linha, já que você não quer isso.

+ Cada linha precisa ser separada em um rótulo e um valor:
    
    ![captura de tela](images/pets-split.png)
    
    Isso dividirá a linha nos espaços, portanto, não inclua espaços nos rótulos. (Você pode adicionar suporte para espaços em rótulos depois.)

+ Você pode receber um erro como este:
    
    ![captura de tela](images/pets-error.png)
    
    Isso acontece se você tiver uma linha vazia no final do seu arquivo.
    
    Você pode corrigir o erro obtendo o rótulo e o valor apenas se a linha não estiver vazia.
    
    To do this, indent the code inside your `for` loop and add the code `if line:` above it:
    
    ![captura de tela](images/pets-fix.png)

+ Você pode remover a linha `print(rotulo, valor)` agora que está tudo funcionando.

+ Agora vamos adicionar o rótulo e o valor a um novo gráfico de pizza e renderizá-lo:
    
    ![screenshot](images/pets-pie2.png)
    
    Note that `add` expects the value to be a number, `int(value)` turns the value from a string into an integer.
    
    If you wanted to use decimals such as 3.5 (floating point numbers) you could use `float(value)` instead.