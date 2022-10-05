# Function counts the duration of all tracks in album

import json
import time


def count_the_duration_all_tracks():
    all_duration = 0
    with open('acdc.json') as file:
        data_from_file = json.load(file)['album']['tracks']['track']
    for element in data_from_file:
        all_duration += int(element['duration'])
        result = time.gmtime(all_duration)
        return time.strftime('%H:%M:%S', result)


print(f"The duration of all tracks 'AC/DC' in album 'Back in Black' is {count_the_duration_all_tracks()}.")
