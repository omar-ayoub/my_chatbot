import requests
import json

url = 'http://localhost:6000/chatbot'
headers = {'Content-Type': 'application/json'}

while True:
    user_input = input("You: ")
    data = {'input': user_input}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.json()["response"]
        print(f"Chatbot: {response_text}")
    else:
        print("Error communicating with server")
