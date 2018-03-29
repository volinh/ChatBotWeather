from sklearn.metrics.pairwise import euclidean_distances
from sklearn.externals import joblib
import setting
import random

class AdapterGreeting(object):

    def __init__(self):
        self.vectorizer = joblib.load(setting.GREETING_MODEL)
        self.data = self.load_data(self.read_file(setting.GREETING_TRAIN_FILE))

    def make_response(self,msg):
        min = 1000
        msg = self.vectorizer.transform([msg])
        for i in self.data:
            vi = self.vectorizer.transform([i])
            a = euclidean_distances(vi[0],msg[0])
            if min > a[0][0]:
                value = i
                min = a[0][0]
        values = self.data[value]
        id = random.randint(0,len(values)-1)
        return self.data[value][id]


    def read_file(self,filePath):
        with open(filePath, "r") as file:
            data = file.readlines()
        data2 = []
        for line in data:
            dline = format(line)
            if dline != "":
                data2.append(dline)
        return data2


    def load_data(self,raw_data):
        data = {}
        for i in range(len(raw_data)):
            if i % 2 == 0:
                line = raw_data[i]
                line2 = raw_data[i + 1]
                keys = line.split("|")
                values = line2.split("|")
                for i in keys:
                    i = i.strip()
                    if i != "":
                        data[i] = values
            else:
                continue
        return data