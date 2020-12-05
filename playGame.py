import gameOfLife
import GUI
import sys 


def printMenu() : 

    print("Hello, welcome to the game of life. Please choose an option : \n")

    userInput = input("1. Begin a game \n \n" + "2. Exit game \n \n")

    if userInput == "1" : 

        def chooseRows() : 
            nbRows = int(input("Choose a number of rows between 10 and 100 for the grid : \n \n"))
            if nbRows > 100 or nbRows < 10 or not isinstance(nbRows, int): 
                print("Please enter a valid value for the number of rows. \n")
                chooseRows()
            return nbRows
    
        def chooseColumns() : 
            nbColumns = int(input("Choose a number of columns between 10 and 100 for the grid : \n \n"))
            if nbColumns > 100 or nbColumns < 10 or not isinstance(nbColumns, int): 
                print("Please enter a valid value for the number of columns. \n")
                chooseColumns()
            return nbColumns

        print("------------------- Creation of a new game ... --------------------")

        nbMaxIter = input("Choose a maximal number of iterations : \n \n")

        nbRows = chooseColumns()
        nbColumns = chooseRows()

        GUI.createGame(gridSize=[int(nbRows), int(nbColumns)], maxIter=int(nbMaxIter))

        sys.exit(0)

    if userInput == "2" : 

        print("Goodbye, thank you for playing. ")
        sys.exit(0)

    else : 

        print("Please enter a correct option. ")
        printMenu()
    
    

def main() : 

    printMenu()


if __name__ == "__main__" : 
    main()