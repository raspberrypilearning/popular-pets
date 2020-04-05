#!/bin/python3

import pygal

kreisdiagramm = pygal.Pie()
kreisdiagramm.title = 'Lieblingshaustiere'
kreisdiagramm.add('Hund', 6)
kreisdiagramm.add('Katze', 4)
kreisdiagramm.add('Hamster', 3)
kreisdiagramm.add('Fisch', 2)
kreisdiagramm.add('Schlange', 1)
kreisdiagramm.render()

balkendiagramm = pygal.Bar()
balkendiagramm.title = 'Lieblingshaustiere'
balkendiagramm.add('Hund', 6)
balkendiagramm.add('Katze', 4)
balkendiagramm.add('Hamster', 3)
balkendiagramm.add('Fisch', 2)
balkendiagramm.add('Schlange', 1)
balkendiagramm.render()
  
kreisdiagramm2 = pygal.Pie()
kreisdiagramm2 = pygal.Bar()

datei = open('pets.txt', 'r')

for zeile in datei.read().splitlines():
  if zeile:
    bezeichnung, wert = zeile.split(' ')
    kreisdiagramm2.add(bezeichnung, int(wert))
    balkendiagramm2.add(bezeichnung, int(wert))
    
datei.close()

#kreisdiagramm2.render()
#balkendiagramm2.render()

schmetterlinge = pygal.Bar()
schmetterlinge.title = 'Anzahl der Schmetterlinge'

datei = open('butterflies.txt', 'r')

for zeile in datei.read().splitlines():
  if zeile:
    bezeichnung, wert = zeile.split(': ')
    schmetterlinge.add(bezeichnung, int(wert))
datei.close()

schmetterlinge.render()

pn = pygal.Bar()
pn.title = 'Piraten vs Ninjas'

datei = open('piratesninjas.txt', 'r')

for zeile in datei.read().splitlines():
  if zeile:
    bezeichnung, wert = zeile.split(' ')
    pn.add(bezeichnung, int(wert))
datei.close()

pn.render()
