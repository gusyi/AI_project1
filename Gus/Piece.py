## A class representing the different piece on the board (red, green, blue, block

class Piece:
    # initialise the piece with type and position on the board
    def __init__(self,type_, q, r):
        self.type = type_
        self.q = q
        self.r = r
        
    # return the type of the piece
    def getType(self): return self.type
    
    #return the Q postion on the board of the piece
    def getQ(self): return self.q
    
    #return the R postion on the board of the piece
    def getR(self): return self.r
    
    #set the type of piece
    def setType(self, newType):
        self.type = newType
        
    #set the q position of the piece
    def setQ(self, newQ):
        self.q = newQ
    #set the r position   
    def setR(self, newR):
        self.r = newR
    
    #move the piece to a new position
    def moveTo(self, newQ, newR):
        self.q = newQ
        self.r = newR
    
    