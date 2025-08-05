import pyshorteners
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    url = request.form['url']
    
    type_tiny = pyshorteners.Shortener()
    
    short_url = type_tiny.tinyurl.short(url)
    return render_template("url.html", short_url = short_url)