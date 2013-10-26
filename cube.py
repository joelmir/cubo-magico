# -*- coding: utf-8 -*-

class Cube(object):
  def __init__(self):
    self.face_yellow = Face("y" ,"Yellow")
    self.face_yellow = Face("w" ,"White")
    self.face_yellow = Face("r" ,"Red")
    self.face_yellow = Face("g" ,"Green")
    self.face_yellow = Face("b" ,"Blue")
    self.face_yellow = Face("o" ,"Orange")


class Face(object):
  left = None
  right = None
  Top = None
  Botton = None

  Name = "undefined"

  elements = []

  def __init__(self, default ,name = "undefined"):
    '''
    Monta a matriz com as pecas
    '''
    self.elements = [default ,default, default, default, default, default]


