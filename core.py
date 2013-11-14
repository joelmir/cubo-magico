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
  options = ['top', 'bottom', 'right' ,'left', 'rotate_clockwise', 'rotate_anti_clockwise'] 
  c.command('top')

def first_nivel():


c = new_cube_clean()  

c.default_face.rotate()
c.translate_right()
c.default_face.rotate()
#print c
c.translate_right()
c.default_face.rotate()
#print c
c.translate_right()
c.default_face.rotate()
#print c
c.translate_left()
c.default_face.rotate()
#print c
c.default_face.rotate()
print c