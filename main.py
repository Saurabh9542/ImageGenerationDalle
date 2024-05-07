import os
from flask import Flask, request, jsonify
# from flask_asgi import asgi
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/generate_image", methods=['POST'])
def generate_image():
    response = client.images.generate(
    model="dall-e-3",
    prompt=request,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = response.data[0].url
    print(request)

    return jsonify(image_url)


if __name__ == '__main__':
    app.run(debug=True)