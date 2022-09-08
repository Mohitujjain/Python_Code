import random
rnumber=random.randrange(1,101)
userInput=int(input("Enter Your Number:---"))
if userInput>rnumber:
    print("Computer Number",rnumber)
    print("Your guess number is too high")
elif rnumber>userInput:
    print("Computer Number",rnumber)
    print("Your guess number is too low")
else:
    print("Computer Number", rnumber)
    print("Your guess number equal")