lower = 0
higher = 100
guess = 0
ans = 'a'

def guess_game():
    global guess, lower, higher, ans
    guess = (higher - lower) / 2
    print "Is your secret number ", guess, "?"
    while ans != 'c':
        ans = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
        if ans == 'l':
            lower = guess
            guess = (higher + lower) / 2
            print "Is your secret number ", guess, "?"
        elif ans == 'h':
            higher = guess
            guess = (higher + lower) / 2
            print "Is your secret number ", guess, "?"
        elif ans == 'c':
            print "Game over. Your secret number was: ", guess
            break
        else:
            print "I'm sorry, I don't understand that command."
            print "Is your secret number ", guess, "?"


print "Please think of a number between 0 and 100!"
guess_game()