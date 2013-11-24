# -*- coding: utf-8 -*-

class Cube(object):
    '''
    Monta o cubo com 6 faces montadas
    '''
    def command(self, str_cmd):
        self.cmd[str_cmd]()

    def rotate_clockwise(self):
        self.default_face.rotate()

    def rotate_anti_clockwise(self):
        self.default_face.rotate(False)

    def translate_top(self):
        self.default_face.left.right ,\
        self.default_face.left.top,\
        self.default_face.left.left,\
        self.default_face.left.bottom = \
        self.default_face.left.top,\
        self.default_face.left.left,\
        self.default_face.left.bottom,\
        self.default_face.left.right
        self.default_face.left.rotate(True, False)

        self.default_face.right.left,\
        self.default_face.right.top,\
        self.default_face.right.right,\
        self.default_face.right.bottom =\
        self.default_face.right.top,\
        self.default_face.right.right,\
        self.default_face.right.bottom,\
        self.default_face.right.left
        self.default_face.right.rotate(False, False)

        self.default_face = self.default_face.top

    def translate_bottom(self):
        self.default_face.right.left,\
        self.default_face.right.top,\
        self.default_face.right.right,\
        self.default_face.right.bottom =\
        self.default_face.right.top,\
        self.default_face.right.right,\
        self.default_face.right.bottom,\
        self.default_face.right.left
        self.default_face.right.rotate(False, False)

        self.default_face.left.right ,\
        self.default_face.left.top,\
        self.default_face.left.left,\
        self.default_face.left.bottom = \
        self.default_face.left.top,\
        self.default_face.left.left,\
        self.default_face.left.bottom,\
        self.default_face.left.right
        self.default_face.left.rotate(True, False)

        self.default_face = self.default_face.bottom

    def translate_right(self):

        self.default_face.top.right ,\
        self.default_face.top.top,\
        self.default_face.top.left,\
        self.default_face.top.bottom = \
        self.default_face.top.top,\
        self.default_face.top.left,\
        self.default_face.top.bottom,\
        self.default_face.top.right
        self.default_face.top.rotate(True, False)

        self.default_face.bottom.left ,\
        self.default_face.bottom.top,\
        self.default_face.bottom.right,\
        self.default_face.bottom.bottom = \
        self.default_face.bottom.top,\
        self.default_face.bottom.left,\
        self.default_face.bottom.bottom,\
        self.default_face.bottom.right
        self.default_face.bottom.rotate(False, False)

        self.default_face.top.top.top,\
        self.default_face.top.top.bottom,\
        self.default_face.top.top.left,\
        self.default_face.top.top.right = \
        self.default_face.top.top.bottom,\
        self.default_face.top.top.top,\
        self.default_face.top.top.right,\
        self.default_face.top.top.left
        #self.default_face.top.top.rotate(True, False)
        #self.default_face.top.top.rotate(True, False)

        self.default_face.left.top,\
        self.default_face.left.bottom,\
        self.default_face.left.left,\
        self.default_face.left.right = \
        self.default_face.left.bottom,\
        self.default_face.left.top,\
        self.default_face.left.right,\
        self.default_face.left.left
        #self.default_face.left.rotate(True, False)
        #self.default_face.left.rotate(True, False)

        self.default_face = self.default_face.right

    def translate_left(self):

        self.default_face.bottom.right = self.default_face.bottom.top
        self.default_face.bottom.top = self.default_face.bottom.left
        self.default_face.bottom.left = self.default_face.bottom.bottom
        self.default_face.bottom.bottom = self.default_face.bottom.right
        self.default_face.bottom.rotate(True, False)


        self.default_face.top.left = self.default_face.top.top
        self.default_face.top.top = self.default_face.top.right
        self.default_face.top.right = self.default_face.top.bottom
        self.default_face.top.bottom = self.default_face.top.left
        self.default_face.top.rotate(False, False)

        self.default_face = self.default_face.left


    def __init__(self):
        '''
        inicializa as faces com as cores
        '''
        self.face_red = Face("r" ,"Red")
        self.face_orange = Face("o" ,"Orange")
        self.face_white = Face("w" ,"White")
        self.face_blue = Face("b" ,"Blue")
        self.face_green = Face("g" ,"Green")
        self.face_yellow = Face("y" ,"Yellow")

        #Monta as referências entre as faces
        #Red
        self.face_red.left = self.face_blue
        self.face_red.right = self.face_orange
        self.face_red.top = self.face_green
        self.face_red.bottom = self.face_yellow

        #Blue
        self.face_blue.left = self.face_white
        self.face_blue.right = self.face_red
        self.face_blue.top = self.face_green
        self.face_blue.bottom = self.face_yellow

        #White
        self.face_white.left = self.face_blue
        self.face_white.right = self.face_orange
        self.face_white.top = self.face_yellow
        self.face_white.bottom = self.face_green

        #Orange
        self.face_orange.left = self.face_red
        self.face_orange.right = self.face_white
        self.face_orange.top = self.face_green
        self.face_orange.bottom = self.face_yellow

        #Gree
        self.face_green.left = self.face_blue
        self.face_green.right = self.face_orange
        self.face_green.top = self.face_white
        self.face_green.bottom = self.face_red

        #Yellow
        self.face_yellow.left = self.face_blue
        self.face_yellow.right = self.face_orange
        self.face_yellow.top = self.face_red
        self.face_yellow.bottom = self.face_white

        #define a face padrão
        self.default_face = self.face_red

        self.cmd = {'top':self.translate_top,
         'bottom':self.translate_bottom,\
         'right':self.translate_right,\
         'left':self.translate_left,\
         'rotate_clockwise':self.rotate_clockwise,\
         'rotate_anti_clockwise':self.rotate_anti_clockwise}

    def __str__(self):
        '''
        Exibe o cubo de forma 'Amigavel' :D
        '''
        #face superior
        res =  '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.top.linha1())
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.top.linha2())
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.top.linha3())
        #face esquera / frente / direita / trás
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.default_face.left.linha1())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t '.format(self.default_face.linha1())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.default_face.right.linha1())
        res += '{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.bottom.bottom.linha1())

        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.default_face.left.linha2())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t '.format(self.default_face.linha2())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.default_face.right.linha2())
        res += '{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.bottom.bottom.linha2())
        
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.default_face.left.linha3())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t '.format(self.default_face.linha3())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.default_face.right.linha3())
        res += '{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.bottom.bottom.linha3())
        #face inferior
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.bottom.linha1())
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.bottom.linha2())
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.default_face.bottom.linha3())
        return res


