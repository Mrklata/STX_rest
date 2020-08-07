import requests
import pandas as pd


def get_all_books():
    data = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')
    data_items = data.json()['items']
    df = pd.json_normalize(data_items)
    print(df)


get_all_books()
