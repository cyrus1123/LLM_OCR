from flask import Flask, request, jsonify, render_template, session
import requests
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session handling

# Define the URL for the chat model
url = "http://localhost:11434/api/generate"

# Load chat UI
@app.route('/chat', methods=['GET'])
def display_chat():
    return render_template('chat.html')

# Handle chat messages and image uploads
@app.route('/submit', methods=['POST'])
def handle_chat():
    message = request.form.get('message')
    file = request.files.get('image')
    extracted_text = None

    if file and file.filename != '':
        filepath = os.path.join("/tmp", file.filename)
        file.save(filepath)

        try:
            image = Image.open(filepath)
            extracted_text = pytesseract.image_to_string(image)
        except Exception as e:
            return jsonify({"error": f"Error processing image: {str(e)}"}), 500
        finally:
            os.remove(filepath)

    if 'chat_history' not in session:
        session['chat_history'] = []

    session['chat_history'].append(f"User: {message}")
    
    if extracted_text:
        session['chat_history'].append(f"Extracted Text: {extracted_text}")

    full_chat_history = "\n".join(session['chat_history'])

    print("Chat History for Debugging:\n", full_chat_history)

    data = {
        "model": "llama3.1",
        "prompt": full_chat_history,
        "stream": False
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        response_data = response.json().get('response')
        session['chat_history'].append(f"Bot: {response_data}")

        return jsonify({"response": response_data, "ocrOutput": extracted_text})
    else:
        return jsonify({
            "error": f"Failed with status code: {response.status_code}. Error message: {response.text}"
        }), 500

# Clear chat history
@app.route('/clear', methods=['POST'])
def clear_chat():
    session.pop('chat_history', None)  # Remove chat history from the session
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)
