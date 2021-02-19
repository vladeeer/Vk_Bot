from datetime import datetime
import Globals as g
import random
from Jokes import *

#General functions
def send_message(vk_session, id_type, id, message=None, keyboard = None):
    if keyboard != None:
        vk_session.method("messages.send", {id_type:id, "message":message, "random_id":0, "keyboard":keyboard})
    else:
        vk_session.method("messages.send", {id_type:id, "message":message, "random_id":0})

def send_to_everyone(event = None, ids = 0, message = "", name = None, keyboard = None):
    print("time "+str(datetime.strftime(datetime.now(), "%H:%M:%S")))
    print((ids[str(event.user_id)].name if event!=None else name)+ " " +(change_format(str(event.text)) if event!=None else message))
    print("-"*30)
    sender = event.user_id if name == None else "0"
    for id in ids:
        if id != str(sender):
            send_message(g.vk_session, "user_id", id,"[" + (ids[str(event.user_id)].name if name == None else name) + "] " + change_format(message), keyboard)

def change_format(string):
    result = string.replace("&quot;", "\"")
    return result



#Chat bot reactions
def react_stop():
    send_to_everyone(ids=g.ids, message="Приятно иметь с Вами дело", name="Server")
    g.is_server_stopped = True

def react_ids():
    send_to_everyone(ids=g.ids, message=str(list(g.ids.keys())), name="Server")

def react_joke():
    joke = random.choice(jokeArr)
    send_to_everyone(ids=g.ids, message=joke, name="Server")

def react_time():
    send_to_everyone(ids=g.ids, message=str(datetime.strftime(datetime.now(), "%H:%M:%S")), name="Server")

def react_base():
    f = open("UserBase.txt", "r")
    send_to_everyone(ids=g.ids, message=str(f.read()), name="Server")
    f.close()

def react_exec(event):
    try:  
        exec(change_format(str(event.text)[1:]))
    except:
        send_to_everyone(ids=g.ids, message="Nope", name="Server")

def react_exec_no_try(event):
    exec(change_format(str(event.text)[1:]))

def react_get(event):
    args = event.text.split()
    user = g.ids[list(g.ids.keys())[int(args[1])-1]]
    val = user.get_stat(args[2])
    if val!=None:
        send_to_everyone(ids=g.ids, message=user.id + " " + args[2] + " is " + val, name="Server")
    else:
        send_to_everyone(ids=g.ids, message=user.id + " " + args[2] + " not found", name="Server")

def react_set(event):
    args = event.text.split()
    try:
        user = g.ids[list(g.ids.keys())[int(args[1])-1]]
        if(user.change_stat(args[2], args[3]) == 0):
            send_to_everyone(ids=g.ids, message="Changed " + user.id + " " + args[2] + " to " + args[3], name="Server")
        else:
            send_to_everyone(ids=g.ids, message=user.id + " " + args[2] + " does not exist", name="Server")
    except:
        send_to_everyone(ids=g.ids, message="Nope", name="Server")