from flask import Flask

app = Flask(__name__)

@app.route('/') #request for the home page of a site
def home():
    return "Hello, world!"

app.run(port=5000)