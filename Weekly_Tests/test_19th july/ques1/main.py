# Chirag, Yugank, and Chris decide to create a python program together.
# But they are not able to understand how they are going to divide the whole program among them.
#  Also, they are confused with the combination process of the program as well.
#   We can divide a big program into smaller parts known as functions.
#   To explain the same thing to three students, write a python program and create different functions to add,
#    subtract, and multiply two numbers.


from addition import add
from subtraction import diff
from multiplication import prod

a=13
b=5
print("The addtion of a and b = ", add(a,b))
print("The difference of a and b = ",diff(a,b))
print("The product of a and b = ",prod(a,b))
