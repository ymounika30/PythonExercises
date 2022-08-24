import itertools
a =[]
b =[]
users_list=[]
combinations=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[3,6,9],[2,5,8],[1,5,9],[3,5,7]]
game=True
while game:
    mounika = int(input("mounika: "))
    while mounika in users_list:
        mounika=int(input("Already enter number choose another number"))
    users_list.append(mounika)
    a.append(mounika)
    print(a)
    chanse = list(itertools.combinations(a,3))
    if len(a) >=3:
        for i in combinations:
            term = list(itertools.permutations(i))
            for j in term:
                if j in chanse:
                    print("mounika win")
                    game=False
    
    if game==True:
        laxmi = int(input("laxmi:"))
        while laxmi in users_list:
            laxmi=int(input("Already enter number choose another number"))
        users_list.append(laxmi)
        b.append(laxmi)
        print(b)
        chanse = list(itertools.combinations(b,3))
        if len(b) >=3:
            for i in combinations:
                term = list(itertools.permutations(i))
                for j in term:
                    if j in chanse:
                        print("laxmi win")
                        game=False
    if len(users_list) >9:
        print("game is Tie")
