a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
if a < b:
    for c in range(a, b+1, 1):
        print(c)
else:
    for c in range(a, b-1, -1):
        print(c)
