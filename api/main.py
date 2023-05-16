form flask import Flask,request
app=Flask(__name__)

@app.route("/")
def home():
    return "hello this is main page / home page"