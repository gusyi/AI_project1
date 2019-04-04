# 2 component

# SingleGreedy(): For a given piece, search the shortest path to goals
#                 return:  (1) final cost
#                          (2) the path to the goal
#                          (3) responding movement, 1: move,   2: jump

# MapGreedy():  Search the lowest cost to the goal for each piece
#               choose the one with highest number of jump
#               if the jump number is same, then choose the shortest one
#               print the path to the goal


# input: List of Cell(broad), list of pieces, goals
# the broad: 2d list


##Test Case for MapGreedy():
"""
q, r = 7, 7;
Board= [[0 for x in range(q)] for y in range(r)] 
for i in range(0,7):
    for j in range(0,7):
        if 3 <= (i+j) < 10:
            Board[i][j] = Cell(i-3, j-3)
        
green_piece = Piece("green", 0, -1)
piece_2 = Piece("green", 1, -3)
piece_3 = Piece("green", 0, -3)
piece_4 = Piece("green", 2, -2)
pieces = [green_piece, piece_2, piece_3, piece_4]
Board[3][2].addPiece(green_piece)
goals = []
goals.append(Node(-3,3))
goals.append(Node(-2,3))
goals.append(Node(-1,3))
goals.append(Node(0,3))
block_1 = Piece("block", -2, 2)
block_2 = Piece("block", -1, 2)
block_3 = Piece("block", 0, 2)
Board[1][5].addPiece(block_1)
Board[2][5].addPiece(block_2)
Board[3][5].addPiece(block_3)
    
MapGreedy(pieces, Board, goals)
"""


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

def checkReachGoal(endNodes, goals):
    for node in endNodes:
        for goal in goals:
            if node.q == goal.q and node.r == goal.r:
                return (True, (goal.q, goal.r))
        
    return (False,(0,0))
            

