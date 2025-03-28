from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form["text"]
        if "file" in request.files:
            file = request.files["file"]
            if file and file.filename.endswith(".txt"):
                user_input = file.read().decode("utf-8")
                
        if user_input:
            client = OpenAI()

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Summarize this text:\n{user_input}"}
                ]
            )
            result = response.choices[0].message.content
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
