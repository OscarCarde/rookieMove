from board import Board


class PiecesGeneral():

    def __init__(self):
        self.moveRange = list(range(Board().width))


class Rook():

    def __init__(self,x,y,colour,moved=False):
        piece = PiecesGeneral()
        self.colour = colour
        self.xPossVec = [xposs for xposs in piece.moveRange if xposs != x]
        self.yPossVec = [yposs for yposs in piece.moveRange if yposs != y]
        self.possibleMoves = [(xcord,y) for xcord in self.xPossVec] \
                                + [(x,ycord) for ycord in self.yPossVec]

class Bishop():

    def __init__(self,x,y,colour):
        piece = PiecesGeneral()
        self.colour = colour
        self.yPossVec = [yposs for yposs in piece.moveRange if yposs != y]
        self.yIntercepts = [y-x,x+y]
        self.possibleMoves = [(y-self.yIntercepts[0],y) for y in self.yPossVec if  0 <= y <= 7 and 0 <= (y-self.yIntercepts[0]) <= 7] \
                                + [(-y+self.yIntercepts[1],y) for y in self.yPossVec if  0 <= y <= 7 and 0 <= (-y+self.yIntercepts[1]) <= 7]

class Queen():

    def __init__(self,x,y,colour):
        piece = PiecesGeneral()
        self.colour = colour
        self.xPossVec = [xposs for xposs in piece.moveRange if xposs != x]
        self.yPossVec = [yposs for yposs in piece.moveRange if yposs != y]
        self.yIntercepts = [y-x,x+y]
        self.possibleMoves = [(y-self.yIntercepts[0],y) for y in self.yPossVec if  0 <= y <= 7 and 0 <= (y-self.yIntercepts[0]) <= 7] \
                                + [(-y+self.yIntercepts[1],y) for y in self.yPossVec if  0 <= y <= 7 and 0 <= (-y+self.yIntercepts[1]) <= 7] \
                                    + [(xcord,y) for xcord in self.xPossVec] \
                                        + [(x,ycord) for ycord in self.yPossVec]

class Pawn():

    def __init__(self,x,y,colour, moved=False):
        self.colour = colour
        a = 1
        if colour == 'B':
            a = -1
        if moved:
            self.possibleMoves = [(x,y+a*1)]
        else:
            self.possibleMoves = [(x,y+a*1),(x,y+a*2)]
        self.possibleTakingMoves = [(x+b,y+a*1) for b in [1,-1] if 0 <= x+b <= 7]

class Knight():

    def __init__(self,x,y,colour):
        self.colour = colour
        self.possiblemoves = [a for a in [(x+2, y-1),(x+2, y+1),(x-2, y-1),(x-2, y+1),(x-1,y+2),(x+1,y+2),(x-1,y-2),(x+1,y-2)] if 0 <= a[0] <= 7 and 0 <= a[1] <= 7]

class King():
    def __init__(self,x,y,colour):
        self.colour = colour
        self.possibleMoves = [(x+a,y+b) for a in [1,1,1,0,0,-1,-1,-1] for b in [1,0,-1,1,-1,1,0,-1]]


print(Rook(0,0,'B').possibleMoves)
print(Bishop(1,2,'B').possibleMoves)