def singleGreedy(piece, board, goals):
    final_path = []
    
    
    # create a temporate map
    q, r = 7, 7;
    Map = [[0 for x in range(q)] for y in range(r)] 
    for i in range(0,7):
        for j in range(0,7):
            if 3 <= (i+j) < 10:
                Map[i][j] = Node(i-3, j-3)
            else:
                Map[i][j] = nonValidNode()
    #print(Map)
    
    # initialise the root
    startNode = Map[piece.getQ() +3][piece.getR() +3]
    startNode.visit(piece.getQ(), piece.getR())
    
    if startNode.isVisited():
        print("finish the initialisation!")
        print("start from " + str((startNode.q, startNode.r)))
    
    # initialiase the root to the priority Queue
    queue = priorityQueue()
    print("finish the queue creation")
    queue.insert(0, startNode)
    print("finish the queue initialisation")
    
    #insert everything to the priority queue
    startNodes =[startNode]
    endNodes = []
    startCost = 1
    destination = checkReachGoal(endNodes, goals)
    
    #while not checkAllVisited(Map) or not checkReachGoal(endNodes, goals):
    while not destination[0]:
        for node in startNodes:
            qloc = node.q
            rloc = node.r
            print("search from "+str((qloc, rloc)))
            
            
            #visit left
            #check for existence of node
            if qloc-1 > -4 and (rloc + qloc -1) > -4:
                print("to the left")
                
                # check for visited and the occupation
                if not Map[qloc+2][rloc+3].isVisited() and not board[qloc+2][rloc+3].isOccupied():
                    Map[qloc+2][rloc+3].visit(qloc, rloc)
                    queue.insert(startCost, Map[qloc+2][rloc+3])
                    endNodes.append(Map[qloc+2][rloc+3])
                
                # if there is a piece or block in the cell, check for jump
                if board[qloc+2][rloc+3].isOccupied() and (qloc -2 >-4) and (rloc + qloc -2 ) >-4:
                    if type(Map[qloc+1][rloc+3]) == Node and not Map[qloc+1][rloc+3].isVisited():
                        Map[qloc+1][rloc+3].visit(qloc, rloc)
                        #check for the block or piece
                        if not board[qloc+1][rloc+3].isOccupied():
                            queue.insert(startCost, Map[qloc+1][rloc+3])
                            endNodes.append(Map[qloc+1][rloc+3])
                    
            
            #visit top left
            #need to check whether it is out out range
            if rloc -1 >= -3 and ((rloc-1) + qloc > -4):
                print("to the top left")
                if not Map[qloc+3][rloc+2].isVisited() and not board[qloc+3][rloc+2].isOccupied():
                    Map[qloc+3][rloc+2].visit(qloc, rloc)
                    queue.insert(startCost, Map[qloc+3][rloc+2])
                    endNodes.append(Map[qloc+3][rloc+2])
                # if the top left exist:
                # check if occupied, then consider jump:
                if board[qloc+3][rloc+2].isOccupied():
                    # check wether the two pieces away exist：
                    if rloc -2 >= -3 and ((rloc-2) + qloc  > -4) and not Map[qloc+3][rloc+1].isVisited():
                        Map[qloc+3][rloc+1].visit(qloc, rloc)
                        
                        # check if there is a block in the cell:
                        if not board[qloc+3][rloc+1].isOccupied():
                            queue.insert(startCost, Map[qloc+3][rloc+1])
                            endNodes.append(Map[qloc+3][rloc+1])
                    
            
            #vist top right
            if rloc -1 >= -3 and (qloc + 1 < 4) and ((rloc-1) + (qloc+1) > -4):
                print("to the top right")
                if not Map[qloc+4][rloc+2].isVisited() and not board[qloc+4][rloc+2].isOccupied():
                    Map[qloc+4][rloc+2].visit(qloc, rloc)
                    queue.insert(startCost, Map[qloc+4][rloc+2])
                    endNodes.append(Map[qloc+4][rloc+2])
                
                #if the top right exist
                # check for occupation:
                if board[qloc+4][rloc+2].isOccupied():
                    # check whethre the two pieces away exist:
                    if rloc -2 >= -3 and ((rloc -2) + (qloc +2) > -4) and not Map[qloc+5][rloc+1].isVisited():
                        Map[qloc+5][rloc+1].visit(qloc, rloc)
                        
                        #check if ther is a block or piece in the cell:
                        if not board[qloc+5][rloc+1].isOccupied():
                            queue.insert(startCost, Map[qloc+5][rloc+1])
                            endNodes.append(Map[qloc+5][rloc+1])
                    
                    
            
            #vist right
            
            #means the rloc exsit, need to check the qloc is in the range or not
            if (qloc + 1) <= 3  and (rloc + (qloc+1) < 4):
                
                print("to the right")
                
                if not Map[qloc+4][rloc+3].isVisited() and not board[qloc+4][rloc+3].isOccupied():
                    Map[qloc+4][rloc+3].visit(qloc, rloc)
                    queue.insert(startCost, Map[qloc+4][rloc+3])
                    endNodes.append(Map[qloc+4][rloc+3])
                #check for occupation  
                if board[qloc+4][rloc+3].isOccupied():
                    #check whether two pieces away exist:
                    if (qloc +2) < 4 and (rloc +(qloc+2) <4) and not Map[qloc+5][rloc+3].isVisited():
                        Map[qloc+5][rloc+3].visit(qloc, rloc)
                        
                        #check if there is a block or piece in the cell
                        if not board[qloc+5][rloc+3].isOccupied():
                            queue.insert(startCost, Map[qloc+5][rloc+3])
                            endNodes.append(Map[qloc+5][rloc+3])
                            
                        
            
            #visit bottom right
            # the qloc exist, need to check the rlocation existence
            if (rloc + 1 <= 3) and ((rloc +1) + qloc < 4):
                
                print("to the bottom right")
                
                if not Map[qloc+3][rloc+4].isVisited() and not board[qloc+3][rloc+4].isOccupied():
                    Map[qloc+3][rloc+4].visit(qloc,rloc)
                    queue.insert(startCost, Map[qloc+3][rloc+4])
                    endNodes.append(Map[qloc+3][rloc+4])
                    
                #check for occupation
                if board[qloc+3][rloc+4].isOccupied():
                    # check whether two pieces away exist
                    if (rloc+2 < 4) and (rloc+3 + qloc < 4) and not Map[qloc+3][rloc+5].isVisited():
                        Map[qloc+3][rloc+5].visit(qloc, rloc)
                        
                        #check if there is a block or piece in the cell
                        if not board[qloc+3][rloc+5].isOccupied():
                            queue.insert(startCost,Map[qloc+3][rloc+5])
                            endNodes.append(Map[qloc+3][rloc+5])
                        
            
            #visit bottom left
            if(qloc -1 > -4) and (rloc +1 < 4):
                
                print("to the bottom left")
                if not Map[qloc+2][rloc+4].isVisited() and not board[qloc+2][rloc+4].isOccupied():
                    Map[qloc+2][rloc+4].visit(qloc,rloc)
                    queue.insert(startCost, Map[qloc+2][rloc+4])
                    endNodes.append(Map[qloc+2][rloc+4])
                    
                #check for occupation
                if board[qloc+2][rloc +4].isOccupied():
                    # check for existence for two more pieces away
                    if (rloc+2 < 4) and (qloc-2 > -4) and not Map[qloc +1][rloc+5].isVisited():
                        Map[qloc+1][rloc+5].visit(qloc, rloc)
                        
                        #check if there is a block or piece in the cell
                        if not board[qloc+1][rloc+5].isOccupied():
                            queue.insert(startCost, Map[qloc+1][rloc+5])
                            endNodes.append(Map[qloc+1][rloc+5])
                            
        startCost += 1
        startNodes = endNodes
        endNodes =[]
        
        destination = checkReachGoal(startNodes, goals)
    
    last = destination[1]
    #final_path.append((piece.getQ(), piece.getR()))    
    while not( last[0] == piece.getQ() and last[1] == piece.getR()) :
        final_path.append(last)
        last = Map[last[0]+3][last[1]+3].getLastNode()
        
    final_path.append(last)

    return final_path



