a=int(input("enter a number"))
board1=1
board2=2
board3=3
board4=4
board5=5
board6=6
board7=7
board8=8
board9=9
l=[]
for i in range(1,a+1):
    b=int(input("enter the number"))
    l.append(b)
    if b==board1:
        print(f"|{l[0]}| | | | |")
        print(f"| | | | | |")
        print(f"| | | | | |")
    if b==board2:
        print(f"|{l[0]}| |{l[1]} | | |")
        print(f"| | | | | |")
        print(f"| | | | | |")
    if b==board3:
        print(f"|{l[0]}| |{l[1]} | |{l[2]} |")
        print(f"| | | | | |")
        print(f"| | | | | |")
    if b==board4:
        print(f"|{l[0]}| |{l[1]} | |{l[2]} |")
        print(f"|{l[3]} | | | | |")
        print(f"| | | | | |")
    if b==board5:
        print(f"|{l[0]}| |{l[1]} | |{l[2]} |")
        print(f"|{l[3]} | |{l[4]} | | |")
        print(f"| | | | | |")
    if b==board6:
        print(f"|{l[0]}| |{l[1]} | |{l[2]} |")
        print(f"| {l[3]}| | {l[4]}| | {l[5]}|")
        print(f"| | | | | |")
    if b==board7:
        print(f"|{l[0]}| |{l[1]} | | {l[2]}|")
        print(f"| {l[3]}| | {l[4]}| |{l[5]} |")
        print(f"| {l[6]}| | | | |")
    if b==board8:
        print(f"|{l[0]}| |{l[1]} | |{l[2]} |")
        print(f"| {l[3]}| |{l[4]} | |{l[5]} |")
        print(f"| {l[6]}| |{l[7]} | | |")
    if b==board9:
        print(f"|{l[0]}| |{l[1]} | | {l[2]}|")
        print(f"| {l[3]}| | {l[4]}| |{l[5]} |")
        print(f"| {l[6]}| | {l[7]}| |{l[8]} |")


