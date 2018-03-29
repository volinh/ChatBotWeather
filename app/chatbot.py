from adapter.intend import adapterIntend
from adapter.greeting import adapterGreeting
from adapter.ner import adapterNer

class Chatbot(object):


    def __init__(self):
        self.history = {}
        self.bot_state = 1
        self.


    def receive(self,user_msg):
        if self.bot_state == 1:
            intend = adapterIntend.detect_intend(user_msg)
            if intend == 1 :
                data = adapterGreeting.make_response()
            elif intend == 2 :
                data = adapterNer.detect_entity(user_msg)
            elif intend == 3 :
                data = adapterNer.detect_entity(user_msg)
            else:
                data = None
            self.response(data, intend=intend)
        elif self.bot_state == 2:
            pass


    def response(self,data=None,intend=4):
        if intend == 1 :
            bot_msg = data

        pass


    def get_data_from_api(self,data):
        return data


