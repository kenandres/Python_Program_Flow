pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)
print()
numbers = [2.3, 4.2, 5.2, 7.3, 8.2, 1.2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "Michelle"
         ]
names.sort(key=str.casefold)
print(names)
