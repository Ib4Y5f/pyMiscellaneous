import requests

url = 'https://w3schools.com/python/demopage.htm'
print('Only printting response Header')
print(requests.get(url))
print(50*'-')
print('printting response body')
print(requests.get(url).text)
