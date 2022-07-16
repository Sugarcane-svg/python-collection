# in the second part of hangman game. 
# a clue word is given by the program that the player has to guess, letter by letter.
# the player guesss one letter at a time until the entire word has been guessed.

# write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.bonus: keep track of the letters the player guessed and display a different massage of the player tries to guess the same letter again.


import Hangman_1 as h1

if __name__ == '__main__':

    print('Welcome to Hangman!')
    word = h1.pickword()
    s = '_ '* len(word)
    print(s)

    b = len(word)
    # 
    while b > 0:
        new_guess = input('Guess your letter: ').upper
        if new_guess not in word.upper:
            print("Incorrect!")
            new_guess = input("Guess your letter: ").upper
        else:
            indexes = []
            for i in range(len(word)):
                if word[i] == new_guess:
                    indexes.append(i)
            
            for j in indexes:
                s[2*j-1] = new_guess
            
            b = b-len(indexes)
            

