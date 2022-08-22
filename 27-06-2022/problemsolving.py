##IPL MATCH DETAILS:-
##
##write a program that reads all the match outcomes and summarizes the information of all the matches.Points are given to the teams based on the outcome of the match.A win esrns a team 3 points.
#A draw earns 
##1.A loss earns O.
##The following info is expected:
##
##MP:Matches played
##W:Matches Won
##D:Matches Drawn(Tied)
##L:Matches Lost
##P:Points
##
##The team info should be displayed in descending order of points
##
##INPUT
##----
##
##The first line contains a single integer N,denoting the total no.of matches played.The following N lines contains outcomes of N matches.
##
##Each of those lines has info on the teams(T1,T2)which played and the outcome(O)in format T1;T2;O.
##
##The outcome(O)is one of 'win','loss','draw' and refers to the first team instead.see sample Input/output for better understanding.
##
##The team name may contain spaces.
##
##OUTPUT
##------
##
##The output should contain summarized info of all the matches in a format similar to 'Team:RCB,Matches played:3,Won:2,Lost:0,Draw:1,Points:7'for each team in anew line.
##
##If there  are no teams to print in summary,print "No Output".
##
##Constraints
##-----------
##
##Names of teams may contain spaces but will be less than 24 characters
##
##100>=N>=0
##
##
##Sample Input:-
##-------------
##
##6
##CSK;RCB;loss
##RCB;DD;draw
##MI;KKR;win
##KKR;RCB;loss
##CSK;DD;draw
##MI;DD;draw
##
##Sample output
##-------------
##
##Team:RCB,Matches played:3,Won:2,Lost:0,Draw:1,Points:7
##Team:MI,Matches played:2,Won:2,Lost:0,Draw:1,Points:4
##Team:DD,Matches played:3,Won:2,Lost:0,Draw:3,Points:3
##Team:CSK,Matches played:2,Won:0,Lost:1,Draw:1,Points:1
##Team:KKR,Matches played:2,Won:0,Lost:2,Draw:0,Points:0
matches = int(input("enter number of matches: "))
RCB = [0,0,0]
MI = [0,0,0]
DD = [0,0,0]
CSK = [0,0,0]
KKR = [0,0,0]
rcb,mi,dd,csk,kkr = 0,0,0,0,0
for i in range(matches):
    team1 = input("enter team1: ")
    team2 = input("enter team2: ")
    result = input("who won the match: ").upper()
    if result == "RCB":
        RCB[0] += 1
        rcb += 1
    elif result=="Draw":
        RCB[2]=1
        rcb+=1
    else:
        RCB[1] += 1
        rcb += 1
    if result=="MI":
        MI[0]+=1
        mi+=1
    elif result=="Draw":
        MI[2]+=1
        mi+=1
    else:
        MI[1]=1
        mi+=1
    if result=="KKR":
        KKR[0]+=1
        kkr+=1
    elif result=="Draw":
        KKR[2]+=1
        kkr=1
    else:
        KKR[1]+=1
        kkr+=1
    if result=="DD":
        DD[0]+=1
        dd+=1
    elif result=="Draw":
        DD[2]+=1
        dd+=1
    else:
        DD[1]+=1
        dd+=1
    if result=="CSK":
        CSK[0]+=1
        csk+=1
    elif result=="Draw":
        CSK[2]+=1
        csk+=1
    else:
        CSK[1]+=1
        csk+=1
print(f"Matches played {rcb}, Won {RCB[0]}, Lost {RCB[1]}, Draw {RCB[2]}, points {RCB[0]*3}")
print(f"Matches played {mi}, Won {MI[0]}, Lost {MI[1]}, Draw {MI[2]}, points {MI[0]*3}")
print(f"Matches played {dd}, Won {DD[0]}, Lost {DD[1]}, Draw {DD[2]}, points {DD[0]*3}")
print(f"Matches played {csk}, Won {CSK[0]}, Lost {CSK[1]}, Draw {CSK[2]}, points {CSK[0]*3}")
print(f"Matches played {kkr}, Won {KKR[0]}, Lost {KKR[1]}, Draw {KKR[2]}, points {KKR[0]*3}")
