################## Assignment 2 ##################
# Functions and loops #


############## Question 1 : ##############

#### Body Mass Index (BMI) calculator ####

def bmi(kg, m):
    "This function calculates the body mass index of the user based on input values of weight and height"
    index = kg/(m**2)
    return index;

kg = float(input("Enter your weight in kilograms: "))
m = float(input("Enter your height in metres: "))
BMI = bmi(kg, m) 

# determining where user's BMI lies on the scale #

print("Your BMI is: ", BMI)
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25: 
    print("Normal weight")
elif 5 <= BMI < 30:
    print("Overweight")
else:
    print("Obesity")


############## Question 2 : ##############

## Prints the integers in the range [a, b] ##

def integers(x, y):
    "This functions creates a list containing the integers in the range [a, b]"
    counter = 0 
    l = [ ] 
    while counter <= (y-x): 
        integer = x + counter 
        l.append(integer) 
        counter = counter + 1
    for i in l: 
        print(i)

a = int(input("Enter an integer for a: "))
b = int(input("Enter an integer for b: "))
integers(a, b) 



############## Question 3 : ##############

## Prints the integers in the range [a, b] ##

import random



#la fonction

def jeu(x,y):
    "Cette fonction genere 10 questions de mathematique"
    operation = int(input("Choisissez l'operation 0) Addition ou 1) Multiplication pour generer 10 questions: "))
    if operation == 0: # les instructions pour les questions d'addition
        print("Vous avez choisi les exercices d'addition. Donnez les reponses aux 10 questions suivantes.")
        compteur = 1 # on ajoute un compteur afin que la boucle genere 10 questions seulement
        bonne = 0
        while compteur <= 10:
                exercice = x + y #la bonne reponse qui se fera comparer avec le input
                print(x, "+", y, "= ", end="") #end="" s'assure que le input sera sur la meme ligne que la question
                reponse = int(input()) #la reponse que l'etudiant input dans le programme
                compteur = compteur + 1
                if reponse == exercice: #si true: bonne (nombre de bonnes reponses) + 1; si c'est la mauvaise reponse bonne restera comme sa valeur la plus recente
                    bonne = bonne + 1 
                if reponse != exercice:
                    print("Incorrect -- la reponse est", exercice) #si l'etudiant a la mauvaise reponse on indique quelle etait la bonne reponse
                x = random.randrange(0, 10) #pour la prochaine boucle les valeurs de x et y changent pour un autre nombre aleatoire
                y = random.randrange(0, 10)
    if operation == 1: #les instructions pour les questions de multiplication, comme pour ceux d'addition
        print("Vous avez choisi les exercices de multiplication. Donnez les reponses aux 10 questions suivantes.")
        compteur = 1
        bonne = 0
        while compteur <= 10:
            print(x, "*", y, "= ", end="")
            exercice = x*y
            reponse = int(input())
            compteur = compteur + 1
            if reponse == exercice:
                bonne = bonne + 1
            if reponse != exercice:
                print("Incorrect -- la reponse est", exercice)
            x = random.randrange(0, 10)
            y = random.randrange(0, 10)
    return bonne;



#les variables

a = random.randrange(0,10) # a et b sont des valeurs entre 0 et 9
b = random.randrange (0,10)
questions = jeu(a,b) #cette variable appelle la fonction avec les parametres ci-dessus et prend la valeur de "bonne"




print("Vous avez eu", questions, "reponses correctes.")

if questions >= 6: #si l'eleve a bien repondu a six questions
    print("Feliciations!")
if questions < 6: #si l'eleve a bien repondu a moins de six questions
    print("Demandez a votre enseignant(e) de vous aider.")




