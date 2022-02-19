import re
import os.path
import json

user_fav_city = []
user_fav_topic = []

from pathlib import Path

def save_user_interest(city=None, *topics):
   f = open('config.txt', 'w')
   f.write(city + '\n')
   for i in topics:
        f.write(i + '\n')
   f.close()

def get_json(what=None):
   try:
        with open("interests.json", 'r', encoding='utf-8') as read_message:
            ocenk = json.load(read_message)
            return ocenk
   except FileNotFoundError:
       pass

def write_json(file):
    with open("interests.json", 'w', encoding='utf-8') as write_message:
        json.dump(file, write_message, ensure_ascii=False, indent=4)


def get_control_interest(name):
    name = name
    get_json(name)

def get_points(points,name):
    try:
        key = get_json()
        key[name] += points
    except KeyError:
        pass

back_up = {
    "Политика": 0,
    "Бизнес": 0,
    "Происшествия": 0,
    "Здравоохранения": 0,
    "Авто": 0,
    "Сахалинская полиция": 0,
    "Короновирус": 0,
    "Финансы": 0,
    "ЖКХ": 0,
    "Спорт": 0,
    "МЧС": 0,
    "Любительская рыбалка": 0,
    "Строительство": 0,
    "Следственный комитет": 0,
    "Недвижимость": 0,
    "Экология": 0,
    "Погода": 0,
    "Пассажирские перевозки": 0,
    "Потрибительский рынок": 0,
    "Видеоновости": 0,
    "Фотоновости": 0
}








trash_symb = '[\n]'
def read_user_conf():
    global user_fav_city
    with open('config.txt', 'r') as f:
            key = get_json()
            i = f.readlines()
            fav_city = i[0]
            trash_symbols = '[\xa0\n\t\t\t]'
            user_fav_city = re.sub(trash_symbols,' ',fav_city).split()
            #print(i[0])

            for o in i[1:]:
                final = re.sub(trash_symb, ' ',o)
                user_fav_topic.append(final.strip())
            for i in user_fav_topic:
                if key.get(i) == 0:
                    key[i] += 10
            write_json(key)




if os.path.exists('config.txt'):
    read_user_conf()
elif os.path.exists('config.txt') == False and os.path.exists('interests.json') == True:
    key = get_json(None)
    for k in key:
        key[k] = 0
elif os.path.exists('config.txt') == False and os.path.exists('interests.json') == False:
    write_json(back_up)

    key = get_json()
    kol = [k for k, v in key.items() if v == max(key.values())]

    for i in range(len(kol)):
        try:
            save_user_interest(user_fav_city[0], kol[i])
        except:
            break