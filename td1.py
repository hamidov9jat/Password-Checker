import requests

url = 'https://api.pwnedpasswords.com/range/' + '75403'
res = requests.get(url)

print(res)
