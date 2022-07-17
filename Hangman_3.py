
import Hangman_1 as h1

def is_guess_in_word(guess):
    if word.find(guess) == -1:
            return False

    return True

def get_indexes(guess):
    indexes = []
    for i in range(len(word)):
        if word[i] == guess:
            indexes.append(i)

    return indexes

def update_str(indexes):
    for j in indexes:
        if new_guess not in set(s):
            s[j] = new_guess

    return s

def is_duplicated(guess):
    if guess in set(s):
        return True
    return False

if __name__ == '__main__':
    # print out title
    print('Welcome to Hangman!')

    # randomly pick a word
    word = h1.pickword()
    
    # get the length of the word
    b = len(word)
    # total guessing time
    t = 6

    """if length of word is greater than total guess time, the player is never going to guess the complete word, so the word length should equal or shorter than the guessing time"""
    while b > t:
        word = h1.pickword()
        b = len(word)
    print(word)
    # after get the new word, the word position and length is printed
    s = ('_ '* len(word)).split()
    print(" ".join(s))

    # guess time and word length should be greater than 0
    while b > 0 and t > 0:
        # make guess
        new_guess = (input('Guess your letter(upper case only): '))
        
        # check if guess is in word
        if is_guess_in_word(new_guess):
            # check is duplicated
            if is_duplicated(new_guess):
                # to cancel out the reduced guess time
                t = t+1
                print("duplicate guess, guess again")
            else:
                # word does not garantee to have unique letter
                index_list = get_indexes(new_guess)
                
                # update the string to current state
                s = update_str(index_list)

                # reduce the length since some character is inserted
                b = b-len(index_list)

        else:
            print("Wrong guess")

        # reduce guess time
        t = t-1
            
        print(" ".join(s) + "\n" + "Remaining Guesses: %d" %t)
        

        
    if b > t:
        print("Out of guess")   
    else:
        print("You guess the word!")

        

   


