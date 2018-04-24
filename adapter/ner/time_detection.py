import datetime
import re

class TimeDetector():

    def __init__(self):
        pass

    def detect_time(self,time):
        data_time = []
        current_time = datetime.datetime.now()
        current_day = current_time.day
        current_month = current_time.month
        current_year = current_time.year
        current_hour = current_time.hour
        current_weekday = current_time.weekday()
        pattern1 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)giờ'
        pattern2 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)h'
        pattern3 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)giờ(?:(?:\s*)([0-5]?[0-9])(?:\s*))?'
        pattern4 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)h(?:\s*)([0-5]?[0-9])(?:\s*)'
        pattern5 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9])'
        big_pattern1 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)giờ(?:\s*)([0-5]?[0-9])(?:\s*)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)giờ'
        big_pattern2 = r'(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)h(?:\s*)([0-5]?[0-9])(?:\s*)|(?:[^0-9\w]|^)([0-1]?[0-9]|2[0-3])(?:\s*)h'
        patterns = re.findall(pattern5, time)
        for pattern in patterns:
            sub_time = {
                "hour": pattern[0],
                "minute": pattern[1]
            }
            data_time.append(sub_time)
        patterns = re.findall(big_pattern1, time)
        for pattern in patterns:
            if pattern[2] != "" :
                sub_time = {
                    "hour": pattern[2],
                    "minute": "00"
                }
            else :
                sub_time = {
                    "hour": pattern[0],
                    "minute": pattern[1]
                }
            data_time.append(sub_time)
        patterns = re.findall(big_pattern2, time)
        for pattern in patterns:
            if pattern[2] != "":
                sub_time = {
                    "hour": pattern[2],
                    "minute": "00"
                }
            else:
                sub_time = {
                    "hour": pattern[0],
                    "minute": pattern[1]
                }
            data_time.append(sub_time)
        if len(data_time) == 0 :
            data_time.append({
                "hour": None,
                "minute": None
            })
        return data_time


    def _detect_range(self):
        pass

    def _detect_return_date(self):
        pass

if __name__ == "__main__" :
    timeDetector = TimeDetector()
    msg = "tôi sẽ đi làm vào 12 giờ , 9giờ , 11:3:4 và 19 giờ 56 ,còn ngày mai lúc 20h06  hoặc lúc 23 h 09 có ca nhạc đêm khuya"
    timeDetector.detect_time(msg)