available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse Pad",
                   "HDMI Cable",
                   "Optical Drive"
                   ]

# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        print("Removing {}".format(current_choice))
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add option from the list below: ")
        for part in available_parts:
            # .index returns the index of the specified element in the list
            print("{0}: {1}".format(available_parts.index(part) + 1, part))

    # Or you can do this instead
    # else:
    # print("Please add option from the list below: ")
    # for number, part in enumerate(available_parts):
    #     print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)
