

##9.4 Write a program to read through the mbox-short.txt and figure out who has
##sent the greatest number of mail messages. The program looks for 'From ' lines
##and takes the second word of those lines as the person who sent the mail.
##The program creates a Python dictionary that maps the sender's mail address
##to a count of the number of times they appear in the file.
##After the dictionary is produced, the program reads through the dictionary
##using a maximum loop to find the most prolific committer


try:
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
except:
    print('error in the file name')
    quit()

handle = open(name)
dicCount= dict()
lstEmail= list()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    else:
        pieces = line.split()
        email= pieces[1]
        lstEmail.append(email)
        
for key in lstEmail:
    dicCount[key] = dicCount.get(key, 0)+1
        

bigValue=None
bigKey=None

for key,value in dicCount.items():
    if bigValue is None or value > bigValue:
        bigValue= value
        bigKey= key
        
print(bigKey, bigValue)
        
        
