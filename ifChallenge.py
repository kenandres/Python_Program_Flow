name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Welcome to the club, {0}!".format(name))
elif age < 18:
    print("Please come back in {0} years.".format(18 - age))
else:
    print("Sorry, {0}, you're not welcome here.".format(name))
