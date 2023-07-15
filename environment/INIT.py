print("Hello, world")
print("python has three numeric data types: float, int, complex")
myvalue=1
print(myvalue)
print(type(myvalue))
print(str(myvalue) + " is of the data type " + str(type(myvalue)))
myvalue=3.142
print(myvalue)
print(str(myvalue) + " is of the data type " + str(type(myvalue)))


print("hello" +"wolrd")

import csv
import copy

myvehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in myvehicle.items():
    print("{} : {}". format(key,value))


userReply = input("Do you need to ship a package?(Enter yes or no)")
if userReply =="yes":
    print("wecan help you ship the package!")
else:
    print("please come back when you need to ship a package.Thankyou.")

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
    
    
    
import random
number = random.randit(1,10)
isGuessRight =False
while isGuessRight !=True:
    while isGuessright != True:
        guess =input("Guess a number between 1 and 10:")
        if int(guess) == number:
            print("You guessd{}.That is correct! You win!".format(guess))
            isGuessRight =True
        else:
            print("You guessed {}. sorry, that isn't it. Train better".fomat(guess))
        for x in range (0,11):
            print(x)
            