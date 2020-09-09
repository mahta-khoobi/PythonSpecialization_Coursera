#Functions:

def HelloWorld():
    print('Hello World!')
    return

HelloWorld()

# function with default argument
def DivideNumbers(a,b=1):
    return(a/b)

print(DivideNumbers(6,3))
print(DivideNumbers(3))
    

#Lambda Function: Anonymous functions
# The def keyword is used to define a function in Python.
##The lambda keyword is used to define an anonymous functions in Python.
##Usually, such a function is meant for one-time use

##The lambda function can have any number of arguments but there's always a
##single expression after the : symbol. When this function is called,
##the expression is its return value

square = lambda x: x*x
# or
#print(lambda x: x*x)
square(3)

sum = lambda x,y,z: x+y+z
print(sum(1,2,3))


##Lambda functions are useful when we want to give the function as one of the
##arguments to another function. In Python, the function is a first order object,
##which means that just as number, string, list, etc. the function can also
##be used as an argument.
##Python has built-in functions which take other functions as arguments.
##The map(), filter() and reduce() functions are important functional programming
##tools. All of them take a function as their argument.
##The argument function can be a normal function or a lambda function.
