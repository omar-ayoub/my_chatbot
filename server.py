import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = "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" # Replace with your OpenAI API key

model_engine = "text-davinci-002" # Replace with the model engine you want to use

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/chatbot", methods=["POST"])
def chatbot():
    prompt = "You are talking to your personal doctor. How may I help you today?" + request.form["prompt"]
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(debug=True,port=6000)
