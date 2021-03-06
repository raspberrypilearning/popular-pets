#!/bin/python3

import pygal

diagramma_a_torta = pygal.Pie()
diagramma_a_torta.title='Animale Preferito'
diagramma_a_torta.add('Cane',6)
diagramma_a_torta.add('Cat',4)
diagramma_a_torta.add('Criceto',3)
diagramma_a_torta.add('Pesce',2)
diagramma_a_torta.add('Serpente',1)
diagramma_a_torta.render()

grafico_a_barre = pygal.Bar()
grafico_a_barre.title = 'Animale Preferito'
grafico_a_barre.add('Cane',6)
grafico_a_barre.add('Gatto',4)
grafico_a_barre.add('Criceto',3)
grafico_a_barre.add('Pesce',2)
grafico_a_barre.add('Serpente',1)
grafico_a_barre.render()
  
diagramma_a_torta2 = pygal.Pie()
grafico_a_barre2 = pygal.Bar()

file = open('animalidomestici.txt', 'r')

for line in file.read().splitlines():
  if line:
    label,value = line.split(' ')
    diagramma_a_torta2.add(label, int(value))
    grafico_a_barre2.add(label, int(value))
    
file.close()

#diagramma_a_torta2.render()
#grafico_a_barre2.render()

farfalle = pygal.Bar()
farfalle.title = 'Calcolo farfalle'

file = open('farfalle.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    farfalle.add(label, int(value))
file.close()

farfalle.render()

pn = pygal.Bar()
pn.title = 'Pirati vs Ninja'

file = open('piratininja.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add(label, int(value))
file.close()

pn.render()
