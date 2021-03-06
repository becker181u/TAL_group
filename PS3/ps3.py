# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*' : 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):

    word = word.lower()
    first_comp = sum(SCRABBLE_LETTER_VALUES[x] for x in word)
    wordlen = len(word)
    second_comp = 7*wordlen - 3*(n-wordlen)
    if second_comp < 1 : #If the second component is less than 1, the second component is 1
        second_comp = 1
    total = first_comp * second_comp
    if total >= 0  :
        return total
    else :
        return 1
    #1st comp = sum(SCRABBLE_LETTER_VALUES[letters] for letters in word)
    #2nd comp = 7*len(word) - 3*(n-len(word))
    #wordlen = lenght of the word, n = lenght of the hand when word is played
    #def prod = 1st comp * 2nd comp
#print get_word_score.lower

    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys(): #pour chaque lettre dans hand
        for j in range(hand[letter]): #
             print(letter)      # print all on the same line
    print()                          # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """


    hand={'*': 1}
    num_vowels = int(math.ceil(n / 3))-1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    word = word.lower()
    word_dict = get_frequency_dict(word)
    #word_dict est le dictionaire correspondant au mot word
    new_hand =hand.copy()
    for letter in word_dict.keys():
        if letter in hand.keys() and word_dict.get(letter) <= hand.get(letter) :
            if word_dict.get(letter) == hand.get(letter) :
                del new_hand[letter]
            else :
                new_hand[letter] -= 1
        else : #si la lettre de word n'est pas pas dans hand ou si elle y est et que la fréquence dans word et plus grande que dans hand
            if word_dict.get(letter, 0) > hand.get(letter,1) :
                del new_hand[letter]
    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    si la lettre est dans la main, on recommence avec la prochain jusqu'à ce qu'il est plus de lettre
    si toutes les lettres de word sont dans main, return True
    sinon return false

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    index = word.find('*') #on cherche si il y a un astérisque
    if not index == -1 : #si il y a un astérisque dans le mot
        vowel_precedent = "*"
        for vowel in VOWELS :  #pour chaque voyelle présente dans la liste des voyelles
            #word = word.replace(vowel_precedent, vowel, 1)
            list_word = list(word)
            list_word[index] = vowel
            word = "".join(list_word)
            if word in word_list :  #si le word existe dans la word_list
                new_hand = hand.copy()
                del new_hand["*"]
                new_hand[vowel] = 1 #on remplace l'astérisque par la vowel
                word = get_frequency_dict(word) #word est un dictionnaire
                for letter in word.keys():  #on cherche la clé de chaque lettre dans word
                    if (not letter in new_hand.keys()) or word.get(letter) > new_hand.get(letter,0): #si la lettre n'est pas dans la main ou si le nombre de lettre est plus grand que le nombre de cette même lettre dans la main
                        print("You have not got this letter in your hand")
                        return False
                return True
            vowel_precedent = vowel
        return False
    else :
        if word in word_list :  #si le word existe dans la word_list
            word = get_frequency_dict(word) #word est un dictionnaire
            for letter in word.keys():  #on cherche la clé de chaque lettre dans word
                if (not letter in hand.keys()) or word.get(letter) > hand.get(letter,0): #si la lettre n'est pas dans la main ou si le nombre de lettre est plus grand que le nombre de cette même lettre dans la main
                    print("You have not got this letter in your hand")
                    return False
        else :
            return False
    return True


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    #[len(x) for x in hand.values()]
    lenght_hand = sum([x for x in hand.values()])
    # print lenght_hand
    return lenght_hand

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # Keep track of the total score
    total=0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0: #tant qu'il reste des lettres dans la main
        # Display the hand
        display_hand(hand)
        # Ask user for input
        word = input("Enter a word: ") #input word
        # If the input is two exclamation points:
        if word == "!!":
            # End the game (break out of the loop)
            print("You pass to another hand")
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list) : #word = valid
                # Tell the user how many points the word earned,
                # and the updated total score
                word_score = get_word_score(word,calculate_handlen(hand))
                print("score du mot : ", word_score) #score displayed
                total += word_score
                print("Total : ", total)

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
            else: #word = invalid word
                print("Incorrect word, input another word")
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print("You haven't got any letter on your hand, Total score of this hand is : ", total)
    # Return the total score as result of function
    return total


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    new_hand = hand.copy()
    x = False
    if letter not in hand:
        print("The letter is not in the hand")
        return hand #si la lettre donnée par le joueur n'est pas dans la main, la main ne change pas
    while x == False:
        new_letter = random.choice(VOWELS + CONSONANTS)

        if new_letter not in hand:
            del new_hand[letter]
            new_hand[new_letter] = hand.get(letter, 1)
            x = True

    return new_hand

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', he will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    x = input("Start a new party?")
<<<<<<< HEAD
    if x == "yes" or x == "y":
        y = int(input("How many hand would you play?"))
=======
    if x == "yes":
        y = int(input("How many hand would you play?")) #demande au joueur combien de mains il veut jouer.
>>>>>>> 66eb024acf3d76c5018baa4bf32c60cd7e0fdadb
        total_score = 0
        substitue_game = False
        replay_hand = False
        for i in range(y): #le jeu continue tant que le nombre de mains n'est pas atteint
            print()
            hand = deal_hand(HAND_SIZE)
            print("Your hand is ",hand)
            if not substitue_game: #tant que le joueur ne veut pas substituer une lettre
                want_substitue = input("Do you want to substitute a letter ?")  #...retourne la question
                if want_substitue == "yes":  #si le joueur veut substituer une lettre:
                    letter_substitue = input("Which letter do you want to substitute ?") #Demande au joueur quelle lettre il veut substituer
                    hand = substitute_hand(hand,letter_substitue) #indique la lettre à substituer
                    substitue_game = True #cette question ne peut être posée qu'une seule fois par jeu
            total = play_hand(hand, word_list) #enregistre le total de chaque main
            if not replay_hand: #tant que le joueur ne veut pas rejouer la même main
                want_replay = input("Do you want to replay the hand?") #...retourne la question
                if want_replay == "yes": #si le joueur veut rejouer la main
                    total_bis = play_hand(hand, word_list) #affiche le score
                    if total_bis > total : #sélectionne le meilleur score
                        total = total_bis
            total_score += total #additionne les différents totaux pour obtenir le score total
            print("Current total score:",total_score) #affiche le score après chaque main
        print("Game over, your total score is : ", total_score) #affiche le score en fin de partie
        return total_score






#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':

    word_list = load_words()
    play_game(word_list)
