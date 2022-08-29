a = [int(b) for b in input("Enter a list of integers separated by a space: ").split()]
count = 0
for c in range(1, len(a) - 1):
    if a[c-1] < a[c] > a[c+1]:
        count += 1
print(count)
