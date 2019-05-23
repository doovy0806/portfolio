import heapq

# a class for A* Search. This contains A* method and the related variables for it.
class Ast :
    def __init__(self, maze, f1):
        self.maze = maze
        self.nRows = len(maze)
        self.nColumns = len(maze[0])
        self.pq = []
        self.root = AstarNode(self.nRows,self.nColumns,0,0)
        self.root.g=0
        self.root.path = self.root.path+[self.root.location]

        self.root.parentNode = None
        self.f = f1
        self.exploredNode = [(0,0)]

    def astsearch(self, temp):
        tempx = temp.x
        tempy = temp.y

        self.f.write(str(temp.y)+" "+str(temp.x)+"\n")
        if tempx == self.nColumns-1 and tempy == self.nRows-1 :
            pathstring=""
            for a in temp.path:
                pathstring = pathstring + str(a)
                # to print the optimal path on the file
            self.f.write(pathstring+"\n"+"\n")
            return

        if tempy + 1 < self.nRows and self.maze[tempy + 1][tempx] == 0 and (tempy+1, tempx) not in temp.path and (tempy+1, tempx) not in self.exploredNode:
            temp.setnodes()
            heapq.heappush(self.pq, temp.nodeS)
            self.exploredNode.append((tempy+1, tempx))
            #I used a heap( or PQ) to pop a node that has the least f-value
        else:
            pass
        if tempx + 1 < self.nColumns and self.maze[tempy][tempx + 1] == 0 and (tempy, tempx+1) not in temp.path and (tempy, tempx+1) not in self.exploredNode:
            temp.setnodew()
            heapq.heappush(self.pq, temp.nodeW)
            self.exploredNode.append((tempy, tempx+1))
        else:
            pass
        if tempx - 1 >= 0 and self.maze[tempy][tempx - 1] == 0 and (tempy, tempx-1) not in temp.path and (tempy, tempx-1) not in self.exploredNode:
            temp.setnodee()
            heapq.heappush(self.pq, temp.nodeE)
            self.exploredNode.append((tempy, tempx-1))
        else:
            pass
        if tempy - 1 >= 0 and self.maze[tempy - 1][tempx] == 0 and (tempy-1, tempx) not in temp.path and (tempy-1, tempx) not in self.exploredNode:
            temp.setnoden()
            heapq.heappush(self.pq, temp.nodeN)
            self.exploredNode.append((tempy-1, tempx))
        else:
            pass

        self.astsearch(heapq.heappop(self.pq))


class AstarNode:
    def __init__(self,nRows, nColumns, y, x):
        self.location = (y, x)
        self.x = x
        self.y = y
        self.nRows = nRows
        self.nColumns = nColumns
        self.h = nRows + nColumns - y - x - 2
        self.g = 0
        self.f = self.h + self.g
        self.childNodes = []
        self.path = []

    def setg(self, node):
        self.g = node.g + 1
        self.f = self.g+self.h
    def setnodew(self):
        self.nodeW = AstarNode(self.nRows, self.nColumns, self.y, self.x + 1)
        self.childNodes.append(self.nodeW)
        self.nodeW.setg(self)
        self.nodeW.setparent(self)
        self.nodeW.path = self.path + [self.nodeW.location]
    def setnodes(self):
        self.nodeS = AstarNode(self.nRows, self.nColumns, self.y+1, self.x)
        self.childNodes.append(self.nodeS)
        self.nodeS.setg(self)
        self.nodeS.setparent(self)
        self.nodeS.path = self.path + [self.nodeS.location]
    def setnodee(self):
        self.nodeE = AstarNode(self.nRows, self.nColumns, self.y, self.x-1)
        self.childNodes.append(self.nodeE)
        self.nodeE.setg(self)
        self.nodeE.setparent(self)
        self.nodeE.path = self.path + [self.nodeE.location]

    def setnoden(self):
        self.nodeN = AstarNode(self.nRows, self.nColumns, self.y-1, self.x)
        self.childNodes.append(self.nodeN)
        self.nodeN.setg(self)
        self.nodeN.setparent(self)
        self.nodeN.path = self.path + [self.nodeN.location]

    def setparent(self, node):
        self.parentNode = node

    #this method is important in that it decides which node comes first at priority queue.
    def __lt__(self, other):
        if self.f < other.f:
            return True
        else:
            return False

f= open("input.txt",'r')
f1 = open("output.txt",'w')
nMazes = int(f.readline())
for i in range(nMazes):
    space = f.readline()
    rcList1 = f.readline().split()
    (nRows, nColumns) = (int(rcList1[0]), int(rcList1[1]))
    i = 0
    maze1 = []
    while i < nRows :
        maze1.append(f.readline().split(','))
        maze1[i] = [int(num) for num in maze1[i]]
        i = i+1
    ast = Ast(maze1, f1)
    ast.astsearch(ast.root)
f1.close()