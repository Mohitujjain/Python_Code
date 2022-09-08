#Python Random randint() Method
#Return a number between 5 and 10 (both included):
import random
print(random.randint(5,10))

#returns a number between3 (included) and 9(not included)
print(random.randrange(3,9))

#Python Random choice() Method
#return a random element from a list:
l=["apple","banana","cherry"]
print(random.choice(l))

p=[10,20,30,30,38]
pc=random.choice(p)
print(pc)

# Random module:
#random(): Returns a random float number between 0 and 1.
#shuffle():Takes a sequence and returns the sequence in a random order.
#uniform():returns a random float number between two given parameters.
#random();
r=random.random()
print(r)

#shuffle();
q=[10,20,30,30,38]
random.shuffle(q)
print(q)

#uniform();
u=random.uniform(3,9)
print(u)

