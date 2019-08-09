#!/bin/python3

import pygal

diagrama_circulara= pygal.Pie()
diagrama_circulara.title = 'Animal de companie favorit'
diagrama_circulara.add('Câine', 6)
diagrama_circulara.add('Pisică', 4)
diagrama_circulara.add('Hamster', 3)
diagrama_circulara.add ('Pește', 2)
diagrama_circulara.add ('Șarpe', 1)
diagrama_circulara.render()

grafic_bare = pygal.Bar()
grafic_bare.title = 'Animal de companie favorit'
grafic_bare.add('Câine', 6)
grafic_bare.add('Pisică', 4)
grafic_bare.add('Hamster', 3)
grafic_bare.add ('Pește', 2)
grafic_bare.add ('Șarpe', 1)
grafic_bare.render()
  
diagrama_circulara2 = pygal.Pie()
grafic_bare2 = pygal.Bar()

file = open('pets.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    diagrama_circulara2.add(label, int(value))
    grafic_bare2.add(label, int(value))
    
file.close()

#diagrama_circulara2.render()
#grafic_bare2.render()

fluturi = pygal.Bar()
fluturi.title = 'Numărul fluturilor'

file = open('butterflies.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    fluturi.add(label, int(value))
file.close()

fluturi.render()

pn = pygal.Bar()
pn.title = 'Pirați vs ninja'

file = open('piratesninjas.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add(label, int(value))
file.close()

pn.render()
