import datetime
import functools

import requests
import validators

import Configuration_file
import sending_mail

now = datetime.datetime.now().date()
WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
message_to_recipient = 'Hello, {}! Today, {}, in the {} city the temperature is {}°C, {} {}, and humidity is {}%. Have a nice day and good luck to you!'


# Function get data by API from url
@functools.lru_cache
def get_data_from_my_url(url):
    response = requests.get(url)
    data = response.json()
    return data


# Function checks e_mails for validity
def email_check(function):
    def wrapper(*args, **kwargs):
        valid_emails = []
        result = function(*args, **kwargs)
        for element in result:
            if validators.email(element['e_mail']):
                valid_emails.append(element)
        return valid_emails

    return wrapper


# Function-decorator
def send_weather_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        final_list_to_send = {}
        for element in result:
            if type(element) == dict and 'e_mail' in element and 'city' in element:
                if element['city'] not in final_list_to_send:
                    final_list_to_send.update({element['city']: {element['e_mail']}})
        for city in final_list_to_send:
            element = get_data_from_my_url(WEATHER_API.format(city_name=city))
            summary_string = Configuration_file.message_to_recipient.format(element['name'], now, element['city'],
                                                                            element['main']['temp'],
                                                                            element['weather'][0]['main'],
                                                                            Configuration_file.weather_emoji[
                                                                                element['weather'][0]['icon']],
                                                                            element['main']['humidity'])
            sending_mail.sending_mails(final_list_to_send[city], summary_string)

    return wrapper


@send_weather_decorator
@email_check
# Function sending weather to recipient
def sending_weather_to_recipient(url):
    new_data = get_data_from_my_url(url)['data']
    return new_data


sending_weather_to_recipient(Configuration_file.MAILING_LIST_URL)
