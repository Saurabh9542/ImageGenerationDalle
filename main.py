import os
from flask import Flask, request, jsonify
from openai import OpenAI
from flask import render_template

client = OpenAI()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route("/generate_image/<prompt>", methods=['POST'])
def generate_image(prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = response.data[0].url
    return jsonify(image_url)


if __name__ == '__main__':
    app.run(debug=True)





