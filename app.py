import os

import openai
from flask import Flask, redirect, render_template, request, url_for

print("pic")


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        entry = request.form["form1"]
        text_response = openai.Completion.create(       # get text
            model="text-davinci-003",
            prompt=generate_text_prompt(entry),
            max_tokens=80,
            temperature=0.6,
        )
        print("IN IF " + text_response.choices[0].text)
        # image_response = openai.Image.create(           # get image
        #     prompt=generate_image_prompt(entry),
        #     n=1,
        #     size="256x256"
        # )
        # print("GENERATED IMAGE URL IS " +
        #       image_response['data'][0]['url'])
        # image_variation_response = openai.Image.create_variation(           # get image
        #     image=open("mark2.png", "rb"),
        #     n=1,
        #     size="256x256"
        # )
        # print("GENERATED IMAGE VARIATION URL IS " +
        #       image_variation_response['data'][0]['url'])
        # code like the bits above which uses the openai.image.create_edit() function to edit the image
        # image_mask_jeremy_response = openai.Image.create_edit(         # get image
        #     image=open("jeremy_sofa.png", "rb"),
        #     mask=open("jeremy_sofa_mask.png", "rb"),
        #     prompt=generate_image_mask_prompt(entry),
        #     n=1,
        #     size="256x256"
        # )
        # print("GENERATED JEREMY EDIT URL IS " +
        #        image_mask_jeremy_response['data'][0]['url']
        #        )
        
        # image_mask_mark_response = openai.Image.create_edit(         # get image
        #     image=open("mark_holding.png", "rb"),
        #     mask=open("mark_holding_mask.png", "rb"),
        #     prompt=generate_image_mask_prompt(entry),
        #     n=1,
        #     size="256x256"
        # )
        # print("GENERATED MARK EDIT URL IS " +
        #        image_mask_mark_response['data'][0]['url']
        #        )


        return redirect(url_for("index",
                                text_result=text_response.choices[0].text,  #.split('\n')  ,
                                #image_result=image_response['data'][0]['url'],
                                #image_variation_result=image_variation_response['data'][0]['url'],
                                #image_mask_jeremy_result=image_mask_jeremy_response['data'][0]['url'],
                                #image_mask_mark_result=image_mask_mark_response['data'][0]['url']                                
                                )
                        )

    text_result = request.args.get("text_result")
    image_result = request.args.get("image_result")
    image_variation_result = request.args.get("image_variation_result")
    image_mask_jeremy_result = request.args.get("image_mask_jeremy_result")
    image_mask_mark_result = request.args.get("image_mask_mark_result")

    return render_template("index.html",
                           text_result=text_result,
                           image_result=image_result,
                           image_variation_result=image_variation_result,
                           image_mask_jeremy_result = image_mask_jeremy_result,
                           image_mask_mark_result = image_mask_mark_result 
                           )


def generate_text_prompt(entry):
    return """A darkly funny script for the TV show peep show where this happens: {}
""".format(
        entry.capitalize()
    )


def generate_image_prompt(entry):
    return """An image of british tv comedian david mitchell
""".format(
        entry.capitalize()
    )

def generate_image_mask_prompt(entry):
    return """{}
    """.format(
        entry.capitalize()
    )
