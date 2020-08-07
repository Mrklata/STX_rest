import json

import requests
import pandas as pd


def get_all_books():
    data = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit').json()
    data_items = data['items']

    print(data_items[0])


get_all_books()
