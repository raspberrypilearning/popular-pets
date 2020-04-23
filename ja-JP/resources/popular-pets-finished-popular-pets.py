#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = '好きなペット'
piechart.add('犬', 6)
piechart.add('猫', 4)
piechart.add('ハムスター', 3)
piechart.add('お魚', 2)
piechart.add('蛇', 1)
piechart.render()

barchart = pygal.Bar()
barchart.title = '好きなペット'
barchart.add('犬', 6)
barchart.add('猫', 4)
barchart.add('ハムスター', 3)
barchart.add('お魚', 2)
barchart.add('蛇', 1)
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
butterflies.title = '蝶々の数'

file = open('butterflies.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    butterflies.add(label, int(value))
file.close()

butterflies.render()

pn = pygal.Bar()
pn.title = '海賊 vs 忍者'

file = open('piratesninjas.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add(label, int(value))
file.close()

pn.render()
