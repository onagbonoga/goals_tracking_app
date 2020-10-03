from flask import Flask, request, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getTime", methods=['GET'])
def getTime():
    print("browser time: ", request.args.get("time"))
    print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
    return "Done"