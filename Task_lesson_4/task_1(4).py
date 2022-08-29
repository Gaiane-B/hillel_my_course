x = int(input("Enter athlete's mileage: "))
y = int(input("Enter athlete's distance: "))
c = 1
while x < y:
    x = x * 1.1
    c = c + 1
print(c)
