#!/bin/python3

import pygal

wykresKolowy = pygal.Pie()
wykresKolowy.title = 'Ulubione zwierzę'
wykresKolowy.add('Pies', 6)
wykresKolowy.add('Kot', 4)
wykresKolowy.add ('Chomik', 3)
wykresKolowy.add ('Ryba', 2)
wykresKolowy.add ('Wąż', 1)
wykresKolowy.render()

wykresSlupokwy = pygal.Bar()
wykresSlupokwy.title = 'Ulubione zwierzę'
wykresSlupokwy.add('Pies', 6)
wykresSlupokwy.add('Kot', 4)
wykresSlupokwy.add ('Chomik', 3)
wykresSlupokwy.add('Ryba', 2)
wykresSlupokwy.add ('Wąż', 1)
wykresSlupokwy.render()
  
wykresKolowy2 = pygal.Pie()
wykresSlupkowy2 = pygal.Bar()

plik = open('pets.txt', 'r')

for linia in plik.read().splitlines():
  if linia:
    etykieta, wartosc = linia.split(' ')
    wykresKolowy2.add(etykieta, int(wartosc))
    wykresSlupkowy2.add(etykieta, int(wartosc))
    
plik.close()

#wykresKolowy2.render()
#wykresSlupkowy2.render()

motyle=pygal.Bar()
motyle.title = 'Liczba Motyli'

plik = open('butterflies.txt', 'r')

for linia in plik.read().splitlines():
  if linia:
    etykieta, wartosc = linia.split(': ')
    motyle.add(etykieta, int(wartosc))
plik.close()

motyle.render()

pn = pygal.Bar()
pn.title = 'Piraci vs Ninja'

plik = open('piratesninjas.txt', 'r')

for linia in plik.read().splitlines():
  if linia:
    etykieta, wartosc = linia.split(' ')
    pn.add(etykieta, int(wartosc))
plik.close()

pn.render()
