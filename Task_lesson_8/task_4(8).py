# Function returns current time and decorator takes 3 seconds

import time


def current_time(func):
    def wrapper():
        count_down = 3
        while count_down > 0:
            time.sleep(1)
            print(count_down)
            count_down -= 1
        return func()

    return wrapper


@current_time
def what_time_is_at_the_moment():
    return time.strftime('%H:%M')


print(what_time_is_at_the_moment)

