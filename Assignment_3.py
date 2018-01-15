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
    '''la fonction crée une liste qui contient les cartes avec la face *, avant que le joueur les découvre'''
    discovered = [None] * len(board)
    for i in range(len(discovered)):
        discovered[i] = '*' #pour chaque object dans la liste on remplace avec un '*'
    return discovered #la fonction return cette nouvelle liste



def wait_for_player():
    '''()->None
    Programme/jeu en pause jusqu'a ce que le joueur appuie sur la touche enter
    '''
    input("\nAppuez sur enter pour continuer. ")
    print('\n'*50) #vu que pour clearer la plate-forme cette fonction arrive en même temps, j'ai combiné les deux -- quand le joueur pousse enter, la plate-forme avancec de 50 lignes



def print_board(discovered): #afin de mieux utiliser la fonction d'une façon que je comprends, je prends la liste discovered et je la rentre dans cette fonction
    '''(list de str)->None
       Affiche la plate forme (board) courante dans un format convenable
    '''
    for i in range(len(discovered)):
        print('{0:4}'.format(discovered[i]), end=' ')
    print()
    for i in range(len(discovered)):
        print('{0:4}'.format(str(i+1)), end=' ')




def print_revealed(discovered, p1, p2, original_board):
    '''(liste de str, int, int, liste de str)->None
    Affiche la nouvelle plate forme (board) avec deux nouvelles positions (p1 & p2) revelees a partir de la plate forme (board) d'origine
    Preconditions: p1 & p2 doivent etre des entiers entre 1 et la longueur de board
    '''
     # VOTRE CODE VA ICI
    for i in range(len(original_board)): #avec les input p1 et p2, on imprime un nouveau board
        if i == (p1-1):
            print('{0:4}'.format(original_board[p1-1]), end=' ')
        if i == (p2-1):
            print('{0:4}'.format(original_board[p2-1]), end=' ')
        #où p1 et p2 figurent dans la liste, on imprime les valeurs originaux du board -- donc, les lettres
        if i != (p1-1) and i != (p2-1):
            print('{0:4}'.format(discovered[i]), end=' ')
        #pour les autres positions, on imprime le reste de discovered
    print()
    for i in range(len(original_board)):
        print('{0:4}'.format(str(i + 1)), end=' ')
    #on imprime les chiffres
    wait_for_player()
    #clear la plate-forme
    #ici, on ré-imprime la plate-forme de discovered. si p1 et p2 ont fait une pair, on store les valeurs de original_board dans discovered
    if original_board[p1-1] == original_board[p2-1]:
        discovered[p1-1] = original_board[p1-1]
        discovered[p2-1] = original_board[p2-1]
    #si p1 et p2 ont fait une pair, on store les valeurs de original_board dans discovered


#############################################################################################
#   FONCTIONS POUR OPTION 2 (avec une plate-forme (board) qui sera lue a partir d'un fichier#
#############################################################################################


def read_raw_board(file):
    '''str->list of str
    Retourne une liste de chaines representant la partie (deck) de cartes sauvegardee dans un fichier. 
    La partie(deck) n'est pas necessairement jouable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list de str->list de str
    La fonction prend en entrée une liste de chaînes représentant un paquet de cartes.
    Elle retourne une nouvelle liste contenant les mêmes cartes que l a l'exception
    que chaque carte qui s'affiche un nombre impair de fois dans l est supprimée
    et toutes les cartes avec un * sur leur cote face sont supprimées
    '''
    print("\nEn cours de supprimer chaque carte qui apparait un nombre impair de fois et supprimer toutes les cartes avec * ...\n")
    playable_board=[]
   # VOTRE CODE VA ICI
    for i in range(len(l)):
        if l.count(l[i])%2 == 1: #l.count nous donne combinen de fois une valeur apparaît -- si elle est impair, on transforme une des valeurs d'index l[i] en *
            l[i]='*'
        elif l[i] != '*':
            playable_board = playable_board + [l[i]] #quand l[i] n'est pas un *, on l'ajoute à playable_board
    return playable_board


def is_rigorous(l):
    '''list de str->bool ou None
    Retourne True si chaque element dans la liste apparait exactement 2 fois ou la liste est vide.
    Sinon, elle retourne False.

    Precondition: Chaque element dans la liste apparait un nombre pair de fois
    '''

    # VOTRE CODE VA ICI
    a = sorted(l) #on organise la liste pour que les valeurs identiques se suivent
    for i in range(0, len(a)-2, 2): #vu qu'on analyze combien de paires il y a, la gamme va de 0 à len(a) - 2. on utilise une intervalle de 2; si il y a une deuxième paire, a[i] == a[i+2] (ex: 3(a[0], 3, 3(a[2], 3 = 2 paires parce que a[0]==a[2]. la gamme doit être dans len(a)-2 sinon on dépasse les valeurs de la liste.
        if a[i] == a[i+2]:
            return False
    return True



        

####################################################################3

