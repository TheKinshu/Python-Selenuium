import os

file = open('.\\OOP\\test.txt')

#print(file.readline())
#print(file.readline())

line = file.readline()

while line != '':
    print(line)
    line = file.readline()

file.close()
