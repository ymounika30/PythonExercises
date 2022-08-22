##Today's task for you guys will be to develop your first-ever Python game i.e., "Snake Water Gun."
##
##Most of you must already be familiar with the game. Still, I will provide you with a brief description.
##
##This is a two-player game where each player chooses one object.  As we know, there are three objects, snake, water, and gun. So, the result will be 
##
##Snake vs. Water: Snake drinks the water hence wins.
##Water vs. Gun: The gun will drown in water, hence a point for water
##Gun vs. Snake: Gun will kill the snake and win.
##In situations where both players choose the same object, the result will be a draw.
##Now moving on to instructions:
##You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
##You do not have to use a print statement in case of the above function.
##Then you have to give input from your side.
##After getting ten consecutive inputs, the computer will show the result based on each iteration.
##You have to use loops(while loop is preferred).
import random
l1=["snake","water","gun"]
r=random.choice(l1)
print("select 0 for snake, select 1 for water, select 2 for gun")
a=3
while a>0:
    user=int(input())
    if user==0 and l1.index(r)==1:
        print("Snakes drink the water hence wins")
    elif user==1 and l1.index(r)==2:
        print("The gun will drown in wter, hence a point of water")
    elif user==2 and l1.index(r)==0:
        print("Gun will kill the snake and win")
    else:
        print("draw")
a-=1
