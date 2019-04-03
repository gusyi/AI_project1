# 2 component

# SingleGreedy(): For a given piece, search the shortest path to goals
#                 return:  (1) final cost
#                          (2) the path to the goal
#                          (3) responding movement, 1: move,   2: jump

# MapGreedy():  Search the lowest cost, and make the move
#               return: the path to the goal

# check 

# input: List of Cell(broad), list of pieces, goals
# the broad: 2d list


# output: the path to the goal, list of tuples
from Cell import Cell
from Piece import Piece

        

def checkEmpty(cell):
    return not cell.isOccupied()

def singleGreedy(piece, board, goals):
    final_path = []
    final_path.append((piece.getQ(), piece.getR()))
    
    # create a temporate map
    Map =[]
    for i in range(0,7):
        for j in range(0,7):
            if 3 <= (i+j) < 9:
                Map[i][j] = Node(i-3, j-3)
                
    # initialise the root
    Map[piece.getQ() +3][piece.getR() +3].visit(piece.getQ(), piece.getR())
    
    
    
    
    
    return final_path