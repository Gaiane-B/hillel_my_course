import requests
import pprint

URL = 'https://script.google.com/macros/s/AKfycbxgEsflPph1UiTe-PWbhWkNCK4hNsgRKsITJMS_kClHeF_kY7um92g0L6Ex7ox7wnWa/exec'

response = requests.get(URL)
data = response.json()
pprint.pprint(data)


def get_data(url=None):
    ...
