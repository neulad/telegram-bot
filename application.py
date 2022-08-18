import requests
from telepot import *

# TODO
bot = Bot("PASTE THERE ID OF THE BOT!!!!!!!!!!!")
updates_id = 0
id_text = 0
while True:
    dates = bot.getUpdates(offset = updates_id + 1)
    for data in dates:
        if data["update_id"] > updates_id:
            updates_id = data["update_id"]
        id_text = data["message"]["chat"]["id"]
        if "text" in data["message"]:
            text = data["message"]["text"]
        else:
            bot.sendMessage(id_text, "Вы прислали недопустимый тип файла!!!")
            continue
        if "/get_ip " in text:
            text = text[8:]
            ip = requests.get("http://ip-api.com/json/" + text).json()
            if ip["status"] == "success":
                bot.sendMessage(id_text, "Страна: " + ip["country"] + "\n" + "Город: " + ip["city"])
            else:
                bot.sendMessage(id_text, "Кажется вы допустили ошибку в IP")
        elif "/start" in text:
            bot.sendMessage(id_text, "Введите команду /get_ip и после неё напишите IP, бот вернёт страну и город, к которым привязан IP")
        else:
            bot.sendMessage(id_text, "Команду /get_ip нужно писать в начале текста, также после этой команды следует указать IP")
