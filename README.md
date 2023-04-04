# Maze-Solving

In this assignment, the problem of finding a path through the maze from a given start position to an end position the maze layout will be given to us in the form of “. lay” files where the “%” stands for wall or border and “P” stands for starting position and “.” stands for ending position. We will select one searching algorithm from “Depth first search” and “Breath first search” and “A*” algorithm with Manhattan distance with heuristic function to solve with different mazes 
We will run each of the selected algorithm on all the four different mazes of various sizes “Small, Medium, Big and Open” for each problem. We will search the path using different algorithms we have implemented and we will report the solution, and it part costs, number of nodes it has explored and the maximum depth of the tree and the maximum size of the fringe the final solution will be described by putting a dot in every node position visited on the path and using pygame we will visualize the solution.
 This practical experience in implementing analysis different search algorithms and understanding their strengths and limitations in solving different types of problems .


MAZE REPRESENTATION
The mazes are represented in “. lay” format where the “%” symbol denotes the wall or border and the “P” denotes the starting point of the pacman and “.” denotes the ending point to be reached and we will convert this “. lay” file into a matrix to work on it 

WORKING OF FUNCTIONS:

layToMatrix(path)
This function reads the path which leads to the “. lay” files and converts into 2D Matrix of characters, where each character represents a cell in the maze.
This function first opens the file using the with open statement, which automatically opens the file and reads all the lines in the file using the “readlines()” function and then it converts each line into a list of character. And finally, it returns a list of lists representing the 2D matters of the characters.

findStartAndEnd(mat)
This function helps to find the starting position of the pacman and the ending position of the maze.
This function iterates through all the lists inside the Matrix and iterate over the characters in the list. 
If the character is equal to “P” it will initiate Start as the indexes 0f (i, j) in to tuple and if the character is equal to “.” it will initialize end as indexes of (i, j) in to tuple and returns the start and end.

neighbours(mazeMat, node)
This function takes 2 parameters. mazeMat and node. were mazeMat is a representation of matrix. And the node is a tuple that consist the current position to which we want to find out the neighbours.
This function returns a list of tuples representing all the valid neighbours from the current position in the maze. It is done by iterating in a predefined “direction” list which contains tuple representing X&Y values neighbour nodes. i.e., up, down, right, left for each neighbour. It checks if the neighbours within the boundary of the matrix and the neighbour is valid, it will be added to the list of neighbours.





findPathUsingDFS(mazeMat)
The function “findPathUsingDFS” is an implementation of depth first search algorithm to find a path through the maze from the given start position to the end position. The input for this function is given in the format of two-dimensional matrix.
This function starts by finding the start and end position of the matrix by calling the function “findStartAndEnd” Function. After that, initiate a “node_expanded” as zero, “max_depth” has zero, and max_fringe has zero and initializes the stacked data structure. With a tuple containing the start node and the list containing the start node, and initializes set named has “visitedPath” to keep the track of visited nodes.
The function then enters the loop that continues While the stack is not empty, end goal is found, In this iteration of the loop. It pops the top node and the path from the stack. And increment the node expanded value of by 1. And also updated the maximum depth and the maximum freeze by keep track in the maximum death and the size of the freeze. The function then calls the draw function to draw the path in pygame console using the colour red. if the popped node is equals to end node, it returns the path and path cost, number of nodes expanded, and the maximum depth of the tree, and the maximum size of the films. If the popped node is not in the visited set, it adds in the visited set and generate list of unvisited neighbours from the popped node using the ‘neighbours’ function. It then appends each unvisited neighbour and its corresponding path to the stack. Finally, the goal is not found, and the stack is empty. The function returns None for all output parameters.

findPathUsingBFS(mazeMat)
The function “findPathUsingBFS” is an implementation of breadth first search algorithm to find a path through the maze from the given start position to the end position. The input for this function is given in the format of two-dimensional matrix.
This function starts by finding the start and end position of the matrix by calling the function “findStartAndEnd” Function. After that, initiate a “node_expanded” as zero, “max_depth” has zero, and max_fringe has zero and initializes the queue(deque) data structure. With a tuple containing the start node and the list containing the start node, and initializes set named has “visitedPath” to keep the track of visited nodes.
The function then enters the loop that continues While the deque is not empty, end goal is found, In this iteration of the loop. It pops the node and the path from the deque. And increment the node expanded value of by 1. And also updated the maximum depth and the maximum freeze by keep track in the maximum death and the size of the freeze. The function then calls the draw function to draw the path in pygame console using the colour red. if the popped node is equals to end node, it returns the path and path cost, number of nodes expanded, and the maximum depth of the tree, and the maximum size of the films. If the popped node is not in the visited set, it adds in the visited set and generate list of unvisited neighbours from the popped node using the ‘neighbours’ function. It then appends each unvisited neighbour and its corresponding path to the deque. Finally, the goal is not found, and the stack is empty. The function returns None for all output parameter
findPathUsingAStar(mazeMat)
The function “findPathUsingAStar” is an implementation of A* algorithm to find a path through the maze from the given start position to the end position. The input for this function is given in the format of two-dimensional matrix.
This function starts by finding the start and end position of the matrix by calling the function “findStartAndEnd” Function. After that, initiate a “node_expanded” as zero, “max_depth” has zero, and max_fringe has zero and initializes the heap (priority queue) data structure. With a tuple containing the start node and the list containing the start node, and initializes set named has “visitedPath” to keep the track of visited nodes.
The cost of the path is sum of the length of the path and the Manhattan distance from the current node to the end node
The function then enters the loop that continues While the heap is not empty, end goal is found, In this iteration of the loop. It pops lowest cost and path from heap and increment the node expanded value of by 1. And also updated the maximum depth and the maximum fringe by keep track in the maximum death and the size of the freeze. The function then calls the draw function to draw the path in pygame console using the colour red. if the popped node is equals to end node, it returns the path and path cost, number of nodes expanded, and the maximum depth of the tree, and the maximum size of the films. If the popped node is not in the visited set, it adds in the visited set and generate list of unvisited neighbours from the popped node using the ‘neighbours’ function. It then appends each unvisited neighbour and its corresponding path and cost to the heap. Finally, the goal is not found, and the stack is empty. The function returns None for all output parameters.
draw(path, color)
The function draw is used to visualize the search path on the maze it takes 2 arguments, path and color. The path is the argument that consists of the nodes representing the path to be visualized and color to be drawn.
The function iterates through each node in the path and draws a rectangle on the screen. Using the given color, the position and the size are determined for the nodes position in the maze and the cell variable, which is representing the size of the node After drawing each rectangle, the function updates the display using “pygame.diplay.flip()” and waits for the short amount of time using the “clock.tick(120)”
main()
The function “main “initialize the python library creates the game window and sets the dimension of the window, and also display the options for the users to choose from 0 to 3 the user display determines which of algorithm to be run if the user chooses “0” the original matrix is displayed on the screen. If The user chooses option “1”. The DFS algorithm will run and the matrix will be displayed and path will be printed on the console, and the path generated by the algorithm is given on the screen in the colour of green. The “pygame.dispaly.update()” after the algorithm is run. And the game windows remain open until the user closes.
