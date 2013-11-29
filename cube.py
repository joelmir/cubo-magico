# -*- coding: utf-8 -*-

class Cube(object):
    '''
    Monta o cubo com 6 faces montadas
    '''
    def command(self, cmd):
        self.cmd[cmd]()

    def __init__(self, test=False):
        '''
        Inicializa o Cubo com as face Montadas

        teste de incilização completa
        >>> Cube(True).matriz
        [['g1', 'g2', 'g3'], \
['g4', 'g5', 'g6'], \
['g7', 'g8', 'g9'], \
['y1', 'y2', 'y3', 'r1', 'r2', 'r3', 'w1', 'w2', 'w3', 'o9', 'o8', 'o7'], \
['y4', 'y5', 'y6', 'r4', 'r5', 'r6', 'w4', 'w5', 'w6', 'o6', 'o5', 'o4'], \
['y7', 'y8', 'y9', 'r7', 'r8', 'r9', 'w7', 'w8', 'w9', 'o3', 'o2', 'o1'], \
['b1', 'b2', 'b3'], \
['b4', 'b5', 'b6'], \
['b7', 'b8', 'b9']]'''

        self.matriz = []
        '''
        inicializa as faces com as cores
        '''
        if test:
            self.matriz.append(['g1','g2','g3'])
            self.matriz.append(['g4','g5','g6'])
            self.matriz.append(['g7','g8','g9'])

            self.matriz.append(['y1','y2','y3','r1','r2','r3','w1','w2','w3','o9','o8','o7' ])
            self.matriz.append(['y4','y5','y6','r4','r5','r6','w4','w5','w6','o6','o5','o4' ])
            self.matriz.append(['y7','y8','y9','r7','r8','r9','w7','w8','w9','o3','o2','o1' ])
            self.matriz.append(['b1','b2','b3'])
            self.matriz.append(['b4','b5','b6'])
            self.matriz.append(['b7','b8','b9'])
        else:
            self.matriz.append(['g','g','g'])
            self.matriz.append(['g','g','g'])
            self.matriz.append(['g','g','g'])

            self.matriz.append(['y','y','y','r','r','r','w','w','w','o','o','o' ])
            self.matriz.append(['y','y','y','r','r','r','w','w','w','o','o','o' ])
            self.matriz.append(['y','y','y','r','r','r','w','w','w','o','o','o' ])
            self.matriz.append(['b','b','b'])
            self.matriz.append(['b','b','b'])
            self.matriz.append(['b','b','b'])

        #define os comandos
        self.cmd = {'right_up':self.right_up,
                     'right_down':self.right_down,\
                     'left_up':self.left_up,\
                     'left_down':self.left_down,\
                     'top_right':self.top_right,\
                     'top_left':self.top_left,\
                     'bottom_right':self.bottom_right,\
                     'bottom_left':self.bottom_left,\
                     'front_clockwise':self.front_clockwise,\
                     'front_anti_clockwise':self.front_anti_clockwise,\
                     'behind_clockwise':self.behind_clockwise,\
                     'behind_anti_clockwise':self.behind_anti_clockwise}
        #registra os lados
        self.base_color = self.matriz[4][4]
        self.left_color = self.matriz[4][1]
        self.right_color = self.matriz[4][7]
        self.top_color = self.matriz[1][1]
        self.bottom_color = self.matriz[7][1]
        self.behind_color = self.matriz[4][10]

    def __str__(self):
        ret = ''
        for idx, line in enumerate(self.matriz):
            line_str = ''
            for element in line:
                line_str += '\t{0}'.format(element)
            if idx in (0,1,2,6,7,8):
                ret += '\t\t\t{0}\n'.format(line_str)
            else:
                ret += '{0}\n'.format(line_str)
        return ret

    def right_up(self):
        '''
        Gira coluna da direita para cima

        >>> Cube(True).right_up()
        [['g1', 'g2', 'r3'], \
['g4', 'g5', 'r6'], \
['g7', 'g8', 'r9'], \
['y1', 'y2', 'y3', 'r1', 'r2', 'b3', 'w7', 'w4', 'w1', 'g9', 'o8', 'o7'], \
['y4', 'y5', 'y6', 'r4', 'r5', 'b6', 'w8', 'w5', 'w2', 'g6', 'o5', 'o4'], \
['y7', 'y8', 'y9', 'r7', 'r8', 'b9', 'w9', 'w6', 'w3', 'g3', 'o2', 'o1'], \
['b1', 'b2', 'o3'], \
['b4', 'b5', 'o6'], \
['b7', 'b8', 'o9']]
        '''
        self.matriz[0][2],self.matriz[1][2],self.matriz[2][2],\
        self.matriz[3][5],self.matriz[4][5],self.matriz[5][5],\
        self.matriz[6][2],self.matriz[7][2],self.matriz[8][2],\
        self.matriz[3][9],self.matriz[4][9],self.matriz[5][9] = \
        self.matriz[3][5],self.matriz[4][5],self.matriz[5][5],\
        self.matriz[6][2],self.matriz[7][2],self.matriz[8][2],\
        self.matriz[5][9],self.matriz[4][9],self.matriz[3][9],\
        self.matriz[2][2],self.matriz[1][2],self.matriz[0][2]

        self.matriz[3][6],self.matriz[3][7],self.matriz[3][8],\
        self.matriz[4][6],self.matriz[4][8],\
        self.matriz[5][6],self.matriz[5][7],self.matriz[5][8] = \
        self.matriz[5][6],self.matriz[4][6],self.matriz[3][6],\
        self.matriz[5][7],self.matriz[3][7],\
        self.matriz[5][8],self.matriz[4][8],self.matriz[3][8]
        return self.matriz

    def right_down(self):
        '''
        Gira coluna da direita para baixo
        >>> Cube(True).right_down()
        [['g1', 'g2', 'o3'], \
['g4', 'g5', 'o6'], \
['g7', 'g8', 'o9'], \
['y1', 'y2', 'y3', 'r1', 'r2', 'g3', 'w3', 'w6', 'w9', 'b9', 'o8', 'o7'], \
['y4', 'y5', 'y6', 'r4', 'r5', 'g6', 'w2', 'w5', 'w8', 'b6', 'o5', 'o4'], \
['y7', 'y8', 'y9', 'r7', 'r8', 'g9', 'w1', 'w4', 'w7', 'b3', 'o2', 'o1'], \
['b1', 'b2', 'r3'], \
['b4', 'b5', 'r6'], \
['b7', 'b8', 'r9']]
        '''
        self.matriz[3][5],self.matriz[4][5],self.matriz[5][5],\
        self.matriz[6][2],self.matriz[7][2],self.matriz[8][2],\
        self.matriz[4][9],self.matriz[5][9],self.matriz[3][9],\
        self.matriz[0][2],self.matriz[1][2],self.matriz[2][2] = \
        self.matriz[0][2],self.matriz[1][2],self.matriz[2][2],\
        self.matriz[3][5],self.matriz[4][5],self.matriz[5][5],\
        self.matriz[7][2],self.matriz[6][2],self.matriz[8][2],\
        self.matriz[5][9],self.matriz[4][9],self.matriz[3][9]

        self.matriz[5][6],self.matriz[4][6],self.matriz[3][6],\
        self.matriz[5][7],self.matriz[3][7],\
        self.matriz[5][8],self.matriz[4][8],self.matriz[3][8] =\
        self.matriz[3][6],self.matriz[3][7],self.matriz[3][8],\
        self.matriz[4][6],self.matriz[4][8],\
        self.matriz[5][6],self.matriz[5][7],self.matriz[5][8]
        return self.matriz

    def left_up(self):
        '''
        Gira coluna da esquerda para cima
        
        >>> Cube(True).left_up()
        [['r1', 'g2', 'g3'], \
['r4', 'g5', 'g6'], \
['r7', 'g8', 'g9'], \
['y3', 'y6', 'y9', 'b1', 'r2', 'r3', 'w1', 'w2', 'w3', 'o9', 'o8', 'g7'], \
['y2', 'y5', 'y8', 'b4', 'r5', 'r6', 'w4', 'w5', 'w6', 'o6', 'o5', 'g4'], \
['y1', 'y4', 'y7', 'b7', 'r8', 'r9', 'w7', 'w8', 'w9', 'o3', 'o2', 'g1'], \
['o1', 'b2', 'b3'], \
['o4', 'b5', 'b6'], \
['o7', 'b8', 'b9']]
        '''
        self.matriz[0][0],self.matriz[1][0],self.matriz[2][0],\
        self.matriz[3][3],self.matriz[4][3],self.matriz[5][3],\
        self.matriz[6][0],self.matriz[8][0],self.matriz[7][0],\
        self.matriz[5][11],self.matriz[4][11],self.matriz[3][11] = \
        self.matriz[3][3],self.matriz[4][3],self.matriz[5][3],\
        self.matriz[6][0],self.matriz[7][0],self.matriz[8][0],\
        self.matriz[5][11], self.matriz[3][11],self.matriz[4][11],\
        self.matriz[0][0],self.matriz[1][0],self.matriz[2][0]

        self.matriz[5][0],self.matriz[4][0],self.matriz[3][0],\
        self.matriz[5][1],self.matriz[3][1],\
        self.matriz[5][2],self.matriz[4][2],self.matriz[3][2] =\
        self.matriz[3][0],self.matriz[3][1],self.matriz[3][2],\
        self.matriz[4][0],self.matriz[4][2],\
        self.matriz[5][0],self.matriz[5][1],self.matriz[5][2]
        return self.matriz

    def left_down(self):
        '''
        Gira coluna da esquerda para baixo
        >>> Cube(True).left_down()
        [['o1', 'g2', 'g3'], \
['o4', 'g5', 'g6'], \
['o7', 'g8', 'g9'], \
['y7', 'y4', 'y1', 'g1', 'r2', 'r3', 'w1', 'w2', 'w3', 'o9', 'o8', 'b7'], \
['y8', 'y5', 'y2', 'g4', 'r5', 'r6', 'w4', 'w5', 'w6', 'o6', 'o5', 'b4'], \
['y9', 'y6', 'y3', 'g7', 'r8', 'r9', 'w7', 'w8', 'w9', 'o3', 'o2', 'b1'], \
['r1', 'b2', 'b3'], \
['r4', 'b5', 'b6'], \
['r7', 'b8', 'b9']]
        '''
        self.matriz[3][3],self.matriz[4][3],self.matriz[5][3],\
        self.matriz[6][0],self.matriz[7][0],self.matriz[8][0],\
        self.matriz[5][11], self.matriz[3][11],self.matriz[4][11],\
        self.matriz[0][0],self.matriz[1][0],self.matriz[2][0] =\
        self.matriz[0][0],self.matriz[1][0],self.matriz[2][0],\
        self.matriz[3][3],self.matriz[4][3],self.matriz[5][3],\
        self.matriz[6][0],self.matriz[8][0],self.matriz[7][0],\
        self.matriz[5][11],self.matriz[4][11],self.matriz[3][11]

        self.matriz[3][0],self.matriz[3][1],self.matriz[3][2],\
        self.matriz[4][0],self.matriz[4][2],\
        self.matriz[5][0],self.matriz[5][1],self.matriz[5][2] = \
        self.matriz[5][0],self.matriz[4][0],self.matriz[3][0],\
        self.matriz[5][1],self.matriz[3][1],\
        self.matriz[5][2],self.matriz[4][2],self.matriz[3][2]
        return self.matriz

    def top_right(self):
        '''
        Gira linha superior para direita

        >>> Cube(True).top_right()
        [['g3', 'g6', 'g9'], \
['g2', 'g5', 'g8'], \
['g1', 'g4', 'g7'], \
['o9', 'o8', 'o7', 'y1', 'y2', 'y3', 'r1', 'r2', 'r3', 'w1', 'w2', 'w3'], \
['y4', 'y5', 'y6', 'r4', 'r5', 'r6', 'w4', 'w5', 'w6', 'o6', 'o5', 'o4'], \
['y7', 'y8', 'y9', 'r7', 'r8', 'r9', 'w7', 'w8', 'w9', 'o3', 'o2', 'o1'], \
['b1', 'b2', 'b3'], \
['b4', 'b5', 'b6'], \
['b7', 'b8', 'b9']]
        '''
        self.matriz[3][:3],self.matriz[3][-9:] = self.matriz[3][9:],self.matriz[3][:9]

        self.matriz[2][0],self.matriz[1][0],self.matriz[0][0],\
        self.matriz[2][1],self.matriz[0][1],\
        self.matriz[2][2],self.matriz[1][2],self.matriz[0][2] =\
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[1][0],self.matriz[1][2],\
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2]
        return self.matriz

    def top_left(self):
        '''
        Gira linha superior para esquerda

        >>> Cube(True).top_left()
        [['g7', 'g4', 'g1'], \
['g8', 'g5', 'g2'], \
['g9', 'g6', 'g3'], \
['r1', 'r2', 'r3', 'w1', 'w2', 'w3', 'o9', 'o8', 'o7', 'y1', 'y2', 'y3'], \
['y4', 'y5', 'y6', 'r4', 'r5', 'r6', 'w4', 'w5', 'w6', 'o6', 'o5', 'o4'], \
['y7', 'y8', 'y9', 'r7', 'r8', 'r9', 'w7', 'w8', 'w9', 'o3', 'o2', 'o1'], \
['b1', 'b2', 'b3'], \
['b4', 'b5', 'b6'], \
['b7', 'b8', 'b9']]

        '''   
        self.matriz[3][9:],self.matriz[3][:9] = self.matriz[3][:3],self.matriz[3][-9:]
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[1][0],self.matriz[1][2],\
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2] = \
        self.matriz[2][0],self.matriz[1][0],self.matriz[0][0],\
        self.matriz[2][1],self.matriz[0][1],\
        self.matriz[2][2],self.matriz[1][2],self.matriz[0][2]
        return self.matriz

    def bottom_right(self):
        '''
        Gira linha inferior para esquerda

        >>> Cube(True).bottom_right()
        [['g1', 'g2', 'g3'], \
['g4', 'g5', 'g6'], \
['g7', 'g8', 'g9'], \
['y1', 'y2', 'y3', 'r1', 'r2', 'r3', 'w1', 'w2', 'w3', 'o9', 'o8', 'o7'], \
['y4', 'y5', 'y6', 'r4', 'r5', 'r6', 'w4', 'w5', 'w6', 'o6', 'o5', 'o4'], \
['o3', 'o2', 'o1', 'y7', 'y8', 'y9', 'r7', 'r8', 'r9', 'w7', 'w8', 'w9'], \
['b7', 'b4', 'b1'], \
['b8', 'b5', 'b2'], \
['b9', 'b6', 'b3']]
        '''
        self.matriz[5][:3],self.matriz[5][-9:] = self.matriz[5][9:],self.matriz[5][:9]

        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2],\
        self.matriz[7][0],self.matriz[7][2],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2] = \
        self.matriz[8][0],self.matriz[7][0],self.matriz[6][0],\
        self.matriz[8][1],self.matriz[6][1],\
        self.matriz[8][2],self.matriz[7][2],self.matriz[6][2]
        return self.matriz

    def bottom_left(self):
        '''
        Gira linha inferior para direita
        >>> Cube(True).bottom_left()
        [['g1', 'g2', 'g3'], \
['g4', 'g5', 'g6'], \
['g7', 'g8', 'g9'], \
['y1', 'y2', 'y3', 'r1', 'r2', 'r3', 'w1', 'w2', 'w3', 'o9', 'o8', 'o7'], \
['y4', 'y5', 'y6', 'r4', 'r5', 'r6', 'w4', 'w5', 'w6', 'o6', 'o5', 'o4'], \
['r7', 'r8', 'r9', 'w7', 'w8', 'w9', 'o3', 'o2', 'o1', 'y7', 'y8', 'y9'], \
['b3', 'b6', 'b9'], \
['b2', 'b5', 'b8'], \
['b1', 'b4', 'b7']]
        '''
        self.matriz[5][9:],self.matriz[5][:9] = self.matriz[5][:3],self.matriz[5][-9:]

        self.matriz[8][0],self.matriz[7][0],self.matriz[6][0],\
        self.matriz[8][1],self.matriz[6][1],\
        self.matriz[8][2],self.matriz[7][2],self.matriz[6][2] =\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2],\
        self.matriz[7][0],self.matriz[7][2],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2]
        return self.matriz

    def front_clockwise(self):
        '''
        Gira a face da frente sentido horário

        >>> Cube(True).front_clockwise()
        [['g1', 'g2', 'g3'], \
['g4', 'g5', 'g6'], \
['y9', 'y6', 'y3'], \
['y1', 'y2', 'b1', 'r7', 'r4', 'r1', 'g7', 'w2', 'w3', 'o9', 'o8', 'o7'], \
['y4', 'y5', 'b2', 'r8', 'r5', 'r2', 'g8', 'w5', 'w6', 'o6', 'o5', 'o4'], \
['y7', 'y8', 'b3', 'r9', 'r6', 'r3', 'g9', 'w8', 'w9', 'o3', 'o2', 'o1'], \
['w7', 'w4', 'w1'], \
['b4', 'b5', 'b6'], \
['b7', 'b8', 'b9']]
        
        '''
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2],\
        self.matriz[3][6],self.matriz[4][6],self.matriz[5][6],\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2],\
        self.matriz[3][2],self.matriz[4][2],self.matriz[5][2] = \
        self.matriz[5][2],self.matriz[4][2],self.matriz[3][2],\
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2],\
        self.matriz[5][6],self.matriz[4][6],self.matriz[3][6],\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2]

        self.matriz[3][3],self.matriz[3][4],self.matriz[3][5],\
        self.matriz[4][3],self.matriz[4][5],\
        self.matriz[5][3],self.matriz[5][4],self.matriz[5][5] = \
        self.matriz[5][3],self.matriz[4][3],self.matriz[3][3],\
        self.matriz[5][4],self.matriz[3][4],\
        self.matriz[5][5],self.matriz[4][5],self.matriz[3][5]
        return self.matriz

    def front_anti_clockwise(self):
        '''
        Gira a face da frente sentido anti-horário
        >>> Cube(True).front_anti_clockwise()
        [['g1', 'g2', 'g3'], \
['g4', 'g5', 'g6'], \
['w1', 'w4', 'w7'], \
['y1', 'y2', 'g9', 'r3', 'r6', 'r9', 'b3', 'w2', 'w3', 'o9', 'o8', 'o7'], \
['y4', 'y5', 'g8', 'r2', 'r5', 'r8', 'b2', 'w5', 'w6', 'o6', 'o5', 'o4'], \
['y7', 'y8', 'g7', 'r1', 'r4', 'r7', 'b1', 'w8', 'w9', 'o3', 'o2', 'o1'], \
['y3', 'y6', 'y9'], \
['b4', 'b5', 'b6'], \
['b7', 'b8', 'b9']]
        '''
        self.matriz[3][2],self.matriz[4][2],self.matriz[5][2],\
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2],\
        self.matriz[3][6],self.matriz[4][6],self.matriz[5][6],\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2] = \
        self.matriz[2][2],self.matriz[2][1],self.matriz[2][0],\
        self.matriz[3][6],self.matriz[4][6],self.matriz[5][6],\
        self.matriz[6][2],self.matriz[6][1],self.matriz[6][0],\
        self.matriz[3][2],self.matriz[4][2],self.matriz[5][2]

        self.matriz[5][3],self.matriz[4][3],self.matriz[3][3],\
        self.matriz[5][4],self.matriz[3][4],\
        self.matriz[5][5],self.matriz[4][5],self.matriz[3][5]=\
        self.matriz[3][3],self.matriz[3][4],self.matriz[3][5],\
        self.matriz[4][3],self.matriz[4][5],\
        self.matriz[5][3],self.matriz[5][4],self.matriz[5][5]
        return self.matriz

    def behind_clockwise(self):
        '''
        Gira a face da trás sentido horário
        >>> Cube(True).behind_clockwise()
        [['y7', 'y4', 'y1'], \
['g4', 'g5', 'g6'], \
['g7', 'g8', 'g9'], \
['b7', 'y2', 'y3', 'r1', 'r2', 'r3', 'w1', 'w2', 'g1', 'o7', 'o4', 'o1'], \
['b8', 'y5', 'y6', 'r4', 'r5', 'r6', 'w4', 'w5', 'g2', 'o8', 'o5', 'o2'], \
['b9', 'y8', 'y9', 'r7', 'r8', 'r9', 'w7', 'w8', 'g3', 'o9', 'o6', 'o3'], \
['b1', 'b2', 'b3'], \
['b4', 'b5', 'b6'], \
['w9', 'w6', 'w3']]
        '''
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[3][8],self.matriz[4][8],self.matriz[5][8],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2],\
        self.matriz[3][0],self.matriz[4][0],self.matriz[5][0] = \
        self.matriz[5][0],self.matriz[4][0],self.matriz[3][0],\
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[5][8],self.matriz[4][8],self.matriz[3][8],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2]
        
        self.matriz[5][9],self.matriz[4][9],self.matriz[3][9],\
        self.matriz[5][10],self.matriz[3][10],\
        self.matriz[5][11],self.matriz[4][11],self.matriz[3][11] =\
        self.matriz[3][9],self.matriz[3][10],self.matriz[3][11],\
        self.matriz[4][9],self.matriz[4][11],\
        self.matriz[5][9],self.matriz[5][10],self.matriz[5][11]
        return self.matriz

    def behind_anti_clockwise(self):
        '''
        Gira a face da trás sentido anti-horário
        >>> Cube(True).behind_anti_clockwise()
        [['w3', 'w6', 'w9'], \
['g4', 'g5', 'g6'], \
['g7', 'g8', 'g9'], \
['g3', 'y2', 'y3', 'r1', 'r2', 'r3', 'w1', 'w2', 'b9', 'o3', 'o6', 'o9'], \
['g2', 'y5', 'y6', 'r4', 'r5', 'r6', 'w4', 'w5', 'b8', 'o2', 'o5', 'o8'], \
['g1', 'y8', 'y9', 'r7', 'r8', 'r9', 'w7', 'w8', 'b7', 'o1', 'o4', 'o7'], \
['b1', 'b2', 'b3'], \
['b4', 'b5', 'b6'], \
['y1', 'y4', 'y7']]
        '''
        self.matriz[3][0],self.matriz[4][0],self.matriz[5][0],\
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[3][8],self.matriz[4][8],self.matriz[5][8],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2] =\
        self.matriz[0][2],self.matriz[0][1],self.matriz[0][0],\
        self.matriz[3][8],self.matriz[4][8],self.matriz[5][8],\
        self.matriz[8][2],self.matriz[8][1],self.matriz[8][0],\
        self.matriz[3][0],self.matriz[4][0],self.matriz[5][0]
        
        self.matriz[3][9],self.matriz[3][10],self.matriz[3][11],\
        self.matriz[4][9],self.matriz[4][11],\
        self.matriz[5][9],self.matriz[5][10],self.matriz[5][11] =\
        self.matriz[5][9],self.matriz[4][9],self.matriz[3][9],\
        self.matriz[5][10],self.matriz[3][10],\
        self.matriz[5][11],self.matriz[4][11],self.matriz[3][11]
        return self.matriz
        

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        print 'Testes:\n' ,doctest.testmod()