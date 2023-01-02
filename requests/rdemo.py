import requests

payload = {
    'username':'kwabena', 'password':'testing'
}



url = "http://httpbin.org/delay/2"
response = requests.get(url)


print(response)
