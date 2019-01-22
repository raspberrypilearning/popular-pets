#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = 'Αγαπημένο Κατοικίδιο Ζώο'
piechart.add('Σκύλος', 6)
piechart.add('Γάτα', 4)
piechart.add('Χάμστερ', 3)
piechart.add('Ψάρι', 2)
piechart.add('Φίδι', 1)
piechart.render()

barchart = pygal.Bar()
barchart.title = 'Αγαπημένο Κατοικίδιο Ζώο'
barchart.add('Σκύλος', 6)
piechart.add('Γάτα', 4)
piechart.add('Χάμστερ', 3)
piechart.add('Ψάρι', 2)
piechart.add('Φίδι', 1)
barchart.render()
  
piechart2 = pygal.Pie()
barchart2 = pygal.Bar()

file = open('pets.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    piechart2.add(label, int(value))
    barchart2.add(label, int(value))
    
file.close()

#piechart2.render()
#barchart2.render()

butterflies = pygal.Bar()
butterflies.title = 'Αριθμός Πεταλούδων'

file = open('butterflies.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    butterflies.add(label, int(value))
file.close()

butterflies.render()

pn = pygal.Bar()
pn.title = 'Πειρατές εναντίον Νίντζα'

file = open('piratesninjas.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add(label, int(value))
file.close()

pn.render()
