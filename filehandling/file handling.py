##Opening in read mode
'''
f = open('student.txt', mode='r', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##========================================================
##Opening in write mode
'''
f = open('student.txt', mode='w', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##======================================================
##Text Mode and Binay Mode
'''
f = open('student.txt', mode='w')
f.write('Hello\n')
f.write('hiii\n')
f.write('How are you')
f.close()
print('Writing Success')

f = open('student.txt', mode='r')
data = f.read()
print(data)
f.close()

f = open('student.txt', mode='rb')
data = f.read()
print(data)
f.close()
'''
##=====================================================================
##Opening in append mode
'''
f = open('student.txt', mode='a', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##====================================================================
# Open for writing and then reading
'''
f = open('student.txt', mode='w+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##=========================================================================
# Open for reading and then writing
'''
f = open('student.txt', mode='r+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##===================================================================
# Open for reading and then writing
'''
f = open('student.txt', mode='r+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##=================================================================
# Open for binary reading
'''
f = open('pythona.jpg', mode='rb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##=============================================================
# Open for binary Writing
'''
f = open('pythona.jpg', mode='wb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##===================================================
# Open for Binary Appending
'''
f = open('pythona.jpg', mode='ab')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##============================================================
# Open for Binary Exlusive Creation
'''
f = open('pythona1.jpg', mode='xb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##============================================================
# Open for Binary reading and then writing
'''
f = open('pythona1.jpg', mode='rb+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##============================================================
# Open for Binary writing and then reading
'''
f = open('pythona.jpg', mode='wb+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##=============================================================
# Open for Binary Appending and then reading
'''
f = open('pythona.jpg', mode='ab+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''
##============================================================
'''
import os
print(os.path.isfile('student.txt'))
'''
##===========================================================
'''
import os
if os.path.isfile('student.txt'):
	f = open('student.txt')
	print('File Opened')
	f.close()
else:
	print('File Not Found')
'''
##=======================================================
# Writing Data with w mode Example 1
'''
f = open('student.txt', mode='w')
f.write('Hello')
f.write('how are you.!!')
f.write('How are you')
f.close()
print('Success')
'''
##==========================================================
# Writing Data with w mode Example 2
'''
f = open('student.txt', mode='w')
f.write('Hello ')
f.write('Great.! ')
f.write('How are you')
f.close()
print('Success')
'''
##==========================================================
# Writing Data with w mode
'''
f = open('student.txt', mode='w')
f.write('Hello\n')
f.write('great.!\n')
f.write('How are you')
f.close()
print('Success')
'''
##===============================================================
# Writing Data with x mode
'''
f = open('student4.txt', mode='x')
f.write('Hello\n')
f.write('great.!!\n')
f.write('How are you')
f.close()
print('Success')
'''
##===============================================================
# Writing Data with a mode
'''
f = open('student.txt', mode='a')
f.write('Hello\n')
f.write('great.!\n')
f.write('How are you')
f.close()
print('Success')
'''
##==================================================================
# Writing Data with w mode
'''
f = open('student.txt', mode='w')
lst = ['Rahul', 'Sonam', 'Sumit', 'Rani', 'Raj']
f.writelines(lst)
f.close()
print('Success')
'''
##=============================================================================
# Writing Data with w mode
'''
f = open('student.txt', mode='w')
lst = ['Rahul\n', 'Sonam\n', 'Sumit\n', 'Rani\n', 'Raj\n']
f.writelines(lst)
f.close()
print('Success')
'''
##=================================================================================
# Writing Data with a mode
'''
f = open('student.txt', mode='a')
lst = ['Rahul\n', 'Sonam\n', 'Sumit\n', 'Rani\n', 'Raj\n']
f.writelines(lst)
f.close()
print('Success')
'''
##====================================================================================
# Reading Data with r mode
'''
f = open('student.txt', mode='r')
data = f.read()
print(data)
f.close()
print('Completed!!!!')
'''
##==========================================================================================
# Reading Data with r mode
'''
f = open('student.txt', mode='r')
data1 = f.read(2)
data2 = f.read(2)
print(data1)
print(data2)
f.close()
'''
##========================================================================================
# Reading Data with r mode
'''
f = open('student.txt', mode='r')
data1 = f.readline()
data2 = f.readline()
print(data1)
print(data2)
f.close()
'''
##=======================================================================================
# Reading Data with r mode
'''
f = open('student.txt', mode='r')
data = f.readlines()
print(data)
for i in data:
	print(i, end='')
f.close()
'''
