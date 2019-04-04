#create  temporary board
q, r = 7, 7;
Board= [[0 for x in range(q)] for y in range(r)] 
for i in range(0,7):
    for j in range(0,7):
        if 3 <= (i+j) < 10:
            Board[i][j] = Cell(i-3, j-3)
        
red_piece = Piece("red", 0, -1)
Board[3][2].addPiece(red_piece)
goal = []
block_1 = Piece("block", -2, 2)
block_2 = Piece("block", -1, 2)
block_3 = Piece("block", 0, 2)
Board[1][5].addPiece(block_1)
Board[2][5].addPiece(block_2)
Board[3][5].addPiece(block_3)
Board



q, r = 7, 7;
Map = [[0 for x in range(q)] for y in range(r)] 
for i in range(0,7):
    for j in range(0,7):
        if 3 <= (i+j) < 10:
            Map[i][j] = Node(i-3, j-3)
        else:
            Map[i][j] = nonValidNode()



for column in Map:
    for i in range(len(Map[0])):
        if type(column[i]) == Node and  not column[i].isVisited():
            print((column[i].q, column[i].r))
            
            
            
a = Cell(1,1)
b = Piece("red", 1,1)
a.addPiece(b)

d = Node(1,1)
d.visit(2,2)
d.getLastNode()