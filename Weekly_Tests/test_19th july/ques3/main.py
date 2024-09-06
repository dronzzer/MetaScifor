# Nidhi is writing a long program. She needs a function that can check whether a given number is a perfect square or not.
#  To help Nidhi, write a program in python and create a function that checks whether the given number is a perfect square or not.

from sqornot import squarecheck

a=int(input("Enter a number: "))
if squarecheck(a):
    print(f"{a} is perfect square")
else:
    print(f"{a} is not a prefect square")