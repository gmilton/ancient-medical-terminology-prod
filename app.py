from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')
#    return "Hello World!"

#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print "Hello"
    return "nothing"
