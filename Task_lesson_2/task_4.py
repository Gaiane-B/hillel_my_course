# Just in case, I wrote three options
# First option
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")

# Second option
def check_leap_year(y):
    if (y % 4) == 0:
        return "YES"
    if (y % 100) == 0:
        return "NO"
    if (y % 400) == 0:
        return "YES"
    else:
        return "NO"

# Third option
def check_leap_year(y):
    if (y % 4) == 0 or (year % 400) == 0:
        return "YES"
    if (y % 100) == 0:
        return "NO"
    else:
        return "NO"
    
