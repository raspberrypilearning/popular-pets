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
barchart.title = 'Animal favori'
barchart.add ('Chien', 6)
barchart.add ('Cat', 4)
barchart.add ('Hamster', 3)
barchart.add ('Poisson', 2)
barchart.add ('Serpent', 1)
barchart.render ()
  
Morceau2 = Pygal.Pie ()
barchart2 = pygal.Bar ()

file = open ('pets.txt', 'r')

pour la ligne dans file.read (). splitlines ():
  si ligne:
    label, valeur = line.split ('')
    atchhart2.add (label, int (valeur))
    barchart2.add (label, int (valeur))
    
file.close ()

#atchhart2.render ()
# barchart2.render ()

papillons = pygal.Bar ()
butterflies.title = 'Nombre de papillons'

file = open ('butterflies.txt', 'r')

pour la ligne dans file.read (). splitlines ():
  si ligne:
    label, valeur = line.split (':')
    papillons.add (étiquette, int (valeur))
file.close ()

butterflies.render ()

pn = pygal.Bar ()
pn.title = 'Pirates vs Ninjas'

fichier = ouvert ('piratesninjas.txt', 'r')

pour la ligne dans file.read (). splitlines ():
  si ligne:
    label, valeur = line.split ('')
    pn.add (étiquette, int (valeur))
file.close ()

pn.render ()
