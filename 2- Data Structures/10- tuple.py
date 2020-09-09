##10.2 Write a program to read through the mbox-short.txt and figure out the
##distribution by hour of the day for each of the messages. You can pull
##the hour out from the 'From ' line by finding the time and then splitting
##the string a second time using a colon.
##From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
##Once you have accumulated the counts for each hour, print out the counts,
##sorted by hour as shown below.


try:
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
except:
    print('error in the file name')
    quit()

handle = open(name)
dicCount= dict()
lstHour= list()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    else:
        pieces = line.split()
        hour= pieces[5]
        hourpieces = hour.split(":")
        h=hourpieces[0]
        
        lstHour.append(h)
        
for key in lstHour:
    dicCount[key] = dicCount.get(key, 0)+1
    
    

for key,value in sorted(dicCount.items()):
    print(key,value)
#print(sorted([ (key, value) for key,value in dicCount.items()]))
