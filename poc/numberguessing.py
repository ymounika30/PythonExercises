##Number Guessing:  
##Python beginners can start with number guessing projects that can be exciting and offer a good learning experience.
##The mini-game can include random numbers between 1 to 10, 1 to 100, etc. followed by a hint so that users can guess the right numbers.
##A simple game will include the major forms of numbers including divisible, multiples, and other combinations. 
import random
import math
lower=int(input())
upper=int(input())
x=random.randint(lower,upper)
print("\n\tYou've only", round(math.log(upper-lower+1,2))," chances to guess the integer!\n")
count=0
while count<math.log(upper-lower+1,2):
    count+=1
    guess=int(input())
    if x==guess:
        print("Conngratulations you did it in", count, "try")
        break
    elif x>guess:
        print("You guessed too small!")
    elif x<guess:
        print("You guessed too high!")
if count >= math.log(upper-lower+1,2):
    print("\n The number is %d" %x)
    print("\t Better Luck Next Time!")
