from typing import Any
import requests
URL = 'https://script.google.com/macros/s/AKfycbxgEsflPph1UiTe-PWbhWkNCK4hNsgRKsITJMS_kClHeF_kY7um92g0L6Ex7ox7wnWa/exec'


# Check: a number not less than 0, and not more than 100
def is_number_in_range(my_number: int, minimum=int(0), maximum=int(100)) -> bool:
    """
    Check, is the my_number not less than minimum, and not more, than maximum
    my_number: number to check
    minimum: minimum range value
    maximum: maximum range value
    If my_number is in range maximum - minimum, function returns: True
    Otherwise, the function returns: False
    """
    if minimum <= my_number <= maximum:
        return True
    return False


# Check: input argument is an integer number
def is_arg_an_integer(arg: Any) -> bool:
    """
    Check, is input argument an integer number
    arg: input argument
    param arg: Any
    return: True or False
    """
    if type(arg) == int:
        return True
    return False


# Get data from url and converts to json format
def get_data_from_url(my_url: str = None) -> dict:
    """
    Function converts link to json format
    my_url: given url in string format
    return: data from my_url in json format
    """
    response = requests.get(my_url)
    data = response.json()
    return data


# Return valid length string
def valid_length_string(my_string: str, length: int = 150):
    """
    Function takes a string, checks its length and returns a string, if the length does not exceed the allowed value
    according to the specified argument. If the length more the allowed value according to the specified argument,
    function return cut string and ...
    my_string: string to check
    length: maximum number of characters; int > 0
    return: my_string or cut my_string and ...
    """
    if len(my_string) <= length:
        return my_string
    if len(my_string) > length:
        new_string = my_string[:length - 3] + '...'
        return new_string


# Function adds text data to a file
def add_text_data(name_of_file: str = 'HILLEL_Task_lesson_5.txt', text_data=''):
    """
    Function add text data in file
    name_of_file: name of chosen file, type - str (string)
    text_data: text data to be added
    return: no return, only saving data to a file
    """
    with open(name_of_file, 'a') as file:
        file.write(text_data + '\n')
    file.close()


# Assert: a number not less than 0, and not more than 100
assert is_number_in_range(50) is True
assert is_number_in_range(105) is False
# Assert: input argument is an integer number
assert is_arg_an_integer(5) is True
assert is_arg_an_integer('five') is False

