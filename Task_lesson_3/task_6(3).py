x1 = int(input("Vertical position 1: "))
y1 = int(input("Horizontal position 1: "))
x2 = int(input("Vertical position 2: "))
y2 = int(input("Horizontal position 2: "))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print("YES")
else:
    print("NO")
