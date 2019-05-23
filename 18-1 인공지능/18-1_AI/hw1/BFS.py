from Node import Node
class BFS:
    def __init__(self, maze, f1):
        self.maze = maze
        self.nRows = len(maze)
        self.nColumns = len(maze[0])
        self.root = Node(self.nRows, self.nColumns,0,0)
        self.searchQueue = []
        self.locationQueue = set()
        self.ifGoal = False
        self.root.setpath([])
        self.f = f1
        self.exploredNode = [(0,0)]


    def bfsearch (self, temp):
        tempy = temp.y
        tempx = temp.x



        if temp.x == self.nColumns-1 and temp.y == self.nRows-1 :
            self.f.write(str(tempy)+" "+str(tempx)+"\n")
            pathstring = ""
            for a in temp.path:
                pathstring = pathstring + str(a)
            self.f.write(pathstring + "\n" + "\n")
            self.ifGoal = True
            return
        else : pass

        if tempx+1< self.nColumns and self.maze[tempy][tempx+1] == 0 and (tempy, tempx+1) not in self.locationQueue and (tempy, tempx+1) not in self.exploredNode:
            temp.setnodew()
            temp.nodeW.setpath(temp.path)
            self.searchQueue.append(temp.nodeW)
            self.exploredNode.append((tempy, tempx+1))
        if tempy+1 < self.nRows and self.maze[tempy+1][tempx] == 0 and (tempy+1, tempx) not in self.locationQueue and (tempy+1, tempx) not in self.exploredNode:
            temp.setnodes()
            temp.nodeS.setpath(temp.path)
            self.searchQueue.append(temp.nodeS)
            self.exploredNode.append((tempy+1, tempx))
        else : pass
        if tempx-1>=0 and self.maze[tempy][tempx-1]==0 and (tempy, tempx-1) not in self.locationQueue and (tempy, tempx-1) not in self.exploredNode:
            temp.setnodee()
            temp.nodeE.setpath(temp.path)
            self.searchQueue.append(temp.nodeE)
            self.exploredNode.append((tempy, tempx-1))
        else: pass
        if tempy-1>=0 and self.maze[tempy-1][tempx]==0 and (tempy-1, tempx) not in self.locationQueue and (tempy-1, tempx) not in self.exploredNode:
            temp.setnoden()
            temp.nodeN.setpath(temp.path)
            self.searchQueue.append(temp.nodeN)
            self.exploredNode.append((tempy-1, tempx))
        else : pass

        self.f.write(str(tempy)+" "+str(tempx)+"\n")


        return

    def bfstart(self, temp):
        self.searchQueue.append(temp)
        while not self.ifGoal:
            self.bfsearch(self.searchQueue.pop(0))



f= open("input.txt",'r')
f1 = open("output_BFS.txt",'w')
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
    bfs = BFS(maze1, f1)
    bfs.bfstart(bfs.root)
f1.close()