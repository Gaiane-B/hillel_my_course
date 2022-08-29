# Number of entered numbers (the final 0 is not counted)
input("Enter the sequence(each number on a new line): ")
now = int(input())
a = 0
while now != 0:
    now = int(input())
    a += 1
print("Number of entered numbers: " + str(a))

# Sum of numbers
input("Enter the sequence(each number on a new line): ")
total = 0
while True:
    a = int(input())
    if a == 0:
        break
    total += a

print("Sum of numbers: " + str(total))

# Product of numbers
input("Enter the sequence(each number on a new line): ")
product = 1
a = int(input())
while a != 0:
    product *= a
    a = int(input())
print("The product of numbers is: ", product)

# Arithmetic mean
input("Enter the sequence(each number on a new line): ")
sum_of_num = 0
len_of_num = 0
element = int(input())
while element != 0:
    sum_of_num += element
    len_of_num += 1
    element = int(input())
print("Arithmetic mean: " + str(sum_of_num / len_of_num))

# Value and ordinal number of the largest element
input("Enter the sequence(each number on a new line): ")
max_number = 0
index_of_max = -1
element = -1
len_of_number = 1
while element != 0:
    element = int(input())
    if element > max_number:
        max_number = element
        index_of_max = len_of_number
    len_of_number += 1
print("Value largest element: " + str(max_number) + ". " + "Ordinal number largest element: " + str(index_of_max) + ".")

# Amount of even and odd elements
input("Enter the sequence(each number on a new line): ")
a = -1
b = -1
odd = 0
while a != 0:
    a = int(input())
    if a % 2 == 0:
        b += 1
    else:
        odd += 1
print("Amount of even elements: " + str(b) + ". " "Amount of odd elements: " + str(odd) + ".")

# Second largest element
input("Enter the sequence(each number on a new line): ")
a = int(input())
max1 = a
max2 = -1
while a != 0:
    a = int(input())
    if a > max1:
        max2 = max1
        max1 = a
    elif a > max2:
        max2 = a
print("Second largest element: " + str(max2))

# How many elements of a sequence are equal to its largest element
input("Enter the sequence(each number on a new line): ")
a = int(input())
max_number = a
b = 0
while a != 0:
    if a > max_number:
        max_number = a
        b = 1
    elif a == max_number:
        b += 1
    a = int(input())
print("Amount of elements in a sequence that are equal to its largest element: " + str(b))
