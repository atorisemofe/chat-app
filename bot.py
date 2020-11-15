"""bot.py"""
from datetime import date
import requests
KEY_CONTENT="contents"
funresponse = []
def helps(_self):
    return "AketiBot: known commands !! help, !! about, !! funtranslate"
def about(_self):
    return "AketiBot: I am the Bot for this Aketi Chatroom"
def fun_translate(_self, _text):
    fun = "https://api.funtranslations.com/translate/yoda.json?text=" + input
    request = requests.get(fun)
    response = request.json()
    key_content = response['content']['translated']
    #funresponse.append({KEY_CONTENT: content1})
    return key_content
def dates(_self):
    today = date.today()
    return "Today date is: " + today
BOT_PREFIX = "!!"
KEY_IS_BOT = "is_bot"
KEY_BOT_COMMAND = "bot_command"
KEY_MESSAGE = "message"
def help_check(message):
    if not message.startswith(BOT_PREFIX):
        return {
          KEY_IS_BOT: False,
          KEY_BOT_COMMAND: None,
           KEY_MESSAGE: message,
        }
    message_components = message.split(" ", 1)
    if len(message_components) == 1:
        possible_bot_cmd, rest_of_message = message_components[0], ""
    else:
        possible_bot_cmd, rest_of_message = message_components[0], message_components[1]
    return {
        KEY_IS_BOT: True,
        KEY_BOT_COMMAND: possible_bot_cmd[len(BOT_PREFIX):],
        KEY_MESSAGE: rest_of_message,
    }
    