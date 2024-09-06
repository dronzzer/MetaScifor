# Sahil is wondering whether we can use the same concept of functions in creating simple and compound interest calculators.
#  He is trying to create it but is unable to return the answers from the functions. Help him in doing the same


from simple_i import simpleint
from compound_i import compoundint


p=int(input( " Enter the principle amount:  "))
r=int(input( " Enter the rate of intrest:  "))
t=int(input( " Enter the time (in years):  "))

print(simpleint(p,r,t))
print(compoundint(p,r,t))

