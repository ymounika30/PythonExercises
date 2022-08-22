a=int(input())
note_1000=0
note_500=0
note_100=0
note_50=0
note_20=0
note_5=0
note_1=0
note_1000=a//1000
a=a%1000
note_500=a//500
a=a%500
note_100=a//100
a=a%100
note_50=a//50
a=a%50
note_20=a//20
a=a%20
note_5=a//5
a=a%5
print("note_1000: "+str(note_1000))
print("note_500: "+str(note_500))
print("note_100: "+str(note_100))
print("note_50: "+str(note_50))
print("note_20: "+str(note_20))
print("note_50: "+str(note_5))
print("note_1: "+str(a)
