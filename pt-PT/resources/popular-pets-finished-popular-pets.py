#!/bin/python3

import pygal

circular = pygal.Pie()
circular.title = 'Animais Favoritos'
 circular.add('Cão', 6)
circular.add('Gato',4)
circular.add('Hamster',3)
circular.add('Peixe',2)
circular.add('Cobra',1)
circular.render()

barras = pygal.Bar()
barras.title = 'Animal Favorito'
barras.add('Cão',6)
barras.add('Gato',4)
barras.add('Hamster',3)
barras.add('Peixe',2)
barras.add('Snake',1)
barras.render()
  
circular2 = pygal.Pie()
barras2 = pygal.Bar()

ficheiro = open('animais.txt','r')

for linha in ficheiro.read().splitlines():
  if linha:
    rotulo, valor = linha.split(' ')
    circular2.add(rotulo, int(valor))
    barras2.add(rotulo, int(valor))
    
ficheiro.close()

#circular2.render()
#barras2.render()

borboletas = pygal.Bar ()
borboletas.title = 'Contagem de Borboletas'

ficheiro = open('borboletas.txt','r')

for linha in ficheiro.read().splitlines():
  if linha:
    rotulo, valor = linha.split(': ')
    borboletas.add(rotulo, int(valor))
ficheiro.close()

borboletas.render()

pn = pygal.Bar ()
pn.title = 'Piratas vs Ninjas'

ficheiro = open('piratasninjas.txt','r')

for linha in ficheiro.read().splitlines():
  if linha:
    rotulo, valor = linha.split(' ')
    pn.add(rotulo, int(valor))
ficheiro.close()

pn.render()
