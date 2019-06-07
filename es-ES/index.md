---
title: Mascotas populares
description: Crea gráficos de sectores y de barras a partir de los datos que recaudes.
notes: "Popular Pets - notes.md"
layout: project
new: true
---

# Introducción {.intro}

In this project you create pie charts and bar graphs from data that you collect from members of your Code Club.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/70d24d92b8?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/pets-finished.png">
</div>

# Step 1: Create a Pie Chart {.activity}

Pie Charts are are useful way of showing data. Let's do a survey of favourite pets in your Code Club and then present the data as a Pie Chart.

## Activity Checklist {.check}

+ Ask your volunteer to help organise a survey. You could record the results on a computer connected to a projector or a whiteboard that everyone can see.
    
    Write a list of pets and make sure everyone's favourite is included.
    
    Then get everyone to vote for their favourite by putting their hand up when it gets called out. Only one vote each!
    
    Por ejemplo:
    
    ![captura de pantalla](images/pets-favourite.png)

+ Abre la plantilla Python en blanco en Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Let's create a pie chart to show the results of your survey. You'll be using the PyGal library to do some of the hard work.
    
    First import the Pygal library:
    
    ![captura de pantalla](images/pets-pygal.png)

+ Now let's create a Pie chart and render (display) it:
    
    ![screenshot](images/pets-pie.png)
    
    Don't worry, it gets more interesting when you add data!

+ Let's add in the data for one of the pets. Use the data that you collected.
    
    ![screenshot](images/pets-add.png)
    
    There's only one piece of data so it takes up the whole pie chart.

+ Now add the rest of the data in the same way.
    
    Por ejemplo:
    
    ![captura de pantalla](images/pets-add-all.png)

+ And to finish off your chart, add a title:
    
    ![captura de pantalla](images/pets-title.png)

## Save Your Project {.save}

## Lee los datos desde un archivo {.challenge}

You can create bar charts in a similar way. Just use `barchart = pygal.Bar()` to create a new barchart, and then add data and render in the same way as for a pie chart.

Collect data from your Code Club members to create your own bar graph.

Make sure that you choose a topic that everyone will know about!

Aquí tienes algunas sugerencias:

+ What is your favourite sport?

+ What is your favourite ice cream flavour?

+ How do you get to school?

+ What month is your birthday?

+ Do you play Minecraft? (yes/no)

Don't ask questions that give personal data such as where people live. Ask your club leader if you're not sure.

Examples:

![captura de pantalla](images/pets-bar-examples.png)

## Save Your Project {.save}

# Step 2: Read data from a file {.activity}

It's useful to be able to store data in a file rather than having to include it in your code.

## Activity Checklist {.check}

+ Add a new file to your project and call it `pets.txt`:
    
    ![captura de pantalla](images/pets-file.png)

+ Now add data to the file. You can use the favourite pets data that you collected or the example data.
    
    ![captura de pantalla](images/pets-data.png)

+ Switch back to `main.py` and comment out the lines that render (display) charts and graphs (so that they aren't displayed):
    
    ![captura de pantalla](images/pets-comment.png)

+ Now let's read the data from the file.
    
    ![captura de pantalla](images/pets-read.png)
    
    The `for` loop will loop over the lines in the file. `splitlines()` removes the newline character from the end of the line as you don't want that.

+ Each line needs to be separated into a label and a value:
    
    ![captura de pantalla](images/pets-split.png)
    
    This will split the line at the spaces so don't include spaces in the labels. (You can add support for spaces in labels later.)

+ You might get an error like this:
    
    ![captura de pantalla](images/pets-error.png)
    
    This happens if you have an empty line at the end of your file.
    
    You can fix the error by only getting the label and value if the line isn't empty.
    
    To do this, indent the code inside your `for` loop and add the code `if line:` above it:
    
    ![captura de pantalla](images/pets-fix.png)

+ You can remove the `print(label, value)` line now everything is working.

+ Now let's add the label and value to a new Pie Chart and render it:
    
    ![captura de pantalla](images/pets-pie2.png)
    
    Note that `add` expects the value to be a number, `int(value)` turns the value from a string into an integer.
    
    If you wanted to use decimals such as 3.5 (floating point numbers) you could use `float(value)` instead.

## Save Your Project {.save}

## Reto: ¡Más cuadros y gráficos! {.challenge}

Can you create a new bar graph or pie chart from data in a file? You'll need to create a new .txt file.

Tip: If you want to have spaces in the labels then use `line.split(': ')` and add colons to your data file, e.g. 'Red Admiral: 6'

![captura de pantalla](images/pets-butterflies.png)

## Save Your Project {.save}

## Challenge: More charts and graphs! {.challenge}

Can you create a pie chart and a bar chart from the same file? You can either use the data you collected earlier or collect some new data.

![captura de pantalla](images/pets-pn-bar.png)

![captura de pantalla](images/pets-pn.png)

## Save Your Project {.save}