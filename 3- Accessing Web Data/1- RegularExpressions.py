## In this assignment you will read through and parse a file with text and
#numbers. You will extract all the numbers in the file and compute the sum of
#the numbers.

##
##The basic outline of this problem is to read the file, look for integers using
##the re.findall(), looking for a regular expression of '[0-9]+' and then
##converting the extracted strings to integers and summing up the integers. 



import re
##try:
##    fname = input("Enter file name: ")
##except:
##    print('There is no such a file')
##    quit()
    
fh = open('regex_sum_792627.txt')
numList=list()
for line in fh :
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    numList = numList+x

sum=0
for num in numList:
    sum = sum + int(num)

print(sum)
x=input('type any key')
