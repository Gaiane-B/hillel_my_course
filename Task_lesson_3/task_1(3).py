# I wrote two options
# First option
number = int(input())
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)

# Second option
number = int(input())
print(number // 100 + number // 10 % 10 + number % 10)
