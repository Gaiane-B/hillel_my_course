# I wrote two options
# First option
a = int(input("Input number of stars: "))
print(a * "*")

# Second option
lines = 1
columns = int(input("Input number of stars: "))
for a in range(lines):
    for b in range(columns):
        print("*", end="")
