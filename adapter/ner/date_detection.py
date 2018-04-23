import datetime
import re

from IPython.external.path import path
from docutils.nodes import paragraph


class DateDetector():

    def __init__(self):
         pass

    def detect_date(self,date):
        data_date = []
        current_time = datetime.datetime.now()
        current_day = current_time.day
        current_month = current_time.month
        current_year = current_time.year
        pattern1 = r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])'
        pattern2 = r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)tháng(?:\s*)(1[0-2]|0?[1-9])'
        pattern3 = r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)tháng(?:\s*)(1[0-2]|0?[1-9])(?:\s*)năm(?:\s*)(2[0-9]{3})'
        pattern4 = r'(?:[^0-9\w]|^)ngày(?:\s*)([1-2][0-9]|3[0-1]|0?[1-9])'
        pattern5 = r'(?:[^0-9\w]|^)tháng(?:\s*)(1[0-2]|0?[1-9])'
        pattern6 = r'(?:[^0-9\w]|^)năm(?:\s*)(2[0-9]{3})'
        pattern7 = r'(?:[^0-9\w]|^)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)(?:[/-]|tháng)(?:\s*)(1[0-2]|0?[1-9])'
        pattern8 = r'(?:[^0-9\w]|^)([1-2][0-9]|3[0-1]|0?[1-9])(?:\s*)(?:[/-]|tháng)(?:\s*)(1[0-2]|0?[1-9])(?:\s*)(?:[/-]|năm)(?:\s*)(2[0-9]{3})'
        pattern_spec1 = r'(hôm nay|bây giờ|bây h|hiện tại|hiện nay|lúc này)'
        pattern_spec2 = r'(ngày mai|mai|hôm sau)'
        pattern_spec3 = r'(ngày kia|ngày mốt|hôm kia)'
        pattern_spec4 = r'(ngày kia nữa|hôm kia nữa)'
        pattern_spec5 = r'(hôm qua)'
        pattern_spec6 = r'(hôm trước)'
        pattern_spec7 = r'(tuần này|tuần hiện tại|tuần hiện giờ)'
        pattern_spec8 = r'(tuần sau|tuần vừa rồi)'
        pattern_spec9 = r'(tuần kia,tuần sau nữa)'
        pattern_spec10 = r'(tuần trước)'
        pattern_spec11 = r'(thứ 2|thứ hai)'
        pattern_spec12 = r'(thứ 3|thứ ba)'
        pattern_spec13 = r'(thứ 4|thứ tư)'
        
        patterns = re.findall(pattern8, date)
        for pattern in patterns:
            # print(pattern)
            sub_date = {
                "day": pattern[0],
                "month": pattern[1],
                "year": pattern[2]
            }
            data_date.append(sub_date)

        # patterns = re.findall(big_pattern1, date)
        # for pattern in patterns:
        #     print(pattern)
        #     if pattern[0] !="" :
        #         sub_date = {
        #             "day": pattern[0],
        #             "month": pattern[1],
        #             "year": current_year
        #         }
        #     elif pattern[2] != "" :
        #         sub_date = {
        #             "day": pattern[2],
        #             "month": pattern[3],
        #             "year": pattern[4]
        #         }
        #     elif pattern[5] != "" :
        #         sub_date = {
        #             "day": pattern[5],
        #             "month": pattern[6],
        #             "year": str(current_year)
        #         }
        #     elif pattern[7] != "":
        #         sub_date = {
        #             "day": pattern[7],
        #             "month": str(current_month),
        #             "year": str(current_year)
        #         }
        #     elif pattern[8] != "":
        #         sub_date = {
        #             "day": None,
        #             "month": pattern[8],
        #             "year": pattern[9]
        #         }
        #     elif pattern[10] != "":
        #         sub_date = {
        #             "day": None,
        #             "month": pattern[10],
        #             "year": current_year
        #         }
        #     elif pattern[11] != "":
        #         sub_date = {
        #             "day": None,
        #             "month": None,
        #             "year": pattern[11]
        #         }
        #     data_date.append(sub_date)

        for i in range(10):
            i = i +1


        for i in data_date:
            print(i)
        return data_date


    def _detect_range(self):
        pass

    def _detect_return_date(self):
        pass

    def get_date_spec(self,pattern,date):
        patterns = re.findall(pattern, date)
        # for pattern in patterns:
        #     sub_date = {
        #         "current": True,
        #         "day": current_day,
        #         "month": current_month,
        #         "year": current_year
        #     }
        #     data_date.append(sub_date)

if __name__ == "__main__" :
    dateDetector = DateDetector()
    # msg = "ngày 20/1 có lịch hẹn ,ngày 18/9/2017 và 5-4 hoặc 12-4-2021 sẽ như thế nào ?"
    # msg = "tháng 1 năm 2017 và năm 2016"
    msg = "ngày mai và hôm qua , đến ngày 24 tháng 6/2011 có gì ,ngày 8 tháng 9"
    dateDetector.detect_date(msg)
