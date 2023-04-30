import os

import openai
from flask import Flask, redirect, render_template, request, url_for

print("pic")


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        entry = request.form["animal"]
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=generate_prompt(entry),
        #     max_tokens=85,
        #     temperature=0.6,
        # )
        response = openai.Image.create(
        prompt=generate_prompt(entry),
        n=1,
        size="256x256"
        )
        image_url = response['data'][0]['url']

        #print(response.choices[0].text)
        print(response['data'][0]['url'])
        return redirect(url_for("index", result=response['data'][0]['url']))

    result = request.args.get("result")
    return render_template("index.html", result=result)



def generate_prompt(entry):
    return """A photo of: {}
""".format(
        entry.capitalize()
    )
