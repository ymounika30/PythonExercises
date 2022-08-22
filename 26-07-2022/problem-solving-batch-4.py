##write a python program the game of rock,paper and scissor?
##import a random module and do the program 
import random
user=input("enter choice (rock,paper,scissors):")
possible=["rock","paper","scissors"]
computer=random.choice(possible)
print("your choice: ",user, "computer choice: ", computer)
if user==computer:
    print("both selected", user, "It is a tie")
elif user=="rock":
    if computer=="scissors":
        print("You win")
    else:
        print("you lose")
elif user=="paper":
    if computer=="rock":
        print("You win")
    else:
        print("you lose")
elif user=="scissors":
    if computer=="paper":
        print("You win")
    else:
        print("you lose")
    

        
   
