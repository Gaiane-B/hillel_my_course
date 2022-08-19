# I wrote two options
# First option
import random
num = random.randint(0, 10)
print("Number:", num)
attempt = 3
msg = "You lose!"

while attempt > 0:
    user_input = int(input("Enter Number: "))

    if user_input == num:
        msg = "You won!"
        break
    else:
        print(f"{attempt - 1} attempt left.")
        attempt -= 1
        continue

print(msg)

# Second option
import random
num = random.randint(1, 10)
print("Enter Number from 1 to 10")
attempt = 3
msg = "You lose!"

while attempt > 0:
    user_input = int(input("Your number: "))

    if user_input == num:
        msg = "You won!"
        break
    else:
        print(f"{attempt - 1} attempt left.")
        attempt -= 1
        continue

print(msg)
