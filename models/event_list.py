from app.models.event import *

event_1 = Event("Pauls disco", "2020-10-08", 6,"Burger King", "hot beats and a hotter ass")
event_2 = Event("Cool Daze", "2020-11-09", 100, "Steve's House", "Autumnal vibes")
events = [event_1, event_2]

def add_new_event(event):
    events.append(event)
