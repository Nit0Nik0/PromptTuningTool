#Some of the flask imports we will save for later.
import os
from dotenv import load_dotenv
import openai
from flask import Flask, redirect, render_template, request, url_for



def buildRequest(settings):    
    response = openai.Completion.create(
        model = settings["model"],
        prompt = settings["prompt"],
        max_tokens = int (settings["max_tokens"]),
        temperature = float(settings["temp"]),
        top_p = float(settings["top_p"]),
        frequency_penalty = float(settings["frequency_penalty"]),
        presence_penalty =float(settings["presence_penalty"])
    )
    return response
    

load_dotenv()
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
        response = buildRequest(settings)
        return redirect(url_for("GPT3", result=response.choices[0].text))
    result = request.args.get("result") 
    return render_template("gpt-3.html", result=result)

app.run(host="0.0.0.0", port = 5001, debug=True)