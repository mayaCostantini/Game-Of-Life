import numpy as np 


class gameOfLife : 

    def __init__(self, gridSize = [10,10], firstIndividualsCoordinates = [], maxIter = 10): 
    # input : 2D grid size (number of lines, number of columns), first individuals coordinates 

        self.firstIndividualsCoordinates = firstIndividualsCoordinates
        self.gridSize = gridSize
        self.grid = np.zeros(tuple(self.gridSize))
        self.maxIter = maxIter

        for coordinates in self.firstIndividualsCoordinates : 
            self.grid[coordinates[0]][coordinates[1]] = 1        

    def nextGeneration(self) : 

        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(self.grid)
        columns = len(self.grid[0])

        newBoard = [[self.grid[row][col] for col in range(columns)] for row in range(rows)]

        for row in range(rows):
            for col in range(columns):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    if (r < rows and r >= 0) and (c < columns and c >= 0) and (newBoard[r][c] == 1):
                        live_neighbors += 1
                if newBoard[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    self.grid[row][col] = 0
                if newBoard[row][col] == 0 and live_neighbors == 3:
                    self.grid[row][col] = 1

        return self.grid


