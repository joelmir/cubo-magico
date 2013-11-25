# -*- coding: utf-8 -*-

class Cube(object):
    '''
    Monta o cubo com 6 faces montadas
    '''
    def command(self, cmd):
        self.cmd[cmd]()

    def __init__(self):
        '''
        Inicializa o Cubo com as face Montadas

        teste de incilização completa
        >>> Cube().matriz
        [['g', 'g', 'g'], \
['g', 'g', 'g'], \
['g', 'g', 'g'], \
['y', 'y', 'y', 'r', 'r', 'r', 'w', 'w', 'w', 'o', 'o', 'o'], \
['y', 'y', 'y', 'r', 'r', 'r', 'w', 'w', 'w', 'o', 'o', 'o'], \
['y', 'y', 'y', 'r', 'r', 'r', 'w', 'w', 'w', 'o', 'o', 'o'], \
['b', 'b', 'b'], \
['b', 'b', 'b'], \
['b', 'b', 'b']]'''

        self.matriz = []
        '''
        inicializa as faces com as cores
        '''
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
        '''
        self.matriz[0][2],self.matriz[1][2],self.matriz[2][2],\
        self.matriz[3][5],self.matriz[4][5],self.matriz[5][5],\
        self.matriz[6][2],self.matriz[7][2],self.matriz[8][2],\
        self.matriz[3][9],self.matriz[4][9],self.matriz[5][9] = \
        self.matriz[3][5],self.matriz[4][5],self.matriz[5][5],\
        self.matriz[6][2],self.matriz[7][2],self.matriz[8][2],\
        self.matriz[4][9],self.matriz[5][9],self.matriz[3][9],\
        self.matriz[0][2],self.matriz[1][2],self.matriz[2][2]

        self.matriz[3][6],self.matriz[3][7],self.matriz[3][8],\
        self.matriz[4][6],self.matriz[4][8],\
        self.matriz[5][6],self.matriz[5][7],self.matriz[5][8] = \
        self.matriz[5][6],self.matriz[4][6],self.matriz[3][6],\
        self.matriz[5][7],self.matriz[3][7],\
        self.matriz[5][8],self.matriz[4][8],self.matriz[3][8]

    def right_down(self):
        '''
        Gira coluna da direita para baixo
        '''
        self.matriz[3][5],self.matriz[4][5],self.matriz[5][5],\
        self.matriz[6][2],self.matriz[7][2],self.matriz[8][2],\
        self.matriz[4][9],self.matriz[5][9],self.matriz[3][9],\
        self.matriz[0][2],self.matriz[1][2],self.matriz[2][2] = \
        self.matriz[0][2],self.matriz[1][2],self.matriz[2][2],\
        self.matriz[3][5],self.matriz[4][5],self.matriz[5][5],\
        self.matriz[6][2],self.matriz[7][2],self.matriz[8][2],\
        self.matriz[3][9],self.matriz[4][9],self.matriz[5][9]

        self.matriz[5][6],self.matriz[4][6],self.matriz[3][6],\
        self.matriz[5][7],self.matriz[3][7],\
        self.matriz[5][8],self.matriz[4][8],self.matriz[3][8] =\
        self.matriz[3][6],self.matriz[3][7],self.matriz[3][8],\
        self.matriz[4][6],self.matriz[4][8],\
        self.matriz[5][6],self.matriz[5][7],self.matriz[5][8]

    def left_up(self):
        '''
        Gira coluna da esquerda para cima
        '''
        self.matriz[0][0],self.matriz[1][0],self.matriz[2][0],\
        self.matriz[3][3],self.matriz[4][3],self.matriz[5][3],\
        self.matriz[6][0],self.matriz[7][0],self.matriz[8][0],\
        self.matriz[3][11],self.matriz[4][11],self.matriz[5][11] = \
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

    def left_down(self):
        '''
        Gira coluna da esquerda para baixo
        '''
        self.matriz[3][3],self.matriz[4][3],self.matriz[5][3],\
        self.matriz[6][0],self.matriz[7][0],self.matriz[8][0],\
        self.matriz[5][11], self.matriz[3][11],self.matriz[4][11],\
        self.matriz[0][0],self.matriz[1][0],self.matriz[2][0] = \
        self.matriz[0][0],self.matriz[1][0],self.matriz[2][0],\
        self.matriz[3][3],self.matriz[4][3],self.matriz[5][3],\
        self.matriz[6][0],self.matriz[7][0],self.matriz[8][0],\
        self.matriz[3][11],self.matriz[4][11],self.matriz[5][11]

        self.matriz[3][0],self.matriz[3][1],self.matriz[3][2],\
        self.matriz[4][0],self.matriz[4][2],\
        self.matriz[5][0],self.matriz[5][1],self.matriz[5][2] = \
        self.matriz[5][0],self.matriz[4][0],self.matriz[3][0],\
        self.matriz[5][1],self.matriz[3][1],\
        self.matriz[5][2],self.matriz[4][2],self.matriz[3][2]

    def top_right(self):
        '''
        Gira linha superior para direita
        '''
        self.matriz[3][:3],self.matriz[3][-9:] = self.matriz[3][9:],self.matriz[3][:9]

        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[1][0],self.matriz[1][2],\
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2] = \
        self.matriz[2][0],self.matriz[1][0],self.matriz[0][0],\
        self.matriz[2][1],self.matriz[0][1],\
        self.matriz[2][2],self.matriz[1][2],self.matriz[0][2]

    def top_left(self):
        '''
        Gira linha superior para esquerda
        '''
        self.matriz[3][9:],self.matriz[3][:9] = self.matriz[3][:3],self.matriz[3][-9:]

        self.matriz[2][0],self.matriz[1][0],self.matriz[0][0],\
        self.matriz[2][1],self.matriz[0][1],\
        self.matriz[2][2],self.matriz[1][2],self.matriz[0][2] =\
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[1][0],self.matriz[1][2],\
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2]

    def bottom_right(self):
        '''
        Gira linha inferior para direita
        '''
        self.matriz[5][9:],self.matriz[5][:9] = self.matriz[5][:3],self.matriz[5][-9:]

        self.matriz[8][0],self.matriz[7][0],self.matriz[6][0],\
        self.matriz[8][1],self.matriz[6][1],\
        self.matriz[8][2],self.matriz[7][2],self.matriz[6][2] =\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2],\
        self.matriz[7][0],self.matriz[7][2],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2]

    def bottom_left(self):
        '''
        Gira linha inferior para esquerda
        '''
        self.matriz[5][:3],self.matriz[5][-9:] = self.matriz[5][9:],self.matriz[5][:9]

        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2],\
        self.matriz[7][0],self.matriz[7][2],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2] = \
        self.matriz[8][0],self.matriz[7][0],self.matriz[6][0],\
        self.matriz[8][1],self.matriz[6][1],\
        self.matriz[8][2],self.matriz[7][2],self.matriz[6][2]

    def front_clockwise(self):
        '''
        Gira a face da frente sentido horário
        '''
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2],\
        self.matriz[3][6],self.matriz[4][6],self.matriz[5][6],\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2],\
        self.matriz[3][2],self.matriz[4][2],self.matriz[5][2] = \
        self.matriz[3][2],self.matriz[4][2],self.matriz[5][2],\
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2],\
        self.matriz[3][6],self.matriz[4][6],self.matriz[5][6],\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2]

        self.matriz[3][3],self.matriz[3][4],self.matriz[3][5],\
        self.matriz[4][3],self.matriz[4][5],\
        self.matriz[5][3],self.matriz[5][4],self.matriz[5][5] = \
        self.matriz[5][3],self.matriz[4][3],self.matriz[3][3],\
        self.matriz[5][4],self.matriz[3][4],\
        self.matriz[5][5],self.matriz[4][5],self.matriz[3][5]

    def front_anti_clockwise(self):
        '''
        Gira a face da frente sentido anti-horário
        '''
        self.matriz[3][2],self.matriz[4][2],self.matriz[5][2],\
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2],\
        self.matriz[3][6],self.matriz[4][6],self.matriz[5][6],\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2] = \
        self.matriz[2][0],self.matriz[2][1],self.matriz[2][2],\
        self.matriz[3][6],self.matriz[4][6],self.matriz[5][6],\
        self.matriz[6][0],self.matriz[6][1],self.matriz[6][2],\
        self.matriz[3][2],self.matriz[4][2],self.matriz[5][2]

        self.matriz[5][3],self.matriz[4][3],self.matriz[3][3],\
        self.matriz[5][4],self.matriz[3][4],\
        self.matriz[5][5],self.matriz[4][5],self.matriz[3][5]=\
        self.matriz[3][3],self.matriz[3][4],self.matriz[3][5],\
        self.matriz[4][3],self.matriz[4][5],\
        self.matriz[5][3],self.matriz[5][4],self.matriz[5][5]

    def behind_clockwise(self):
        '''
        Gira a face da trás sentido horário
        '''
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[3][8],self.matriz[4][8],self.matriz[5][8],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2],\
        self.matriz[3][0],self.matriz[4][0],self.matriz[5][0] = \
        self.matriz[3][0],self.matriz[4][0],self.matriz[5][0],\
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[3][8],self.matriz[4][8],self.matriz[5][8],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2]
        
        self.matriz[5][9],self.matriz[4][9],self.matriz[3][9],\
        self.matriz[5][10],self.matriz[3][10],\
        self.matriz[5][11],self.matriz[4][11],self.matriz[3][11] =\
        self.matriz[3][9],self.matriz[3][10],self.matriz[3][11],\
        self.matriz[4][9],self.matriz[4][11],\
        self.matriz[5][9],self.matriz[5][10],self.matriz[5][11]

    def behind_anti_clockwise(self):
        '''
        Gira a face da trás sentido anti-horário
        '''
        self.matriz[3][0],self.matriz[4][0],self.matriz[5][0],\
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[3][8],self.matriz[4][8],self.matriz[5][8],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2] =\
        self.matriz[0][0],self.matriz[0][1],self.matriz[0][2],\
        self.matriz[3][8],self.matriz[4][8],self.matriz[5][8],\
        self.matriz[8][0],self.matriz[8][1],self.matriz[8][2],\
        self.matriz[3][0],self.matriz[4][0],self.matriz[5][0]
        
        self.matriz[3][9],self.matriz[3][10],self.matriz[3][11],\
        self.matriz[4][9],self.matriz[4][11],\
        self.matriz[5][9],self.matriz[5][10],self.matriz[5][11] =\
        self.matriz[5][9],self.matriz[4][9],self.matriz[3][9],\
        self.matriz[5][10],self.matriz[3][10],\
        self.matriz[5][11],self.matriz[4][11],self.matriz[3][11]
        

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        print 'Testes:\n' ,doctest.testmod()