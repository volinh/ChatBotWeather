from builtins import dict
from nltk.tag.stanford import StanfordNERTagger
from nltk import word_tokenize
import datetime

import setting
import re

class AdapterNer(object):

    def __init__(self):
        classifier = 'data/chatbot-ner.ser.gz'
        jar = 'stanford-ner/stanford-ner.jar'
        self.st = StanfordNERTagger(classifier, jar)
        self.dict_weather = self.read_file(setting.DIC_WEATHER_FILE)


    def detect_entity(self,user_msg):
        sentence = word_tokenize(user_msg.lower().strip())
        list_entity = self.st.tag(sentence)
        return self.pass_entity(list_entity,user_msg)


    def detect_weather(self,user_msg):
        result = []
        for i in self.dict_weather:
            if i in user_msg :
                result.append(i)
        return result


    def pass_entity(self,list_entity,user_msg):
        result = {}
        result['LOC'] = []
        result['TIME'] = []
        result['WEATHER'] = self.detect_weather(user_msg)
        for tup in list_entity :
            if tup[1] == "LOC" :
                result['LOC'].append(tup[0])
            if tup[1] == "TIME":
                result['TIME'].append(tup[0])
        # result['LOC'] = self.convert_loc(result['LOC'])
        # result['TIME'] = self.convert_time(result['TIME'])
        return result


    @staticmethod
    def read_file(filePath):
        dic_weather = []
        with open(filePath, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    dic_weather.append(line)
        return dic_weather


    @staticmethod
    def detect_question_again(user_msg):
        user_msg = re.sub("\?","",user_msg).strip()
        matchObj = re.match(r'(vậy|vậy còn) (.*) .*', user_msg, re.M | re.I)
        if matchObj :
            return True
        return False


    @staticmethod
    def convert_time(data):
        data_time = {}
        current_time = datetime.datetime.now()
        print(current_time)
        current_day = current_time.day
        current_month = current_time.month
        current_year = current_time.year
        current_hour = current_time.hour
        current_weekday = current_time.weekday()

        data_time["hour"] = 8
        data_time["minute"] = 30
        data_time["day"] = 13
        data_time["month"] = 4
        data_time["year"] = 2018
        # data_time[]
        return data_time


    @staticmethod
    def convert_loc(data):
        data_loc = {}
        data_loc["city"] = "Ha noi"
        data_loc["country"] = "VN"
        return data_loc


if __name__ == "__main__" :
    # a = AdapterNer.detect_question_again("vậy còn hà nội thì sao ?")
    # print(a)
    AdapterNer.convert_time([])
    # !/usr/bin/python3
    # import re
    #
    # line = "hay nếu hà nội thì sao ?"
    #
    # matchObj = re.match(r'(.*) (vậy|nếu còn) (.*) .*', line, re.M | re.I)
    # if matchObj:
    #     print("matchObj.group() : ", matchObj.group())
    #     print("matchObj.group(1) : ", matchObj.group(1))
    #     print("matchObj.group(2) : ", matchObj.group(2))
    #     print(matchObj.group(3))
    # else:
    #     print("No match!!")
    # print(AdapterNer().detect_weather("mai trời có mưa không ?"))
    # AdapterNer().