# -*- coding: utf-8 -*-

class Cube(object):
    '''
    Monta o cubo com 6 faces montadas
    '''

    def rotation_line(self,key):
        '''
        Rotaciona as faces de acordo com as configurações:
        '''
        configurations = {  'top_clockwise': \
                                {'positions': (0, 1, 2), \
                                    'face1':self.default_face, \
                                    'face2':self.default_face.right, \
                                    'face3':self.default_face.right.right, \
                                    'face4':self.default_face.right.right.right, \
                                    'affected_face':self.default_face.top.sef_rotation, \
                                    'clockwise':True}, \
                            'top_anti_clockwise':\
                                {'positions': (0, 1, 2), \
                                    'face1':self.default_face.left, \
                                    'face2':self.default_face.left.left, \
                                    'face3':self.default_face.left.left.left, \
                                    'face4':self.default_face.left.left.left.left, \
                                    'affected_face':self.default_face.top.sef_rotation, \
                                    'clockwise':False},\
                            'botton_clockwise': \
                                {'positions': (5,6,7), \
                                    'face1':self.default_face, \
                                    'face2':self.default_face.right, \
                                    'face3':self.default_face.right.right, \
                                    'face4':self.default_face.right.right.right, \
                                    'affected_face':self.default_face.botton.sef_rotation, \
                                    'clockwise':True}, \
                            'botton_anti_clockwise':\
                                {'positions': (5,6,7), \
                                    'face1':self.default_face.left, \
                                    'face2':self.default_face.left.left, \
                                    'face3':self.default_face.left.left.left, \
                                    'face4':self.default_face.left.left.left.left, \
                                    'affected_face':self.default_face.botton.sef_rotation, \
                                    'clockwise':False},\
                            'left_clockwise': \
                                {'positions': (0,3,5), \
                                    'face1':self.default_face, \
                                    'face2':self.default_face.top, \
                                    'face3':self.default_face.top.top, \
                                    'face4':self.default_face.top.top.top, \
                                    'affected_face':self.default_face.left.sef_rotation, \
                                    'clockwise':True}, \
                            'left_anti_clockwise':\
                                {'positions': (0,3,5), \
                                    'face1':self.default_face, \
                                    'face2':self.default_face.botton, \
                                    'face3':self.default_face.botton.botton, \
                                    'face4':self.default_face.botton.botton.botton, \
                                    'affected_face':self.default_face.left.sef_rotation, \
                                    'clockwise':False}}
                
        if key in configurations:
            config = configurations[key]
            for idx in config['positions']:
                config['face1'].elements[idx], \
                    config['face2'].elements[idx], \
                    config['face3'].elements[idx], \
                    config['face4'].elements[idx] = \
                    config['face2'].elements[idx], \
                    config['face3'].elements[idx], \
                    config['face4'].elements[idx], \
                    config['face1'].elements[idx]
            config['affected_face'](config['clockwise'])
        else:
            print 'Linha {0} não é uma linha valida :/ '.format(key)


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
        self.face_red.botton = self.face_yellow

        #Orange
        self.face_orange.left = self.face_red
        self.face_orange.right = self.face_white
        self.face_orange.top = self.face_green
        self.face_orange.botton = self.face_yellow

        #White
        self.face_white.left = self.face_orange
        self.face_white.right = self.face_blue
        self.face_white.top = self.face_yellow
        self.face_white.botton = self.face_green

        #Blue
        self.face_blue.left = self.face_white
        self.face_blue.right = self.face_red
        self.face_blue.top = self.face_green
        self.face_blue.botton = self.face_yellow

        #Gree
        self.face_green.left = self.face_blue
        self.face_green.right = self.face_orange
        self.face_green.top = self.face_white
        self.face_green.botton = self.face_red

        #Yellow
        self.face_yellow.left = self.face_orange
        self.face_yellow.right = self.face_blue
        self.face_yellow.top = self.face_red
        self.face_yellow.botton = self.face_white

        #define a face padrão
        self.default_face = self.face_red

    def __str__(self):
        '''
        Exibe o cubo de forma 'Amigavel' :D
        '''
        #face superior
        res =  '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_green.linha1())
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_green.linha2())
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_green.linha3())
        #face esquera / frente / direita / trás
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.face_blue.linha1())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t '.format(self.face_red.linha1())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.face_orange.linha1())
        res += '{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_white.linha1())

        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.face_blue.linha2())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t '.format(self.face_red.linha2())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.face_orange.linha2())
        res += '{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_white.linha2())
        
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.face_blue.linha3())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t '.format(self.face_red.linha3())
        res += '{0[0]}\t{0[1]}\t{0[2]}\t'.format(self.face_orange.linha3())
        res += '{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_white.linha3())
        #face inferior
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_yellow.linha1())
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_yellow.linha2())
        res += '\t\t\t{0[0]}\t{0[1]}\t{0[2]}\n'.format(self.face_yellow.linha3())
        return res


class Face(object):
    '''
    Representa uma face do Cubo
    '''
    left = None
    right = None
    top = None
    botton = None

    name = "-"

    elements = []

    def sef_rotation(self, clockwise=True):
        '''
        Rotaciona a face em 90º

        Direção horária ou anti-horária
        '''

        if clockwise:
            self.elements[0], self.elements[1], self.elements[2], self.elements[3], \
                self.elements[4], self.elements[5], self.elements[6], self.elements[7] = \
                self.elements[5], self.elements[3], self.elements[0], self.elements[6], \
                self.elements[1], self.elements[7], self.elements[4], self.elements[2]
        else:
            self.elements[0], self.elements[1], self.elements[2], self.elements[3], \
                self.elements[4], self.elements[5], self.elements[6], self.elements[7] = \
                self.elements[2], self.elements[4], self.elements[7], self.elements[1], \
                self.elements[6], self.elements[0], self.elements[3], self.elements[5]

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


