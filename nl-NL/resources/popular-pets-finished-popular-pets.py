#!/bin/python3

import pygal

taartdiagram = pygal.Pie()
taartdiagram.title = 'Favoriete huisdieren' 
taartdiagram.add('Hond', 6)
taartdiagram.add('Kat', 4)
taartdiagram.add('Hamster', 3)
taartdiagram.add('Vis', 2)
taartdiagram.add('Slang', 1)
taartdiagram.render()

staafdiagram = pygal.Bar()
staafdiagram.title = 'Favoriete huisdieren' 
staafdiagram.add('Hond', 6)
staafdiagram.add('Kat', 4)
staafdiagram.add('Hamster', 3)
staafdiagram.add('Vis', 2)
staafdiagram.add('Slang', 1)
staafdiagram.render()
  
taartdiagram2 = pygal.Pie()
staafdiagram2 = pygal.Bar()

bestand = open('huisdieren.txt', 'r')

for regel in bestand.read().splitlines():
  if regel:
    naam, waarde = regel.split(' ')
    taartdiagram2.add(naam,int(waarde))
    staafdiagram2.add(naam,int(waarde))
    
bestand.close()

#taartdiagram2.render()
#staafdiagram2.render()

vlinders = pygal. Bar()
vlinders.title = 'Vlinder telling'

bestand = open('vlinders.txt', 'r')

for regel in bestand.read().splitlines():
  if regel:
    naam, waarde = regel.split(' ')
    vlinders.add(naam, int(waarde))
bestand.close()

vlinders.render()

pn = pygal.Bar()
pn.title = 'Piraten tegen Ninjas'

bestand = open('piratenninjas.txt', 'r')

for regel in bestand.read().splitlines():
  if regel:
    naam, waarde = regel.split(' ')
    pn.add(naam,int(waarde))
bestand.close()

pn.render()
