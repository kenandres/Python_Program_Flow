print("Please choose your option:")
print("1: Python")
print("2: Java")
print("3: CSS")
print("4: C++")
print("5: Exit")

while True:
    choice = input("Pick your best choice: ")

    if choice == "5":
        print("Bye.")
        break
    elif choice in "12345":
        print("You picked {}.".format(choice))
        break

