import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url)

print(f'Status code: {response.status_code}')

data = response.json()
print('Response JSON:')
print(data)