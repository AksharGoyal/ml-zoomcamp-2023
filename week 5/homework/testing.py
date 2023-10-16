# This file is check if the communication with homework_app is established or not
import requests

url = 'http://localhost:9696/predict'
customer = {"job": "unknown", "duration": 270, "poutcome": "failure"}
# customer = {"job": "retired", "duration": 445, "poutcome": "success"}

response = requests.post(url, json=customer).json()
print(response)

if response['result'] == True:
    print('sending promo email')
else:
    print('not sending promo email')