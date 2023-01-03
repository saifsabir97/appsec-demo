# import the Flask class from the flask module
import sqlite3

from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        conn = get_db_connection()
        user = conn.execute(
            f'SELECT * FROM users WHERE name = "{request.form["username"]}" AND password = "{request.form["password"]}"').fetchone()
        conn.close()
        print(user)
        if not user:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
