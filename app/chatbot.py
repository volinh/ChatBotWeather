from adapter.intend.adapterIntend import AdapterIntend
from adapter.greeting.adapterGreeting import AdapterGreeting
from adapter.ner.adapterNer import AdapterNer

class Chatbot(object):

    def __init__(self):
        self.history = {}
        self.bot_state = 1
        self.bot_msg = ""
        self.adapterGreeting = AdapterGreeting()
        self.adapterIntend = AdapterIntend()
        self.adapterNer = AdapterNer()
        self.time = None
        self.loc = None
        self.weather = "thời tiết"


    def response(self,user_msg):
        intend = self.adapterIntend.get_intend(user_msg)
        if self.bot_state == 1:
            if intend == 1 :
                data = self.adapterGreeting.make_response(user_msg)
            elif intend == 2 :
                data = self.adapterNer.detect_entity(user_msg)
            elif intend == 3 :
                data = self.adapterNer.detect_entity(user_msg)
            else:
                data = None
            return self.make_msg(data,intend)
        elif self.bot_state == 2:
            if intend == 1 :
                data = self.adapterGreeting.make_response(user_msg)
            elif intend == 2 :
                data = self.adapterNer.detect_entity(user_msg)
            elif intend == 3 :
                data = self.adapterNer.detect_entity(user_msg)
            else:
                data = None
            return self.make_msg(data,intend)
            pass


    def make_msg(self,data=None,intend=4):
        data_msg = {}
        if intend == 1 :
            self.loc = None
            self.time =None
            self.bot_msg = data
            self.weather = "thời tiết"
            self.bot_state = 1
        elif intend == 2 :
            self.loc = data["LOC"]
            self.time = data["TIME"]
            self.bot_msg = "chua co api"
            self.weather = self.weather
            if self.loc == None:
                self.bot_msg = "bạn cho xin địa điểm :D"
                self.bot_state = 2
            elif self.time == None:
                self.bot_msg = "bạn cho xin thời gian :D"
                self.bot_state = 2
            else:
                self.bot_state = 1
        elif intend == 3 :
            self.loc = data["LOC"]
            self.time = data["TIME"]
            self.bot_msg = "chua co api"
            self.weather = self.weather
            if self.loc == None:
                self.bot_msg = "bạn cho xin địa điểm :D"
                self.bot_state = 2
            elif self.time == None:
                self.bot_msg = "bạn cho xin thời gian :D"
                self.bot_state = 2
            else:
                self.bot_state = 1
        else:
            self.loc = None
            self.time = None
            self.bot_msg = "mình không hiểu ý bạn :("
            self.weather = "thời tiết"
            self.bot_state = 1
        data_msg["intend"] = intend
        data_msg["loc"] = self.loc
        data_msg["time"] = self.time
        data_msg["weather"] = self.weather
        data_msg["msg"] = self.bot_msg
        data_msg["state"] = self.bot_state
        return data_msg


    # def get_data_from_api(self,data):
    #     return data


    def main(self):
        while True:
            msg = input("human : ")
            if msg == "":
                print("bot : bạn nhập tin nhắn đi !")
            else:
                bot_msg = self.response(msg)
                print("bot : {}".format(bot_msg))
                print("\n")




