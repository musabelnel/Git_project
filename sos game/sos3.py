score_player1 = 0
score_player2 = 0
# turn is a variable use to switch between the 2 player .
turn = 0
# the board size is 4x4 :
board = [[' ',' ',' ',' '],\
         [' ',' ',' ',' '],\
         [' ',' ',' ',' '],\
         [' ',' ',' ',' '],]
# print the board in the screen
def display_board():
    print(board[0], end= "\n")
    print(board[1], end= "\n")
    print(board[2], end= "\n")
    print(board[3], end= "\n")
# take the action from the pkayer
def get_player_action(player):
    # Check the entered row and column number
    # Check if the cell is empty or not
    row = input("please enter row number (0-3) :")
    if row < 0 or row > 3 :
        return
    col = input("please enter col number (0-3) :")
    if row < 0 or row > 3 :
        return
    cell = board [row] [col]
    if cell == "S" or cell == "O" :
        cell = int(input("invalied cell number, try again:"))
        return
    # Check entered character
    letter = input("please enter (S or O) :")
    letter.upper()
    while (letter != "S") and (letter!= "O"):
        letter = input("try again :")
        letter.upper()
    # Cases of scoring SOS using the letter S
    if letter == "S":
        def get_points_s (i,j) :
            points = 0
            if board [i][j:j+3] == ['S', 'O', 'S']:
                points+=1
            if board [i][j-2:j+1] == ['S', 'O', 'S']:
                points+=1
            if i - 2 >= 0:
                if [board[i-2][j], board[i-1][j], board[i][j]] == ['S', 'O', 'S'] :
                    points += 1
            if i+2<=3 :
                if [board [i+2][j], board[i+1][j], board[i][j]] == ['S', 'O', 'S']:
                    points += 1
            if i+2<=3 and j+2<=3 :
                if [board [i][j], board [i+1][j+1], board [i+2][j+2]] == ['S', 'O', 'S']:
                    points+= 1
            if i-2>=0 and j-2>=0 :
                if [board[i-2][j-2], board[i-1][j-1], board[i][j]] == ['S', 'O', 'S']:
                    points+=1
            if i+2<=3 and j-2>=0 :
                if [board[i+2][j-2], board[i+1][j-1], board[i][j]] == ['S', 'O', 'S']:
                    points+=1
            if i-2>=0 and j+2<=3 :
                if [board[i-2][j+2], board[i-1][j+1], board[i][j]] == ['S', 'O', 'S']:
                    points+=1
            return points
    # Cases of scoring SOS using the letter O
    elif letter =="O":
        def get_points_o (i,j) :
            points = 0
            if (i==1 or i ==2) and (j==0 or j==3):
                if [board[i-1][j], board[i][j], board[i+1][j]]== ['S', 'O', 'S']:
                    points+=1
            if (i==0 or i==3) and (j==1 or j==2) :
                if [board[i][j-1], board[i][j], board[i][j+1]]== ['S', 'O', 'S']:
                    points+=1
            if (i==1 or i==2) and (j==1 or j==2) :
                if [board[i-1][j], board[i][j], board[i+1][j]]== ['S', 'O', 'S']:
                    points+=1
                if [board[i][j-1], board[i][j], board[i][j+1]]== ['S', 'O', 'S']:
                    points+=1
                if [board[i-1][j-1], board[i][j], board[i+1][j+1]]==['S', 'O', 'S']:
                    points+=1
                if [board[i-1][j+1], board[i][j], board[i+1][j-1]]==['S', 'O', 'S']:
                    points+=1
            return points
# board update after player action
def update_game_board (action, player) :
    board [action] = player
    display_board()
def play_game():
    display_board()
    # n_actions are used for record the actions to stop the while loop when the board is full .
    n_actions = 0
    while n_actions != 16 :
        action = get_player_action(player_1())
        update_game_board(action)
        n_actions += 1
        # turn check the number is even or odd and select the player
        turn+=1


        action = get_player_action(player_2())
        update_game_board(action)
        n_actions += 1

# if the board is full check the winner 
    if n_actions == 16 :
        if score_player1 > score_player2 :
            print("player 1 is the winner ")
        elif score_player1 < score_player2 :
            print("player 2 is the winner ")
        else:
            print("Draw")

