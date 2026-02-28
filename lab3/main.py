#Блог. Написанный текст должен сохраняться и выводиться по убыванию даты.

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def init():
    return render_template("init.html")
if __name__ == "__main__":
    app.run()