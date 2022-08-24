##Dice  Rolling Simulation: 
##The imitation of rolling dice can be an interesting project for the developers to generate a random number between 1 and 6.
##It is a beginner-level python project that can help in solidifying the foundation for the developers and clearing basic fundamental programming concepts. 
import random
import math
start=1
end=100
user1=0
user2=0
number1=0
number2=0
user1_list=[]
user2_list=[]
snakes=[23,45,67,97]
snakes_landing=[2,11,32,50]
laders=[12,34,56,78]
laders_landing=[30,49,72,98]
game=True
while game:
    user1=input("mounika: ")
    number=random.randint(1,6)
    print(number)
    user1_list+=[number]
    number1=number1+number
    print(user1_list)
    print(number1)
    if number1>=100:
        print("mounika won")
        game=False
    for i in range(4):
        if number1==snakes[i]:
            print("snake is biting mounika")
            number1=snakes_landing[i]
        if number==laders[i]:
            print("Congratulations mounika got ladder")
    if game==True:
        user2=input("ramesh: ")
        number=random.randint(1,6)
        user2_list+=[number]
        number2+=number
        print(user2_list)
        print(number2)
        if number2>=100:
            print("Ramesh won")
            game=False
        for j in range(4):
            if number2==snakes[j]:
                print("snake is bitting ramesh")
                number2=snakes_landing[j]
            if number2==laders[j]:
                print("Congratulations Ramesh got ladder")
                number2=laders_landing[j]
            
        
