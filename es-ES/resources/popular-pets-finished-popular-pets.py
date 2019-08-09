#!/bin/python3

import pygal

grafico_circular = pygal.Pie()
grafico_circular.title = 'Mascota Favorita'
grafico_circular.add('Perro', 6)
grafico_circular.add('Gato', 4)
grafico_circular.add('Hamster', 3)
grafico_circular.add('Conejo', 2)
grafico_circular.add('Tortuga', 1)
grafico_circular.render()

grafico_barras = pygal.Bar()
grafico_barras.title = 'Mascota Favorita'
grafico_barras.add('Perro', 6)
grafico_barras.add('Gato', 4)
grafico_barras.add('Hamster', 3)
grafico_barras.add('Conejo', 2)
grafico_barras.add('Tortuga', 1)
grafico_barras.render()
  
grafico_circular2 = pygal.Pie()
grafico_barras2 = pygal.Bar()

archivo = open('pets.txt', 'r')

for linea in archivo.read().splitlines():
  if linea:
    etiqueta, valor = linea.split(' ')
    grafico_circular2.add(etiqueta, int(valor))
    grafico_barras2.add(etiqueta, int(valor))
    
archivo.close()

#grafico_circular2.render()
#grafico_barras2.render()

mariposas = pygal.Bar()
mariposas.title = 'Conteo de Mariposas'

archivo = open('butterflies.txt', 'r')

for linea in archivo.read().splitlines():
  if linea:
    etiqueta, valor = linea.split(': ')
    mariposas.add(etiqueta, int(valor))
archivo.close()

mariposas.render()

pn = pygal.Bar()
pn.title = 'Piratas vs Ninjas'

archivo = open('piratesninjas.txt', 'r')

for linea in archivo.read().splitlines():
  if linea:
    etiqueta, valor = linea.split(' ')
    pn.add(etiqueta, int(valor))
archivo.close()

pn.render()
