# */

# /*

# Stone, Paper, Scissors Game
from random import randint
import random

for i in range(10):
    com = randint(1, 3)
    print(com)
    user = int(input("Enter; 1 for Stone, 2 for Paper & 3 for Scissor: "))

    if com == user:
         print("Game Tied !")
    else:
        if com == 1 and user == 2:
            print("User Wins!")
        elif com == 2 and user == 3:
            print("User Wins!")
        elif com == 3 and user == 1:
             print("User Wins!")
        else:
            print("Computer Wins!")
            #  if com == 1:
            #     print("Computer chose Stone.")
            # elif com == 2:
            #      print("Computer chose Paper.")
            # elif com == 3:
            #     print("Computer chose Scissor.")