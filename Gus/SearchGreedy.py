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
from Cell import *
from Piece import *
from Node import *
from priorityQueue import *

        

def checkEmpty(cell):
    return not cell.isOccupied()

def checkAllVisited(Map):
    for column in Map:
        for i in range(Map[0]):
            if type(column[i]) == Node:
                if not Node.isvisited():
                    return False
    return True
            

def singleGreedy(piece, board, goals):
    final_path = []
    final_path.append((piece.getQ(), piece.getR()))
    
    # create a temporate map
    q, r = 7, 7;
    Map = [[0 for x in range(q)] for y in range(r)] 
    for i in range(0,7):
        for j in range(0,7):
            if 3 <= (i+j) < 10:
                Map[i][j] = Node(i-3, j-3)
            else:
                Map[i][j] = nonValidNode()
                
    # initialise the root
    startNode = Map[piece.getQ() +3][piece.getR() +3]
    startNode.visit(piece.getQ(), piece.getR())
    
    # initialiase the root to the priority Queue
    queue = priorityQueue()
    queue.insert(0, startNode)
    
    #insert everything to the priority queue
    startNodes =[startNode]
    endNodes = []
    startCost = 1
    
    while not checkAllVisited(Map):
        for node in startNodes:
            qloc = node.q
            rloc = node.r
            
            
            #visit left
            #check for existence of node
            if type(Map[qloc+2][rloc+3]) == Node and not Map[qloc+2][rloc+3].isVisited():
                Map[qloc+2][rloc+3].visit(qloc, rloc)
                
                # if there is a piece or block in the cell, check for jump
                if board[qloc+2][rloc+3].isOccupied():
                    if type(Map[qloc+1][rloc+3]) == Node and not Map[qloc+1][rloc+3].isVisited():
                        Map[qloc+1][rloc+3].visit(qloc, rloc)
                        #check for the block or piece
                        if not board[qloc+1][rloc+3].isOccupied():
                            queue.insert(startCost, Map[qloc+1][rloc+3])
                            
                # if thers is not piece or block in the cell
                else:
                    queue.insert(startCost, Map[qloc+2][rloc+3])
            
            #visit top left
            #need to check whether it is out out range
            
            #vist top right
            
            #vist right
            
            #visit bottom right
            
            #visit bottom left
        
        
        
    
    
    
    return final_path