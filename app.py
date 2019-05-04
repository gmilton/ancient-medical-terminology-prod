from flask import Flask, render_template, jsonify
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
            entry = {}
            entry['term'] = word.term
            entry['definition'] = word.definition
            entry['greek_latin'] = word.greek_latin
            entry['pos'] = word.pos
            new_word_list.append(entry)

    return sorted(new_word_list, key=lambda w: w['term'])

def search_defs(word_list, search):
    new_word_list = []

    for word in word_list:
        if search.lower() in word.definition.lower():
            print(search.lower(), word.term.lower())
            entry = {}
            entry['term'] = word.term
            entry['definition'] = word.definition
            entry['greek_latin'] = word.greek_latin
            entry['pos'] = word.pos
            new_word_list.append(entry)

    return sorted(new_word_list, key=lambda w: w['term'])

def find_prefix(word_list, prefix):
    new_word_list = []

    for word in word_list:
        if word.term.lower().startswith(prefix.lower()):
            entry = {}
            entry['term'] = word.term
            entry['definition'] = word.definition
            entry['greek_latin'] = word.greek_latin
            entry['pos'] = word.pos
            new_word_list.append(entry)

    return sorted(new_word_list, key=lambda w: w['term'])

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
    if cmd[0] == "search":
        if cmd[1] == TERMS:
            if cmd[2]:
                search = cmd[2]
            else:
                search = "NULL"
            terms_list = search_terms(WORD_LIST, search)
            response = {}
            response['terms'] = terms_list
        elif cmd[1] == DEFS:
            if cmd[2]:
                search = cmd[2]
            else:
                search = "NULL"
            terms_list = search_defs(WORD_LIST, search)
            response = {}
            response['terms'] = terms_list
    elif cmd[0] == "prefix":
        prefix = cmd[1]
        terms_list = find_prefix(WORD_LIST, prefix)
        response = {}
        response['terms'] = terms_list
    else:
        response = 'No search done'
    return jsonify(response), 200, {'Content-Type': 'application/json'}

#background process happening without any refreshing
#@app.route('/search_terms')
#def search_terms():
#    print("Hello")
#    return "nothing"
