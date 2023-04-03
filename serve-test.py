from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    request_data = request.get_json()
    user_input = request_data['input']
    response = f"Hello, you said: {user_input}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
