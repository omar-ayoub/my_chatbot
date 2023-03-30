from flask import Flask, request, jsonify ,render_template
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

# Initialize conversation history
history = []

# Define a function to generate response
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def generate_response(prompt):
    # Append the user's message to the conversation history
    history.append("Human: " + prompt)
    # Concatenate the conversation history to use as prompt
    prompt = "I am your psychiatrist, I am here to help, and you can ask me anything you want and I will answer".join(history)
    # Call OpenAI's GPT-3 API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + start_sequence,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    # Get the response text
    response_text = response.choices[0].text.strip()
    # Append the response to the conversation history
    history.append("AI: " + response_text)
    # Return the response
    return response_text

# Define a route to receive chat requests
@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's message from the request
    message = request.json["message"]
    # Generate a response using the user's message as prompt
    response = generate_response(message)
    # Return the response as JSON
    return jsonify({"response": response})


@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)
