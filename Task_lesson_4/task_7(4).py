# Numbers in first and second list
list_1 = input("Enter the list one: ")
list_2 = input("Enter the list two: ")
result = list(set(list_1) & set(list_2))
print("Numbers in first and second list: " + str(result))

# Numbers that are present in first list but not in second list
list_1 = input("Enter the list one: ")
list_2 = input("Enter the list two: ")
result = list(set(list_1) - set(list_2))
print("Numbers that are present in first list but not in second list: " + str(result))

# Unique numbers for the first and second list
list_1 = input("Enter the list one: ")
list_2 = input("Enter the list two: ")
result = list(set(list_1) ^ set(list_2))
print("Unique numbers for the first and second list: " + str(result))
