import requests

response = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit').json()
data = response['items']

print(data[0].get('volumeInfo', {}).get('title'))