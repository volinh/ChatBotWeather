from nltk import classify
from pyvi.pyvi import ViTokenizer



def tokenizer(text):
    ttext = ViTokenizer.tokenize(text)
    return ttext

def get_intend(text):
    pass

def load_model():
    pass


if __name__ == "__main__" :
    # text = "thời tiết hôm nay có âm u không ?"
    # ttext = tokenizer(text)
    # print(ttext)
    pass

    # a = "a a"
    # b = a.split(" ")
    # b.remove("a")
    # print(len(b))
    # for i in b :
    #     print(i)
