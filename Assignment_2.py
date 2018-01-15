############ Assignment 2 ############
        # Functions and loops #



############ Question 1 : ############

## Body Mass Index (BMI) calculator ##

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



############ Question 2 : ############

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



############ Question 3 : ############

## Generates a simple math game of either 10 addition questions, or 10 multiplication questions ##

import random

def game(x,y):
    "This function generates 10 simple math questions"
    operation = int(input("Choose 0) Addition or 1) Multiplication to generate 10 questions: "))
    if operation == 0:
        print("You chose the addition questions. Answer the following 10 questions.")
        counter = 1
        correct = 0
        while counter <= 10:
                question = x + y 
                print(x, "+", y, "= ", end="")
                answer = int(input())
                counter = counter + 1
                if answer == question:
                    correct = correct + 1 
                if answer != question:
                    print("Incorrect -- the answer is", question)
                x = random.randrange(0, 10)
                y = random.randrange(0, 10)
    if operation == 1:
        print("You chose the multiplication questions. Answer the following 10 questions.")
        counter = 1
        correct = 0
        while counter <= 10:
            print(x, "*", y, "= ", end="")
            question = x*y
            answer = int(input())
            counter = counter + 1
            if answer == question:
                correct = correct + 1
            if answer != question:
                print("Incorrect -- the answer is", question)
            x = random.randrange(0, 10)
            y = random.randrange(0, 10)
    return correct;

a = random.randrange(0,10)
b = random.randrange (0,10)
questions = game(a,b) 

print("You have answered", questions, "questions correctly.")
if questions >= 6:
    print("Congratulations!")
if questions < 6: 
    print("Ask your teacher for assistance.")



############ Question 4 : ############

## Generates a simple math game of 10 questions of addition and multiplication ##

import random

def game(x,y,z):
    "Cette fonction genere 10 questions de mathematique de maniere aleatoire"
    print("This is a randomly generated math quiz. Answer the 10 following questions.")
    counter = 1
    correct = 0
    while counter <= 10:
        operation = z
        if operation == 0:
            print(x, "+", y, "= ", end="")
            question = x + y
            reponse = int(input())
            if reponse == question:
                correct = correct + 1
            if reponse != question:
                print("Incorrect -- the answer is", question)
        if operation == 1:
            print(x, "*", y, "= ", end="")
            question = x * y
            reponse = int(input())
            if reponse == question:
                correct = correct + 1
            if reponse != question:
                print("Incorrect -- the answer is", question)
        counter = counter + 1
        z = random.randrange(0, 2)
        x = random.randrange(0, 10)
        y = random.randrange(0, 10)
    return correct


a = random.randrange(0, 10)
b = random.randrange(0, 10)
c = random.randrange(0, 2)
questions = game(a,b,c)

print("You have answered", questions, "questions correctly.")
if questions >= 6:
    print("Congratulations!")
if questions < 6:
    print("Ask your teacher for assistance.")


