#math.ceil(x):-
#return the ceiling of x,the smallest integer greaterthan or equal to x.If x is not a float,delegates
# to x.__ceil(),which should return an interval value.
import math  # import lib math first
x=10.5
print(math.ceil(x))  #output11

b=13.9
print(math.ceil(b))

c=13.1
print(math.ceil(c))

e=  -13.9
print(math.ceil(e))

#math.fabs:--> always give you positive
d=  -13.9
print(math.fabs(d))  #always give u positive value when u put -ve its convert into +ve using fabs


#math.factorial(x):-Return x factorial as an integer.Raises Value Error if x is not integral or is negative
x=5
print(math.factorial(x))

#math.floor-> Return the floor of x,the largest integer less than or equal to x.If x is not a float,
#delegates to x.__floor__(),which should return an integral value.

x=9.7
print(math.floor(x))

#math.fsum(iterable):-
#return an accurate floating point sum of values in the iterable.
l=[10,20,40,30,50]
print(math.fsum(l))

#math.sqrt(x)):
#Return the square root of x.
print(math.sqrt(144)) #give the value of sqrt directly
 #https://docs.python.org/3.7/library/math.html

