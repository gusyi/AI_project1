
class Cell:
    
    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.node = None
        self.occupied = False
    
    def addPiece(self, tile):
        self.node = Piece(tile.tiletype, self.q, self.r)
        self.occupied = True
        
    def removePiece(self):
        self.node = None
        self.occupied = False
        
    def isOccupied(self):
        return self.occupied
    
    