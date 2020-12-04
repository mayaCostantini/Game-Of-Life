import pygame
import gameOfLife
import numpy as np 

def createGame(gridSize, maxIter) : 

    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    pygame.init()

    # Create game : 

    newGame = gameOfLife.gameOfLife(gridSize = gridSize, maxIter = maxIter)

    size = (newGame.gridSize[0]*(newGame.gridSize[1] + newGame.gridSize[0]//2), newGame.gridSize[1]*(newGame.gridSize[0] + newGame.gridSize[1]//2))
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Game of Life")

    width = newGame.gridSize[0]
    height = newGame.gridSize[1]
    margin = 4

    done = False

    iterationsLeft = newGame.maxIter 

    while not done and (iterationsLeft != 0 or (newGame.grid == np.zeros(tuple(newGame.gridSize))).all()) :

        for event in pygame.event.get(): 

            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                column = position[0] // (width + margin)
                row = position[1] // (height + margin)
                newGame.grid[row][column] = 1
                newGame.firstIndividualsCoordinates.append([row, column])
            elif event.type == pygame.KEYDOWN : 
                newGame.nextGeneration()
                iterationsLeft -= 1 

        position = pygame.mouse.get_pos()
        x = position[0]
        y = position[1]
        
        screen.fill(BLACK)

        for row in range(width):
            for column in range(height):
                if newGame.grid[row][column] == 1:
                    color = GREEN
                else:
                    color = WHITE
                pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
                
        pygame.display.flip()

    pygame.quit()




