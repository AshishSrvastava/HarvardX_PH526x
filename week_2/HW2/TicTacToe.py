import numpy as np
import random
import matplotlib.pyplot as plt
import time

#Defining board. A 3x3 matrix with all 0s (empty values)
def create_board():
    return np.zeros((3,3))

#Defining place(board, player, position) and using create_board() functions, where player is either 1 or 2 and acts as a marker
#Position is a tuple of length 2, dictating the position in the board (a 3x3 matrix). This function only allows the current 
#player to place a marker at a spot at the board if it is empty (has a 0 there)
#create_board() stores a board as 'board' 
board = create_board()
def place(board, player, position):
    #making sure player value is 1 or 2
    if player!=1: 
        if player!=2:
            return ("Error: Player must be 1 or 2")
            pass
        else:
            pass
    #making sure position is correctly inputted
    if type(position)!=tuple:
        return ("Error: Position must be a tuple of the form (x,y)")
        pass
    else:
        if len(position)!=2:
            return ("Error: Position can only have two items: (x,y)")
            pass
    
    #Checks if position has a 0 (no marker has been placed there). If no markers, it places the player's
    #marker (a 1 or 2) in that position
    if board[position] == 0:
        board[position]=player
    else:
        return ("Error: Position already marked by a player")
        pass
    return board


#determining which positions are available to the player: a function called possibilities(board), which returns as tuples
#the coordinate pairs on the board that are empty
def possibilities(board):
    empty=np.where(board == 0)
    return list(zip(empty[0], empty[1]))