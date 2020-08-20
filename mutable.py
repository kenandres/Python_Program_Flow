shopping_list = new_list = ["milk",
                 "sugar",
                 "spam",
                 "eggs",
                 "bread",
                 "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["siomai"]
print(shopping_list)
print(id(shopping_list))
print("New Line")

# .append method adds item to the list
shopping_list.append("Siopao")
new_list.append("Noodles")
print(new_list)
