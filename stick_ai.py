import random
import os
import time


def clear():
    os.system("clear")


def intro():
    clear()
    ai_brain = {}
    ai_knowledge = []
    for i in range(1, 20):
        ai_brain[i] = [1, 2, 3]
    print("Welcome to the stick game.")
    print("Options:")
    print("\tPlay against a friend (1)")
    print("\tPlay against the computer (2)")
    choice = int(input("What'll it be (1 - 2)? "))
    if choice == 1:
        player_v_player()
    elif choice == 2:
        player_v_ai(ai_knowledge, ai_brain)


def play_again_ai(ai_knowledge, ai_brain):
    play_again = input("\nPlay again? Y/n ").lower()
    if play_again != 'n':
        clear()
        player_v_ai(ai_knowledge, ai_brain)
    else:
        print("\n\n\n\nCatch ya later!\n\n\n\n")
        time.sleep(1.5)
        clear()
        exit()


def play_again_player():
    play_again = input("\nPlay again? Y/n ").lower()
    if play_again != 'n':
        clear()
        intro()
    else:
        print("\n\n\n\nCatch ya later!\n\n\n\n")
        time.sleep(1.5)
        clear()
        exit()


def choice_error(choice):

    if choice not in range(1, 4):
        print("You can only pick 1 - 3 sticks. Try again.")
    else:
        return True


def add_knowledge(turns, count, ai_brain, learned_list):
    if turns % 2 == 1 and count == 1:
        return ai_brain[learned_list[0]].append(learned_list[1])


def player_v_ai(ai_knowledge, ai_brain):
    clear()
    print("PLAYER VS. CPU")
    count = 20
    turns = 1

    while count > 1:

        print("\nThere are {} sticks left on the board.".format(count))

        if turns % 2 == 1:
            choice = int(input("Player 1: How many sticks do you take? (1 - 3) "))
            if choice_error(choice) is True:
                count -= choice
                turns += 1

        elif turns % 2 == 0:
            for key in ai_brain:
                if count == int(key):
                    choice = random.choice(ai_brain[key])
                    if count - choice <= 0:
                        choice == 1
                    print('AI chose {}'.format(choice))
                    ai_knowledge = (count, choice)
                    learned_list = []
                    learned_list.append((count, choice))
                    count -= choice
                    turns += 1

    while count <= 1:

        if turns % 2 == 1:
            if count == 1:
                print("\nThere is 1 stick left on the board. Player loses.")
                add_knowledge(turns, count, ai_brain, ai_knowledge)
                play_again_ai(ai_knowledge, ai_brain)
                print(ai_brain)

            if count < 1:
                print("CPU loses.")
                play_again_ai(ai_knowledge, ai_brain)

        elif turns % 2 == 0:
            ai_brain = {}
            for i in range(1, 20):
                ai_brain[i] = [1, 2, 3]
            if count == 1:
                print("\nThere is 1 stick left on the board. CPU loses.")
                play_again_ai(ai_knowledge, ai_brain)

            if count < 1:
                print("That's it! Good luck next time, LOSER!")
                add_knowledge(turns, count, ai_brain, ai_knowledge)
                play_again_ai(ai_knowledge, ai_brain)


def player_v_player():
    clear()
    print("PLAYER VS. PLAYER")
    count = 10
    turns = 1

    while count > 1:
        print("\nThere are {} sticks left on the board.".format(count))

        if turns % 2 == 1:
            choice = int(input("Player 1: How many sticks do you take? (1 - 3) "))
            if choice_error(choice) is True:
                count -= choice
                turns += 1

        elif turns % 2 == 0:
            choice = int(input("Player 2: How many sticks do you take? (1 - 3) "))
            if choice_error(choice) is True:
                count -= choice
                turns += 1

    if count == 1:
        print("\nThere is 1 stick left on the board.")
        choice = int(input("Enter [1] and take the last stick, loser. "))
        if choice != 1:
            print("Good try but there's only 1. YOU LOSE!")
        else:
            play_again_player()

    if count < 1:
        print("That's it! Good luck next time, LOSER!")
        play_again_player()


if __name__ == '__main__':
    intro()
