---
title: Animais de estimação populares
description: Crie gráficos de pizza e gráficos de barra dos dados que você coletar.
notes: "Animais de estimação populares - notes.md"
layout: projeto
new: verdadeiro
---
# Introdução {.intro}

Neste projeto, você cria gráficos de pizza e gráficos de barras a partir dos dados coletados dos membros do seu Code Club.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/70d24d92b8?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/pets-finished.png">
</div>

# Passo 1: Criar um gráfico de pizza {.activity}

Gráficos de pizza são uma forma útil de mostrar dados. Vamos fazer uma pesquisa com os animais favoritos no seu Code Club e então apresentar os dados como um gráfico de pizza.

## Lista de atividades {.check}

+ Peça ao seu voluntário para ajudar a organizar uma pesquisa. Você pode gravar os resultados em um computador conectado a um projetor ou quadro branco que todos possam ver.
    
    Escreva uma lista de animais de estimação e certifique-se de que os favoritos de todos estejam incluídos.
    
    Então faça com que todos votem em seu favorito, colocando a mão para cima quando for chamado. Apenas um voto cada!
    
    Por exemplo:
    
    ![screenshot](images/pets-favourite.png)

+ Abra o modelo Trinket em branco do Python: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Vamos criar um gráfico de pizza para mostrar os resultados da sua pesquisa. Você estará usando a biblioteca PyGal para fazer um pouco do trabalho pesado.
    
    Primeiro importe a biblioteca Pygal:
    
    ![screenshot](images/pets-pygal.png)

+ Agora vamos criar um gráfico de pizza e renderizar (exibir):
    
    ![screenshot](images/pets-pie.png)
    
    Não se preocupe, fica mais interessante quando você adiciona dados!

+ Vamos adicionar os dados de um dos animais de estimação. Use os dados que você coletou.
    
    ![screenshot](images/pets-add.png)
    
    Há apenas um dado, então ele ocupa todo o gráfico de pizza.

+ Agora adicione o restante dos dados da mesma maneira.
    
    Por exemplo:
    
    ![screenshot](images/pets-add-all.png)

+ E para finalizar seu gráfico, adicione um título:
    
    ![screenshot](images/pets-title.png)

## Salve seu projeto {.save}

## Desafio: crie seu próprio gráfico de barras {.challenge}

You can create bar charts in a similar way. Just use `barchart = pygal.Bar()` to create a new barchart, and then add data and render in the same way as for a pie chart.

Collect data from your Code Club members to create your own bar graph.

Make sure that you choose a topic that everyone will know about!

Here are some ideas:

+ What is your favourite sport?

+ What is your favourite ice cream flavour?

+ How do you get to school?

+ What month is your birthday?

+ Do you play Minecraft? (yes/no)

Don't ask questions that give personal data such as where people live. Ask your club leader if you're not sure.

Examples:

![screenshot](images/pets-bar-examples.png)

## Save Your Project {.save}

# Step 2: Read data from a file {.activity}

It's useful to be able to store data in a file rather than having to include it in your code.

## Activity Checklist {.check}

+ Add a new file to your project and call it `pets.txt`:
    
    ![screenshot](images/pets-file.png)

+ Now add data to the file. You can use the favourite pets data that you collected or the example data.
    
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