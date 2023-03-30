import requests

# Define the server URL
server_url = "http://localhost:5000/chat"

# Start the conversation with the doctor's greeting
response = requests.post(server_url, json={"message": "Hello"})
response_text = response.json()["response"]
print("Chatbot:", response_text)

while True:
    # Get the user's message
    message = input("You: ")
    # Send the message to the server
    response = requests.post(server_url, json={"message": message})
    # Get the server's response
    response_text = response.json()["response"]
    # Print the response
    print("Chatbot:", response_text)
