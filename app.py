from flask import Flask, render_template
app = Flask(__name__)

TERMS, DEFS = "terms", "definitions"
AVAILABLE_COMMANDS = {
    'Terms': TERMS,
    'Definitions': DEFS
}

@app.route('/')
def hello():
    return render_template('index.html', commands=AVAILABLE_COMMANDS)

#rendering the HTML page which has the button
#@app.route('/terms')
#def terms():
#    return render_template('terms.html')

@app.route('/<cmd>')
def command(cmd=None):
    if cmd == TERMS:
       camera_command = "X"
       f = open("word_lists.csv")
       line = f.readline()
       response = "Searching {}: {}".format(cmd.capitalize(), line)
    else:
        camera_command = cmd[0].upper()
        response = "Searching {}".format(cmd.capitalize())

    # ser.write(camera_command)
    return response, 200, {'Content-Type': 'text/plain'}

#background process happening without any refreshing
#@app.route('/search_terms')
#def search_terms():
#    print("Hello")
#    return "nothing"
