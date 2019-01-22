#!/bin/python3

import pygal

kruznigraf = pygal.Pie()
kruznigraf.title = 'Omiljeni ljubimac'
kruznigraf.add('Pas', 6)
kruznigraf.add('Mačka', 4)
kruznigraf.add('Hrčak', 3)
kruznigraf.add('Riba', 2)
kruznigraf.add('Zmija', 1)
kruznigraf.render()

stubicastigraf = pygal.Bar()
stubicastigraf.title = 'Omiljeni ljubimac'
stubicastigraf.add('Pas', 6)
stubicastigraf.add('Mačka', 4)
stubicastigraf.add('Hrčak', 3)
stubicastigraf.add('Riba', 2)
stubicastigraf.add('Zmija', 1)
stubicastigraf.render()
  
kruznigraf2 = pygal.Pie()
stubicastigraf2 = pygal.Bar()

datoteka = open('ljubimci.txt', 'r')

for red in datoteka.read().splitlines():
  if red:
    naziv, vrijednost = red.split(' ')
    kruznigraf2.add(naziv, int(vrijednost))
    stubicastigraf2.add(naziv, int(vrijednost))
    
datoteka.close()

#kruznigraf2.render()
#stubicastigraf2.render()

leptiri = pygal.Bar()
leptiri.title = 'Broj leptira'

datoteka = open('leptiri.txt', 'r')

for red in datoteka.read().splitlines():
  if red:
    naziv, vrijednost = red.split(': ')
    leptiri.add(naziv, int(vrijednost))
datoteka.close()

leptiri.render()

gn = pygal.Bar()
gn.title = 'Gusari protiv Nindži'

datoteka = open('gusarinindze.txt', 'r')

for red in datoteka.read().splitlines():
  if red:
    naziv, vrijednost = red.split(' ')
    gn.add(naziv, int(vrijednost))
datoteka.close()

gn.render()
