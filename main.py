from app.chatbot import Chatbot
# from adapter.ner import train
# train.main()
chatbot = Chatbot()
chatbot.main()
#
# import re
#
# str = 'Hoc lap trinh Toidicode.com he ads Toidicode.com jij j'
# match = re.search(r'(.*) Toidicode.com (.*)', str)
# if match: #nếu tồn tại chuỗi khớp
#     print (match.groups()) # in ra chuỗi đó
# else:
#     print ('Khong tim thay!') # Không thì hiện thông báo
#
