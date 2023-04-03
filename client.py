import requests


data="""
The following is a conversation with a mental doctor. The doctor will first ask "How may I help you today?" and then respond to the user's concerns in a professional and empathetic manner.

Doctor: How may I help you today?
User: [user input]
Doctor: [response]
"""
response = requests.post("http://localhost:6000/chatbot", data=data.encode('utf-8'))
print("ChatBot:", response.json()["response"])

while True:
    prompt = input("You: ")
    response = requests.post("http://localhost:6000/chatbot", data={"prompt": prompt})
    response_text = response.json()["response"]
    print("ChatBot:", response_text)
