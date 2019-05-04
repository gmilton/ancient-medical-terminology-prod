from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

#rendering the HTML page which has the button
@app.route('/terms')
def json():
    return render_template('terms.html')

#background process happening without any refreshing
@app.route('/search_terms')
def search_terms():
    print "Hello"
    return "nothing"
