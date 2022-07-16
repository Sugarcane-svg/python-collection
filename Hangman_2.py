# in the second part of hangman game. 
# a clue word is given by the program that the player has to guess, letter by letter.
# the player guesss one letter at a time until the entire word has been guessed.

# write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.bonus: keep track of the letters the player guessed and display a different massage of the player tries to guess the same letter again.


from re import A
import Hangman_1 as h1

if __name__ == '__main__':

    print('Welcome to Hangman!')
    word = h1.pickword()
    s = ('_ '* len(word)).split()
    print(" ".join(s))

    b = len(word)
    # 
    while b > 0:
        new_guess = (input('Guess your letter(upper case only): '))
        if word.find(new_guess) == -1:
            print("Incorrect!")
        else:
            indexes = []
            for i in range(len(word)):
                if word[i] == new_guess:
                    indexes.append(i)

            for j in indexes:
                s[j] = new_guess

            b = b-len(indexes)
        print(" ".join(s))
    print("Well Done!")
            