class Face(object):
    '''
    Representa uma face do Cubo
    '''
    left = None
    right = None
    top = None
    bottom = None

    name = "-"

    elements = []

    def rotate(self, clockwise=True , border=True):
        '''
        Rotaciona a face em 90º

        Direção horária ou anti-horária
        '''

        if clockwise:
            #Giro das peças da face 
            self.elements[0], self.elements[1], self.elements[2], self.elements[3], \
                self.elements[4], self.elements[5], self.elements[6], self.elements[7] = \
                self.elements[5], self.elements[3], self.elements[0], self.elements[6], \
                self.elements[1], self.elements[7], self.elements[4], self.elements[2]
            if(border):
                #Giro das peças da borda
                self.left.elements[2], \
                self.bottom.elements[0], \
                self.right.elements[5], \
                self.top.elements[7] = \
                self.bottom.elements[0], \
                self.right.elements[5], \
                self.top.elements[7] , \
                self.left.elements[2]

                self.left.elements[4], \
                self.bottom.elements[1], \
                self.right.elements[3], \
                self.top.elements[6] = \
                self.bottom.elements[1], \
                self.right.elements[3], \
                self.top.elements[6], \
                self.left.elements[4]

                self.left.elements[7], \
                self.bottom.elements[2], \
                self.right.elements[0], \
                self.top.elements[5] = \
                self.bottom.elements[2], \
                self.right.elements[0], \
                self.top.elements[5],\
                self.left.elements[7]

            
        else:
            #Giro das peças da face
            self.elements[0], self.elements[1], self.elements[2], self.elements[3], \
                self.elements[4], self.elements[5], self.elements[6], self.elements[7] = \
                self.elements[2], self.elements[4], self.elements[7], self.elements[1], \
                self.elements[6], self.elements[0], self.elements[3], self.elements[5]

            if(border):
                #Giro das peças da borda
                self.bottom.elements[0], \
                self.right.elements[5], \
                self.top.elements[7] , \
                self.left.elements[2] = \
                self.left.elements[2], \
                self.bottom.elements[0], \
                self.right.elements[5], \
                self.top.elements[7]
                
                self.bottom.elements[1], \
                self.right.elements[3], \
                self.top.elements[6], \
                self.left.elements[4] = \
                self.left.elements[4], \
                self.bottom.elements[1], \
                self.right.elements[3], \
                self.top.elements[6]
                
                self.bottom.elements[2], \
                self.right.elements[0], \
                self.top.elements[5],\
                self.left.elements[7] = \
                self.left.elements[7], \
                self.bottom.elements[2], \
                self.right.elements[0], \
                self.top.elements[5]

    def __init__(self, default ,name = "-"):
        '''
        Monta a matriz com as pecas
        '''
        self.name = name
        self.elements = [default ,default, default, default, default, default,default,default]

    def linha1(self):
        '''
        Retorna a primeira linha da face
        '''
        return (self.elements[0],self.elements[1],self.elements[2])
    def linha2(self):
        '''
        Retorna a segunda linha da face
        '''
        return (self.elements[3],self.name,self.elements[4])
    def linha3(self):
        '''
        Retorna a terceira linha da face
        '''
        return (self.elements[5],self.elements[6],self.elements[7])

    def __str__(self):
        '''
        Retorna a face de forma amigável
        '''
        res = '{0}\t{1}\t{2}\n'.format(self.elements[0],self.elements[1],self.elements[2]) 
        res += '{0}\t{1}\t{2}\n'.format(self.elements[3],self.name,self.elements[4])
        res += '{0}\t{1}\t{2}\n'.format(self.elements[5],self.elements[6],self.elements[7])
        return res


