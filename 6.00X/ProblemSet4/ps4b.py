from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    best_score = 0

    # Create a new variable to store the best word seen so far (initially None)
    best_word = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        dict_word = getFrequencyDict(word)
        def test_word(hand, word):
            if word == {}:
                return True
            letter = word.keys()[0]
            if letter in hand:
                if word[letter] <= hand[letter]:
                    del word[letter]
                    return True and test_word(hand, word)
                else:
                    return False
            else:
                return False

        if test_word(hand, dict_word):
            # Find out how much making that word is worth
            temp_score = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if temp_score > best_score:

                # Update your best score, and best word accordingly
                best_score = temp_score
                best_word = word

    # return the best word you found.
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """

    # Keep track of the total score
    score = 0
    
    # As long as there are still letters left in the hand:
    while compChooseWord(hand, wordList, n) != None:
    
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)

        word = compChooseWord(hand, wordList, n)

        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
        points = getWordScore(word, n)
        score += points
        print '"' + str(word) + '"', 'earned', points, "points. Total:", score, "points"
        print
        
        # Update the hand
        hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if len(hand) > 0:
        print "Current Hand: ",
        displayHand(hand)
    print "Total score:", score, 'points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE
    hand = ''

    def second_choice():
        second_choice = str(raw_input("Enter u to have yourself play, c to have the computer play: "))
        if second_choice == 'c':
            print
            compPlayHand(hand, wordList, n)
        elif second_choice == 'u':
            print
            playHand(hand, wordList, n)
        else:
            print "Invalid command."
            print
            second_choice()

    first_choice = str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))

    while first_choice != 'e':
        if first_choice == "n":
            hand = dealHand(n)
            print
            second_choice()
            print
            first_choice = str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        elif first_choice == 'r':
            if hand == '':
                print "You have not played a hand yet. Please play a new hand first!"
                print
                first_choice = str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
            else:
                print
                second_choice()
                print
                first_choice = str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        else:
            print "Invalid command."
            print
            first_choice = str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))

        
#
# Build data structures used for entire session and play game
#
# if __name__ == '__main__':
#     wordList = loadWords()
#     playGame(wordList)

wordList = loadWords()
# print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
# print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
# print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
# print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)

# print compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
# print compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
# compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
# compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 8)
