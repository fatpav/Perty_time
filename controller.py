from app import app
from flask import render_template
from app.models.event_list import events

@app.route('/')
def index():
    return render_template('index.html', title = 'Home', events = events)

# @app.route('/add-event', methods=['post'])
# def add_event():
#     return "Perty posted"