from flask import Flask

app = Flask(__name__)
app.debug = False

@app.route('/<page>')
def show_page(page):
    return 'You are currently on the ' + page + ' page'

@app.route("/")
def hello_flask():
    display = """<h2><font face = 'WildWest' size = 45 color = 'maroon'>Lab 6 - Flask</font></h2>
    <p><h4><a href="/Index">Index</a></h4></p>
    """
    return display

@app.route("/Index")
def index():
    welcome = '<p><a href="/Welcome">Welcome</a></p>'
    photos = '<p><a href="/Photos">Photos</a></p>'
    wiki = '<p><a href="/Wiki">Wiki</a></p>'
    home = '<p><a href="/">Home</a></p>'
    index = welcome + photos + wiki + home + show_page("Index")
    return index

@app.route("/Welcome")
def hello():
    return "This is a flask application!"

@app.route("/Photos")
def photos():
    pics = '''<br><img src = "/static/working_cat.jpeg" alt = 'Working Cat' width = '600' height = 'auto'/></br>
    <br><img src = 'https://i.pinimg.com/originals/bc/fc/4c/bcfc4c270dfa79feffbbc47656e8960a.jpg' alt = 'Lake Isabel' width = '600' height = 'auto'/></br>'''
    return pics

@app.route("/Wiki")
def wiki():
    return '<a href="https://www.wikipedia.org/"><h1><color=blue>Wikipedia</color></h1></a>'
