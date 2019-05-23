class Node:
    def __init__(self, nRows, nColumns, y, x):
        self.x = x
        self.y = y
        self.location = (y ,x)
        self.nColumns = nColumns
        self.nRows = nRows
        self.childNodes = []
        self.path = []

        self.h = nColumns - x + nRows - y

    ifExplored = False
    def setnodew(self):
        self.nodeW = Node(self.nRows, self.nColumns, self.y, self.x+1)
        self.childNodes.append(self.nodeW)
    def setnodes(self):
        self.nodeS = Node(self.nRows, self.nColumns, self.y+1, self.x)
        self.childNodes.append(self.nodeS)
    def setnodee(self):
        self.nodeE = Node(self.nRows, self.nColumns, self.y, self.x-1)
        self.childNodes.append(self.nodeE)
    def setnoden(self):
        self.nodeN = Node(self.nRows, self.nColumns, self.y-1, self.x)
        self.childNodes.append(self.nodeN)
    def decideh(self):
        self.h = (self.nRows - self.y) + (self.nColumns - self.nRows)
    def __eq__(self, other):
        if (self.x, self.y) == (other.x, other.y):
            return True
        else:
            return False
    def setparent(self, parent):
        self.parentNode = parent
    def setpath(self, path):
        self.path = path + [self.location]
    def __ge__ (self, other):
        if self.h >= other.h :
            return True
        else:
            return False
    def __le__(self, other):
        if self.h <= other.h:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.h < other.h:
            return True
        else:
            return False