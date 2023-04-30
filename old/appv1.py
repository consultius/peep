import os

import openai
from flask import Flask, redirect, render_template, request, url_for

print("app")


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        entry = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(entry),
            max_tokens=2048,
            temperature=0.6,
        )
        print(response.choices[0].text)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)



def generate_prompt(entry):
    return """Create a script for an episode of the TV Show which includes the following: {}
""".format(
        entry.capitalize()
    )
