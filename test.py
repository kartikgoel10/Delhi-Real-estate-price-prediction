from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def hello():
    return"hi"

if __name__ == "__main__":
    print{"server"}
app.run()