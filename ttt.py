#Tic Tac Toe

def vertical():
    print("     |     |     ")


def horizontal():
    print("-----------------")


def choose(p, position, symbol, player):
    position = input(player + ": pick an available position between 1-9:")
    position = check1(position, player)
    position = check2(position, player)
    choice(p,int(position), symbol, player)
    return position
       


def check1(position, player):
    while not (position.isdigit()):
        position = input(player + ": Please pick an available position between 1-9:")
    return position


def check2(position, player):
    while (int(position) < 1) | (int(position) > 9):
        position = input(player + ": Please pick an available position between 1-9:")
        position = check1(position, player)
    return position


def choice(p, position, symbol, player):
    if (p[position - 1] == position):
        p[position - 1] = symbol
        return p
    else:
        choose(p, position, symbol, player)
  

def board(p, player, symbol):

    vertical()
    print("  " + str(p[0]) + "  |  " + str(p[1]) + "  |  " + str(p[2]) + "  ")
    vertical()
    horizontal()
    vertical()
    print("  " + str(p[3]) + "  |  " + str(p[4]) + "  |  " + str(p[5]) + "  ")
    vertical()
    horizontal()
    vertical()
    print("  " + str(p[6]) + "  |  " + str(p[7]) + "  |  " + str(p[8]) + "  ")
    vertical()


def win(p, player):
    if (p[0] == p[1] == p[2]) | (p[3] == p[4] == p[5]) | (p[6] == p[7] == p[8]) | \
        (p[0] == p[3] == p[6]) | (p[1] == p[4] == p[7]) | (p[2] == p[5] == p[8]) | \
        (p[0] == p[4] == p[8]) | (p[2] == p[4] == p[6]):
        return "winner"
    x = [1,2,3,4,5,6,7,8,9]
    counter = 0;
    t = 0;
    for i in range(9):
        if x[t] in p:
            counter += 1
        t += 1
    if counter == 0:
        return "tie"


def play(p,player1,player2,symbol1,symbol2):
    for i in range(5):
        position1 = 0
        position2 = 0
        position1 = choose(p, position1, symbol1, player1)
        board(p, 1, symbol1)
        decision = win(p, 1)
        if (decision == "winner"):
            print("Winner: " + player1)
            return
        elif (decision == "tie"):
            print("Tie!")
            return
        position2 = choose(p, position2, symbol2, player2)
        board(p, 2, symbol2)
        decision = win(p, 2)
        if (decision == "winner"):
            print("Winner: " + player2)
            return
        elif (decision == "tie"):
            print("Tie!")
            return

                          
def  main():
    p = [1,2,3,4,5,6,7,8,9]
                              
    print("Welcome to Tic-Tac-Toe!")
    print("I will not Die!")
    player1 = input("Player 1: What is your name? ")
    player2 = input("player 2: What is your name? ")
    while (player1 == player2):
        player2 = input("Player 2: The name " + player2 + " is already taken. Please choose a different name:")
                          

    symbol1 = input(player1 + ": Please choose your symbol:")
    symbol2 = input(player2 + ": Please choose your symbol:")
    while (symbol1 == symbol2):
        symbol2 = input(player2 + ": The symbol " + symbol2 + " is taken. Please choose a different symbol:")
                          
                          
    print("Let's play!")
    board(p, 1, symbol1)
                          
    play(p,player1,player2,symbol1,symbol2)                      
  

    
if __name__ == "__main__":
    main()


