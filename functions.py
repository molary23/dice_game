import random

player1_score = 0
player2_score = 0


def roll_dice(player):
    player_turn = player + " press Enter to roll the dice...\t"
    input(player_turn)
    rolled = random.randint(1, 6)
    print(player, " rolled", rolled)
    return rolled


def winner(player, session):
    global player1_score, player2_score
    if session == "round":
        if player == "Player 1":
            player1_score += 1
        elif player == "Player 2":
            player2_score += 1
        print(player, " won")
        print("=========================")
        print()
    elif session == "game":
        print(player, " is the winner")


def get_player_score(player):
    if player == "Player 1":
        return player1_score
    elif player == "Player 2":
        return player2_score
