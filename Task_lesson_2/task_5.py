# I wrote two options
# First option
x = int(input("sign(x): "))
if x > 0:
    print("sign(x)=", 1)
elif x == 0:
    print("sign(x)=", 0)
else:
    print("sign(x)=", -1)

# Second option
def number_sign_function(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
