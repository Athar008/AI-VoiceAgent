import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_history = [
    {
        "role": "system",
        "content": "You are a helpful, friendly assistant. Keep replies concise and conversational — 1-3 sentences unless more detail is truly needed."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    chat_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=chat_history
        )
        reply = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/clear", methods=["POST"])
def clear():
    chat_history.clear()
    chat_history.append({
        "role": "system",
        "content": "You are a helpful, friendly assistant. Keep replies concise and conversational — 1-3 sentences unless more detail is truly needed."
    })
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(debug=True)
