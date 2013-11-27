# -*- coding: utf-8 -*-

from cube import Cube
import random

'''
Trabalho de complexidade de algoritmos
Resolver o cubo mágico 
'''
options =  ['right_up', 'right_down', \
            'left_up', 'left_down', \
            'top_right', 'top_left', \
            'bottom_right', 'bottom_left', \
            'front_clockwise', 'front_anti_clockwise', \
            'behind_clockwise', 'behind_anti_clockwise' ]

reverse = {'right_up':'right_down',\
            'right_down':'right_up',\
            'left_up':'left_down',\
            'left_down':'left_up',\
            'top_right':'top_left', \
            'top_left':'top_right',\
            'bottom_right':'bottom_left',\
            'bottom_left':'bottom_right',\
            'front_clockwise':'front_anti_clockwise',\
            'front_anti_clockwise':'front_clockwise',\
            'behind_clockwise':'behind_anti_clockwise',\
            'behind_anti_clockwise':'behind_clockwise'}

def new_cube_clean():
    '''
    Retorna o cubo montado de forma correta
    '''
    return Cube()

def shuffle_cube(cube):
    '''
    Embaralha o cubo tracando as faces
    '''
    random.shuffle(options)
    for cmd in options:
        cube.command(cmd)

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

def backtraking_step_one(cube, level = 0, best_rate = 0):
    #avalia o estado atual do cubo
    local_rate = evaluation_step_one(cube)
    #Resultado encontrado
    if local_rate == 4:
        return True
    #Melhor resultado zera os niveis de atuação
    if local_rate > best_rate:
        level = 0
        best_rate = local_rate

    #Não melhorou a pontuação em 4 niveis Aborta
    if level == 4 and local_rate < best_rate:
        return False
    #incrementa o nivel
    level += 1
    #Verifica se não atingiu o ultimo nivel (sétimo)
    if level < 7:
        #randomiza a sequencia de operações
        random.shuffle(options)
        for cmd in options:
            #executa a alteração
            cube.command(cmd)
            #chama o backtraking e avalia o resultado
            if backtraking_step_one(cube, level, best_rate):#,rate, level, live):
                return True 
            #desfazo a alteração no cubo
            cube.command(reverse[cmd])
    return False

def backtraking_step_two(cube, level = 0, best_rate = 0):
    #Avalia os passos anteriores
    step_1 = evaluation_step_one(cube)
    #Caso já está no 4 nivel sem melhorar aborta
    if step_1 < 4 and level == 4:
        return False

    #avalia o estado atual do cubo
    local_rate = evaluation_step_two(cube)
    
    #Resultado encontrado
    if local_rate == 4 == step_1:
        return True
    #Melhor resultado zera os niveis de atuação
    if local_rate > best_rate:
        level = 0
        best_rate = local_rate

    #Não melhorou a pontuação em 4 niveis Aborta
    if level == 4 and local_rate < best_rate:
        return False
    #incrementa o nivel
    level += 1
    #Verifica se não atingiu o ultimo nivel (sétimo)
    if level < 7:
        #randomiza a sequencia de operações
        random.shuffle(options)
        for cmd in options:
            #executa a alteração
            cube.command(cmd)
            #chama o backtraking e avalia o resultado
            if backtraking_step_two(cube, level, best_rate):#,rate, level, live):
                return True 
            #desfazo a alteração no cubo
            cube.command(reverse[cmd])
    return False

#def first_nivel():
c = new_cube_clean()  
print c
shuffle_cube(c)
print c
#c.command('right_up')
print backtraking_step_one(c)
print c
print backtraking_step_two(c)
print c

#print evaluation_step_one(c)
#print evaluation_step_two(c)
#print evaluation_step_three(c)
#print evaluation_step_four(c)
#print evaluation_step_five(c)