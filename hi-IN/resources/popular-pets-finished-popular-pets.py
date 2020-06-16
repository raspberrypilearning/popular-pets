#!/bin/python3

import pygal

piechart2 = pygal.Pie()
piechart.title = 'पसंदीदा पालतू'
piechart.add ('कुत्ता', 6)
piechart.add ('बिल्ली', 4)
piechart.add ('हम्सटर', 3)
piechart.add ('मछली', 2)
piechart.add ('साँप', 1)
piechart.render()

barchart = pygal.Bar()
barchart.title = 'पसंदीदा पालतू'
piechart.add ('कुत्ता', 6)
piechart.add ('बिल्ली', 4)
piechart.add ('हम्सटर', 3)
piechart.add ('मछली', 2)
piechart.add ('साँप', 1)
barchart.render()
  
piechart2 = pygal.Pie()
barchart = pygal.Bar()

file = open ('pets.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    piechart2.add(label, int(value))
    barchart2.add(label, int(value))
    
file.close ()

# Piechart2.render ()
# Barchart2.render ()

butterflies= pygal.Bar ()
butterflies.title = 'तितली गणना'

फ़ाइल = खुला ('butterflies.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    barchart2.add(label, int(value))
file.close ()

butterflies.render ()

pn = pygal.Bar ()
pn.title = 'समुद्री-डाकू बनाम निन्जा'

file = open ('piratesninjas.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add (label, int(value))
file.close ()

pn.render ()
