#Some of the flask imports we will save for later.
import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# Uncomment next line when you need to use api
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/GPT-3/", methods=("GET", "POST"))
def GPT3():
    if request.method == "POST":
        settings = request.form
        
        return redirect(url_for("index", result=response.choices[0].text))     

    return render_template("gpt-3.html")

app.run(host="0.0.0.0", port = 5001, debug=True)


# Helper Functions
def buildRequest(settings):
    return null