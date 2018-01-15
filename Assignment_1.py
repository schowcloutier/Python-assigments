############ Assignment 1 ############
# Practice with using math functions #



############ Question 1 : ############

#### Pounds to kilograms converter ####

lb = float(input("How many pounds? "))
on = float(input("How many ounces? "))
kg = (0.453592*lb ) + (0.0283495*on)
print(lb, "pounds and", on, "ounces is equivalent to", kg, "kilograms.")



############ Question 2 : ############

## Pounds to kilograms converter (function) ##

def conversion(lb, on):
    "This functions calculates how many  kilograms make (X) pounds and (X) ounces"
    kg = (0.453592*lb ) + (0.0283495*on)
    return kg;

lb = float(input("Combien de livres? "))
on = float(input("Combien d'onces? "))
kg = conversion(lb, on)

print(lb, "pounds and", on, "ounces is equivalent to", kg, "kilograms.")



############ Question 3 : ############

#### Change calculator ####

money = 100*(float(input("How many dollars of change need to be returned? ")))

q = money//25
d = (money%25)//10
n = ((money%25)%10)//5
p = ((money%25)%10)%5
change = int(q+d+n+p)

print("The cashier has to return: ", change, "pieces of change.")



############ Question 4 : ############

#### Change calculator (function) ####  

def pieces_of_change(money):
    "Cette fonction calcule le nombre minimal de pieces"
    q = money//25
    d = (money%25)//10
    n = ((money%25)%10)//5
    p = ((money%25)%10)%5
    change = int(q+d+n+p)
    return change;
    

money = 100*(float(input("Quel est le montant en dollars? ")))
change = pieces_of_change(money)

print("Le caissier doit rendre: ", change, "pieces de monnaie.")



############ Question 5 : ############

#### Light year calculator #### 

# a)
def y_in_s(sidereal):
    "This functions calculates the number of seconds in a light year"
    s = (365.26*sidereal)*86400
    return s
sidereal = float(input("Enter the number of sidereal years: "))
seconds = y_in_s(sidereal)
print("The number of de light seconds is: ", seconds, "s")

# b)
def s_in_km(seconds):
    "This function calculates the distance traveled by light"
    km = seconds*300000
    return km
distance = s_in_km(s)
print("The distance traveled is: ", distance, "km")

# c)
def stars_in_km(star1, star2):
    "This function calculates the distance between two stars"
    s = y_in_s(star1 + star2)
    km = s_in_km(s)
    return km
star1 = float(input("Enter the distance between the first star and Earth: "))
star2 = float(input("Enter the distance between the second star and Earth: "))
km = stars_in_km(star1, star2)
print("The distance between the two stars is: ",km, "km")


    
