#Some of the flask imports we will save for later.
import os
#import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# Uncomment next line when you need to use api
# openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/GPT-3/")
def GPT3():
    return render_template("gpt-3.html")

app.run(host="0.0.0.0", port = 5001)