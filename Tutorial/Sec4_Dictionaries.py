##Like the list and the tuple, dictionary is also a collection type.
##However, it is not an ordered sequence, and it contains key-value pairs.
##One or more key:value pairs separated by commas are put inside curly brackets
##to form a dictionary object.

capitals = { "Iran": "Tehran", "USA": "NewYork", "Germany": "Berlin"}
print(capitals);

#The key should be an immutable object. A number, string or tuple can be used
#as key but not Lists!

##The same key cannot appear more than once in a collection. If the key appears
##more than once, only the last will be retained. The value can be of any
##data type. One value can be assigned to more than one key.
##

#Accessing a Dictionary: Get()

capitals.get("Iran");
capitals.get("Japan", "none") # when you want to make sure that if you hadnt the key
#it still returns a default value ( none ) but not error.



for key in capitals:
    print("Key = " + key + ", Value = " + capitals[key])

#Update:
capitals['Iran']= 'Shiraz'
print(capitals)

#Delete a key or whole the dictionary:

##del capitals['Iran']
##del capitals

# View Keys and Values and Items:
capitals.keys()
capitals.values()
capitals.items()
# all return the results as a list object, items() return a list of tuples


# bulit-in methods;
len(capitals) # number of pairs key:value
max(capitals)
min(capitals)
capitals.clear() # make it empty
capitals2 = {"Turkey":"Ankara"} # assign the capitals2 to capitals1
capitals.update(capitals2)
print(capitals)


#for-loop
dict={ 1:100, 2:200, 3:300 }
for pair in dict.items():
    print (pair)

dict={ 1:100, 2:200, 3:300 }
for k,v in dict.items():
    print("key=" + k + ", value=" + v)

dict={1:100, 2:200, 3:300}
for k in dict.keys():
    print(k, dict.get(k))
