from collections import deque
import heapq
import sys
import pygame

mazeFile = ['bigMaze.lay','mediumMaze.lay','smallMaze.lay','openMaze.lay']
cell=20
clock = pygame.time.Clock()

def matrixConvert(layPath):
    with open(layPath,'r') as f:
        matrix  =[list(line.strip()) for line in f.readlines()]
    return matrix

def neighbours(matrix,currNode):
    neighbors = []
    direction = [(-1, 0), (1, 0),(0, 1), (0, -1)]
    for x,y in direction:
        xx=currNode[0]+x
        yy=currNode[1]+y
        if 0 <= xx < len(matrix) and 0 <= yy < len(matrix[0]) and matrix[xx][yy] != '%':
            neighbors.append((xx, yy))
    return neighbors

def startAndEnd(mat):
    for i in range(len(mat)):
        for j in  range(len(mat[i])):
            if mat[i][j]=='P':
                intialPos = (i,j)
            elif mat[i][j]=='.':
                endingPos = (i,j)
    return intialPos,endingPos

def draw(path,screen,color,cost,maxDepth,nodeExpanded,maxFringe):
    global cell,clock
    for currNode in path:
        pygame.display.set_caption("Maze Route")
        pygame.draw.rect(screen,color,(currNode[1] * cell, currNode[0] * cell, cell, cell),5)
        display_info(screen, cost,maxDepth, nodeExpanded,maxFringe)
        pygame.display.flip()
        clock.tick(120)


def display_info(screen, cost, maxDepth, nodesExpanded, maxFringe):
    font = pygame.font.SysFont('Verdana', 30,bold=True, italic=True)
    text1 = font.render("Path Cost: {}".format(cost), True, (255, 255, 255))
    text2 = font.render("Max Depth: {}".format(maxDepth), True, (255, 255, 255))
    text3 = font.render("Nodes Expanded: {}".format(nodesExpanded), True, (255, 255, 255))
    text4 = font.render("Max Fringe: {}".format(maxFringe), True, (255, 255, 255))
    screen.blit(text1, (30, 30))
    screen.blit(text2, (30, 60))
    screen.blit(text3, (30, 90))
    screen.blit(text4, (30, 120))


def mark(currNode,screen,color):
        pygame.display.set_caption("Maze Route")
        pygame.draw.rect(screen,color,(currNode[1] * cell, currNode[0] * cell, cell, cell),3)
        pygame.display.flip()
        clock.tick(60)

class dfs():

    
    def findPath(matrix,screen,startAndEnd,neighbours,draw ):
        
        nodesExpanded=0
        maxDepth=0
        maxFringe=0
        intialPos,endingPos = startAndEnd(matrix)
        stack = [(intialPos,[intialPos])]
        vistedPath = set()
        while stack:
            currNode, path = stack.pop()
            nodesExpanded+=1
            maxDepth=max(maxDepth,len(path))
            maxFringe=max(maxFringe,len(stack))
            red=(255,0,0)
            
            
            if currNode ==endingPos:
                return path,len(path)-1,nodesExpanded,maxDepth,maxFringe
            
            if currNode not in vistedPath:
                mark(currNode,screen,red)
                vistedPath.add(currNode)
                for _ in neighbours(matrix , currNode):
                    if _ not in vistedPath:
                        stack.append((_ , path+[_]))
        return None,None, None,None,None

class bfs():
    
    def findPath(matrix,screen,startAndEnd,neighbours,draw):
        nodesExpanded=0
        maxDepth=0
        maxFringe=0
        intialPos,endingPos = startAndEnd(matrix)
        q = deque([(intialPos,[intialPos])])
        vistedSet = set()

        while q:
            currNode ,path = q.popleft()
            nodesExpanded+=1
            maxDepth=max(maxDepth,len(path))
            maxFringe=max(maxFringe,len(q))
            red=(255,0,0)
            if currNode == endingPos:
                return path , len(path)-1,nodesExpanded,maxDepth,maxFringe
            if currNode not in vistedSet:
                mark(currNode,screen,red)
                vistedSet.add(currNode)
                for _ in neighbours(matrix,currNode):
                    if _ not in vistedSet:
                        q.append((_ , path+[_]))
        
        return None,None,None,None,None

