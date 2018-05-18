from flask import Flask
import json
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "Hello World."

port = int(os.environ.get('PORT', 5000))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)