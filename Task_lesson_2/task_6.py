# I wrote two options
# First option
a = abs(float(input()))
my_list = range(10, 101, 10)
if a in my_list:
    print("Yes")
else:
    print("No")

# Second option
a = abs(float(input())) in range(10, 101, 10)
print(a)
