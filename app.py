
from flask import Flask, render_template, request, jsonify
import openai
import os

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY", "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")

app = Flask(__name__)

def get_bot_response(user_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_text},
            ]
        )
        message = response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        message = str(e)
    return message

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("user_input")
    bot_response = get_bot_response(user_input)
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
