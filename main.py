from flask import Flask, request
import pandas as pd 

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'This is the landing page for Minnesota ICD Code details'

if __name__ == '__main__':
    app.run(debug=True)



    