from functions import winner, roll_dice, get_player_score

player1_score = 0
player2_score = 0
play_again = True

while play_again:
    num_rounds = int(input("How many rounds would you like to play??\t"))
    for i in range(num_rounds):
        player1_value = roll_dice("Player 1")
        player2_value = roll_dice("Player 2")

        if player1_value > player2_value:
            winner("Player 1", "round")
        elif player2_value > player1_value:
            winner("Player 2", "round")
        else:
            print("It's a tie")
            print("=========================")
            print()
    player1_score = get_player_score("Player 1")
    player2_score = get_player_score("Player 2")
    if player1_score > player2_score:
        winner("Player 1", "game")
    elif player2_score > player1_score:
        winner("Player 2", "game")
    else:
        print("Its a tie!")
    print("Game End")
    print("=========================")
    print()
    agree = input("Do you want to play again (Y/N)? ")
    if agree.lower() == "n":
        print("Thank you for playing!")
        play_again = False
