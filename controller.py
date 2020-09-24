from app import app
from flask import render_template

@app.route('/')
def index():
    return "Welcome to the interwebs perty ! Grab a beer"