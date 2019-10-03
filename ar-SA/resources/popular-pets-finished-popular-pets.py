#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = 'الحيوانات الأليفة المفضلة'
piechart.add('كلب', 6)
piechart.add('قط', 4)
piechart.add('هامستر', 3)
piechart.add('سمك', 2)
piechart.add('ثعبان', 1)
piechart.render()

barchart = pygal.Bar()
barchart.title = 'الحيوانات الأليفة المفضلة'
piechart.add('كلب', 6)
piechart.add('قط', 4)
piechart.add('هامستر', 3)
piechart.add('سمك', 2)
piechart.add('ثعبان', 1)
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
butterflies.title = 'عدد الفراشات'

file = open('butterflies.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    butterflies.add(label, int(value))
file.close()

butterflies.render()

pn = pygal.Bar()
pn.title = 'قراصنة مقابل النينجا'

file = open('piratesninjas.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add(label, int(value))
file.close()

pn.render()
