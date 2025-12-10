from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is our first flask tutorial</h1>"

@app.route('/Contact')
def Message_me():
    return "<h1>This Contact page</h1>"

@app.route('/about')
def about_me():
    return "<h1>This about page</h1>"

app.run(debug=True)