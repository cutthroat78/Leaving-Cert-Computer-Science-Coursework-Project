#!/usr/bin/python3
# Above commented line makes it easier to run this program with python3 on *nix (Linux, Mac, BSD, etc.) systems

import random, sys, statistics # Import the library named random and the library named sys
from pandas import *
from pathlib import Path

def game(player_one, player_two,player_one_name,player_two_name):
    gameboard = ["1","2","3","4","5","6","7","8","9"]
    player_one_turns = [ ]
    player_two_turns = [ ]
    
    games_played = 0

    
    while True:
        if check_win(gameboard) == "X" or check_win(gameboard) == "O" or check_win(gameboard) == "Tie":
            if check_win(gameboard) == "X":
                who_won = player_one_name
                draw_board(gameboard)
                print("\n" + player_one_name + " won!\n")
            elif check_win(gameboard) == "O":
                who_won = player_two_name
                draw_board(gameboard)
                print("\n" + player_two_name + " won!\n")
            elif check_win(gameboard) == "Tie":
                who_won = "Tie"
                draw_board(gameboard)
                print("It's a tie!\n")
            str_player_one_turns = '"' + ','.join(player_one_turns) + '"'
            str_player_two_turns = '"' + ','.join(player_two_turns) + '"'
            csv_entry = csv_gamemode + "," + who_won + "," + player_one_name + "," + str_player_one_turns + "," + player_two_name + "," + str_player_two_turns + "\n"
            f = open("data.csv", "a")
            f.write(csv_entry)
            f.close()
            if player_one == "computer" and player_two == "computer":
                games_played += 1
                if games_played == simulation_amount:
                    new_game = "2"
                    print("Simulation has ended")
                else:
                    new_game = "1"
            else:
                new_game = input("Would you like to play again? Type the number of your choice!\n\n1. Yes\n2. No\n\n>")
            while True:
                if str(new_game) != "1" and str(new_game) != "2":
                    new_game = input("Please type the number of your choice on whether or not to play another game?\n\n1. Yes\n2. No\n\n>")
                else:
                    break
            if str(new_game) == "1":
                player_one_turns = [ ]
                player_two_turns = [ ]
                gameboard = ["1","2","3","4","5","6","7","8","9"]
                continue
            elif str(new_game) == "2":
                break
        else:
            pass
        draw_board(gameboard)
        game_turn("player_one",player_one,player_one_name,gameboard,player_one_turns,player_two_turns)
        if check_win(gameboard) == "X" or check_win(gameboard) == "O" or check_win(gameboard) == "Tie":
            if check_win(gameboard) == "X":
                who_won = player_one_name
                draw_board(gameboard)
                print("\n" + player_one_name + " won!\n")
            elif check_win(gameboard) == "O":
                who_won = player_two_name
                draw_board(gameboard)
                print("\n" + player_two_name + " won!\n")
            elif check_win(gameboard) == "Tie":
                who_won = "Tie"
                draw_board(gameboard)
                print("It's a tie!\n")
            str_player_one_turns = '"' + ','.join(player_one_turns) + '"'
            str_player_two_turns = '"' + ','.join(player_two_turns) + '"'
            csv_entry = csv_gamemode + "," + who_won + "," + player_one_name + "," + str_player_one_turns + "," + player_two_name + "," + str_player_two_turns + "\n"
            f = open("data.csv", "a")
            f.write(csv_entry)
            f.close()
            if player_one == "computer" and player_two == "computer":
                games_played += 1
                if games_played == simulation_amount:
                    new_game = "2"
                    print("Simulation has ended")
                else:
                    new_game = "1"
            else:
                new_game = input("Would you like to play again? Type the number of your choice!\n\n1. Yes\n2. No\n\n>")
            while True:
                if str(new_game) != "1" and str(new_game) != "2":
                    new_game = input("Please type the number of your choice on whether or not to play another game?\n\n1. Yes\n2. No\n\n>")
                else:
                    break
            if str(new_game) == "1":
                player_one_turns = [ ]
                player_two_turns = [ ]
                gameboard = ["1","2","3","4","5","6","7","8","9"]
                continue
            elif str(new_game) == "2":
                break
        else:
            pass
        draw_board(gameboard)
        game_turn("player_two",player_two,player_two_name,gameboard,player_one_turns,player_two_turns)
        if check_win(gameboard) == "X" or check_win(gameboard) == "O" or check_win(gameboard) == "Tie":
            if check_win(gameboard) == "X":
                who_won = player_one_name
                draw_board(gameboard)
                print("\n" + player_one_name + " won!\n")
            elif check_win(gameboard) == "O":
                who_won = player_two_name
                draw_board(gameboard)
                print("\n" + player_two_name + " won!\n")
            elif check_win(gameboard) == "Tie":
                who_won = "Tie"
                draw_board(gameboard)
                print("It's a tie!\n")
            str_player_one_turns = '"' + ','.join(player_one_turns) + '"'
            str_player_two_turns = '"' + ','.join(player_two_turns) + '"'
            csv_entry = csv_gamemode + "," + who_won + "," + player_one_name + "," + str_player_one_turns + "," + player_two_name + "," + str_player_two_turns + "\n"
            f = open("data.csv", "a")
            f.write(csv_entry)
            f.close()
            if player_one == "computer" and player_two == "computer":
                games_played += 1
                if games_played == simulation_amount:
                    new_game = "2"
                    print("Simulation has ended")
                else:
                    new_game = "1"
            else:
                new_game = input("Would you like to play again? Type the number of your choice!\n\n1. Yes\n2. No\n\n>")
            while True:
                if str(new_game) != "1" and str(new_game) != "2":
                    new_game = input("Please type the number of your choice on whether or not to play another game?\n\n1. Yes\n2. No\n\n>")
                else:
                    break
            if str(new_game) == "1":
                player_one_turns = [ ]
                player_two_turns = [ ]
                gameboard = ["1","2","3","4","5","6","7","8","9"]
                continue
            elif str(new_game) == "2":
                break
        else:
            pass

