from flask import Flask
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
import psycopg2 

app = Flask(__name__)

@app.route('/')
def start():
    db = psycopg2.connect(
        host="localhost"
    )
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (nick varchar, pass varchar)")

    return '<h1>Hello World<br><a href="/login">LOGIN</a></h1>'

@app.route('/test')
def test():
    return 'This is <b>test</b> site'

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello {name}</h1>'

@app.route('/invalid')
def invalid():
    return f'<h1>Invalid name or pass</h1>'

def login_page():
    return """<html>
   <body>
      <form action = "http://localhost:5000/login" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "nick" /></p>
         <p><input type = "password" name = "pass" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>"""

def auth(name, password):
    db = psycopg2.connect("db.sqlite3")
    cur = db.cursor()
    query = "SELECT * FROM users WHERE nick=? AND pass = ?"
    cur.execute(query, (name, password))
    num = len(cur.fetchall())
    cur.close()
    db.close()
    return num

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return login_page()
    elif request.method == 'POST':
        user = request.form['nick']
        password = request.form['pass']

    if auth(user, password) > 0:
        return redirect(url_for('greet',name=user))
    else:
        return redirect(url_for('invalid'))

app.run(debug=True)