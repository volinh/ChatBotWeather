import re

pattern1 = "ngày ([0-9]{1,2}) (.*)"
pattern2 = "ngày ([0-9]{1,2}) tháng ([0-9]{1,2})"
pattern3 = "ngày ([0-9]{1,2}/[0-9]{1,2})"
pattern4 = "(ngày |)(([0-9]{1,2})|([0-9]{1,2}/[0-9]{1,2})|([0-9]{1,2}/[0-9]{1,2}/[0-9]{4}))"
pattern5 = "(2|3|4)"

str = "3"

b = re.match(pattern5,str)

if b :
    print(b.group(0))
    print(b.group(1))


    print(True)
else :
    print(False)