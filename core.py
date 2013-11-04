# -*- coding: utf-8 -*-

from cube import Cube

'''
Trabalho de complexidade de algoritmos
Resolver o cubo mágico 
'''


def new_cube_clean():
  '''
  Retorna o cubo montado de forma correta
  '''
  return Cube()

def shuffle_cube(cube):
  '''
  Embaralha o cubo tracando as faces
  '''

c = new_cube_clean()
c.rotation('botton'  ,False)
print c