#!/bin/python3

import pygal

grafico_circular = pygal.Pie()
grafico_circular.title= 'Animal Favorito'
grafico_circular.add('Cachorro', 6)
grafico_circular.add('Gato', 4)
grafico_circular.add('Hamster', 3)
grafico_circular.add('Peixe', 2)
grafico_circular.add('Cobra', 1)
grafico_circular.render()

grafico_barra = pygal.Bar()
grafico_barra.title = 'Animal Favorito'
grafico_barra.add('Cachorro', 6)
grafico_barra.add('Gato', 4)
grafico_barra.add('Hamster', 3)
grafico_barra.add('Peixe', 2)
grafico_barra.add('Cobra', 1)
grafico_barra.render()
  
grafico_circular2 = pygal.Pie()
grafico_barra2 = pygal.Bar()

arquivo = open('pets.txt', 'r')

for linha in arquivo.read().splitlines():
  if linha:
    rotulo, valor = linha.split(' ')
    grafico_circular2.add(rotulo, int(valor))
    grafico_barra2.add(rotulo, int(valor))
    
arquivo.close()

#grafico_circular2.render()
#grafico_barra2.render()

borboletas = pygal.Bar()
borboletas.title = 'Contagem de Borboletas'

arquivo = open('butterflies.txt', 'r')

for linha in arquivo.read().splitlines():
  if linha:
    rotulo, valor = linha.split(' ')
    borboletas.add(rotulo, int(valor))
arquivo.close()

borboletas.render()

pn = pygal.Bar()
pn.title = 'Piratas vs Ninjas'

arquivo = open('piratesninjas.txt', 'r')

for linha in arquivo.read().splitlines():
  if linha:
    rotulo, valor = linha.split(' ')
    pn.add(rotulo, int(valor))
arquivo.close()

pn.render()
