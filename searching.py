shopping_list = ["milk", "sugar", "spam", "eggs", "bread", "rice"]

# item_to_find = "spam"
# found_at = None
#
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#
# print("Item found at position {}".format(found_at))

item_to_find = "eggs"
found_at = None

# for index in range(6):
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position: {}".format(found_at))
else:
    print("'{}' not found".format(item_to_find))
