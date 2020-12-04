for _ in range(newGame.maxIter) : 
    updatedGrid = newGame.nextGeneration()
    for row in range(newGame.gridSize[0]) : 
        for column in range(newGame.gridSize[1]) : 
            if grid[row][column] == 1:
                color = GREEN
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
    
