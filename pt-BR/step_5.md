## Ler dados de um arquivo

É útil poder armazenar dados em um arquivo em vez de incluí-lo em seu código.

+ Adicione um novo arquivo ao seu projeto e chame-o de `pets.txt`:
    
    ![captura de tela](images/pets-file.png)

+ Agora adicione dados ao arquivo. Você pode usar os dados favoritos de animais de estimação coletados ou os dados de exemplo.
    
    ![captura de tela](images/pets-data.png)

+ Volte para `main.py` e comente as linhas que renderizam (exibem) gráficos e gráficos (para que não sejam exibidos):
    
    ![captura de tela](images/pets-comment.png)

+ Agora vamos ler os dados do arquivo.
    
    ![captura de tela](images/pets-read.png)
    
    O loop `para` fará um loop pelas linhas no arquivo. `splitlines ()` remove o caractere de nova linha do final da linha, pois você não quer isso.

+ Cada linha precisa ser separada em um rótulo e um valor:
    
    ![captura de tela](images/pets-split.png)
    
    Isso dividirá a linha nos espaços, portanto, não inclua espaços nos rótulos. (Você pode adicionar suporte para espaços em rótulos posteriormente.)

+ Você pode receber um erro como este:
    
    ![captura de tela](images/pets-error.png)
    
    Isso acontece se você tiver uma linha vazia no final do seu arquivo.
    
    Você pode corrigir o erro obtendo apenas o rótulo e o valor se a linha não estiver vazia.
    
    Para fazer isso, indente o código dentro do seu loop `para` e adicione o código `se a linha:` acima:
    
    ![captura de tela](images/pets-fix.png)

+ Você pode remover a `linha de impressão (rótulo, valor)` agora está tudo funcionando.

+ Agora vamos adicionar o rótulo e o valor a um novo gráfico de pizza e renderizá-lo:
    
    ![captura de tela](images/pets-pie2.png)
    
    Note que `add` espera que o valor seja um número, `int (value)` transforma o valor de uma string em um inteiro.
    
    Se você quisesse usar decimais como 3.5 (números de ponto flutuante) você poderia usar `float (value)`.