from builtins import NULL
class Cell:
    
    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.node = NULL
        self.occupied = False
    
    def addPiece(self, tile, tiletype):
        self.node = Piece(tile, tiletype, self.q, self.r)
        self.occupied = True
        
    def removePiece(self):
        self.node = NULL
        self.occupied = False
        
    def havePiece(self):
        return self.occupied
    
    