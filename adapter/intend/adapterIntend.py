from nltk import classify
from pyvi.pyvi import ViTokenizer
import setting
import re


def tokenizer(text):
    ttext = ViTokenizer.tokenize(text)
    return ttext


def get_intend(text):
    pass


def load_model():
    pass


def train():
    pass


def load_data_train():
    list_file_path = [setting.GREETING_FILE,setting.WH_WEATHER_FILE,setting.YESNO_WEATHER_FILE,setting.ORTHER_FILE]
    data = []
    labels = []
    for filePath in list_file_path:
        if filePath == setting.GREETING_FILE:
            read_file(filePath,data,labels,label=1)
        elif filePath == setting.WH_WEATHER_FILE:
            read_file(filePath,data,labels,label=2)
        elif filePath == setting.YESNO_WEATHER_FILE:
            read_file(filePath,data,labels,label=3)
        else:
            read_file(filePath,data,labels,label=4)
    return data,labels


def read_file(filePath,data,labels,label):
    with open(filePath,"r") as file:
        lines = file.readlines()
    for line in lines:
        fline = format(line)
        if(fline!="") :
            data.append(fline)
            labels.append(label)


def format(line):
    fline = re.sub("\?","",line)
    fline = fline.strip()
    return fline


if __name__ == "__main__" :
    train_data,train_labels = load_data_train()
    print(len(train_data))
    print(len(train_labels))
    # text = "thời tiết hôm nay có âm u không ?"
    # ttext = tokenizer(text)
    # print(ttext)


    # a = "a a"
    # b = a.split(" ")
    # b.remove("a")
    # print(len(b))
    # for i in b :
    #     print(i)
