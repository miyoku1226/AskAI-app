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
        user_input = request.form.get("text", "").strip()

        if "file" in request.files:
            file = request.files["file"]
            if file and file.filename.endswith(".txt"):
                try:
                    file_content = file.read()
                    user_input = file_content.decode("utf-8-sig").strip()
                    if not user_input:
                        result = "Error: Uploaded file appears to be empty or unreadable."
                        return render_template("index.html", result=result)
                except Exception as e:
                    result = "Error: Could not read uploaded file."
                    return render_template("index.html", result=result)

        if user_input:
            mode = request.form.get("mode", "summarize")

            if mode == "summarize":
                prompt = f"Summarize this text:\n{user_input}"
            elif mode == "translate":
                prompt = f"Translate the following text to Chinese:\n{user_input}"
            elif mode == "analyze":
                prompt = f"What is the overall sentiment of this text? Respond with Positive, Negative, or Neutral.\n{user_input}"
            else:
                prompt = user_input

            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content
            except Exception as e:
                result = "Error: GPT API request failed."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
