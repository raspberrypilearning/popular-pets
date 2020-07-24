#!/bin/python3

import pygal

kordiagram = pygal.Pie()
kordiagram.title = 'Kedvenc kisállat'
kordiagram.add('Kutya', 6)
kordiagram.add('Macska', 4)
kordiagram.add('Hörcsög', 3)
kordiagram.add('Hal', 2)
kordiagram.add('Kígyó', 1)
kordiagram.render()

oszlopdiagram = pygal.Bar ()
oszlopdiagram.title = 'Kedvenc kisállat'
oszlopdiagram.add('Kutya', 6)
oszlopdiagram.add ('Macska', 4)
oszlopdiagram.add('Hörcsög', 3)
oszlopdiagram.add('Hal', 2)
oszlopdiagram.add ('Kígyó', 1)
oszlopdiagram.render ()
  
kordiagram2 = pygal.Pie()
oszlopdiagram2 = pygal.Bar()

file = open('pets.txt', 'r')

for sor in file.read().splitlines():
  if sor:
    cimke, ertek = sor.split(' ')
    kordiagram2.add(cimke, int(ertek))
    oszlopdiagram2.add(cimke, int(ertek))
    
file.close()

#kordiagram2.render()
#oszlopdiagram2.render()

pillangok = pygal.Bar()
pillangok.title = 'Pillangók száma'

file = open('butterflies.txt', 'r')

for sor in file.read().splitlines():
  if sor:
    cimke, ertek = sor.split ('')
    pillangok.add(cimke, int(ertek))
file.close()

pillangok.render()

kalozok = pygal.Bar()
kalozok.title = 'Kalózok vagy nindzsák'

file = open('piratesninjas.txt', 'r')

for sor in file.read().splitlines():
  if sor:
    cimke, ertek = sor.split(' ')
    kalozok.add(cimke, int(ertek))
file.close()

kalozok.render()
