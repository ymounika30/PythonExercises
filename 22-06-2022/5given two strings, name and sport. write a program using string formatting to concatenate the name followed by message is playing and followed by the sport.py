##5. given two strings, name and sport. write a program using string formatting to concatenate the name followed by message "is playing" and followed by the sport
##input: raju
##       cricket
##output: raju is playing cricket
a=input()
b=input()
msg="{arg1} is playing {arg2}"
print(msg.format(arg1=a,arg2=b))