class astar():
    
    def findPath(mazeMat,screen,startAndEnd,neighbours,draw):
        nodesExpanded=0
        maxDepth=0
        maxFringe=0
        intialPos,endingPos = startAndEnd(mazeMat)
        heap  = [(0,intialPos,[intialPos])]
        vistedSet = set()
        
        while heap:
            K, currNode, path = heapq.heappop(heap)
            nodesExpanded+=1
            maxDepth=max(maxDepth,len(path))
            maxFringe=max(maxFringe,len(heap))
            red=(255,0,0)
            
            if currNode == endingPos:
                
                return path , len(path)-1,nodesExpanded,maxDepth,maxFringe
            if currNode not in vistedSet:
                mark(currNode,screen,red)
                vistedSet.add(currNode)
                for _ in neighbours(mazeMat,currNode):
                    if _ not in vistedSet:
                        cost  =len(path)+1
                        cost += abs(_[0]-endingPos[0])+abs(_[1]-endingPos[1])
                        heapq.heappush(heap,(cost, _ ,path+[_]))
        return None,None,None,None,None
 
class main():
    
    def main():
        mazeFile = ['bigMaze.lay','mediumMaze.lay','smallMaze.lay','openMaze.lay']
        print("Enter Input of LayOut File Choice: \n 0 for bigMaze \n 1 for mediunMaze \n 2 for smallMaze \n 3 for openMaze")
        layChoice = int(input())
        
        def matrixConvert(path):
            with open(path, 'r') as f:
                maze =  [list(line.strip()) for line in f.readlines()]
            return maze

        matrix=matrixConvert(mazeFile[layChoice])
        
        print("Enter Input of Choice:\n 0 for original matrix \n 1 for DFS Algo path \n 2 for BFS Algo path \n 3 for A* Algo path")
        algoChoice =int(input())
        
        pygame.init()
        BREATH=(len(matrix)*cell)
        LENGTH=len(matrix[0])*cell
        screen = pygame.display.set_mode((LENGTH, BREATH),pygame.RESIZABLE)
        pygame.display.set_caption("Maze Route")
        
        flag=True
        
        WALL_COLOR = (0,0,0)       
        START_COLOR = (255, 0, 0)    
        END_COLOR = (0, 255, 0)      
        EMPTY_COLOR = (178,159,126)  
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if flag:
                for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        cell_color = EMPTY_COLOR
                        if matrix[i][j] == '%':
                            cell_color = WALL_COLOR
                        elif matrix[i][j] == 'P':
                            cell_color = START_COLOR
                        elif matrix[i][j] == '.':
                            cell_color = END_COLOR
                        pygame.draw.rect(screen, cell_color, (j * cell, i * cell, cell, cell))  
                
                green =(0,255,0)
                if algoChoice==0:
                    pygame.display.flip()
                
                if algoChoice == 1 :
                    pygame.display.flip()
                    path,cost,nodeExpanded,maxDepth,maxFringe = dfs.findPath(matrix,screen,startAndEnd,neighbours,draw)
                    print("DFS path:", path)
                    draw(path,screen,green,cost,maxDepth,nodeExpanded,maxFringe)
                    pygame.time.wait(10)
                    pygame.display.flip()
                    algoChoice=0
                
                if algoChoice == 2 :
                    pygame.display.set_caption("Maze Route BFS")
                    pygame.display.flip()
                    path,cost,nodeExpanded,maxDepth,maxFringe  = bfs.findPath(matrix,screen,startAndEnd,neighbours,draw)
                    print("BFS path:", path)
                    draw(path,screen,green,cost,maxDepth,nodeExpanded,maxFringe)
                    pygame.time.wait(10)
                    pygame.display.flip()
                    algoChoice=0
            
                if algoChoice == 3 :
                    pygame.display.set_caption("Maze Route ASTAR")
                    pygame.display.flip()
                    path,cost,nodeExpanded,maxDepth,maxFringe  = astar.findPath(matrix,screen,startAndEnd,neighbours,draw)
                    print("A* path:", path)
                    draw(path,screen,green,cost,maxDepth,nodeExpanded,maxFringe)
                    pygame.time.wait(10)
                    pygame.display.flip()
                    algoChoice=0
                
                pygame.display.flip() 
                flag=False
    main()
