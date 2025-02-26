from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

# import controller.user_controller
# import controller.product_controller
from controller import *

if __name__ == '__main__':
    app.run(debug=True)