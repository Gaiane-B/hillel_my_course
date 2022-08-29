# I wrote two options
# First option
number = int(input("Enter number n: "))
for a in range(number):
    for b in range(1, a + 2):
        print(b, end="")
    print("")

# Second option
number = int(input("Number n < or = 9. Enter number: "))
a = 0
if number <= 9:
  for a in range(1, number + 1):
    for b in range(1, a+1):
      print(b, end="")
    print("")
