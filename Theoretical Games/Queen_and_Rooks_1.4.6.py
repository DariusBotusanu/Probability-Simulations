# -*- coding: utf-8 -*-

'''
for a given n 2-> 10, simulates the following game on a (standard) chessboard:

     place randomly a black queen on a square of the chessboard;
     then, place randomly n white rooks on the remaining free squares of the
    chessboard;
     count how many white rooks does the black queen attack;
     count how many white rooks attack the black queen.
'''

import numpy as np

def queen_rooks(rooks_number):
    chessboard = np.reshape(np.arange(0,64), (8,8))
    #we generate the position of the queen
    x_q = np.random.randint(0,8)
    y_q = np.random.randint(0,8)
    queen_pos = (x_q, y_q) #where is the queen placed
    rooks = []
    while len(rooks) < rooks_number:
        #we generate the position of a rook
        x_r = np.random.randint(0,8)
        y_r = np.random.randint(0,8)
        pos = (x_r, y_r)
        if ((pos in rooks) == False & (pos != queen_pos)):
            rooks.append(pos)
    #a queen only vertically, horizontally and diagonally
    rooks_vs_queen = [] #the rooks that attack the queen (and vice versa)
    queen_vs_rooks = [] #the rooks that are attacked by queen (on the diagonals of the queen)
    for pos in rooks:
        if (pos[0] == x_q or pos[1] == y_q):
            rooks_vs_queen.append(pos)
            
    i, j = x_q-1, y_q-1
    #now we check the diagonals
    while((i>=0) & (i<8) & (j>=0) & (j < 8)):
        aux_tuple = (i,j)
        if aux_tuple in rooks:
            queen_vs_rooks.append(aux_tuple)
        i -= 1
        j -= 1
    
    i, j = x_q+1, y_q+1
    while((i>=0) & (i<8) & (j>=0) & (j < 8)):
        aux_tuple = (i,j)
        if aux_tuple in rooks:
            queen_vs_rooks.append(aux_tuple)
        i += 1
        j += 1
        
    i, j = x_q-1, y_q+1
    while((i>=0) & (i<8) & (j>=0) & (j < 8)):
        aux_tuple = (i,j)
        if aux_tuple in rooks:
           queen_vs_rooks.append(aux_tuple)
        i -= 1
        j += 1
    
    i, j = x_q+1, y_q-1
    while((i>=0) & (i<8) & (j>=0) & (j < 8)):
        aux_tuple = (i,j)
        if aux_tuple in rooks:
            queen_vs_rooks.append(aux_tuple)
        i += 1
        j -= 1

    return (np.size(rooks_vs_queen), np.size(queen_vs_rooks)+np.size(rooks_vs_queen))


def simulate_queen_rooks(rooks_number, N):
    rooks_vs_queen = []
    queen_vs_rooks = []
    for i in range(N):
        result = queen_rooks(rooks_number)
        rooks_vs_queen.append(result[0])
        queen_vs_rooks.append(result[1])
    
    avg_rooks_attack = np.mean(rooks_vs_queen)
    avg_queen_attacks = np.mean(queen_vs_rooks)
    print("In {} simulations an average of {} rooks from {} attack the queen".format(N, avg_rooks_attack, rooks_number))
    print("So there is a {} probability that all the rooks attack the queen".format(avg_rooks_attack/rooks_number))
    print("In {} simulations the queen atatcks an average of {} rooks from {}".format(N, avg_queen_attacks, rooks_number))
    print("So there is a {} probability that the queen attacks all the rooks".format(avg_queen_attacks/rooks_number))
 

for i in range(2,11):
    simulate_queen_rooks(i, 20000)
    print("-------------------")
        
            
            
    