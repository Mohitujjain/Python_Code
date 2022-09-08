"""name = "Mohit"
age = 26

name = "Duggu"
age = 12

print(name)
print(age)
# Add a person with name Tony Stark. Tony's age is 51yrs old.Tony is genius.
first_name = "Mohit"  #example 1
last_name = "Singh"
age = 26
is_adult = True

print(first_name + " " + last_name)
print(age)
print(is_adult)

first_name = "Tony"   ## example 2
last_name = "Spark"
age = 13
is_adult = False

print(first_name + " " + last_name)
print(age)
print(is_adult)

name = input("What is your name? ")
print("Hello " + name)

# Tony is secretly a superhero. Ask him for his  superhero name & show it on the terminal.
old_age = input("enter your old age : ")
new_age = int(old_age) + 3
print(new_age)

number = 18
print(float(18))

# example of sum
first = input("enter first number : ")
second = input("enter second number : ")
sum = int(first) + int(second)
print("the sum is : " + str(sum))

name = "Mohit Singh"
print(name.upper())
print(name)

name = "Mohit Singh"
print(name.lower())
print(name)

name = " Mohit Singh"
print(name.find('S'))

name = "Duggu Babu"
print(name.replace("Babu" , "DugDug"))
print(name)

name = "Mohit Singh"
print('S' in name)

print(5 // 2)
print(5 % 2)
print(5 ** 2)

i = 5
i = i + 2 
i += 2
i -= 2
i *= 2

result = 2 + 3 * 5
print(result)

#print(3 >= 2)
#print(3 != 2)

# print(2 > 3 or 2 >1 )
# print(4 > 3 and 2 >1 )
# print(not 3 > 2)

# example if -else
age = 19

if age >= 18:
    print("you are an adult")
    print("You can vote")
print("thank you")

age = 13

if age >= 18:
    print("you are an adult")
    print("You can vote")
elif age < 18 and age > 3:
    print(" you are in school")
else:
    print(" you are child")
# lets build a calculator
# a +b , a-b, a*b, a/b, a%b, mini calculator project
first = input("enter first number : ")
operator = input("enter operator (+,-,*,%,/) :")
second = input("enter second number :")

first =int(first)
second=int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")

number = range(5) #0,1,2,3,4,5
print(number)

##LOOP
i = 1
while i <= 5:
    print(i)
    i = i +1

i = 1
while i <= 5:
    print(i * "*")
    i = i +1

i = 1
while i <= 5:
    print(i * "hello")
    i = i +1

i = 5
while i >= 0:
    print(i * "*")
    i = i - 1

# for loop
for item in range(5):
    print(item + 1)

#list
marks = [95,98,97]
print(marks)

marks = [95,98,97]
print(marks[-1])

marks = [95,98,97]
print(marks[1:3])

marks = [98,89,90]

for score in marks:
    print(score)

marks = [98,89,90]

marks.append(99)
print(marks)

marks = [98,89,90]

marks.insert(0,99)
print(99 in marks)

marks = [98,89,90] 

marks.insert(0,99)
print(len(marks))

marks = [95, 98, 97]

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

marks.clear()
print(marks)

students = ["Ram","Shayam","krishna","Radhe","Mohan"]

for student in students:
    if student == "Radhe":
        break;
    print(student)

students = ["Ram","Shayam","krishna","Radhe","Mohan"] # continue

for student in students:
    if student == "krishna":
        continue;
    print(student)

# Tuple
marks = (95,98,97,97)
print(marks.count(97))

marks = (95,98,97,97)
print(marks.index(97))

marks = { 95, 98,97,97} # set

for score in marks:
    print(score)

# Dict
marks = {"english": 96, "chemistry":98}
print(marks["chemistry"])
marks["physics"] = 97;
print(marks)

marks["physics"] = 99;
print(marks) """

# function
#In-built function, #Module function, # user defined function

from math import sqrt
print(sqrt(16))

# def function_name(parameters):
def print_sum(first, second):
    print(first + second)

print_sum(1,2)


















