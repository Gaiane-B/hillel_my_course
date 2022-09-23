import requests
import Msg
import datetime
now = datetime.datetime.now().date()
emoji = '\U0001F947'
URL = 'https://script.google.com/macros/s/AKfycbxgEsflPph1UiTe-PWbhWkNCK4hNsgRKsITJMS_kClHeF_kY7um92g0L6Ex7ox7wnWa/exec'

###


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


###


# Function check students scores
def student_scores(data, min_student_score=90, max_student_score=100):
    """
    Function check, student score is in range of 90 to 100
    data: this is the input data from which we need to extract the elements and process them
    param data: we have a list from our url
    min_student_score: minimum allowable student score
    param min_student_score: int
    max_student_score: maximum allowable student score
    param max_student_score: int
    return: returns items (as a list) with a score in range of 90 to 100
    """
    my_new_list = []
    for element in data:
        if min_student_score < element['score'] > max_student_score:
            my_new_list.append(element)
    return my_new_list


# Function check students rewards
def check_student_rewards(data, has_rewards=True):
    """
    Function checks, the students truly has rewards
    data: this is the input data from which we need to extract the elements and process them
    param data: we have a list from our url
    has_rewards: checking the rewards parameter
    param has_rewards: True
    return: returns the elements (as a list) where has_rewards = True
    """
    my_new_list = []
    for element in data:
        if element['has_rewards'] == has_rewards:
            my_new_list.append(element)
    return my_new_list


# Function check students age
def student_age_check(data, min_student_age=9, max_student_age=18):
    """
    Function check, student age is in range of 9 to 18
    data: this is the input data from which we need to extract the elements and process them
    param data: we have a list from our url
    min_student_age: minimum allowable student age
    param min_student_age: int
    max_student_age: maximum allowable student age
    param max_student_age: int
    return: returns elements (as a list) with an age in range of 9 to 18
    """
    my_new_list = []
    for element in data:
        if min_student_age < element['age'] < max_student_age:
            my_new_list.append(element)
    return my_new_list


# Function create string
def create_string(data):
    """
    Function forms a string from the selected data.
    data: List of dictionaries to which the text element should be added
    return: list with added element
    """
    for element in data:
        element['message'] = Msg.STUDENT_WITH_REWARD.format(now, element['name'], emoji, element['score'], element['notes'])
    return data


###
def text_to_dict(data):
    """
    data: get a list of dictionaries, from which we select the "message" element and add it to a separate list
    return: element we want
    """
    new_list = []
    for element in data:
        new_list.append(element['message'])
        continue
    return new_list


#
def add_to_file(data):
    """
    Function writes received text in file
    data: element 'message'
    return: write element in file
    """
    for element in data:
        add_text_data(text_data=element + '\n')
        continue
    return data

