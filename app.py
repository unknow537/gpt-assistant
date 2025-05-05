from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Remplace ceci par ta propre clé API OpenAI
openai.api_key = "your-openai-api-key-here"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150,
        temperature=0.7
    )
    
    ai_message = response.choices[0].text.strip()
    return jsonify({"response": ai_message})

if __name__ == '__main__':
    app.run(debug=True)