def MapGreedy(pieces, board, goals):
    exitNumber = len(pieces)
    
    while exitNumber != 0:
        exitmove = False
        
        #check for exist move:     
        for i in range(len(pieces)):
            if checkForExit(pieces[i], goals):
                piece = pieces[i]
                print("EXIT from "+str((piece.getQ(), piece.getR())))
                #remove it from the board
                board[piece.getQ()+3][piece.getR()+3].removePiece()
                del pieces[i]
                exitmove=True
                exitNumber -= 1
                # can only move one at each round
                break
        #can only move one at each round
        if exitmove:
            continue
        
        
        #for each piece find the best path to the goal
        paths = []
        for piece in pieces:
            paths.append(singleGreedy(piece, Board, goals)[::-1])
        
        #search for the path with highest number of jump
        jumps = []
        for path in paths:
            jumps.append(jumpActionsDetection(path))
        maxjump = max(jumps)
        #print(maxjump)
        
        #check for the shorttest path in the maxjump
        shortestloc = 0
        shortestlen = 999
        for i in range(len(jumps)):
            if jumps[i] == maxjump:
                if len(paths[i]) < shortestlen:
                    shortestlen = len(paths[i])
                    shortestloc = i
                    #print(i)
        #do the move!
        currentloc = paths[shortestloc][0]
        nextloc = paths[shortestloc][1]
        
        #deregister from the current node
        board[currentloc[0]+3][currentloc[1]+3].removePiece()
        
        #move the piece and register it at the new node
        pieces[shortestloc].setQ(nextloc[0])
        pieces[shortestloc].setR(nextloc[1])
        board[nextloc[0]+3][nextloc[1]+3].addPiece(pieces[shortestloc])
        
        if abs(currentloc[0] - nextloc[0]) == 2 or abs(currentloc[1] - nextloc[1]) ==2:
            print("JUMP from "+str(currentloc) + " to "+ str(nextloc))
        else:
            print("Move from "+str(currentloc) + " to "+ str(nextloc))
        
                
        