def game_turn(player_number, player_type, player_name, gameboard, player_one_turns, player_two_turns):
    if player_number == "player_one":
        symbol = "X"
    elif player_number == "player_two":
        symbol = "O"
    else:
        print("Please define whether this is player one or two")

    while True:
        if player_type == "human":
            player_choice = input("It is " + player_name + "'s turn!\n\nPick a number in a square that hasn't already been taken\n\n>")
        elif player_type == "computer":
            player_choice = str(random.randint(1,9))
        else:
            print("Please define whether this player is a human or a computer")

        if player_choice in gameboard:
            choice = int(player_choice) - 1
            gameboard[choice] = symbol
            if player_number == "player_one":
                player_one_turns.append(player_choice)
            elif player_number == "player_two":
                player_two_turns.append(player_choice)
            if player_type == "computer":
                print("\n" + player_name + " has chosen square " + player_choice + " for their turn!\n")
                break
            else:
                break
        else:
            if player_type == "computer":
                continue
            elif player_type == "human":
                print("\nPlease input a number that is inside an empty square\n")
                continue
            else:
                print("Player type seems to not be specified")
                continue

def check_win(gameboard):
    if gameboard[0] == "X" and gameboard[1] == "X" and gameboard[2] == "X":
        return "X"
    if gameboard[0] == "X" and gameboard[3] == "X" and gameboard[6] == "X":
        return "X"
    if gameboard[0] == "X" and gameboard[4] == "X" and gameboard[8] == "X":
        return "X"
    if gameboard[1] == "X" and gameboard[4] == "X" and gameboard[7] == "X":
        return "X"
    if gameboard[2] == "X" and gameboard[5] == "X" and gameboard[8] == "X":
        return "X"
    if gameboard[2] == "X" and gameboard[4] == "X" and gameboard[6] == "X":
        return "X"
    if gameboard[3] == "X" and gameboard[4] == "X" and gameboard[5] == "X":
        return "X"
    if gameboard[6] == "X" and gameboard[7] == "X" and gameboard[8] == "X":
        return "X"
    if gameboard[0] == "O" and gameboard[1] == "O" and gameboard[2] == "O":
        return "O"
    if gameboard[0] == "O" and gameboard[3] == "O" and gameboard[6] == "O":
        return "O"
    if gameboard[0] == "O" and gameboard[4] == "O" and gameboard[8] == "O":
        return "O"
    if gameboard[1] == "O" and gameboard[4] == "O" and gameboard[7] == "O":
        return "O"
    if gameboard[2] == "O" and gameboard[5] == "O" and gameboard[8] == "O":
        return "O"
    if gameboard[2] == "O" and gameboard[4] == "O" and gameboard[6] == "O":
        return "O"
    if gameboard[3] == "O" and gameboard[4] == "O" and gameboard[5] == "O":
        return "O"
    if gameboard[6] == "O" and gameboard[7] == "O" and gameboard[8] == "O":
        return "O"
    for n in range(9):
        if str(gameboard[n]).isdigit():
            break
    else:
        return "Tie"
    return False


