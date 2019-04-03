# Node for path finding in the map
class Node:
    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.visited = False
        self.last = (q, r)
        
    def isVisited(self):
        return self.visited
    
    def visit(self, lastq, lastr):
        self.visited - True
        self.last = (lastq, lastr)
        
    def getLastNode(self):
        return self.last