# Function returns a dict where each key is the index of the list, and the value of the list is the value of the key

my_list = ['a', 'b', 'c', 'd', 'e']


def list_in_dict(list_of_values) -> dict:
    new_dict = dict(enumerate(list_of_values))
    return new_dict


print(list_in_dict(my_list))
