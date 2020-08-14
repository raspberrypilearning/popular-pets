#!/bin/python3

import pygal

camembert = pygal.Pie()
camembert.title = 'Animaux de compagnie préférés'
camembert.add('Chien', 6)
camembert.add('Chat', 4)
camembert.add('Hamster', 3)
camembert.add('Poisson', 2)
camembert.add('Serpent', 1)
camembert.render()

histogramme = pygal.Bar()
histogramme.title = 'Animaux de compagnie préférés'
histogramme.add('Chien', 6)
histogramme.add('Chat', 4)
histogramme.add('Hamster', 3)
histogramme.add('Poisson', 2)
histogramme.add('Serpent', 1)
histogramme.render()
  
camembert2 = Pygal.Pie()
histogramme2 = pygal.Bar()

fichier = open('pets.txt', 'r')

for ligne in fichier.read().splitlines():
  if ligne:
    libelle, value = line.split(' ')
    camembert2.add(libelle, int(value))
    histogramme2.add(libelle, int(value))
    
fichier.close()

#camembert2.render()
# histogramme2.render()

papillons = pygal.Bar()
papillons.title = 'Comptage des papillons'

fichier = open('butterflies.txt', 'r')

for ligne in fichier.read().splitlines():
  if ligne:
    libelle, value = line.split(': ')
    papillons.add(libelle, int(value))
fichier.close()

papillons.render()

pn = pygal.Bar()
pn.title = 'Pirates vs Ninjas'

fichier = open('piratesninjas.txt', 'r')

for ligne in fichier.read().splitlines():
  if ligne:
    libelle, value = line.split(' ')
    pn.add(libelle, int(value))
fichier.close()

pn.render()
