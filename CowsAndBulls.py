# build the game with the user. 
# instruction:
# randomly generate a 4-digit number. ask the user to guess a 4-digit number. for every digit that the user guessed correctly in the correct place, they have a "cow". for every digit the user guessed correctly in wrong place is a 'bull'. every time the user makes a guess, tell them how many 'cow' and 'bull' they have. once the user guesses the correct number, ther game is over. keep track of the number of guesses the user makes throughout the game and tell the user at the end

import numpy as np
computer_generate = np.random.randint(1000,9999)
list_version = list(str(computer_generate))
#print(list_version)
def cow_and_bull(num):
    
    temp = list(str(num))
    cow = 0
    bull = 0
    for i in range(4):
        if temp[i] == list_version[i]:
            cow +=1
        elif temp[i] in list_version:
            bull +=1

    return cow, bull

if __name__ == '__main__':
    user_input = int(input("please enter a 4-digit number or enter '-1' to quit game: "))
    num_of_guess = 0
    while user_input != computer_generate and user_input != -1:
        num_of_guess += 1
        print("cow: %d, bull: %d" % cow_and_bull(user_input))
        user_input = int(input("try one more or enter 'exit' to leave the game: "))

    print("you've made %d guesses" % num_of_guess)