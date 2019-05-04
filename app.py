from flask import Flask, render_template
from words import load_words, Word, Node, Tree
app = Flask(__name__)

TERMS, DEFS = "terms", "definitions"
AVAILABLE_COMMANDS = {
    'Terms': TERMS,
    'Definitions': DEFS
}
WORD_LIST = load_words()

def search_terms(word_list, search):
    new_word_list = []

    for word in word_list:
        if search.lower() in word.term.lower():
            print(search.lower(), word.term.lower())
            new_word_list.append(word)

    return sorted(new_word_list, key=lambda w: w.term)

@app.route('/')
def hello():
    return render_template('index.html', commands=AVAILABLE_COMMANDS)

#rendering the HTML page which has the button
#@app.route('/terms')
#def terms():
#    return render_template('terms.html')

@app.route('/<cmd>')
def command(cmd=None):
    cmd = cmd.split(";")
    if cmd[0] == TERMS:
       camera_command = "X"
       f = open("word_lists.csv")
       line = f.readline()
       if cmd[1]:
           search = cmd[1]
           CONTAINS = cmd[1]
       else:
           search = "NULL"
       terms_list = search_terms(WORD_LIST, search)
       response = "Searching {} for {}: {}".format(cmd[0].capitalize(), search, terms_list)
    else:
        camera_command = cmd[0][0].upper()
        response = "Searching {}".format(cmd[0].capitalize())

    # ser.write(camera_command)
    return response, 200, {'Content-Type': 'text/plain'}

#background process happening without any refreshing
#@app.route('/search_terms')
#def search_terms():
#    print("Hello")
#    return "nothing"
