from flask import Flask, request, jsonify, session, render_template
import openai
from flask_cors import CORS
from flask_session import Session

openai.api_key_path = "./ops/openai.api.key"

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config["SESSION_TYPE"] = "filesystem"  # Options: 'filesystem', 'redis', 'memcached', 'sqlalchemy'
app.config["SESSION_PERMANENT"] = False  # Session resets when the browser closes
Session(app)

model = "gpt-3.5-turbo"

@app.route('/', methods=['GET', 'POST'])
def launch_app():

    # Initialize conversation history in session
    if "history" not in session:
        session["history"] = []

    return render_template("application.html", model=model)


@app.route('/clear', methods=['GET', 'POST'])
def clear():

    # Initialize conversation history in session
    if "history" not in session or len(session["history"]) == 0:
        return render_template("startup_message.html")

    session.clear()
    return render_template("chat_cleared_message.html")


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    user_message = request.json.get("user_message", "Who is Chandler Bing?")

    # Initialize conversation history in session
    if "history" not in session:
        session["history"] = []

    if user_message == "":
        return render_template("chat_log.html", chat_log=session["history"])

    session["history"].append({"role": "user", "content": user_message})

    response = openai.ChatCompletion.create(
        model=model,  # Use "gpt-4" for better performance
        messages=session["history"]
    )

    # Extract the assistant's response
    bot_reply = response["choices"][0]["message"]["content"]

    # Append assistant's response to session history
    session["history"].append({"role": "assistant", "content": bot_reply})
    session.modified = True  # Ensure session updates are saved

    return render_template("chat_log.html", chat_log=session["history"])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
