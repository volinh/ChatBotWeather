import os
import re
import setting

def create_train_file_yesno_weather(filePath):
    data = []
    with open(filePath,"r") as file:
        lines = file.readlines()
    for line in lines:
        if(line.strip() == ""):
            continue
        else:
            data.append(line.strip())

    data2 = []
    for d in data:
        d2 = re.sub("trời","thời tiết",d)
        data2.append(d2)

    with open(filePath,"a") as file:
        for d in data2:
            file.writelines("\n")
            file.writelines(d)


def create_train_file_wh_weather(filePath):
    data = []
    with open(filePath, "r") as file:
        lines = file.readlines()
    for line in lines:
        if (line.strip() == ""):
            continue
        else:
            data.append(line.strip())

    data2 = []
    for d in data:
        if("như thế nào" in d):
            d2 = re.sub("như thế nào", "ra sao", d)
            data2.append(d2)

    with open(filePath, "a") as file:
        for d in data2:
            file.writelines("\n")
            file.writelines(d)

if __name__ == "__main__":
    # filePath1 = setting.YESNOWHEATHER
    # create_train_file_yesno_weather(filePath1)
    create_train_file_wh_weather(setting.WH_WEATHER_FILE)
