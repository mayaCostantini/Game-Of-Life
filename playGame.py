import gameOfLife
import GUI
import sys 


def main() : 

    print("Hello, welcome to the game of life. Please choose an option : \n")

    userInput = input("1. Begin a game \n \n" + "2. Exit game \n \n")

    if userInput == "1" : 

        nbRows = input("Choose a number of rows for the grid : \n \n")
        nbColumns = input("Choose a number of rows for the grid : \n \n")

        nbMaxIter = input("Choose a maximal number of iterations : \n \n")

        print("----------------- Creation of a new game ... --------------------")

        GUI.createGame(gridSize=[int(nbRows), int(nbColumns)], maxIter=int(nbMaxIter))

    if userInput == "2" : 
        print("Goodbye, thank you for playing")
    
    sys.exit(0)


if __name__ == "__main__" : 
    main()