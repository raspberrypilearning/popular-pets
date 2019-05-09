#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = '좋아하는 동물'
piechart.add('개', 6)
piechart.add('고양이', 4)
piechart.add('햄스터', 3)
piechart.add('물고기', 2)
piechart.add('뱀', 1)
piechart.render()

barchart = pygal.Bar()
barchart.title = '좋아하는 동물'
barchart.add('개', 6)
barchart.add('고양이', 4)
barchart.add('햄스터', 3)
barchart.add('물고기', 2)
barchart.add('뱀', 1)
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
butterflies.title = '나비'

file = open('butterflies.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    butterflies.add(label, int(value))
file.close()

butterflies.render()

pn = pygal.Bar()
pn.title = '해적 vs 닌자'

file = open('piratesninjas.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add(label, int(value))
file.close()

pn.render()
