# Number: Python includes three numeric types to represent numbers: integer, float, and complex.

# Exponent: a**b

# Devision: a/b
 a = 21
 b = 10
 a/b
# 2.1

##Floor Devision:
 a=9
 b=2
 c=a//b
 c
##4


# Built in functions:
##int	Returns the integer object from a float or a string containing digits.
##float	Returns a floating-point number object from a number or string containing digits with decimal point or scientific notation.
##complex	Returns a complex number with real and imaginary components.
##hex	Converts a decimal integer into a hexadecimal number with 0x prefix.
##oct	Converts a decimal integer in an octal representation with 0o prefix.
##pow	Returns the power of the specified numbers.
##abs	Returns the absolute value of a number without considering its sign.
##round	Returns the rounded number.

#//////////////////////////////////////////////////////////////////////////

#Sequenc: A sequence is defined as an ordered collection of items.
#1) String:
 myString='hello'
 myString[0]
##'h'
 myString[1]
##'e'
 myString[4]
##'o'

##The string is an immutable object. Hence, it is not possible to modify it. The attempt to assign different characters at a certain index results in errors.
##
##>>> myString[1]='a'
##TypeError: 'str' object does not support item assignment

myString.capitalize()
# Hello
myString.upper();
# HELLO
myString.lower();

 mystr='python tutorial from tutorials teacher'
 mystr.title()
#'Python Tutorial From Tutorials Teacher'

 mystr='Python Tutorial From Tutorials Teacher'
mystr.find('From')
 # 16
 mystr.find('xyz')
# -1

# number of occurance of something in string
mystr='Python Tutorial From Tutorials Teacher'
 mystr.count('Tutorial')

 str1='2000'
 str1.isdigit()
#True
str2='2,000'
 str2.isdigit()
#False
