from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionGeo(Action):
    
    def name(self):
        return 'action_geo'
    def run(self, dispatcher, tracker, domain):
        from geopy.geocoders import Nominatim
        nom= Nominatim(timeout=100)
        loc = tracker.get_slot('location')
        n=nom.geocode(str(loc))
       
        latitude=n.latitude
        longitude=n.longitude
      

        response = """latitude= {} ,longitude= {}""".format(latitude,longitude)


        dispatcher.utter_message(response)
        return []
