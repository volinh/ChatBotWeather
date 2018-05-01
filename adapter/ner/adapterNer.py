from builtins import dict
from nltk.tag.stanford import StanfordNERTagger
from nltk import word_tokenize
import datetime
from adapter.ner.time_detection import TimeDetector
from adapter.ner.date_detection import DateDetector
from adapter.ner.location_detection import LocationDetector
import setting
import re

class AdapterNer(object):

    def __init__(self):
        classifier = 'model/chatbot-ner.ser.gz'
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
        sub_loc = ""
        for tup in list_entity:
            if tup[1] == "LOC" :
                sub_loc = sub_loc + " " + tup[0]
            else :
                if sub_loc != "":
                    result['LOC'].append(sub_loc.strip())
                sub_loc = ""
        if sub_loc != "" :
            result['LOC'].append(sub_loc.strip())
        sub_time = ""
        for tup in list_entity :
            if tup[1] == "TIME" :
                sub_time = sub_time + " " + tup[0]
            else :
                if sub_time != "" :
                    result['TIME'].append(sub_time.strip())
                sub_time = ""
        if sub_time != "":
            result['TIME'].append(sub_time.strip())
        print(result)
        result['LOC'] = self.convert_loc(result['LOC'])
        result['TIME'] = self.convert_time(result['TIME'])
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
        matchObj = re.match(r'(vậy|vậy còn|thế còn|còn|thế) (.*) .*', user_msg, re.M | re.I)
        if matchObj :
            return True
        return False


    @staticmethod
    def convert_time(data):
        timeDetector = TimeDetector()
        dateDetector = DateDetector()
        data_time = []
        for time in data :
            sub_time = timeDetector.detect_time(time)
            print(sub_time)
            sub_date = dateDetector.detect_date(time)
            print(sub_date)
            for i in sub_time :
                for j in sub_date:
                    sub_data = {}
                    sub_data.update(i)
                    sub_data.update(j)
                    data_time.append(sub_data)
        return data_time


    @staticmethod
    def convert_loc(data):
        locationDetector = LocationDetector()
        data_loc = []
        for loc in data :
            sub_loc = locationDetector.detect_location(loc)
            if sub_loc == None:
                continue
            data_loc.append(sub_loc)
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