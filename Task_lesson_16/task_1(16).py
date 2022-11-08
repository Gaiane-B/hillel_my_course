# Check, if a string is a car number

import re


def check_car_number():
    user_input = input("Enter a car number: ")
    convert_letters = {'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н', 'I': 'І', 'K': 'К', 'M': 'М', 'O': 'О',
                       'P': 'Р', 'T': 'Т', 'X': 'Х'}
    correct_number_format = re.search(r'^[AKBCEHIMOPTXАКВСЕНІМОРТХ]{2}\d{4}(?<!0{4})[AKBCEHIMOPTXАКВСЕНІМОРТХ]{2}$',
                                      user_input)
    if correct_number_format:
        return 'This is the car number'
    else:
        return 'This is not a car number'


print(check_car_number())
