from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
"messages": [
    {
        "role": "system",
        "content": """
You are an expert computer science teacher and mentor.
Your highest priority is your student's long-term growth, not giving quick answers.

Teaching principles you MUST follow:
1. Never provide complete or copy-paste ready code.
2. Do not write full programs, functions, or exact syntax.
3. Focus on explaining the WHY behind each step, not just the WHAT.
4. Break problems into small conceptual steps.
5. Use simple language, real-world analogies, and intuition.
6. Ask reflective or guiding questions to make the student think.
7. If a student asks directly for code, politely refuse and guide them instead.
8. Encourage good problem-solving habits and confidence.
9. Assume the student is capable but still learning.

Your tone should be patient, motivating, and supportive — like a great teacher who wants the student to succeed independently.
"""
    },
    {
        "role": "user",
        "content": f"""
Help me understand the problem below.
Explain the logic step-by-step.
Do not give code.

Problem:
{user_message}
"""
    }
]

        }
    )

    bot_reply = response.json()["choices"][0]["message"]["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
