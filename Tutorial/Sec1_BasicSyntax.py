help('keywords')

# enter is an end to a statement:
msg="Hello World"
code=123
name="Steve"



#However, you can use / to use enter but still continue the statement
msg1="Hello Pythonista \
Welcome to Python Tutorial \
from TutorialsTeacher.com"



#Similarly, use the semicolon ; to write multiple statements in a single line.
msg="Hello World";code=123;name="Steve"



##Python uses uniform indentation to denote a block of statements.When a block is to be started, type the colon symbol (:) and press Enter.
##Any Python-aware editor (like IDLE) goes to the next line leaving an additional whitespace (called indent).
##Subsequent statements in the block follow the same level of indent. In order to signal the end of a block,
##the whitespace is de-dented by pressing the backspace key. If your editor is not configured for Python,
##you may have to ensure that the statements in a block have the same indentation level by pressing the spacebar or Tab key.
##The Python interpreter will throw an error if the indentation level in the block is not same.



# press Alt + 3 to comment many lines



# The input() function always reads the input as a string, even if comprises of digits.
name = input('Enter Your Name: ')
print(name)



##Dynamic Typing:
# A variable in Python is not bound permanently to a specific data type.
##Instead, it only serves as a label to a value of a certain type. Hence, the prior declaration of variable's data type is not possible.
##In Python, the data assigned to a variable decides its data type and not the other way around.

name = 'Steve'
type(name)
name=123
type(name)
#We can see that the data type of a variable has now been changed to integer. This is why Python is called a dynamically-typed language.



