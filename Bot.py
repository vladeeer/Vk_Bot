#/send_to_everyone(ids=g.ids, name = "Server", keyboard = g.keyboard.get_keyboard())

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import importlib
import Globals as g
from User import User
from Functions import *


#login, password='+375295946590','Не скажу'
#vk_session = vk_api.VkApi(login, password, app_id=2685278)
#vk_session.auth()

g.init()

token ='1a6da07ef532322890c2053594b085aac1dda7239efe4b7467df04eff18168213a07f8f423e2134f2e373'
g.vk_session = vk_api.VkApi(token=token)

g.session_api = g.vk_session.get_api()

g.longpoll = VkLongPoll(g.vk_session)

#g.ids = {"212790860":User("212790860"), 
#         "176323020":User("176323020"), 
#         "294961717":User("294961717"),
#         "404679904":User("404679904")}

g.ids = {"212790860":User("212790860"), 
         "222194858":User("222194858"), 
         #"294961717":User("294961717"), 
         #"404679904":User("404679904")
         }

#g.keyboard = VkKeyboard(one_time = False)

#g.keyboard.add_button("I have a", color = VkKeyboardColor.POSITIVE)
#g.keyboard.add_button("I have an", color = VkKeyboardColor.POSITIVE)
#g.keyboard.add_button("I have", color = VkKeyboardColor.POSITIVE)
#g.keyboard.add_line()
#g.keyboard.add_button("pen", color = VkKeyboardColor.PRIMARY)
#g.keyboard.add_button("apple", color = VkKeyboardColor.PRIMARY)
#g.keyboard.add_button("pine", color = VkKeyboardColor.PRIMARY)
#g.keyboard.add_button("oof", color = VkKeyboardColor.NEGATIVE)
#g.keyboard.add_line()

#g.keyboard.add_button("ᅠ", color = VkKeyboardColor.DEFAULT)
#g.keyboard.add_line()

#g.keyboard.add_button("Ведьмаку заплатите", color = VkKeyboardColor.POSITIVE)
#g.keyboard.add_button("Уоуоу", color = VkKeyboardColor.NEGATIVE)
#g.keyboard.add_button("Вам", color = VkKeyboardColor.NEGATIVE)
#g.keyboard.add_line()
#g.keyboard.add_button("Чеканой монетой", color = VkKeyboardColor.POSITIVE)
#g.keyboard.add_button("Зачтется всё это", color = VkKeyboardColor.POSITIVE)

print("Bot started")
send_to_everyone(ids = g.ids, message = "Добрый день, господа", name = "Server")

#212790860 я
#176323020 юля
#egarclub  егор
#404679904 маша

g.is_server_stopped = False
while not(g.is_server_stopped):
    for event in g.longpoll.check():
        if (event.type == VkEventType.MESSAGE_NEW) and (event.from_user) and not(event.from_me):
            send_to_everyone(event=event, ids=g.ids, message=event.text)

            if (str(event.user_id) == "212790860") and ("stop" in str(event.text).lower()):     
                react_stop()

            if (str(event.user_id) == "212790860") and (event.text.lower().split()[0]=="set"):
                react_set(event)
            
            if (str(event.user_id) == "212790860") and (event.text.lower().split()[0]=="get"):
                react_get(event)

            if (event.text == "ids"):
                react_ids()
            
            if ("шутк" in str(event.text).lower()):
                react_joke()

            if ("врем" in str(event.text).lower()):
                react_time()

            if (str(event.text).lower() == "base"):
                react_base()

            if (str(event.user_id) == "212790860") and (str(event.text)[0] == '/'):
                react_exec(event)

            if (str(event.user_id) == "212790860") and (str(event.text)[0] == '\\'):
                react_exec_no_try(event)
