from nis import match
import random
'''
"R" for "rock", 
"P" for "paper"
"S" for "scissors"
'''
game_options = ['R','P','S']
user_input = None
cpu_value = None
while True:
    user_input = input('pick an option between R, P & S \n'+ 'R for Rock, P for Paper and S for scissors: ')
    if not user_input in game_options:
        print('value not amongst our options')
        user_input = input('pick an option between R, P & S \n'+ 'R for Rock, P for Paper and S for scissors: ')
    else:       
        cpu_value = random.choice(game_options)
        if user_input == "R" and cpu_value == "S":
            print("You have won and the CPU has lost")
            break
        elif user_input == "P" and cpu_value == "R":
            print("You have won and the CPU has lost")
            break
        elif user_input == "S" and cpu_value == "P":
            print("You have won and the CPU has lost")
            break
        elif user_input == cpu_value:
            print("There is a tie")
            user_input = input('pick an option between R, P & S \n'+ 'R for Rock, P for Paper and S for scissors: ')
        else:
            print("CPU has won")
            break

        