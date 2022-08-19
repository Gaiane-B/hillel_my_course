# Fractional part
user_number = input()
fractional_part = user_number.split(".")
print(fractional_part[1])


# First number after dot

number = float(input())
print(int(number * 10) % 10)