def play_game(board):
    # c'est la fonction pour jouer le jeu
    # VOTRE CODE VA ICI
    '''(list de str)->None
    Joue le jeu de concentration utilisant un partie (board) existante
    Precondition: Prendre une liste representant une partie (deck) jouable 
    '''
    shuffle_deck(board) #on mélange la liste et on lui assigne à original_board
    wait_for_player()
    original_board = board
    discovered = create_discovered(board) #on crée la variable discovered qui prend la liste de create_discovered(board)
    print()
    print("Prêt à jouer...")
    print()
    essai = 0 #le nombre d'essai commence à 0
    while discovered != original_board: #la boucle dépend sur si la liste discovered est égale à original_board -- donc si toutes les valeurs ont été découvertes et mises en paires
        print_board(discovered) #on commence par imprimer la plate-forme
        print()
        #ici on demande le joueur quelles positions il veut révéler
        print("Entrez deux positions distinctes sur la plate-forme que vous voulez révéler (dans la gamme [ 1,", len(discovered), "])")
        p1 = int(input("Entrez position 1: "))
        p2 = int(input("Entrez position 2: "))
        #il faut rester dans la gamme
        while (p1 < 1 or p1 > len(original_board)) or (p2 < 1 or p2 > len(original_board)):
                print("Vous êtes hors de la gamme.\nVeuillez ré-essayer.")
                print("Entrez deux positions distinctes sur la plate-forme que vous voulez révéler (dans la gamme [ 1,",len(original_board), "])")
                p1 = int(input("Entrez position 1: "))
                p2 = int(input("Entrez position 2: "))
        while p1 == p2:
        #les positions doivent êtres distincts
            print("Vous avez choisi la même position.\nVeuillez ré-essayer. Cet essai ne vas pas compter. Votre nombre d'essai est", essai,'.')
            print("Entrez deux positions distinctes sur la plate-forme que vous voulez révéler (dans la gamme [ 1,", len(discovered), "])")
            p1 = int(input("Entrez position 1: "))
            p2 = int(input("Entrez position 2: "))
        while discovered[p1-1] != '*' or discovered[p2-1] != '*':
        #on ne peut pas choisir une position déjà découverte -- donc, la valeur de original_board serait déja affiché
            print("Une ou les deux positions ont déjà été découvertes.")
            print("Entrez deux positions distinctes sur la plate-forme que vous voulez révéler (dans la gamme [ 1,", len(discovered), "])")
            p1 = int(input("Entrez position 1: "))
            p2 = int(input("Entrez position 2: "))
        essai = essai + 1 #après le input, le nombre d'essais augmente par 1
        print()
        print_revealed(discovered, p1, p2, original_board) #imprime la nouvelle plate-forme
        print()
    print('Bravo! Vous avez complété le jeu en', essai, 'essais. Cela est', (essai - (len(original_board)//2)),'de plus que le meilleur résultat possible.')





#PROGRAMME PRINCIPAL (main)

print("Prêt pour jouer ...\n")
print('*' * 46, '\n*', ' ' * 42, '*', '\n*  __Bienvenue à mon jeu de concentration__  *', '\n*', ' ' * 42,'*\n' + '*' * 46)

   
# VOTRE CODE pour l'option 1 ou l'option 2 du joueur VA ICI

print("Aimeriez-vous (entrez 1 ou 2 pour indiquer votre choix) :\n(1) que je génère une plate-forme rigoureuse\n(2) ou télécharger la partie à partir d'un fichier?")
choix = int(input())
while not (choix == 1 or choix == 2):
    print(choix, "n'est pas une option. Essayez une autre fois. Entrez 1 ou 2 pour indiquer votre choix.")
    choix = int(input())

    
    # VOTRE CODE POUR OPTION 1 VA ICI
if choix == 1:
    # Pour option 1 vous aurrez besoin de faire l'appel suivant:
    # board=create_board(size)
    print("Vous avez choisi d'avoir une plate-forme rigourouse générée pour vous.\nCombien de cartes voulez-vous jouer avec?\nEntrez un nombre paire entre 0 et 52: ")
    size = int(input())
    while size%2==1:
        print("Entrez un nombre paire entre 2 et 52: ")
        size = int(input())
    while size < 2:
        print("Entrez un nombre paire entre 2 et 52: ")
        size = int(input())
    while size > 52:
        print("Entrez un nombre paire entre 2 et 52: ")
        size = int(input())
    board = create_board(size)
    play_game(board)


    # VOTRE CODE POUR OPTION 2 VA ICI
if choix == 2:
    # Pour option 2 vous aurrez besoin de faire executer les 4 lignes suivantes une apres l'autre
    print("Vous avez choisi de charger la partie a partir d'un fichier")
    file = input("Entrez le nom du fichier: ")
    file = file.strip()
    board = read_raw_board(file)
    if len(board) == 0:
        print("La plate-forme est vide.\nVous ne pouvez pas jouer sans cartes.\nAu revoir.")
        exit()
    board = clean_up_board(board)
    if is_rigorous(board):
        print('*' * 76, '\n*', ' ' * 72, '*', '\n*       __Ce jeu est maintenant jouable et rigoureux avec ' + str(len(board)) + ' cartes__       *', '\n*', ' ' * 72, '*\n' + '*' * 76)
    else:
        print('*' * 78, '\n*', ' ' * 74, '*', '\n*  __Ce jeu est maintenant jouable mais n\'est pas rigoureux avec ' + str(len(board)) + ' cartes__  *', '\n*', ' ' * 74, '*\n' + '*' * 78)
    play_game(board)
