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

wykresSlupkowy = pygal.Bar()
wykresSlupkowy.title = 'Ulubione zwierzę'
wykresSlupkowy.add('Pies', 6)
wykresSlupkowy.add('Kot', 4)
wykresSlupkowy.add ('Chomik', 3)
wykresSlupkowy.add('Ryba', 2)
wykresSlupkowy.add ('Wąż', 1)
wykresSlupkowy.render()
  
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
