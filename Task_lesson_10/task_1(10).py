# Online currency converter

import requests
import calendar
import argparse
import json
from pprint import pprint
from datetime import datetime as dt
from datetime import timedelta


URL = 'https://api.exchangerate.host/convert'


def argument_handling():
    parser = argparse.ArgumentParser(description='Process currency from, currency to, amount, date  '
                                                 'and do you want to save it in file.')

    parser.add_argument('currency_from', metavar='cur_from', default='USD',
                        type=str, help='currency to convert from. Default USD')

    parser.add_argument('currency_to', metavar='cur_to', default='UAH',
                        type=str, help='currency to convert to. Default UAH')

    parser.add_argument('amount', type=float, default=100,
                        help='Amount of money, you want to convert (default: 100)')

    parser.add_argument('--start_date', type=str, default=f'{dt.now().date()}',
                        help='Enter date in format YYYY-MM-DD. Default - today')

    args = parser.parse_args()
    return args


def get_and_check_data_from_json_file(cur_from: str, cur_to: str) -> bool:
    with open('symbols.json', 'r', encoding='utf-8') as symbols:
        data = json.load(symbols)
        if cur_from in data['symbols'] and cur_to in data['symbols']:
            return True
        return False


def check_and_create_date_list(date: str) -> list:
    dates_list = []
    now = dt.now().date()
    if is_valid_date_format_from_user(date):
        user_date = dt(*[int(x) for x in date.split('-')]).date()
        if user_date >= now:
            dates_list.append(now.strftime('%Y-%m-%d'))
            return dates_list
        else:
            while user_date <= now:
                dates_list.append(user_date.strftime('%Y-%m-%d'))
                user_date += timedelta(1)
            return dates_list
    else:
        dates_list.append(now.strftime('%Y-%m-%d'))
        return dates_list


def currency_converter(cur_from: str, cur_to: str, amount: float, date: str):
    if get_and_check_data_from_json_file(cur_from, cur_to):
        valid_date = check_and_create_date_list(date)
        result = [['DATE', 'FROM', 'TO', 'AMOUNT', 'RATE', 'RESULT']]
        for day in valid_date:
            data = requests.get(URL, params={'from': cur_from, 'to': cur_to, 'amount': str(amount), 'date': day})
            response = data.json()
            currency_converter_list = [response['date'], response['query']['from'], response['query']['to'],
                                       response['query']['amount'], response['info']['rate'], response['result']]
            result.append(currency_converter_list)
        return result
    else:
        return print('This is an invalid currency format.')


def is_valid_date_format_from_user(value) -> bool:
    """Expect date in format data in str format %Y-%m-%d"""
    if not value:
        return False

    try:
        year, month, day = [int(value) for value in value.split('-')]
    except Exception:
        return False

    is_valid_year = False
    is_valid_month = False
    is_valid_day = False

    if 1919 < year < 9999:
        is_valid_year = True

    if 0 < month < 13:
        is_valid_month = True

    if all([calendar.isleap(year), month == 2, (0 < day <= 29)]):
        is_valid_day = True
    elif all([calendar.isleap(year), month == 2, (0 < day <= 28)]):
        is_valid_day = True
    elif month in [1, 3, 5, 7, 8, 10, 12] and (0 < day <= 31):
        is_valid_day = True
    elif month in [4, 6, 9, 11] and 0 < day <= 30:
        is_valid_day = True

    return all([is_valid_year, is_valid_month, is_valid_day])


if __name__ == '__main__':
    arg = argument_handling()
    currency_data = currency_converter(arg.currency_from, arg.currency_to, arg.amount, arg.start_date)
    pprint(currency_data)
