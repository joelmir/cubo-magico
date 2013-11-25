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
    options = [ 'right_up', 'right_down', \
        'left_up', 'left_down', \
        'top_right', 'top_left', \
        'bottom_right', 'bottom_left', \
        'front_clockwise', 'front_anti_clockwise', \
        'behind_clockwise', 'behind_anti_clockwise' ]
    cube.command(options[0])

def evaluation_step_one(cube):
    '''
    Avalia o X ( primeira fase )
    '''
    rate = 0
    if cube.matriz[3][4] == cube.base_color and cube.matriz[2][1] == cube.top_color:
        rate += 1
    if cube.matriz[4][3] == cube.base_color and cube.matriz[4][2] == cube.left_color:
        rate += 1
    if cube.matriz[4][5] == cube.base_color and cube.matriz[4][6] == cube.right_color:
        rate += 1
    if cube.matriz[5][4] == cube.base_color and cube.matriz[6][1] == cube.bottom_color:
        rate += 1
    if rate == 4:
        print 'Step 1 OK!'
    return rate

def evaluation_step_two(cube):
    '''
    Avalia os cantos ( segunda fase )
    '''
    rate = 0
    if cube.matriz[3][3] == cube.base_color and \
        cube.matriz[2][0] == cube.top_color and \
        cube.matriz[3][2] == cube.left_color:
        rate += 1
    if cube.matriz[3][5] == cube.base_color and \
        cube.matriz[2][2] == cube.top_color and \
        cube.matriz[3][6] == cube.right_color:
        rate += 1

    if cube.matriz[5][3] == cube.base_color and \
        cube.matriz[6][0] == cube.bottom_color and \
        cube.matriz[5][2] == cube.left_color:
        rate += 1
    if cube.matriz[5][5] == cube.base_color and \
        cube.matriz[6][2] == cube.bottom_color and \
        cube.matriz[5][6] == cube.right_color:
        rate += 1
    if rate == 4:
        print 'Step 2 OK!'
    return rate

def evaluation_step_three(cube):
    '''
    Avalia o meio do cubo ( terceira fase )
    '''
    rate = 0
    if cube.matriz[3][1] == cube.left_color and \
        cube.matriz[1][0] == cube.top_color:
        rate += 1
    if cube.matriz[3][7] == cube.right_color and \
        cube.matriz[1][2] == cube.top_color:
        rate += 1
    if cube.matriz[5][1] == cube.left_color and \
        cube.matriz[7][0] == cube.bottom_color:
        rate += 1
    if cube.matriz[5][7] == cube.right_color and \
        cube.matriz[7][2] == cube.bottom_color:
        rate += 1
    if rate == 4:
        print 'Step 3 OK!'
    return rate

def evaluation_step_four(cube):
    '''
    Avalia a cruz superior ( quarta fase )
    '''
    rate = 0
    if cube.matriz[3][10] == cube.behind_color and cube.matriz[0][1] == cube.top_color:
        rate += 1
    if cube.matriz[4][11] == cube.behind_color and cube.matriz[4][0] == cube.left_color:
        rate += 1
    if cube.matriz[4][9] == cube.behind_color and cube.matriz[4][8] == cube.right_color:
        rate += 1
    if cube.matriz[5][10] == cube.behind_color and cube.matriz[8][1] == cube.bottom_color:
        rate += 1
    if rate == 4:
        print 'Step 4 OK!'
    return rate

def evaluation_step_five(cube):
    '''
    Avalia os cantos superior ( quinta fase )
    '''
    rate = 0
    if cube.matriz[3][11] == cube.behind_color and \
        cube.matriz[0][0] == cube.top_color and \
        cube.matriz[3][0] == cube.left_color:
        rate += 1
    if cube.matriz[3][9] == cube.behind_color and \
        cube.matriz[0][2] == cube.top_color and \
        cube.matriz[3][8] == cube.right_color:
        rate += 1

    if cube.matriz[5][11] == cube.behind_color and \
        cube.matriz[8][0] == cube.bottom_color and \
        cube.matriz[5][0] == cube.left_color:
        rate += 1
    if cube.matriz[5][9] == cube.behind_color and \
        cube.matriz[8][2] == cube.bottom_color and \
        cube.matriz[5][8] == cube.right_color:
        rate += 1
    if rate == 4:
        print 'Step 5 OK!'
    return rate

#def first_nivel():
c = new_cube_clean()  
print c
print evaluation_step_one(c)
print evaluation_step_two(c)
print evaluation_step_three(c)
print evaluation_step_four(c)
print evaluation_step_five(c)