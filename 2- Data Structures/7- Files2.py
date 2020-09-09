##7.2 Write a program that prompts for a file name,
##then opens that file and reads through the file, looking for lines of the form:
##X-DSPAM-Confidence:    0.8475
##Count these lines and extract the floating point values from each of the lines and
##compute the average of those values and produce an output as shown below.
##Do not use the sum() function or a variable named sum in your solution.
##You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
##when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name

try:
    fname = input("Enter file name: ")
except:
    print('There is no such a file')
    quit()

count=0
addedNumbers=0
avg=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        count = count + 1
        pos=line.find(':')
        pos= pos + 2
        number = line[pos:]
        number = float(number)
        addedNumbers= addedNumbers + number
        
avg = addedNumbers/count
print('Average spam confidence:', avg)