def draw_board(gameboard):
    print("-------------")
    print("|   |   |   |")
    print("| " + gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2] + " |")
    print("|   |   |   |")
    print("-------------")
    print("|   |   |   |")
    print("| " + gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5] + " |")
    print("|   |   |   |")
    print("-------------")
    print("|   |   |   |")
    print("| " + gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8] + " |")
    print("|   |   |   |")
    print("-------------")

if sys.argv[1:]:
    name = sys.argv[1]
else:
    name = input("What is your name?\n\n>")

while True:
    if len(name) >= 6:
        break
    name = input("Please input a name that is longer than 6 characters\n\n>")

if sys.argv[2:]:
    email = sys.argv[2]
else:
    email = input("What is your email\n\n>")

while True:
    if "@" in email:
        break
    email = input("Please input a valid email\n\n>")

if sys.argv[3:]:
    gamemode = sys.argv[3]
else:
    gamemode = input("Welcome to Tic Tac Toe!\n\nChoose Your Gamemode by Typing the Number of the Gamemode Below:\n\n1. Singleplayer\n2. Multiplayer\n3. Simulation\n4. Statistical Analysis\n5. Exit\n\n>") 

gamemode_options = [ "1", "2", "3", "4", "5" ]

while True:
    if str(gamemode) in gamemode_options:
        break
    else:
        gamemode = input("Please input a valid gamemode by typing the number of the gamemode\n\n1. Singleplayer\n2. Multiplayer\n3. Simulation\n4. Statistical Analysis \n5. Exit\n\n>")

if gamemode == "1":
    csv_gamemode = "Singleplayer"
    game("human","computer",name,"Computer 1")

if gamemode == "2":
    csv_gamemode = "Multiplayer"
    if sys.argv[4:]:
        name2 = sys.argv[4]
    else:
        name2 = input("What is the second player's name?\n\n>")

    while True:
        if len(name2) >= 6:
            break
        else:
            name2 = input("The second player's name must be longer than 6 characters\n\n>")

    game("human","human",name,name2)

if gamemode == "3":
    csv_gamemode = "Simulation"
    if sys.argv[4:]:
        simulation_amount_input = sys.argv[4]
    else:
        simulation_amount_input = input("How many games would you like the simulation to run for?\n\n>")

    while True:
        if simulation_amount_input.isdigit():
            simulation_amount = int(simulation_amount_input)
            break
        simulation_amount_input = input("Please input a number\n\n>")

    name = "Computer 1"
    name2 = "Computer 2"

    game("computer","computer",name,name2)

if gamemode == "4":
    if Path("./data.csv").is_file():
        stat_option = input("\nWhat type of statistical analysis would you like to do?\n\n1. Frequency\n2. Mean\n3. Median\n4. Mode\n\n>")
        csv_data = read_csv("data.csv", header=None, names=["gamemode","who_won","player_one_name","str_player_one_turns","player_two_name","str_player_two_turns"])
        game_outcomes = csv_data["who_won"].tolist()
        stat_name = input("\nEnter the name of the player's data you would like to analyse\n\n>")
    else:
        print("data.csv doesn't exist. Please, play some games to generate some data")

if gamemode == "5":
    print("\nGoodbye!")
