from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

# Define a function to generate response
def generate_response(prompt):
    # Call OpenAI's GPT-3 API
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Return the response
    return response.choices[0].text.strip()

# Define a route to receive chat requests
@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's message from the request
    message = request.json["message"]
    # Generate a response using the user's message as prompt
    response = generate_response(message)
    # Return the response as JSON
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()
