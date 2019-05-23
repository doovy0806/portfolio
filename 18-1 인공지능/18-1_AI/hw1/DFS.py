from Node import Node
class DFS :
    def __init__(self, maze, f1):
        self.nRows = len(maze)
        self.nColumns = len(maze[0])
        self.maze = maze
        self.root = Node(nRows, nColumns, 0,0)
        self.fringe = []
        self.fringeSet = set()
        self.ifGoal = False
        self.f = f1
        self.exploredNode =[(0,0)]

    def dfsearch(self, temp):
        tempx = temp.x
        tempy = temp.y
        self.f.write(str(temp.y)+" "+str(temp.x)+"\n")


        if tempy+1 < self.nRows and self.maze[tempy+1][tempx] == 0 and (tempy+1, tempx) not in self.fringeSet and (tempy+1, tempx) not in self.exploredNode :
            temp.setnodes()
            self.exploredNode.append((tempy+1, tempx))
        else : pass
        if tempx+1< self.nColumns and self.maze[tempy][tempx+1] ==0 and (tempy, tempx+1) not in self.fringeSet and (tempy, tempx+1) not in self.exploredNode:
            temp.setnodew()
            self.exploredNode.append((tempy, tempx+1))
        else : pass
        if tempx-1>=0 and self.maze[tempy][tempx-1]==0 and (tempy, tempx-1) not in self.fringeSet and (tempy, tempx-1) not in self.exploredNode:
            temp.setnodee()
            self.exploredNode.append((tempy, tempx-1))
        else: pass
        if tempy-1>=0 and self.maze[tempy-1][tempx]==0 and (tempy-1, tempx) not in self.fringeSet and (tempy-1, tempx) not in self.exploredNode:
            temp.setnoden()
            self.exploredNode.append((tempy-1, tempx))
        else : pass

        for node in temp.childNodes :
            if node.h < temp.h :
                if node.x == self.nColumns-1 and node.y == self.nRows-1 :
                    pathstring = ""
                    for a in self.fringe:
                        pathstring = pathstring + str(a)
                    self.f.write(pathstring + "\n" + "\n")
                    self.ifGoal =True
                    return
                else :
                    self.fringe.append(node.location)
                    self.fringeSet.add(node.location)
                    #print(node.location)

                    self.dfsearch(node)
                    if self.ifGoal:
                        return

            else :
                self.fringe.append(node.location)
                self.fringeSet.add(node.location)
                #print(node.location)
                self.dfsearch(node)
                if self.ifGoal:
                    return

            self.fringeSet.remove(node.location)
            self.fringe.remove(node.location)
            
f= open("input.txt",'r')
f1 = open("output_DFS.txt",'w')
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
    dfs = DFS(maze1, f1)
    dfs.dfsearch(dfs.root)
f1.close()


