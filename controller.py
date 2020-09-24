from app import app
from flask import render_template, request, redirect
from app.models.event_list import events, add_new_event
from app.models.event import *

@app.route('/')
def index():
    return render_template('index.html', title = 'Home', events = events)

@app.route('/add-event', methods=['post'])
def add_event():     
    event_name = request.form["name"]
    event_date = request.form["date"]
    event_guest_number = request.form["guest_number"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    new_event = Event(event_name, event_date, event_guest_number, event_location, event_description)
    add_new_event(new_event)
    return redirect('/')

    