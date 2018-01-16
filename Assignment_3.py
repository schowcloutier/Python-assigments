############ Assignment 3 ############
            # Memory game #


#Combination of pre-made code and own code


import random

def shuffle_deck(deck):
    "randomizes the values of the deck to create a playable deck"
    print("Mixing the deck...")
    for i, j in enumerate(deck):
        rand = random.randint(0, len(deck)-1)
        deck[i] = deck[rand]
        deck[rand] = j

#GIVEN CODE
def create_board(size):
    '''Precondition: size is an even, positive integer in [2, 52]
       Returns a playable deck/board of a given size.
    '''
    board = [None]*size
    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board


def create_discovered(board):
    '''creates a list containing the cards with the face * before the player flips them'''
    discovered = [None] * len(board)
    for i in range(len(discovered)):
        discovered[i] = '*'
    return discovered


#GIVEN CODE
def wait_for_player():
    '''()->None
    Game on hold until the player presses on enter
    '''
    input("\nPress on enter to continue. ")
    print('\n'*50)


#GIVEN CODE
def print_board(discovered):
    '''(list of str)->None
       Displays the current board
    '''
    for i in range(len(discovered)):
        print('{0:4}'.format(discovered[i]), end=' ')
    print()
    for i in range(len(discovered)):
        print('{0:4}'.format(str(i+1)), end=' ')



def print_revealed(discovered, p1, p2, original_board):
    '''(liste of str, int, int, liste of str)->None
    DIsplays the new board with two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 have to be integers between 1 and the length of the board
    '''
    for i in range(len(original_board)):
        if i == (p1-1):
            print('{0:4}'.format(original_board[p1-1]), end=' ')
        if i == (p2-1):
            print('{0:4}'.format(original_board[p2-1]), end=' ')
        if i != (p1-1) and i != (p2-1):
            print('{0:4}'.format(discovered[i]), end=' ')
    print()
    for i in range(len(original_board)):
        print('{0:4}'.format(str(i + 1)), end=' ')
    wait_for_player()
    if original_board[p1-1] == original_board[p2-1]:
        discovered[p1-1] = original_board[p1-1]
        discovered[p2-1] = original_board[p2-1]


#############################################################################################
#            FUNCTIONS FOR OPTION 2 (platform (board) imported/read from a file)            #
#############################################################################################

#GIVEN CODE
def read_raw_board(file):
    '''str->list of str
    Retourne une liste de chaines representant la partie (deck) de cartes sauvegardee dans un fichier. 
    La partie(deck) n'est pas necguessrement jouable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str
    Takes a list of strings representing a deck of cards. 
    Returns a new list with the same cards, except that cards 
    that came up a number of odd times are supressed to turn into pair, 
    and cards containing * are supressed.
    '''
    print("\nCleaning up the board...\n")
    playable_board=[]
    for i in range(len(l)):
        if l.count(l[i])%2 == 1:
            l[i]='*'
        elif l[i] != '*':
            playable_board = playable_board + [l[i]]
    return playable_board


def is_rigorous(l):
    '''list de str->bool ou None
    Retourne True si chaque element dans la liste apparait exactement 2 fois ou la liste est vide.
    Sinon, elle retourne False.

    Precondition: Chaque element dans la liste apparait un nombre pair de fois
    '''
    a = sorted(l)
    for i in range(0, len(a)-2, 2):
        if a[i] == a[i+2]:
            return False
    return True



        

####################################################################3

def play_game(board):
    '''(list de str)->None
    Plays the memory game using an existing, playable board (list)
    '''
    shuffle_deck(board)
    wait_for_player()
    original_board = board
    discovered = create_discovered(board)
    print()
    print("Ready to play...")
    print()
    guess = 0
    while discovered != original_board:
        print_board(discovered)
        print()
        print("Enter two distinct positions on the board you would like to reveal (in the range [ 1,", len(discovered), "])")
        p1 = int(input("Enter position 1: "))
        p2 = int(input("Enter position 2: "))
        while (p1 < 1 or p1 > len(original_board)) or (p2 < 1 or p2 > len(original_board)):
                print("You're out of range.\Please try again.")
                print("Enter two distinct positions on the board you would like to reveal (in the range [ 1,", len(discovered), "])")
                p1 = int(input("Enter position 1: "))
                p2 = int(input("Enter position 2: "))
        while p1 == p2:
            print("You have chosen the same position.\nPlease try again. This guess will not count. Your number of guesses is", guess,'.')
            print("Enter two distinct positions on the board you would like to reveal (in the range [ 1,", len(discovered), "])")
            p1 = int(input("Enter position 1: "))
            p2 = int(input("Enter position 2: "))
        while discovered[p1-1] != '*' or discovered[p2-1] != '*':
            print("One or two of these positions has already been discovered.")
            print("Enter two distinct positions on the board you would like to reveal (in the range [ 1,", len(discovered), "])")
            p1 = int(input("Enter position 1: "))
            p2 = int(input("Enter position 2: "))
        guess = guess + 1
        print()
        print_revealed(discovered, p1, p2, original_board)
        print()
    print("Congratulations! You have completed the game in", guess, "guesses. That's", (guess - (len(original_board)//2)),"more than the best result possible.")





#MAIN PROGRAM

print("Ready to play ...\n")
print('*' * 46, '\n*', ' ' * 42, '*', '\n*       __Welcome to my memory game__        *', '\n*', ' ' * 42,'*\n' + '*' * 46)



print("Would you like (enter 1 or 2 to indicate your choice) :\n(1) a generated rigourous deck\n(2) or upload a deck from a file?")
choix = int(input())
while not (choix == 1 or choix == 2):
    print(choix, "isn't an option. Please try again. Enter 1 or 2 to indicate your choice.")
    choix = int(input())

    
    #OPTION 1
if choix == 1:
    print("You have chosen to have a rigourous deck generated for you.\nHow many cards would you like to play with?\nEnter an even integer between 0 and 52: ")
    size = int(input())
    while size%2==1:
        print("Enter an even number between 0 and 52: ")
        size = int(input())
    while size < 2:
        print("Enter an even number between 0 and 52: ")
        size = int(input())
    while size > 52:
        print("Enter an even number between 0 and 52: ")
        size = int(input())
    board = create_board(size)
    play_game(board)


    #OPTION 2
if choix == 2:
    print("You have chosen to upload a deck from a file.")
    file = input("Enter the name of the file: ")
    file = file.strip()
    board = read_raw_board(file)
    if len(board) == 0:
        print("The deck is empty.\nYou can't play without any cards.\nGoodbye.")
        exit()
    board = clean_up_board(board)
    if is_rigorous(board):
        print('*' * 76, '\n*', ' ' * 72, '*', '\n*         __This deck is now playable and rigorous with ' + str(len(board)) + ' cards__         *', '\n*', ' ' * 72, '*\n' + '*' * 76)
    else:
        print('*' * 78, '\n*', ' ' * 74, '*', '\n*        __The deck is now playable but not rigorous with ' + str(len(board)) + ' cards__         *', '\n*', ' ' * 74, '*\n' + '*' * 78)
    play_game(board)
