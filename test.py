import re

# pattern1 = "ngày ([0-9]{1,2}) (.*)"
# pattern2 = "ngày ([0-9]{1,2}) tháng ([0-9]{1,2})"
# pattern3 = "ngày ([0-9]{1,2}/[0-9]{1,2})"
# pattern4 = "(ngày |)(([0-9]{1,2})|([0-9]{1,2}/[0-9]{1,2})|([0-9]{1,2}/[0-9]{1,2}/[0-9]{4}))"
# pattern5 = "(2|3|4)"
#
# str = "3"
#
# b = re.match(pattern5,str)
#
# if b :
#     print(b.group(0))
#     print(b.group(1))
#
#
#     print(True)
# else :
#     print(False)
# patterns1 ="(?:nd|st|rd|th)?"
# s = re.match(patterns1,"st")
# print(s.group(0))
msg = "lúc 17 : 17 : 12"
patterns2 = re.findall(r'\D(?:(00|[0]?[2-9]|[0]?1[0-9]?|2[0-3]):([0-5]?[0-9]))', msg)
patterns3 = re.findall(r'\D(0?[0-9]|1[0-9]|2[0-3])(?:\s*):(?:\s*)([0-5]?[0-9])', msg)

# for pattern in patterns2:
#     print(pattern)\D
print(patterns2)
print(patterns3)