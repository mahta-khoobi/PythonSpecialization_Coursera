# Python - List:
names=["Jeff", "Bill", "Steve", "Mohan"]

L1=[1,2,3]
L2=[4,5,6]
print(L1+L2)


L1=[1, 2, 3, 4, 5, 6]
4 in L1

L1=[1, 2, 3, 4, 5, 6]
4 not in L1

len(L1)
max(L1)
min(L1)

L1.append(7)
print(L1)

#insert with index
L1.insert(0,0)
print(L1)

##L1.remove(1)
##
##L1.pop()
##
##L1.reverse()
##
##L1.sort()

#convert a tuple to list
tup= (1,2,3)
lst=list(tup)

#convert a list to tuple
tpl=tuple(L2)


#forloop
for item in L1:
    print(item)
