from nltk.tag.stanford import StanfordNERTagger
from nltk import word_tokenize

class AdapterNer(object):

    def __init__(self):
        classifier = 'data/chatbot-ner.ser.gz'
        jar = 'stanford-ner/stanford-ner.jar'
        self.st = StanfordNERTagger(classifier, jar)


    def detect_entity(self,user_msg):
        sentence = word_tokenize(user_msg.lower().strip())
        list_entity = self.st.tag(sentence)
        return self.pass_entity(list_entity)


    def pass_entity(self,list_entity):
        result = {}
        result['LOC'] = []
        result['TIME'] = []
        for tup in list_entity :
            if tup[1] == "LOC" :
                result['LOC'].append(tup[0])
            if tup[1] == "TIME":
                result['TIME'].append(tup[0])
        return result

    def detect_wether(self):
        pass


    def convert_time(self):
        pass


    def convert_loc(self):
        pass