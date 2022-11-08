# Convert phone number to correct format

import re


class CorrectPhoneNumber:

    def __init__(self, user_number: str):
        self.user_phone_number = user_number
        self.correct_phone_number = re.sub(r'\D', '', self.user_phone_number)
        self.new_number = self.create_new_number()

    def create_new_number(self):
        if len(self.correct_phone_number) < 13:
            change_phone_format = re.sub(r"^(.*?)(0\d{2})(\d{3})(\d{2})(\d{2})$", r"(+38) \2 \3-\4-\5",
                                         self.correct_phone_number)
            return change_phone_format
        else:
            return self.user_phone_number


if __name__ == '__main__':
    user_number_input = str(input('Enter your phone number please:'))
    number = CorrectPhoneNumber(user_number_input)
    print(number.create_new_number())
