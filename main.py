import time
from random import randint

# This is a text-based tic-tac-toe game

game_list = ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]"]

game_answer = ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]"]

# Takes the name of the player 1
user1 = input("Enter the name of the first player (X): \n")

# Takes the name of player 2 or the computer if the player decides to play against the computer
user2 = input("Enter the name of the second player (O) "
              "or enter 'Computer' (case-sensitive) if you would like to play against the computer: \n")
print(f"{game_list[:3]}\n{game_list[3:6]}\n{game_list[6:9]}\n")


# function that checks if a player has won the game
def check_winner(game_answer_list, user_name):
    global winner
    if game_answer_list[0] == game_answer_list[1] == game_answer_list[2] or \
            game_answer_list[0] == game_answer_list[4] == game_answer_list[8] or \
            game_answer_list[0] == game_answer_list[3] == game_answer_list[6] or \
            game_answer_list[1] == game_answer_list[4] == game_answer_list[7] or \
            game_answer_list[2] == game_answer_list[5] == game_answer_list[8] or \
            game_answer_list[3] == game_answer_list[4] == game_answer_list[5] or \
            game_answer_list[6] == game_answer_list[7] == game_answer_list[8] or \
            game_answer_list[2] == game_answer_list[4] == game_answer_list[6]:
        winner = True
        print(f"The winner of the game is {user_name}")


winner = False
user_entries = []
# ensures that the game runs as long as there is no winner and all the player turns have not been exhausted.
while not winner and len(user_entries) <= 9:
    user_1_input = int(input(f"Enter a number {user1} from the available ones above: ")) - 1
    # Checks if the slot of the user input has already been taking or is not valid
    # and asks the user to enter another input till a valid input in entered
    while user_1_input in user_entries or user_1_input > 8 or user_1_input < 0:
        if user_1_input > 8 or user_1_input < 0:
            print("The number you entered in invalid")
            user_1_input = int(input(f"Enter a number {user1}: ")) - 1
        else:
            print("This spot is already filled")
            user_1_input = int(input(f"Enter a number {user1}: ")) - 1
    game_answer[user_1_input] = "X"
    user_entries.append(user_1_input)
    time.sleep(1)
    print(f"{game_answer[:3]}\n{game_answer[3:6]}\n{game_answer[6:9]}\n")
    check_winner(game_answer_list=game_answer, user_name=user1)
    if winner is True:
        break
    if len(user_entries) == 9:
        print("The game ended as a draw")
        break

    # Runs if the user selects to play against the computer, the computer generates a random index number
    # and ensure it is valid through the while loop below
    if user2 == "Computer":
        user_2_input = randint(0, 8)
        while user_2_input in user_entries:
            user_2_input = randint(0, 8)
        game_answer[user_2_input] = "O"
        user_entries.append(user_2_input)

        time.sleep(3)
        print(f"{game_answer[:3]}\n{game_answer[3:6]}\n{game_answer[6:9]}\n")
        check_winner(game_answer_list=game_answer, user_name=user2)
        if winner is True:
            break
        if len(user_entries) == 9:
            print("The game ended as a draw")
            break

    # repetition of what was done for player 1 but for player 2 this time around
    else:
        user_2_input = int(input(f"Enter a number {user2} from the available ones above: ")) - 1
        while user_2_input in user_entries or user_2_input > 8 or user_2_input < 0:
            if user_2_input > 8 or user_2_input < 0:
                print("The number you entered in invalid")
                user_2_input = int(input(f"Enter a number {user2}: ")) - 1
            else:
                print("This spot is already filled")
                user_2_input = int(input(f"Enter a number {user2}: ")) - 1
        game_answer[user_2_input] = "O"
        user_entries.append(user_2_input)
        time.sleep(1)
        print(f"{game_answer[:3]}\n{game_answer[3:6]}\n{game_answer[6:9]}\n")
        check_winner(game_answer_list=game_answer, user_name=user2)
        if winner is True:
            break
        if len(user_entries) == 9:
            print("The game ended as a draw")
            break


