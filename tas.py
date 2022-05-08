from pickle import TRUE
import random
play = input("are you ready? y or n")

while TRUE:
    if play == "y":
        x = random.randint(1 , 6)
        print (x)
    else: 
        break
    if x == 6 :
        y=random.randint(1,6)


print (y)