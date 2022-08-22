##create a-z  of 26 files and write a different sentence in each file and delete all files by using os module
##filenames should be 1.a.file,2.b.file........26.z.file
##in each file each sentence is to start with character of  its own filename
##after entering data delete all the files

for i in range(97,97+26):
    filename=chr(i)+".txt"
    with open (chr(i)+".txt","w") as f:
        f.writelines(str(i))
