class TimeDetector():

    def __init__(self):
         pass

    def detect_time(self,data):
        data_time = {}
        subdata = {}
        subdata['hour'] = None
        subdata['minute'] = None
        subdata['second'] = None
        data_time['time'] = subdata
        pattern1 = r'\D(0?[0-9]|1[0-9]|2[0-3])(?:\s*)giờ'
        pattern2 = r'\D(0?[0-9]|1[0-9]|2[0-3])(?:\s*)h'
        pattern3 = r'\D(0?[0-9]|1[0-9]|2[0-3])(?:\s*)giờ(?:\s*)(0?[0-9]|(?:1|2|3|4|5)[0-9])(?:\s*)'
        pattern4 = r'\D(0?[0-9]|1[0-9]|2[0-3])(?:\s*)h(?:\s*)(0?[0-9]|(?:1|2|3|4|5)[0-9])(?:\s*)'
        pattern6 = r'\D(0?[0-9]|1[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9])'
        line = ""
        for i in data:
            line = line + " " + i
        line = line.strip()





    # def _detect_range(self):
    #     pass
    #
    # def _detect_return_date(self):
    #     pass